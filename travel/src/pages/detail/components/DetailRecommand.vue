<template>
  <div class="reco-container">
      <div class="reco-header border-bottom">
        <span class="iconfont custom">&#xe6be;</span>
        去哪儿推荐
    </div>
    <ticket-info></ticket-info>
  </div>
</template>

<script>
import TicketInfo from 'common/TicketInfo'
export default {
  name: 'DetailRecommand',
  components: {
    TicketInfo
  }
}
</script>

<style lang="stylus" scoped>
  .reco-container
    padding: .2rem 0
    background: #f5f5f5
    .reco-header
      box-sizing: border-box
      padding-left: .1rem
      font-size: .32rem
      line-height: .88rem
      height: .88rem
      color: #f76e6e
      background: #fff
</style>
