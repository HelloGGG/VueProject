export default {
  changeCurrentCity (state, city) {
    state.city = city
    // 浏览器隐身模式,或用户关闭本地存储会让localStorage抛出异常
    try {
      localStorage.city = city
    } catch (e) {
      console.log('localStorage error')
    }
  },
  changeCurrentPic (state, currentPic) {
    state.currentPic = currentPic
  }
}
