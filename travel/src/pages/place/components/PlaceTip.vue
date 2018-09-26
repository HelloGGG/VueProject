<template>
  <div>
    <place-title>温馨提示</place-title>
    <div class="tip-content">
      <p
        v-for="(tip, index) in tips"
        :key="index"
        class="spec-tip">{{tip}}</p>
    </div>
    <div class="c-margin"></div>
  </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
export default {
  props: {
    tips: Array
  },
  name: 'PlaceTip',
  components: {
    PlaceTitle
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .c-margin
    componentMargin()
  .tip-content
    padding: 0 .2rem
    .t-title
      font-weight: bold
      color: #333
      line-height: .42rem
      font-size: .28rem
    .spec-tip
      comment()
</style>
