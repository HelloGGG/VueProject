<template>
  <div class="user-wrapper">
    <div class="name-stars">
      <span class="u-name">娟*娟</span>
      <span class="iconfont stars">&#xe642;&#xe642;&#xe642;&#xe642;&#xe642;</span>
    </div>
    <div class="date">2018-09-07</div>
    <img class="avatar" src="http://img1.qunarzz.com/ucenter/headshot/201308/12/734e34abd3ea98c57c43c4d7.jpg"/>
    <div class="words" :class="{intercept: isActive }" ref="words">
      最主要是方便，如果想一天来回的话真的是很好的选择！纯玩，尽情的玩，尽情的拍！乌镇已经商业化了，没有我期待的静...所以我觉得一天也够了…现在国内哪都是人~~这不是乌镇一个地方的缺点，只要是景点都这样。此团唯一不好的是，早上集合时我多等了快一个小时，十点出发，导游们通知的都是9点，呜呜...我只是想多睡会，哈哈😄
    </div>
    <div v-if="isControl">
        <list-more class="listmore-custom"
      v-show="listmodeShow"
      @click.native="handleListMoreClick"
      >&#xe62c;
      </list-more>
      <list-more class="listmore-custom"
        v-show="!listmodeShow"
        @click.native="handleListMoreClick"
      >&#xe62e;
      </list-more>
    </div>
    <div class="imgs-container">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
      <img  class="img" src="https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_240x240_7d7b0d6d.jpg" alt="">
    </div>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
export default {
  name: 'UserComm',
  components: {
    ListMore
  },
  data () {
    return {
      listmodeShow: false,
      isActive: false,
      isControl: false
    }
  },
  methods: {
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    }
  },
  mounted () {
    // var gContent = ''
    // var bContent = ''
    // for (let i = 0; i < this.user.stars; i++) {
    //   gContent += '&#xe642;'
    // }
    // for (let i = 0; i < 5 - this.user.stars; i++) {
    //   bContent += '&#xe642;'
    // }
    // // 页面元素挂载时初始化操作
    // this.$refs.good.innerHTML = gContent
    // this.$refs.bad.innerHTML = bContent
    this.isControl = this.$refs.words.offsetHeight > 105
    this.isActive = this.isControl
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .listmore-custom
    line-height: .5rem !important
  .intercept
    overflow: hidden
    max-height: 2.1rem
  .user-wrapper
    position: relative
    padding: .3rem
    .name-stars
      margin-top: .15rem
      padding-left: 1rem
      color: #9e9e9e
      font-size: .2rem !important
      .stars
        margin-left: .2rem
        color: #ffb436
        font-size: .2rem
    .date
      margin-top: .05rem
      padding-left: 1rem
      color: #9e9e9e
      font-size: .2rem
    .avatar
      position: absolute
      top: .3rem
      left: .3rem
      height: .8rem
      width: .8rem
      border-radius: .4rem
    .words
      padding-top: .3rem
      comment()
    .imgs-container
      white-space: nowrap
      word-break: keep-all
      max-height: 2.2rem
      overflow-x: auto
      .img
        display: inline-block
        width: 1.4rem
        height: 1.4rem
        margin-right: .05rem
</style>
