# import re
# import json
# import requests
# # url = 'http://touch.piao.qunar.com/touch/detail.htm?id=3413962493&from=as_recommend_sight'
# COMMENT_URL = 'https://touch.piao.qunar.com/touch/queryCommentsAndTravelTips.json?type=mp&pageSize=10&fromType=SIGHT&pageNum=1&sightId={}&tagType=0'
# resText = requests.get(COMMENT_URL.format('3911355788'), timeout=10).text
# obj = json.loads(resText)
# print(obj.get('data').get('commentList'))

# import time
# import datetime
# today = datetime.date.today()
# print(today.month)
# print(today.year)
# print(time.localtime(time.time()))

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
