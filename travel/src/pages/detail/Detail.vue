<template>
  <div>
    <detail-header></detail-header>
    <detail-banner></detail-banner>
    <detail-brief-info></detail-brief-info>
    <detail-recommand></detail-recommand>
    <detail-ticket></detail-ticket>
    <detail-comment></detail-comment>
    <detail-book></detail-book>
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
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
