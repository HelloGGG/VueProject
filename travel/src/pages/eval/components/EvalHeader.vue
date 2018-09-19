<template>
  <div>
    <div class="header">
      <div class="h-left"></div>
      <div class="h-raiders"
        :class="{active: isSliderShow}"
        @click="handlePlanClick"
        >攻略
        <div
          class="tab-slider"
          :class="{toright: !isSliderShow}"
          ></div>
      </div>
      <div class="h-comment"
        :class="{active: !isSliderShow}"
        @click="handleCommentClick"
      >点评
      </div>
      <div class="h-right"></div>
      <router-link
        tag="div"
        class="iconfont icon-backto"
        to="/detail/:id"
        >&#xe624;</router-link>
    </div>
    <div class="h-main"></div>
  </div>
</template>

<script>
export default {
  name: 'EvalHeader',
  data () {
    return {
      isSliderShow: true
    }
  },
  methods: {
    handlePlanClick () {
      this.isSliderShow = true
      this.$emit('changeContent', true)
    },
    handleCommentClick () {
      this.isSliderShow = false
      this.$emit('changeContent', false)
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .active
    color: $bg
  .toright
    left: 2.62rem !important
  .h-main
    height: .88rem
  .header
    position: fixed
    right: 0
    left: 0
    display: flex
    line-height: .88rem
    height: .88rem
    background: #fff
    flex-flow: row nowrap
    font-size: .36rem
    text-align: center
    z-index: 100
    .h-left, .h-right
      flex: 1
    .h-raiders, .h-comment
      width: 1.62rem
    .h-raiders
      margin-right: 1rem
    .h-raiders, .h-comment
      position: relative
      .tab-slider
        position: absolute
        left: 0
        bottom: 0
        height: .04rem
        width: 100%
        background: $bg
        transition: all 1s
    .icon-backto
      position: absolute
      top: 0
      left: .4rem
      font-size: .4rem
</style>
