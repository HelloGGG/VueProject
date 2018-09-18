<template>
  <div class="ticket-item">
      <div class="ticket-name">{{item.title}}</div>
      <div class="ticket-price">
        <span class="symbo">¥</span>
        {{item.price}}
        <span class="iconfont" @click="handleDownClick" v-show="!ticketShow">起 &#xe62e;</span>
        <span class="iconfont" @click="handleDownClick" v-show="ticketShow">起 &#xe62c;</span>
      </div>
      <ticket-info
      v-show="ticketShow"
      v-for="ritem in recommandList"
      :key="ritem.id"
      :tags="ritem.tags"
      >
        <template slot="title">{{ritem.title}}</template>
        <template slot="time">{{ritem.time}}</template>
        <template slot="price">{{ritem.price}}</template>
      </ticket-info>
    </div>
</template>

<script>
import TicketInfo from 'common/TicketInfo'
export default {
  props: {
    item: Object,
    recommandList: Array
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
