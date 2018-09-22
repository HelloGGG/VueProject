<template>
  <div>
    <router-link
      tag="div"
      class="banner"
      @click="handleBannerClick"
      to="/picPreview"
    >
      <img :src="headerImg" alt="">
      <div class="banner-info">
        <div class="iconfont pic-num">&#xe600;<span>{{imgsNum}}</span></div>
        <div class="place-name">{{describe}}</div>
      </div>
      <div class="mask"></div>
      <div class="backto iconfont"
          @click.stop="handleBackClick"
          v-show="backShow"
      >&#xe624;</div>
    </router-link>
    <gallery
      @close="handleClose"
      v-show="show"
    ></gallery>
  </div>
</template>

<script>
import Gallery from 'common/Gallery'
import DetailHeader from './DetailHeader'
export default {
  props: {
    imgsNum: String,
    describe: String,
    headerImg: String
  },
  name: 'DetailBanner',
  components: {
    Gallery,
    DetailHeader
  },
  data () {
    return {
      show: false,
      backShow: true
    }
  },
  methods: {
    handleClose () {
      this.show = false
    },
    handleBannerClick () {
      this.show = true
    },
    handleBackClick () {
      this.$router.push('/')
    },
    handleScroll () {
      let top = document.documentElement.scrollTop
      this.backShow = top <= 0
    }
  },
  activated () {
    window.addEventListener('scroll', this.handleScroll)
  },
  // 全局事件解绑
  deactivated () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="stylus" scoped>
  .banner
    position: relative
    overflow: hidden;
    height: 0;
    width: 100%;
    padding-bottom: 55%;
    img
      width: 100%
    .banner-info
      position: absolute
      color: #fff
      left: 0
      right: 0
      bottom: 0
      padding: .2rem .2rem 0.35rem .2rem
      .pic-num
        line-height: .4rem
        height: .4rem
        margin-bottom: .15rem
        font-size: .25rem
        background: rgba(0, 0, 0, 0.5)
        width: 1.2rem
        border-radius: .2rem
        text-align: center
        span
          margin-left: .1rem
      .place-name
        font-size: .36rem
    .mask
      position: absolute
      left: 0
      right: 0
      bottom: 0
      min-height: .5rem
      background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.8))
    .backto
      position: absolute
      top: .2rem
      left: .2rem
      width: .72rem
      line-height: .72rem
      color: #fff
      text-align: center
      background: rgba(0,0,0,0.5)
      border-radius: .36rem
</style>
