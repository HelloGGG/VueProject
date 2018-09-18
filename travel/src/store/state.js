var defaultCity = '上虞'
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
  isShowMask: false
}
