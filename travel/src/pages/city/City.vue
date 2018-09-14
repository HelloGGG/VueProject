<template>
  <div>
    <div class="header-search">
      <city-header></city-header>
      <city-search @changeAjax="handleChangeAjax"></city-search>
    </div>
    <city-list
      :cities="cities"
      :hotCities="hotCities"
      :letter="letter"
    ></city-list>
    <city-alpha-bet
      :cities="cities"
      :letters="letters"
      @change="handleChange"
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
      letter: ''
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
      axios.get('/api/cities.json').then(this.getCityDataSucc)
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
    handleChangeAjax (arg) {
      if (arg) {
        axios.get('/api/cities.json').then(this.getCityDataSucc)
      } else {
        axios.get('/api/foregin.json').then(this.getCityDataSucc)
      }
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
  .header-search
    position: absolute
    width: 100%
    z-index: 1
</style>
