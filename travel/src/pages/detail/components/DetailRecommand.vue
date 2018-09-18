<template>
  <div class="reco-container">
      <div class="reco-header border-bottom">
        <span class="iconfont custom">&#xe6be;</span>
        去哪儿推荐
    </div>
    <ticket-info
      v-for="item in recommandList"
      :key="item.id"
      :tags="item.tags"
      >
      <template slot="title">{{item.title}}</template>
      <template slot="time">{{item.time}}</template>
      <template slot="price">{{item.price}}</template>
    </ticket-info>
  </div>
</template>

<script>
import TicketInfo from 'common/TicketInfo'
export default {
  name: 'DetailRecommand',
  data () {
    return {
      recommandList: [
        {
          id: '001',
          title: '嘉兴乌镇东栅+西栅大门票',
          time: '23:45前可订明日',
          tags: ['自营', '无需换票', '条件退'],
          price: '200'
        }, {
          id: '002',
          title: '嘉兴乌镇西栅大门票',
          time: '23:30前可订明日',
          tags: ['自营', '条件退'],
          price: '150'
        }
      ]
    }
  },
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
