<template>
    <div>
        <home-header></home-header>
        <home-swiper :list="swiperList"></home-swiper>
        <home-icons :list="iconsList"></home-icons>
        <home-recommand :list="recommandList"></home-recommand>
        <home-weekend :list="weekendList"></home-weekend>
    </div>
</template>

<script>
import HomeHeader from './components/HomeHeader'
import HomeSwiper from './components/HomeSwiper'
import HomeIcons from './components/HomeIcons'
import HomeRecommand from './components/HomeRecommand'
import HomeWeekend from './components/HomeWeekend'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'Home',
  components: {
    HomeHeader,
    HomeSwiper,
    HomeIcons,
    HomeRecommand,
    HomeWeekend
  },
  data () {
    return {
      swiperList: [],
      iconsList: [],
      recommandList: [],
      weekendList: [],
      latestCity: ''
    }
  },
  computed: {
    ...mapState(['city'])
  },
  methods: {
    getHomeData () {
      axios.get('/api/index.json?city=' + this.city).then(this.getHomeDataSucc)
    },
    getHomeDataSucc (res) {
      if (res.data.ret && res.data.data) {
        const data = res.data.data
        this.swiperList = data.swiperList
        this.iconsList = data.iconsList
        this.recommandList = data.recommandList
        this.weekendList = data.weekendList
      }
    }
  },
  mounted () {
    this.getHomeData()
    this.latestCity = this.city
  },
  // keep-alive 组件激活时调用
  activated () {
    if (this.latestCity !== this.city) {
      this.getHomeData()
      this.latestCity = this.city
    }
  }
}
</script>

<style scope>
</style>
