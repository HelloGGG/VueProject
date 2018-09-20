<template>
  <div class="user-wrapper">
    <div class="name-stars">
      <span class="u-name">{{user.name}}</span>
      <div class="starlevel">
        <span class="good iconfont" ref="good"></span>
        <span class="bad iconfont" ref="bad"></span>
      </div>
    </div>
    <div class="date">{{user.date}}</div>
    <img class="avatar" :src="user.avatar"/>
    <div class="words" :class="{intercept: isActive }" ref="words">
      {{user.words}}
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
      <img
      v-for="(img, index) in user.imgs"
      :key="index"
      class="img"
      :src="img"
      @click="handleImgClick(index)"
      >
    </div>
    <gallery :imgs="user.imgs"
          v-if="galleryShow"
          @close="handleClose"
    ></gallery>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import ListMore from 'common/ListMore'
import Gallery from 'common/Gallery'
export default {
  props: {
    user: Object
  },
  name: 'UserComm',
  components: {
    ListMore,
    Gallery
  },
  data () {
    return {
      listmodeShow: false,
      isActive: false,
      isControl: false,
      galleryShow: false
    }
  },
  methods: {
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    },
    handleImgClick (index) {
      this.galleryShow = true
      this.changeCurrentPic(index)
      console.log(this.originImgs)
    },
    handleClose () {
      this.galleryShow = false
    },
    ...mapMutations(['changeCurrentPic'])
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
  @import '~styles/minx.styl'
  .good
    color: #ffb436
    margin: 0
    font-size: 0.2rem
  .bad
    position: relative
    color: #ddd
    margin: 0
    font-size: 0.2rem
    right: .08rem
  .listmore-custom
    line-height: .5rem !important
  .intercept
    overflow: hidden
    max-height: 1.65rem
  .user-wrapper
    position: relative
    padding: .3rem
    .name-stars
      margin-top: .15rem
      padding-left: 1rem
      color: #9e9e9e
      font-size: .2rem !important
      .starlevel
        display: inline-block
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
