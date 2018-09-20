<template>
    <div class="ref-wrapper">
      <div class="ref-title border-bottom">入园参考</div>
      <div class="condion-wrapper"
          ref="words"
          :class="{intercept: isActive }"
      >
        <div class="condition">
        <div class="condi-title">开放时间</div>
          <p class="condi-cont">西栅：9:00-22:00；</p>
          <p class="condi-cont">东栅：夏令7:00-18:00，冬令7:00-17:30</p>
        </div>
        <div class="condition">
          <div class="condi-title">免票政策</div>
          <p class="condi-cont">凭本人有效证件即可进入 ：</p>
          <p class="condi-cont">· 国家旅游局颁发的国导证（IC卡）、领队证； </p>
          <p class="condi-cont">· 国务院、中央军委颁发的老干部离休证； </p>
          <p class="condi-cont">· 残疾证（中国残疾人联合会制发）、残疾军人证（中华人民民政部制发）；   </p>
          <p class="condi-cont">·  1.2米以下儿童。 </p>
          <p class="condi-cont">凭本人以下有效证件至景区接待中心办理相关手续进入： </p>
          <p class="condi-cont">· 中央新闻总署颁发的最新版本新闻记者证； </p>
          <p class="condi-cont">· 国家旅游局所颁发的旅行社经理资格证（附本人名片）； </p>
        </div>
      </div>
      <list-more
        v-if="isControl"
        class="border-topbottom listmore-custom"
        v-show="!listmodeShow"
        @click.native="handleListMoreClick"
      >查看更多 &#xe62e;</list-more>
      <div class="ref-margin"></div>
    </div>
</template>

<script>
import ListMore from 'common/ListMore'
export default {
  name: 'PlaceReference',
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
    this.isControl = this.$refs.words.offsetHeight > 105
    this.isActive = this.isControl
  }
}

</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  @import '~styles/minx.styl'
  .ref-margin
    height: .22rem
    width: 100%
    background: #f5f5f5
  .intercept
    overflow: hidden
    max-height: 1.5rem
  .listmore-custom
    color: #333
  .ref-wrapper
    box-sizing: border-box
    background: #fff
    .ref-title
      position: relative
      line-height: .88rem
      padding: 0 .35rem
      height: .88rem
      font-weight: bold
      color: #333
      font-size: .3rem
    .ref-title::after
      position: absolute
      top: .28rem
      left: .22rem
      display: inline
      content: ''
      background: $bg
      height: .28rem
      width: .05rem
      line-height: .5rem
      border-radius: .02rem
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
