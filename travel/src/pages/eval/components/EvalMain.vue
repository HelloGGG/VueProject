<template>
  <div class="eval-main">
    <div class="eval-img-container">
      <img :src="user.imgs[0]" alt="">
      <div class="iconfont eval-icon">&#xe600;&nbsp;&nbsp;{{user.imgs.length}}</div>
    </div>
    <div class="eval-content">
      <div class="avatar-wrapper">
        <img  class="avatar" :src="user.avatar" alt="">
      </div>
      <div class="info">
        <div class="user-name">{{user.name}}</div>
         <div class="starlevel">
            <span class="good iconfont" ref="good"></span>
            <span class="bad iconfont" ref="bad"></span>
        </div>
      </div>
      <div class="date">{{user.date}}</div>
      <div class="eval-words" ref="words"  :class="{intercept: isActive }">
        {{user.words}}
      </div>
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
    <div class="m-m"></div>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
export default {
  props: {
    user: Object
  },
  name: 'EvalMain',
  components: {
    ListMore
  },
  data () {
    return {
      listmodeShow: false,
      isControl: false,
      isActive: false
    }
  },
  methods: {
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    }
  },
  mounted () {
    var gContent = ''
    var bContent = ''
    for (let i = 0; i < this.user.stars; i++) {
      gContent += '&#xe642;'
    }
    for (let i = 0; i < 5 - this.user.stars; i++) {
      bContent += '&#xe642;'
    }
    this.$refs.good.innerHTML = gContent
    this.$refs.bad.innerHTML = bContent
    this.isControl = this.$refs.words.offsetHeight > 105
    this.isActive = this.isControl
  }
}
</script>

<style lang="stylus" scoped>
  .m-m
    height: .25rem
    background: #f5f5f5
  .good
    color: #ffb436
    margin: 0
    font-size: 0.05rem
  .bad
    position: relative
    color: #ddd
    margin: 0
    font-size: 0.1rem
    right: .08rem
  .intercept
    overflow: hidden
    max-height: 2.1rem
  .listmore-custom
    line-height: .5rem !important
  .eval-img-container
    position: relative
    height: 0
    width: 100%
    padding-bottom: 48%
    overflow: hidden
    img
      width: 100%
    .eval-icon
      position: absolute
      bottom: .2rem
      right: .2rem
      width: 1.2rem
      height: .4rem
      background: rgba(0,0,0,.5)
      border-radius: .2rem
      font-size: .24rem
      color: #fff
      line-height: .4rem
      text-align: center
  .eval-content
    position: relative
    padding: .1rem .3rem
    .avatar-wrapper
      position: absolute
      display: flex
      align-items: center
      justify-content: center
      top: -.64rem
      left: .2rem
      width: 1.28rem
      height: 1.28rem
      border-radius: .8rem
      background: #fff
      .avatar
        width: 1.2rem
        height: 1.2rem
        border-radius: .6rem
    .info
      display: flex
      flex-flow: row nowrap
      line-height: .48rem
      height: .48rem
      font-size: .24rem
      padding-left: 1.3rem
      .user-name
        color: #616161
        margin-right: .2rem
        padding-top: .02rem
    .date
      position: absolute
      right: .4rem
      top: .22rem
      float: right
      color: #9e9e9e
    .eval-words
      line-height: .42rem
      font-size: .28rem
      color: #616161
      word-break: break-all
      word-wrap: break-word
      margin-top: .25rem
</style>
