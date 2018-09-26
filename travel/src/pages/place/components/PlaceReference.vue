<template>
    <div class="ref-wrapper">
      <place-title>入园参考</place-title>
      <div class="condion-wrapper"
          ref="words"
          :class="{intercept: isActive }"
      >
        <div
          v-for="(item, index) in refercence"
          :key="index"
          class="condition">
        <div class="condi-title">{{item.title}}</div>
          <p
            v-for="pContent in item.content"
            :key="pContent.id"
            class="condi-cont"
          >{{pContent}}</p>
        </div>
      </div>
      <list-more
        v-if="isControl"
        class="border-topbottom listmore-custom"
        v-show="!listmodeShow"
        @click.native="handleListMoreClick"
      >查看更多 &#xe62e;</list-more>
      <div class="c-margin"></div>
    </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
import ListMore from 'common/ListMore'
export default {
  props: {
    reference: Array
  },
  name: 'PlaceReference',
  components: {
    ListMore,
    PlaceTitle
  },
  data () {
    return {
      listmodeShow: false,
      isActive: false,
      isControl: false
    }
  },
  computed: {
    randomNum () {
      return Math.random() * 10000 + 1
    }
  },
  methods: {
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    }
  },
  mounted () {
    this.isControl = this.$refs.words.offsetHeight > 105
    this.isActive = this.isControl
  }
}

</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  @import '~styles/minx.styl'
  .c-margin
    componentMargin()
  .intercept
    overflow: hidden
    max-height: 1.5rem
  .listmore-custom
    color: #333
  .ref-wrapper
    box-sizing: border-box
    background: #fff
    .condition
      .condi-title
        line-height: .42rem
        font-weight: bold
        font-size: .28rem
        color: #333
        padding:.1rem .2rem 0 .2rem
      .condi-cont
       comment()
       padding-left: .2rem
       font-size: .28rem
</style>
