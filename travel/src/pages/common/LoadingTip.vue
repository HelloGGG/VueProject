<template>
  <div>
    <div class="loading-mask"></div>
    <div class="tip-content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoadingTip'
}
</script>

<style lang="stylus" scoped>
  .loading-mask
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    background: rgba(0, 0, 0, .6)
    z-index: 100
  .tip-content
    position: fixed
    top: 50%
    left: 50%
    height: 1.5rem
    width: 2rem
    margin-top: -.75rem
    margin-left: -1rem
    background: #fff
    text-align: center
    line-height: 1.5rem
    z-index: 101
    border-radius: .2rem
</style>
