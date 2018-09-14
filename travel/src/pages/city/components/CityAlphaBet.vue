<template>
  <div class="alpha-bet">
    <div class="alpha"
        v-for="(item, key) in cities"
        :key="key">
        {{key}}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    cities: Object
  },
  name: 'CityAlphaBet'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .alpha-bet
    display: flex
    flex-flow: column wrap
    align-items: center
    position: absolute
    right: 0
    top: 3.5rem
    width: .2rem
    z-index: 10
    margin-right: .1rem
    .alpha
     line-height: .3rem
     margin:.02rem 0
     color: $bg
</style>
