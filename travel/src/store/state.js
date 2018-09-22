var defaultCity = '绍兴'
try {
  if (localStorage.city) {
    defaultCity = localStorage.city
  }
} catch (e) {
  console.log('localStorage error')
}

export default {
  city: defaultCity,
  currentPic: 0,
  isShowMask: false,
  defaultSightId: '3270977086',
  defaultDetailUrl: 'http://touch.piao.qunar.com/touch/detail.htm?id=3270977086&from=as_recommend_sight'
}
