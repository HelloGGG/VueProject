import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    city: '上虞'
  },
  mutations: {
    changeCurrentCity (state, city) {
      state.city = city
    }
  }
})
