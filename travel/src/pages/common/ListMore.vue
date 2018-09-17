<template>
  <div class="container border-bottom iconfont">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'ListMore'
}
</script>

<style lang="stylus" scoped>
  .container
    text-align: center
    line-height: .88rem
    color: #616161
    font-size: .28rem
</style>
