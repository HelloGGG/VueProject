<template>
  <div>
    <div class="ticket-kind border-bottom">
      <span class="ticket-icon"></span>
        西栅
    </div>
    <ticket
      v-for="(item, index) in ticketList"
      :item="item"
      :key="item.id"
      v-show="index < ticketsCount"
      :recommandList="item.recommandList">
    </ticket>
    <list-more v-if="isExist" @click.native="handleListMoreClick">查看剩余内容 &#xe62e;</list-more>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
import Ticket from './Ticket'
export default {
  props: {
    isTicketMore: Boolean
  },
  name: 'DetailTicket',
  data () {
    return {
      ticketShow: false,
      isExist: true,
      ticketList: [
        {
          id: '0001',
          title: '[周末]嘉兴乌镇西栅成人票',
          price: '165',
          recommandList: [
            {
              id: '001',
              title: '嘉兴乌镇东栅+西栅大门票',
              time: '23:45前可订明日',
              tags: ['自营', '无需换票', '条件退'],
              price: '165'
            }, {
              id: '002',
              title: '嘉兴乌镇西栅大门票',
              time: '23:30前可订明日',
              tags: ['自营', '条件退'],
              price: '150'
            }
          ]
        }, {
          id: '0002',
          title: '[平日]嘉兴乌镇西栅成人票',
          price: '155',
          recommandList: [
            {
              id: '001',
              title: '嘉兴乌镇东栅+西栅大门票',
              time: '23:45前可订明日',
              tags: ['自营', '无需换票', '条件退'],
              price: '155'
            }
          ]
        }, {
          id: '0003',
          title: '嘉兴乌镇西栅亲子票(1大1小)',
          price: '198',
          recommandList: [
            {
              id: '001',
              title: '嘉兴乌镇西栅大门票',
              time: '23:30前可订明日',
              tags: ['自营', '条件退'],
              price: '198'
            }
          ]
        }, {
          id: '0004',
          title: '【刷码入园】乌镇西栅成人票（含电子导游）',
          price: '135',
          recommandList: [
            {
              id: '001',
              title: '【刷身份证入园  电子票】乌镇东栅成人票+手机电子讲解',
              time: '可订明日',
              tags: ['无需换票', '条件退'],
              price: '135'
            }
          ]
        }
      ]
    }
  },
  components: {
    ListMore,
    Ticket
  },
  computed: {
    ticketsCount () {
      return this.isTicketMore ? this.ticketList.length : 2
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
