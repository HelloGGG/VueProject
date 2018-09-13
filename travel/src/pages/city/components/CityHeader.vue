<template>
  <div class="header">
    <router-link to="/">
      <div class="header-left iconfont">&#xe624;</div>
    </router-link>
      城市选择
  </div>
</template>

<script>
export default {
  name: 'CityHeader'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .header
    position: relative
    height: $headerHeight
    line-height: $headerHeight
    background: $bg
    color: #fff
    text-align: center
    font-size: .32rem
    .header-left
      width: 0.7rem
      position: absolute
      top: 0
      left: 0
      color: #fff
</style>
