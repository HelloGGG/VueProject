<template>
  <div class="b-wrapper" v-show="isShowMask">
    <div class="b-mask" @click="handleCloseClick"></div>
    <div class="b-content">
      <div class="b-title">嘉兴乌镇东栅+西栅大门票</div>
      <div class="b-price"><span>¥ </span><span class="emphasize">200</span> /张</div>
      <div class="b-calendar">价格日历</div>
      <div class="calendar-tags">
        <day-tag v-for="(item, index) in days" :key="index"
          :class="{disabled: !item.canBuy}"
          ref="tag"
          @click.native="handleDayClick(index)"
        >
          <template slot="day">{{item.name}}</template>
          <template slot="specific">{{item.day}}</template>
        </day-tag>
      </div>
      <div class="tip-info">需要在游玩前1天的23:45前预订</div>
      <div class="btn-book" @click="hanldeBookClick">立即预定</div>
      <div class="iconfont b-close" @click="handleCloseClick">&#xe61a;</div>
    </div>
  </div>
</template>

<script>
import DayTag from 'common/DayTag'
import { mapState, mapMutations } from 'vuex'
export default {
  props: {
    days: Array
  },
  name: 'DetailBook',
  components: {
    DayTag
  },
  data () {
    return {
      isActived0: true,
      isActived1: false,
      isActived2: false,
      isActived: false
    }
  },
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
    handleDayClick (index) {
      for (let i = 0; i < this.days.length; i++) {
        var tagEle = this.$refs.tag[i].$el
        if (!tagEle.classList.contains('disabled')) {
          i === index ? tagEle.classList.add('actived') : tagEle.classList.remove('actived')
        }
      }
    },
    ...mapMutations(['showMask'])
  }
}
</script>

<style lang='stylus' scoped>
  @import '~styles/variable.styl'
  .disabled
    color: #9e9e9e !important
    opacity: 0.4
  .actived
    background: $bg
    color: #fff !important
  .acti
    color: #fff !important
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
