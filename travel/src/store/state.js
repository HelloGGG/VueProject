var defaultCity = '绍兴'
var defaultSightId = '3270977086'
var defaultDetailUrl = 'http://touch.piao.qunar.com/touch/detail.htm?id=3270977086&from=as_recommend_sight'
var defaultPlace = 'http://touch.piao.qunar.com/touch/sight/introduction.htm?sightId=4085764381'
try {
  if (localStorage.city) {
    defaultCity = localStorage.city
  }
} catch (e) {
  console.log('localStorage error')
}

try {
  if (localStorage.sightId) {
    defaultSightId = localStorage.sightId
  }
} catch (e) {
  console.log('localStorage error')
}

try {
  if (localStorage.detailUrl) {
    defaultDetailUrl = localStorage.detailUrl
  }
} catch (e) {
  console.log('localStorage error')
}

try {
  if (localStorage.place) {
    defaultPlace = localStorage.place
  }
} catch (e) {
  console.log('localStorage error')
}

export default {
  city: defaultCity,
  currentPic: 0,
  sightId: defaultSightId,
  detailUrl: defaultDetailUrl,
  place: defaultPlace,
  bookTicketStatus: false,
  bookTicketTitle: '',
  bookTicketPrice: '',
  otherDay: '?',
  otherMonth: '?'

}
