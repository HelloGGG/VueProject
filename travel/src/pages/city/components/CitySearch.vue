<template>
  <div class="search">
    <div class="domestic"
      :class="{activate: isActivate}"
      @click="handleClick">
      境内
      </div>
    <div class="overseas"
      :class="{activate: !isActivate}"
      @click="handleClick">
      境外·港澳台
      </div>
  </div>
</template>

<script>
export default {
  name: 'CitySearch',
  data () {
    return {
      isActivate: true
    }
  },
  methods: {
    handleClick () {
      this.isActivate = !this.isActivate
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .activate
    color: $bg
    background: #fff
  .search
    position: relative
    display: flex
    height: .4rem
    line-height: .4rem
    background: $bg
    padding: 0 1rem .2rem 1rem
    color: #fff
    text-align: center
    .domestic, .overseas
      flex: 1
      border: 1px solid #fff
      height: .4rem
      line-height: .4rem
    .overseas
      border-left: none
</style>
