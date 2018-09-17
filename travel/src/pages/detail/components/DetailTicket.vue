<template>
  <div>
    <div class="ticket-kind border-bottom">
      <span class="ticket-icon"></span>
        西栅
    </div>
    <div class="ticket-item">
      <div class="ticket-name">嘉兴乌镇西栅大门票</div>
      <div class="ticket-price">
        <span class="symbo">¥</span>
        165
        <span class="iconfont" @click="handleDownClick" v-show="!ticketShow">起 &#xe62e;</span>
        <span class="iconfont" @click="handleDownClick" v-show="ticketShow">起 &#xe62c;</span>
      </div>
      <ticket-info v-show="ticketShow"></ticket-info>
    </div>
    <list-more></list-more>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
import TicketInfo from 'common/TicketInfo'
export default {
  name: 'DetailTicket',
  data () {
    return {
      ticketShow: false
    }
  },
  components: {
    ListMore,
    TicketInfo
  },
  methods: {
    handleDownClick () {
      this.ticketShow = !this.ticketShow
    }
  }
}
</script>

<style lang="stylus" scoped>
  .ticket-kind
    display: flex
    align-items: center
    width: 100%
    line-height: .88rem
    font-size: .32rem
    align-items: center
    padding: 0 .2rem
    flex-flow: raw wrap
    height: .88rem
    .ticket-icon
      display: inline-block;
      width: .36rem;
      height: .36rem;
      background: url(http://s.qunarzz.com/piao/image/touch/sight/detail.png) 0 -.45rem no-repeat;
      margin-right: .05rem;
      background-size: .4rem 3rem;
  .ticket-item
    position: relative
    line-height: .88rem
    font-size: .3rem
    .ticket-name
      padding: 0 .2rem
    .ticket-price
      position: absolute
      top: 0
      right: .2rem
      font-size: .4rem
      color: #ff9800
      span
        font-size: .24rem
      span:nth-child(2), span:nth-child(3)
        color: #9e9e9e
</style>
