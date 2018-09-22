<template>
  <div>
    <detail-header :headerTitle="headerTitle"></detail-header>
    <detail-banner
      :imgsNum="imgsNum"
      :describe="describe"
      :headerImg="headerImg"
    ></detail-banner>
    <detail-brief-info
      :location="location"
      :score="score"
      :comPlan="comPlan"
    ></detail-brief-info>
    <detail-recommand
      v-if="recomTickets"
      :recomTickets="recomTickets"
    ></detail-recommand>
    <detail-ticket
      @ticketMore="handleTicketMore"
      :isTicketMore="isTicketMore"
      :tickets="tickets"
    ></detail-ticket>
    <detail-comment
      :commentList="commentList"
    ></detail-comment>
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
import axios from 'axios'
import { mapState } from 'vuex'
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
  computed: {
    ...mapState(['defaultSightId', 'defaultDetailUrl'])
  },
  data () {
    return {
      isTicketMore: false,
      score: '',
      comPlan: '',
      headerTitle: '',
      commentList: [],
      describe: '',
      imgsNum: '',
      headerImg: '',
      location: '',
      plans: '',
      recomTickets: [],
      tickets: []
    }
  },
  methods: {
    handleTicketMore () {
      this.isTicketMore = true
    },
    getDetailData () {
      axios.get('/api/detail?sightId=' + this.$store.state.defaultSightId + '&detailUrl=' + this.$store.state.defaultDetailUrl).then(this.getDetailDataSucc)
    },
    getDetailDataSucc (res) {
      console.log(res)
      if (res) {
        const data = res.data
        this.score = data.score
        this.comPlan = data.comPlan
        this.commentList = data.commentList
        this.headerTitle = data.headerTitle
        this.describe = data.describe
        this.imgsNum = data.imgsNum
        this.headerImg = data.headerImg
        this.location = data.location
        this.plans = data.plans
        this.recomTickets = data.recomTickets
        this.tickets = data.tickets
      }
    }
  },
  mounted () {
    this.getDetailData()
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
