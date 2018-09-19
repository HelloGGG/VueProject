<template>
  <div>
    <detail-header></detail-header>
    <detail-banner></detail-banner>
    <detail-brief-info></detail-brief-info>
    <detail-recommand></detail-recommand>
    <detail-ticket @ticketMore="handleTicketMore" :isTicketMore="isTicketMore"></detail-ticket>
    <detail-comment></detail-comment>
    <detail-book :days="days"></detail-book>
  </div>
</template>

<script>
import DetailBanner from './components/DetailBanner'
import DetailHeader from './components/DetailHeader'
import DetailBriefInfo from './components/DetailBriefInfo'
import DetailRecommand from './components/DetailRecommand'
import DetailTicket from './components/DetailTicket'
import DetailComment from './components/DetailComment'
import DetailBook from './components/DetailBook'
export default {
  name: 'Detail',
  components: {
    DetailBanner,
    DetailHeader,
    DetailBriefInfo,
    DetailRecommand,
    DetailTicket,
    DetailComment,
    DetailBook
  },
  data () {
    return {
      isTicketMore: false,
      list: [
        {
          title: '成人票',
          children: [
            {
              title: '成人三日游',
              children: [{
                title: '某某旅游社提供'
              }]
            }
          ]
        }, {
          title: '儿童票'
        }, {
          title: '团体票'
        }
      ],
      days: [
        {
          canBuy: false,
          name: '今天',
          day: '9月18日'
        }, {
          canBuy: true,
          name: '明天',
          day: '9月19日'
        }, {
          canBuy: true,
          name: '后天',
          day: '9月20日'
        }, {
          canBuy: true,
          name: '其他日子',
          day: ''
        }
      ]
    }
  },
  methods: {
    handleTicketMore () {
      this.isTicketMore = true
    }
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
