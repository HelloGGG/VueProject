<template>
<div>
  <div v-for="(ticket, index) in tickets" :key="index">
    <div class="ticket-kind border-bottom">
      <span class="ticket-icon"></span>
        {{ticket.bigName}}
    </div>
    <ticket
      v-for="(item, index) in ticket.type"
      :item="item"
      :key="index"
      >
    </ticket>
    <div class="c-margin"></div>
  </div>
</div>
</template>

<script>
import ListMore from 'common/ListMore'
import Ticket from './Ticket'
export default {
  props: {
    isTicketMore: Boolean,
    tickets: Array
  },
  name: 'DetailTicket',
  data () {
    return {
      ticketShow: false,
      isExist: true
    }
  },
  components: {
    ListMore,
    Ticket
  },
  computed: {
    ticketsCount () {
      return this.isTicketMore ? this.tickets.type.length : 2
    }
  },
  methods: {
    handleListMoreClick () {
      this.$emit('ticketMore')
      this.isExist = false
    }
  }
}
</script>

<style lang="stylus" scoped>
 .c-margin
   height: .2rem
   background: #f5f5f5
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
</style>
