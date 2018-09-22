<template>
  <div>
    <eval-header @changeContent="handleChangeContent"></eval-header>
    <eval-main-plan
      v-for="user in users"
      :key="user.id"
      :user="user"
      v-if="isShowPlan"
    ></eval-main-plan>
    <eval-main-comment
      :users="users"
      v-if="!isShowPlan"
      :tags="tags"
      :commentAvgScore="commentAvgScore"
    ></eval-main-comment>
    <div
      class="top-wrapper"
      @click="handleTopClick"
      v-show="isTopShow"
    ><div class="iconfont toTop">&#xe635;</div></div>
    <div
      v-show="!isShowPlan"
      :class="{originWrapper: isOrigin, circleWrapper: !isOrigin}"
      @click="handleCommentClick"
    >
    <div
      ref="toComment"
      :class="{origin: isOrigin, circle: !isOrigin, animated:!isOrigin, jello:!isOrigin, 'delay-1s': !isOrigin}"
    >写点评</div>
    </div>
  </div>
</template>

<script>
import EvalHeader from './components/EvalHeader'
import EvalMainPlan from './components/EvalMainPlan'
import EvalMainComment from './components/EvalMainComment'
import axios from 'axios'
export default {
  name: 'Eval',
  components: {
    EvalHeader,
    EvalMainPlan,
    EvalMainComment
  },
  data () {
    return {
      isOrigin: true,
      isTopShow: false,
      isShowPlan: true,
      users: [],
      lastestSightId: '',
      tags: [],
      commentAvgScore: ''
    }
  },
  methods: {
    handleTopClick () {
      window.scrollTo(0, 0)
    },
    handleScroll () {
      let top = document.documentElement.scrollTop
      this.isTopShow = top > 150
      if (top === 0) {
        this.isOrigin = true
        this.$refs.toComment.innerText = '写点评'
      } else {
        this.isOrigin = false
        this.$refs.toComment.innerText = '点评'
      }
    },
    handleChangeContent (flag) {
      this.isShowPlan = flag
    },
    handleCommentClick () {
      console.log('commmit')
    },
    getEvalData () {
      axios.get('/api/comment?sightId=' + this.$store.state.sightId).then(this.getEvalDataSucc)
    },
    getEvalDataSucc (res) {
      console.log(res)
      if (res) {
        this.users = res.data.data.commentList
        this.tags = res.data.data.tagList
        this.commentAvgScore = res.data.data.commentAvgScore
      }
    }
  },
  mounted () {
    this.lastestSightId = this.$store.state.defaultSightId
    this.getEvalData()
  },
  activated () {
    if (this.isShowPlan) {
      window.addEventListener('scroll', this.handleScroll)
    }
    if (this.lastestSightId !== this.$store.state.defaultSightId) {
      this.getEvalData()
      this.lastestSightId = this.$store.state.defaultSightId
    }
  },
  deactivated () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .originWrapper
    box-sizing: border-box
    position: fixed
    display: flex
    align-items: center
    justify-content: center
    bottom: 0
    right: 0
    background: #fff
    line-height: 1rem
    height: 1rem
    padding: 0 .2rem
    width: 100%
    .origin
      width: 100%
      height: .72rem
      line-height: .72rem
      background: $bg
      color: #fff
      text-align: center
  .top-wrapper, .circleWrapper
    position: fixed
    display: flex
    align-items: center
    justify-content: center
    bottom: 1.38rem
    right: .2rem
    background: #fff
    line-height: 1rem
    width: 1rem
    height: 1rem
    border-radius: .5rem
    .toTop
      border-radius: .4rem
      color: $bg
      z-index: 100
      font-size: .8rem
    .circle
      background: $bg
      color: #fff
      width: .8rem
      height: .8rem
      line-height: .8rem
      text-align: center
      border-radius: .4rem
      font-size: .24rem
  .circleWrapper
    background: #fff
    bottom: .3rem
    transition: all 1s
</style>
