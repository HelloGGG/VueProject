<template>
  <div class="header">
    <div class="header-left iconfont"
      @click="handleClick"
    >&#xe624;</div>
    <div class="header-title">景区图片</div>
  </div>
</template>

<script>
export default {
  name: 'PreviewHeader',
  methods: {
    handleClick () {
      this.$router.push('/detail/:id')
    }
  }
}
</script>

<style lang="stylus" scoped>
  .header
    font-size: .32rem
    text-align: center
    color: #333
    width: 100%
    height: .88rem
    z-index: 100
    .header-title
      width: 100%
      text-align: center
      line-height: .88rem
    .header-left
      position: absolute
      top: 0
      left: .1rem
      font-size: .48rem
      line-height: .88rem
</style>
