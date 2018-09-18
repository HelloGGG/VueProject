<template>
  <div class="tag">
      <div class="day"><slot name="day"></slot></div>
      <div class="specific"><slot name="specific"></slot></div>
  </div>
</template>

<script>
export default {
  name: 'DayTag'
}
</script>

<style lang="stylus" scoped>
  .tag
    box-sizing: border-box
    width: 22%
    padding: .05rem
    text-align: center
    border-radius: .1rem
    border: .02rem solid #bdbdbd;
    .day
      line-height: .36rem
      font-size: .28rem
      padding-top: .08rem
    .specific
      line-height: .32rem
      font-size: .24rem
      // color: #9e9e9e
</style>
