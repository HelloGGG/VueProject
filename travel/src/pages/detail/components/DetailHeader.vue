<template>
  <div
    class="header"
    :style="OpacityStyle">
    <router-link to="/">
      <div class="header-left iconfont">&#xe624;</div>
    </router-link>
      景点名称
  </div>
</template>

<script>
export default {
  name: 'DetailHeader',
  data () {
    return {
      OpacityStyle: {
        opacity: 0
      }
    }
  },
  methods: {
    handleScroll () {
      let top = document.documentElement.scrollTop
      this.OpacityStyle.opacity = top / 120
      this.OpacityStyle.opacity = this.OpacityStyle.opacity > 1 ? 1 : this.OpacityStyle.opacity
      this.$emit('changeShow', true)
    }
  },
  activated () {
    window.addEventListener('scroll', this.handleScroll)
  },
  deactivated () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .header
    position: fixed
    top: 0
    left: 0
    right: 0
    height: $headerHeight
    line-height: $headerHeight
    background: $bg
    color: #fff
    text-align: center
    font-size: .32rem
    z-index: 10
    .header-left
      width: 0.7rem
      position: absolute
      top: 0
      left: 0
      color: #fff
</style>
