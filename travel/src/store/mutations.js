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
  },
  showMask (state, info) {
    state.bookTicketStatus = info.status
    state.bookTicketTitle = info.title
    state.bookTicketPrice = info.specificPrice
  },
  changeDetail (state, detail) {
    state.sightId = detail.sid
    state.detailUrl = detail.did
    try {
      // 浏览器缓存,刷新还是刚刚的页面
      localStorage.sightId = detail.sid
      localStorage.detailUrl = detail.did
    } catch (e) {
      console.log('localStorage error')
    }
  }
}
