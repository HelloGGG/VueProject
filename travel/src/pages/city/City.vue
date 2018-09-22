<template>
  <div>
    <city-header></city-header>
    <city-search
    :isShow="!show"
    @changeAjax="handleChangeAjax"
    @changeList="handleChangeList"
    :cities="cities"
    ></city-search>
    <city-list
      :cities="cities"
      :hotCities="hotCities"
      :letter="letter"
      v-show="show"
    ></city-list>
    <city-alpha-bet
      :cities="cities"
      :letters="letters"
      @change="handleChange"
      v-show="show"
    ></city-alpha-bet>
  </div>
</template>

<script>
import CityHeader from './components/CityHeader'
import CitySearch from './components/CitySearch'
import CityList from './components/CityList'
import CityAlphaBet from './components/CityAlphaBet'
import axios from 'axios'
export default {
  name: 'City',
  components: {
    CityHeader,
    CitySearch,
    CityList,
    CityAlphaBet
  },
  data () {
    return {
      hotCities: [],
      cities: {},
      letter: '',
      show: true
    }
  },
  computed: {
    letters () {
      var letters = []
      for (let i in this.cities) {
        letters.push(i)
      }
      return letters
    }
  },
  methods: {
    getCityData () {
      axios.get('/static/cities.json').then(this.getCityDataSucc)
    },
    getCityDataSucc (res) {
      console.log(res)
      if (res.data.ret && res.data.data) {
        const data = res.data.data
        this.hotCities = data.hotCities
        this.cities = data.cities
      }
    },
    handleChange (arg) {
      this.letter = arg
    },
    handleChangeAjax (arg, isShow) {
      this.show = isShow
      if (arg) {
        axios.get('/static/cities.json').then(this.getCityDataSucc)
      } else {
        axios.get('/static/foregin.json').then(this.getCityDataSucc)
      }
    },
    handleChangeList (arg) {
      this.show = arg
    }
  },
  mounted () {
    this.getCityData()
  }
}
</script>

<style lang="stylus" scoped>
  html, body
    overflow: hidden
    overflow-y: auto
</style>
