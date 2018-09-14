<template>
  <div class="alpha-bet">
    <div class="alpha"
        v-for="(item, key) in cities"
        :key="key"
        :ref="key"
        @click="handleClick"
        @touchstart="handleTouchStart"
        @touchmove="handleTouchMove"
        @touchend="handleTouchEnd"
    >
        {{key}}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    cities: Object,
    letters: Array
  },
  data () {
    return {
      touchStatus: false
    }
  },
  name: 'CityAlphaBet',
  methods: {
    handleClick (e) {
      this.$emit('change', e.target.innerText)
    },
    handleTouchStart () {
      this.touchStatus = true
    },
    handleTouchMove (e) {
      if (this.touchStatus) {
        this.letter = e.target.innerText
        var startY = this.$refs['A'][0].offsetTop
        var endY = e.touches[0].clientY
        var index = Math.floor((endY - startY) / 15)
        if (index >= 0 && index <= this.letters.length) {
          this.$emit('change', this.letters[index])
        }
      }
    },
    handleTouchEnd (e) {
      this.touchStatus = false
    }
  }
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
    width: .2rem
    z-index: 15
    margin-right: .1rem
    height: 100%
    justify-content: center
    .alpha
     line-height: .3rem
     margin:.02rem 0
     color: $bg
</style>
