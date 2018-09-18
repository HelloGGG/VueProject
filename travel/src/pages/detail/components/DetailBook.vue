<template>
  <div class="b-wrapper" v-show="isShowMask">
    <div class="b-mask" @click="handleCloseClick"></div>
    <div class="b-content">
      <div class="b-title">嘉兴乌镇东栅+西栅大门票</div>
      <div class="b-price"><span>¥ </span><span class="emphasize">200</span> /张</div>
      <div class="b-calendar">价格日历</div>
      <div class="calendar-tags">
        <div class="tag">
          <div class="day disabled">今天</div>
          <div class="specific">9月18号</div>
        </div>
        <div class="tag">
          <div class="day">今天</div>
          <div class="specific">9月18号</div>
        </div>
        <div class="tag">
          <div class="day">今天</div>
          <div class="specific">9月18号</div>
        </div>
        <div class="tag">
          <div class="day">今天</div>
          <div class="specific">9月18号</div>
        </div>
      </div>
      <div class="tip-info">需要在游玩前1天的23:45前预订</div>
      <div class="btn-book" @click="hanldeBookClick">立即预定</div>
      <div class="iconfont b-close" @click="handleCloseClick">&#xe61a;</div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'DetailBook',
  computed: {
    ...mapState(['isShowMask'])
  },
  methods: {
    handleCloseClick () {
      this.showMask(false)
    },
    hanldeBookClick () {
      this.showMask(true)
    },
    ...mapMutations(['showMask'])
  }
}
</script>

<style lang='stylus' scoped>
  @import '~styles/variable.styl'
  .b-mask
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    overflow: hidden
    z-index: 100
    background: rgba(0, 0, 0, 0.5)
  .b-content
    position: fixed
    left: 0
    right: 0
    bottom:0
    background: #fff
    z-index: 101
    padding: .1rem .2rem
    box-sizing: border-box
    .b-title
      line-height: .8rem
      font-size: .34rem
    .b-price
      line-height: .48rem
      font-size: .24rem
      color: #9e9e9e
      span:nth-child(1)
        color: $emphasizeColor
      .emphasize
        font-size: .36rem
        color: $emphasizeColor
    .b-calendar
      line-height: .65rem
      font-size: .26rem
      color: #333
    .calendar-tags
      display: flex
      flex-flow: row nowrap
      justify-content: space-between
      .tag
        box-sizing: border-box
        width: 24%
        padding: .1rem
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
    .tip-info
      padding: .14rem 0
      line-height: .36rem
      font-size: .24rem
      color: $emphasizeColor
    .btn-book
      width: 100%
      height: 1rem
      background: $emphasizeColor
      color: #fff
      text-align: center
      line-height: 1rem
      font-size: .4rem
    .b-close
      position: absolute
      top: .2rem
      right: .1rem
      font-size: .4rem
      color: #9e9e9e
</style>
