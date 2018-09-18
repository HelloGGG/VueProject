<template>
    <div class="ticket border-bottom">
      <div class="title">嘉兴乌镇东栅大门票</div>
      <div class="can-buy">
        <span class="iconfont time-icon">&#xe675;</span>
        23:45前可订明日
      </div>
      <div class="tips">
        <div class="tip">自营</div>
        <div class="tip">条件退</div>
      </div>
      <div class="price-book">
        <div class="price"><span>¥</span>200</div>
        <div class="book" @click="handleBookClick">预定</div>
      </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'TicketInfo',
  methods: {
    handleBookClick () {
      this.showMask(true)
    },
    ...mapMutations(['showMask'])
  }
}
</script>

<style lang="stylus" scoped>
  .custom
    font-size: .4rem
    color: #f76e6e
  .time-icon
    font-size: .24rem
    color: #00afc7
  .ticket
    position: relative
    background: #fff
    padding: .2rem
    color: #616161
    .title
      font-size: .3rem
      line-height: .52rem
    .can-buy
      font-size: .24rem
      line-height: .32rem
      height: .32rem
    .tips
      display: flex
      margin-top: .1rem
      .tip
        box-sizing: border-box
        color: #00afc7
        font-size: .2rem
        line-height: .32rem
        height: .32rem
        margin-right: .1rem
    .price-book
      position: absolute
      top: .2rem
      right: .2rem
      color: #ff9800
      text-align: center
      .price
        font-size: .4rem
        line-height: .4rem
        span
          font-size: .24rem
      .book
        height: .6rem
        font-size: .28rem
        background-image: linear-gradient(130deg, #ffab1e 37%, #ff8c12 100%)
        color: #fff
        line-height: .6rem
        padding: .02rem .5rem
        border-radius: .1rem
</style>
