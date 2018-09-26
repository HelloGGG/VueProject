<template>
  <div>
    <loading-tip v-if="isLoading">加载中</loading-tip>
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
      :placeUrl="placeUrl"
    ></detail-brief-info>
    <detail-recommand
      v-if="recomTickets.length"
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
    <detail-book
      @showCalendar="handleShowCalendar"
    ></detail-book>
    <my-calendar
    v-show="isCalendarShow"
    :currentYear="currentYear"
    :currentMonth="currentMonth"
    @showCalendar="handleShowCalendar"
  ></my-calendar>
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
import LoadingTip from 'common/LoadingTip'
import MyCalendar from 'common/MyCalendar'
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
    DetailBook,
    LoadingTip,
    MyCalendar
  },
  computed: {
    ...mapState(['defaultSightId', 'defaultDetailUrl']),
    currentYear () {
      return (new Date()).getFullYear()
    },
    currentMonth () {
      return (new Date()).getMonth() + 1
    }
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
      placeUrl: '',
      headerImg: '',
      location: '',
      plans: '',
      recomTickets: [],
      tickets: [],
      isLoading: true,
      latestSightId: '',
      isCalendarShow: false
    }
  },
  methods: {
    handleTicketMore () {
      this.isTicketMore = true
    },
    getDetailData () {
      axios.get('/api/detail?sightId=' + this.$store.state.sightId + '&detailUrl=' + this.$store.state.detailUrl).then(this.getDetailDataSucc)
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
        this.placeUrl = data.placeUrl
        this.headerImg = data.headerImg
        this.location = data.location
        this.plans = data.plans
        this.recomTickets = data.recomTickets
        this.tickets = data.tickets
      }
      this.isLoading = false
    },
    handleShowCalendar (flag) {
      this.isCalendarShow = flag
    }
  },
  mounted () {
    this.getDetailData()
    this.isLoading = true
    this.latestSightId = this.$store.state.sightId
  },
  activated () {
    if (this.latestSightId !== this.$store.state.sightId) {
      this.getDetailData()
      this.isLoading = true
      this.latestSightId = this.$store.state.sightId
    }
  },
  updated () {
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
