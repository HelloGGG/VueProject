<template>
  <div>
    <detail-header></detail-header>
    <detail-banner></detail-banner>
    <div class="content"></div>
  </div>
</template>

<script>
import DetailBanner from './components/DetailBanner'
import DetailHeader from './components/DetailHeader'
export default {
  name: 'Detail',
  components: {
    DetailBanner,
    DetailHeader
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
