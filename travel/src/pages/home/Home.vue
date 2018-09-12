<template>
    <div>
        <home-header></home-header>
        <home-swiper></home-swiper>
        <home-icons></home-icons>
        <home-recommand></home-recommand>
        <home-weekend></home-weekend>
    </div>
</template>

<script>
import HomeHeader from './components/HomeHeader'
import HomeSwiper from './components/HomeSwiper'
import HomeIcons from './components/HomeIcons'
import HomeRecommand from './components/HomeRecommand'
import HomeWeekend from './components/HomeWeekend'
export default {
  name: 'Home',
  components: {
    HomeHeader,
    HomeSwiper,
    HomeIcons,
    HomeRecommand,
    HomeWeekend
  }
}
</script>

<style scope>
</style>
