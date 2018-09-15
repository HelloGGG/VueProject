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
      weekendList: []
    }
  },
  methods: {
    getHomeData () {
      axios.get('/api/index.json').then(this.getHomeDataSucc)
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
  }
}
</script>

<style scope>
</style>
