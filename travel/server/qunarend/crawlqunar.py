import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json
import random
import re
import requests.exceptions
import time
from threading import Thread
import datetime


BASE_URL = 'http://touch.piao.qunar.com/touch/index_{}.html'
COMMENT_URL = 'https://touch.piao.qunar.com/touch/queryCommentsAndTravelTips.json?type=mp&pageSize=10&fromType=SIGHT&pageNum=1&sightId={}&tagType=0'
TIME_OUT = 30
class CrawlQunar(object):

  # 首页爬取,首页请求
  def parse_index(self, url):
    response = requests.get(url, timeout=TIME_OUT)
    soup = BeautifulSoup(response.text, 'lxml')
    print('开始爬取...')
    result = {
      'swipers': [],
      'icons': [],
      'places': [],
      'weekendRecommand': []
    }
    indexId = 1
    swipers = soup.select('div.mpw-swipe-item img.swipe-img')
    icons = soup.select('div.mp-category-item')
    indexLis = soup.select('ul.mp-like-list li.mp-like-item.mp-border-bottom')
    wrecommands = soup.select('#weekend-trip div.mp-product-item')
    for swiper in swipers:
      result['swipers'].append(swiper.attrs['src'])

    for icon in icons:
      iconItem = {}
      iconItem['iconUrl'] = icon.select('img')[0].attrs['src']
      iconItem['iconName'] = icon.select('div.keywords')[0].get_text()
      result['icons'].append(iconItem)

    for indexLi in indexLis:
      placeInfo = {}
      placeInfo['id'] = indexId
      placeInfo['name'] = indexLi.select('div.mp-like-info div.mp-like-title')[0].get_text()
      placeInfo['price'] = indexLi.select('.mpg-price-num')[0].get_text()
      placeInfo['stars'] = indexLi.select('span.mpf-starlevel')[0].attrs['data-score']
      placeInfo['comments'] = indexLi.select('span.mp-comment-num')[0].get_text()
      placeInfo['birefLocation'] = indexLi.select('span.mp-like-address')[0].get_text()
      placeInfo['detailUrl'] = indexLi.select('a.mp-fulllink')[0].attrs['href']
      placeInfo['sightId'] = re.findall('id=(.+?)&', placeInfo['detailUrl'])[0]
      placeInfo['imgUrl'] = indexLi.select('img.mp-like-img')[0].attrs['src']
      indexId = indexId + 1
      result['places'].append(placeInfo)

    for wrecommand in wrecommands:
      wItem = {}
      wItem['detailUrl'] = wrecommand.select('a')[0].attrs['href']
      wItem['imgUrl'] = wrecommand.select('a div.product-imgcontainer img')[0].attrs['src']
      wItem['name'] = wrecommand.select('a p.product-name')[0].get_text()
      wItem['desc'] = wrecommand.select('a p.product-desc')[0].get_text()
      result['weekendRecommand'].append(wItem)

    with open('result01.json', 'w', encoding='utf-8') as f:
      json.dump(result, f, ensure_ascii=False, indent=4)
    return result

  def parse_detail(self, detailUrl, sightId):
    print('开始爬取...')
    placeInfo = {}
    # 爬详情页
    try:
      detailSoup = BeautifulSoup(requests.get(detailUrl, timeout=TIME_OUT).text, 'lxml')
    except:
      print('连接超时,再次重试')
      detailSoup = BeautifulSoup(requests.get(detailUrl, timeout=TIME_OUT).text, 'lxml')
    # recommand
    placeInfo['location'] = detailSoup.select('p.mp-baseinfo-address-txt')[0].get_text()
    placeInfo['location'] = re.sub('\\ue608|F', '', placeInfo['location'])
    placeInfo['plans'] = detailSoup.select('span.mp-totalcommentnum')[0].get_text()
    placeInfo['describe'] = detailSoup.select('div.mp-headfeagure-title')[0].get_text()
    placeInfo['imgsNum'] = detailSoup.select('.mp-imgswipeicon-number')[0].get_text()
    placeInfo['headerTitle'] = detailSoup.select('.mp-header-title')[0].get_text()
    placeInfo['headerImg'] = detailSoup.select('.mp-headfigure-img')[0].attrs['src']
    placeInfo['score'] = detailSoup.select('span.mp-commentcard-score')[0].get_text()
    placeInfo['comPlan'] = detailSoup.select('.mp-totalcommentnum')[0].get_text()
    placeInfo['placeUrl'] = 'http:' + detailSoup.select('.mpg-flexbox-item.mp-border-left.mp-flexlink-con a')[0].attrs['href']
    # 获取comment
    placeInfo['commentList'] = self.parse_comment(sightId).get('data').get('commentList')
    time.sleep(1.0)

    placeInfo['recomTickets'] = []
    placeInfo['tickets'] = []
    reTickets = detailSoup.select('div.mp-promote div.mp-ticket-item')
    # recommandTickets
    for reTicket in reTickets:
      item = {}
      # 有些没有推荐
      try:
        item['title'] = reTicket.select('h6.mp-ticket-title')[0].get_text()
        if not len(item['title']):
          item['title'] = reTicket.select('h6.mp-ticket-onedaytitle')[0].get_text()
      except:
        item['title'] = ''
      item['desctag'] = reTicket.select('span.mp-ticket-desctag')[0].get_text()
      item['specificPrice'] = reTicket.select('.mp-price-num')[0].get_text()
      item['labelIcons'] = []
      for la in reTicket.select('ul.mp-ticket-labelcon span.mp-ticket-label'):
        item['labelIcons'].append(la.get_text())
      placeInfo['recomTickets'].append(item)

    ticketGroups = detailSoup.select('div.mp-ticket-group')
    # 爬取tickets
    for group in ticketGroups:
      # 大区块
      bigBlock = {}
      bigBlock['type'] = []
      bigBlock['bigName'] = group.select('h3.mp-ticket-type')[0].get_text()

      ticketLists = group.select('div.mp-ticket-list')
      # 小区块
      for oneT in ticketLists:
        typesContainer = {}
        typesContainer['roughPrice'] = oneT.select('div.mp-ticket-type-price .mp-price-num')[0].get_text()
        typesContainer['smallName'] = oneT.select('.mp-ticket-type-name')[0].get_text()
        typesContainer['specs'] = []
        specTs = oneT.select('div.mp-ticket-item')
        # 具体tickets
        for specT in specTs:
          tempSpec = {}
          try:
            tempSpec['title'] = specT.select('h6.mp-ticket-title')[0].get_text()
          except:
            tempSpec['title'] = ''
          tempSpec['desctag'] = specT.select('span.mp-ticket-desctag')[0].get_text()
          tempSpec['specificPrice'] = specT.select('.mp-price-num')[0].get_text()
          tempSpec['labelIcons'] = []
          for la in specT.select('ul.mp-ticket-labelcon span.mp-ticket-label'):
            tempSpec['labelIcons'].append(la.get_text())

          typesContainer['specs'].append(tempSpec)
        bigBlock['type'].append(typesContainer)
      placeInfo['tickets'].append(bigBlock)
      print(placeInfo)
    return placeInfo

  def parse_comment(self, sightId):
    return  json.loads(requests.get(COMMENT_URL.format(sightId), timeout=TIME_OUT).text)

  def parse_place(self, url):
    result = {
      'reference': [],
      'play': [],
      'tips': [],
      'transportation': []

    }
    requests.get(url, timeout=TIME_OUT)
    placeSoup = BeautifulSoup(requests.get(url, timeout=TIME_OUT).text, 'lxml')
    ares = placeSoup.select('.mp-area')
    texts = []

    referenceItems = ares[0].select('.mp-text-item')
    imgWraps = ares[1].select('.mp-imgwrap')
    textInfos = ares[2].select('div.mp-text-info p')
    # transportations = ares[3].select('.mp-area-content')
    # print(transportations)
    # 入园参考
    for item in referenceItems:
      temp = {}
      temp['title'] = item.select('.mp-text-title')[0].get_text()
      arr = []
      for p in item.select('div.mp-text-info p'):
        arr.append(p.get_text())
      temp['content'] = arr
      result['reference'].append(temp)

    temp={
      'imgs': [],
      'info': [],
      'text': []
    }
    # 特色玩法
    for img in imgWraps:
    
      for im in img.select('img.mp-img'):
        temp['imgs'].append(im.attrs['data-original-src'])

      for info in img.select('p.mp-imginfo'):
        temp['info'].append(info.get_text())
    
    for text in ares[1].select('.mp-text-item div.mp-text-info'):
      temp['text'].append(text.get_text())


    obj = []
    for index in range(len(temp.get('imgs'))):
      tempObj = {}
      try:
        tempObj['img'] = temp['imgs'][index]
        tempObj['info'] = temp['info'][index]
        tempObj['text'] = temp['text'][index]
      except:
        tempObj = {}
      obj.append(tempObj)

    result['play'] = obj
    # 温馨提示
    for text in textInfos:
      texts.append(text.get_text())
    
    result['tips'] = texts


    myMap ={
      'mapImg': '',
      'routes': []
    }
    # 交通
    # for tr in transportations[0].select('.mp-text-item'):
    #   temp = {}
    #   temp['rName'] = tr.select('.mp-text-title')[0].get_text()
    #   for one_route in tr.select('.mp-text-info p'):
    #     arr = []
    #     arr.append(one_route.get_text())
    #   temp['ro'] = arr 
    #   myMap['routes'].append(temp)
    # result['transportation'] = myMap
    return result

if __name__ == '__main__':
  begin_time = time.time()
  spider = CrawlQunar()
  spider.parse_detail('http://touch.piao.qunar.com/touch/detail.htm?id=1405179041&from=as_recommend_sight', '1405179041')
  end_time = time.time()
  print(end_time - begin_time)
