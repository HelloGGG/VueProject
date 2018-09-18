<template>
  <div>
    <div class="content border-bottom">
      <div class="starlevel-datetime">
          <div class="starlevel">
            <span class="good iconfont" ref="good">&#xe642;&#xe642;&#xe642;
                <span class="bad iconfont" ref="bad">&#xe642;</span>
            </span>
          </div>
          <div class="datetime">{{user.name}}&nbsp;&nbsp;{{user.date}}</div>
      </div>
      <div class="words" :class="{intercept: isActive }">
        {{user.words}}
      </div>
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
    <list-more>查看全部评论 &#xe62d;</list-more>
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
      isActive: true,
      galleryShow: false,
    }
  },
  computed: {
    originImgs () {
      var newImgs = []
      var arr = [...this.user.imgs]
      console.log(this.imgs)
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
    for (let i = 0; i < user.stars; i ++) {
      gContent += '&#xe642;'
    }
     for (let i = 0; i < 5 - user.stars; i ++) {
      bContent += '&#xe642;'
    }
    this.$refs.good.$el.innerHTML = gContent
    this.$refs.bad.$el.innerHTML = bContent
  }
}
</script>

<style lang="stylus" scoped>
  .intercept
    overflow: hidden
    height: 2.1rem
  .listmore-custom
    line-height: .48rem
  .good
    color: #ffb436
    margin: 0
    font-size: 0.05rem
  .bad
    color: #ddd
    margin: 0
    font-size: 0.1rem
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
    line-height: .42rem
    font-size: .26rem
    color: #616161
    word-break: break-all
    word-wrap: break-word
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
