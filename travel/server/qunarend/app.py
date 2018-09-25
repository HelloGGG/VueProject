from flask import Flask, jsonify, request
from crawlqunar import CrawlQunar
from urllib.parse import quote
app = Flask(__name__)
BASE_URL = 'http://touch.piao.qunar.com/touch/index_{}.html'
COMMENT_URL = 'https://touch.piao.qunar.com/touch/queryCommentsAndTravelTips.json?type=mp&pageSize=10&fromType=SIGHT&pageNum=1&sightId={}&tagType=0'

@app.route('/api/home')
def index():
  city = request.args.get('city')
  spider = CrawlQunar()
  return jsonify(spider.parse_index(BASE_URL.format(quote(city))))

@app.route('/api/detail')
def detail():
  sightId = request.args.get('sightId')
  detailUrl = request.args.get('detailUrl')
  spider = CrawlQunar()
  return jsonify(spider.parse_detail(detailUrl, sightId))

@app.route('/api/comment')
def comment():
  sightId = request.args.get('sightId')
  spider = CrawlQunar()
  return jsonify(spider.parse_comment(sightId))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')