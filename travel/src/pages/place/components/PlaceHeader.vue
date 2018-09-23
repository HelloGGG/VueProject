<template>
  <div>
    <div class="pl-header">
      详情介绍
      <router-link tag="div" to="/detail" class="iconfont backto">&#xe624;</router-link>
    </div>
    <div class="header-padding"></div>
  </div>
</template>

<script>
export default {
  name: 'PlaceHeader'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .pl-header
    position: fixed
    line-height: .88rem
    height: .88rem
    background: $bg
    top: 0
    left: 0
    right: 0
    text-align: center
    color: #fff
    font-size: .32rem
    z-index: 100
    .backto
      position: absolute
      top: 0
      left: .2rem
      font-size: .4rem
  .header-padding
    width: 100%
    height: .88rem
</style>
