<template>
  <div>
    <div class="ticket-item">
      <div class="ticket-name">{{item.smallName}}</div>
      <div class="ticket-price">
        <span class="symbo">¥</span>
            {{item.roughPrice}}
        <span class="iconfont" @click="handleDownClick" v-show="!ticketShow">起 &#xe62e;</span>
        <span class="iconfont" @click="handleDownClick" v-show="ticketShow">起 &#xe62c;</span>
      </div>
      <ticket-info
      class="custom-bg"
      v-for="(ritem, index) in item.specs"
      :key="index"
      :tags="ritem.labelIcons"
      v-show="ticketShow"
      >
        <template slot="title">{{ritem.title}}</template>
        <template slot="time">{{ritem.desctag}}</template>
        <template slot="price">{{ritem.price}}</template>
      </ticket-info>
    </div>
  </div>
</template>

<script>
import TicketInfo from 'common/TicketInfo'
export default {
  props: {
    item: Object,
    isTicketMore: Boolean
  },
  components: {
    TicketInfo
  },
  name: 'Ticket',
  data () {
    return {
      ticketShow: false
    }
  },
  methods: {
    handleDownClick () {
      this.ticketShow = !this.ticketShow
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .custom-bg
    background: #f5f5f5
  .ticket-item
    position: relative
    line-height: .88rem
    font-size: .3rem
    background: #fff
    .ticket-name
      margin-right: 1.8rem
      padding: 0 .2rem
      ellipsis()
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
