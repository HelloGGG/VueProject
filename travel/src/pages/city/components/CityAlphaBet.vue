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
      touchStatus: false,
      startY: 0,
      timer: null
    }
  },
  name: 'CityAlphaBet',
  updated () {
    this.startY = this.$refs['A'][0].offsetTop
  },
  methods: {
    handleClick (e) {
      this.$emit('change', e.target.innerText)
    },
    handleTouchStart () {
      this.touchStatus = true
    },
    handleTouchMove (e) {
      if (this.touchStatus) {
        if (this.timer) {
          clearTimeout(this.timer)
        }
        var endY = e.touches[0].clientY
        var index = Math.floor((endY - this.startY) / 15)
        this.timer = setTimeout(() => {
          if (index >= 0 && index <= this.letters.length) {
            this.$emit('change', this.letters[index])
          }
        }, 16)
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
    top: 0
    right: 0
    bottom: 0
    justify-content: center
    .alpha
     line-height: .36rem
     margin:.02rem 0
     color: $bg
</style>
