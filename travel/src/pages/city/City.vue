<template>
  <div>
    <city-header></city-header>
    <city-search></city-search>
    <city-list></city-list>
    <city-alpha-bet></city-alpha-bet>
  </div>
</template>

<script>
import CityHeader from './components/CityHeader'
import CitySearch from './components/CitySearch'
import CityList from './components/CityList'
import CityAlphaBet from './components/CityAlphaBet'
export default {
  name: 'City',
  components: {
    CityHeader,
    CitySearch,
    CityList,
    CityAlphaBet
  }
}
</script>

<style lang="stylus" scoped>
  html
    overflow-y: hidden
</style>
