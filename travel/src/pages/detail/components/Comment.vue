<template>
  <div>
    <div class="content border-bottom">
      <div class="starlevel-datetime">
          <div class="starlevel">
            <span class="good iconfont" ref="good"></span>
            <span class="bad iconfont" ref="bad"></span>
          </div>
          <div class="datetime">{{user.name}}&nbsp;&nbsp;{{user.date}}</div>
      </div>
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
      <div class="pic-display">
        <div class="pic-wrap"
        @click="handleImgClick(index)"
        v-for="(item, index) in user.imgs"
        :key="index"
        >
          <img :src="item" alt="">
        </div>
      </div>
      </div>
      <gallery :imgs="originImgs"
          v-if="galleryShow"
          @close="handleClose"
      ></gallery>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Gallery from 'common/Gallery'
import ListMore from 'common/ListMore'
export default {
  props: {
    user: Object
  },
  name: 'Comment',
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
  computed: {
    originImgs () {
      var newImgs = []
      var arr = [...this.user.imgs]
      arr.forEach((value, index) => {
        newImgs.push(value.replace(/_228x168_.+?\.jpg/, ''))
      })
      return newImgs
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
    // 页面元素挂载时初始化操作
    this.$refs.good.innerHTML = gContent
    this.$refs.bad.innerHTML = bContent
    this.isControl = this.$refs.words.offsetHeight > 105
    this.isActive = this.isControl
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .intercept
    overflow: hidden
    max-height: 2.1rem
  .listmore-custom
    line-height: .48rem
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
  .content
    padding: .1rem .2rem .4rem .2rem
  .starlevel-datetime
    position: relative
    line-height: .6rem
  .datetime
    position: absolute
    top: 0
    right: 0
    font-size: .24rem
  .words
    comment()
  .pic-display
    display: flex
    flex-flow: row wrap
    .pic-wrap
      box-sizing: border-box
      width: 33.33%
      padding: .05rem
      img
        width: 100%
</style>
