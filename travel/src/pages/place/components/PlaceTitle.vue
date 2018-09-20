<template>
  <div class="title-wrapper">
      <div class="title-title border-bottom"><slot></slot></div>
  </div>
</template>

<script>
export default {
  name: 'PlaceTitle'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .title-wrapper
    box-sizing: border-box
    background: #fff
    .title-title
      position: relative
      line-height: .88rem
      padding: 0 .35rem
      height: .88rem
      font-weight: bold
      color: #333
      font-size: .3rem
    .title-title::after
      position: absolute
      top: .28rem
      left: .22rem
      display: inline
      content: ''
      background: $bg
      height: .28rem
      width: .05rem
      line-height: .5rem
      border-radius: .02rem
</style>
