<template>
  <div class="eval-comment">
    <div class="eval-score border-bottom">
      综合评分
      <div class="iconfont stars">&#xe642;&#xe642;&#xe642;&#xe642;&#xe642;</div>
      <div class="spec-socre"><span>4.9</span>/5分</div>
    </div>
    <ul class="eval-tags"
      ref="tags"
      :class="{intercept: isActive}"
      >
      <li class="tag"
      v-for="(item, index) in tags"
      :key="index"
      @click="handleTagClick(index)"
      ref="tag"
      >{{item}}</li>
    </ul>
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
    <user-comm v-for="user in users"
     :key="user.id"
     :user="user"
    ></user-comm>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
import UserComm from './UserComm'
export default {
  props: {
    users: Array
  },
  name: 'EvalMainComment',
  data () {
    return {
      listmodeShow: false,
      isActive: false,
      isControl: false,
      tags: [
        '全部',
        '好评 12707',
        '有图 12707',
        '待改善 12707',
        '最新',
        '来自订单 11742',
        '江南水乡 956',
        '江南水乡 956',
        '江南水乡 956',
        '江南水乡 956',
        '江南水乡 956',
        '江南水乡 956'
      ]
    }
  },
  components: {
    ListMore,
    UserComm
  },
  methods: {
    handleTagClick (index) {
      let tagsEl = this.$refs.tag
      for (let i = 0; i < this.tags.length; i++) {
        i === index ? tagsEl[i].classList.add('active') : tagsEl[i].classList.remove('active')
      }
    },
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    }
  },
  mounted () {
    this.$refs.tag[0].classList.add('active')
    console.log(this.$refs.tags.offsetHeight)
    this.isControl = this.$refs.tags.offsetHeight > 84
    this.isActive = this.isControl
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .intercept
    overflow: hidden
    max-height: 1.4rem
  .active
    background-image: linear-gradient(135deg, #0fdfff 0, #00cbe6 100%)
    color: #fff !important
  .eval-comment
    .eval-score
      display: flex
      flex-flow: row nowrap
      line-height: .5rem
      height: .5rem
      font-size: .28rem
      padding: .2rem .4rem 0 .4rem
      align-items: center
      .stars
        position: relative
        top: -.05rem
        font-size: .2rem
        color: #ffb436
        margin: 0 .4rem 0 .2rem
      .spec-socre
        font-size: 0.25rem
        span
          color: $emphasizeColor
    .eval-tags
      padding: .3rem .4rem 0 .4rem
      .tag
        display: inline-block
        border: .02rem solid #e0e0e0
        border-radius: 0.1rem
        height: .4rem
        line-height: .4rem
        margin: .15rem .12rem 0 0
        font-size: .24rem
        color: #616161
        padding: .05rem .1rem
</style>
