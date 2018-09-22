<template>
  <div>
    <div class="iconfont title">
      <span class="icon">&#xe616;</span>
      猜你喜欢</div>
      <router-link tag="div"
      class="recommand-box border-bottom"
      v-for="item in list"
      :key="item.id"
      to="/detail"
      @click.native="handleRecomClick(item.sightId, item.detailUrl)"
      >
        <img :src="item.imgUrl" alt="">
        <div class="info">
          <p class="place">{{item.name}}</p>
          <div class="starlevel">
            <span class="good iconfont" ref="good"></span>
            <span class="bad iconfont" ref="bad"></span>
            <span class="comment">{{item.comments}}</span>
          </div>
          <div class="price">
            <span class="price-num">
              {{item.price}}
            </span>
            起
            <p class="brief-location">{{item.birefLocation}}</p>
          </div>
        </div>
      </router-link>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'HomeRecommand',
  props: {
    list: Array
  },
  methods: {
    handleRecomClick (sightId, detailUrl) {
      this.changeDetail({
        sid: sightId,
        did: detailUrl
      })
    },
    renderStars () {
      for (let k = 0; k < this.list.length; k++) {
        var gContent = ''
        var bContent = ''
        var obj = this.list[k]
        var stars = Math.ceil(obj.stars)
        for (let i = 0; i < stars; i++) {
          gContent += '&#xe642;'
        }
        for (let i = 0; i < 5 - stars; i++) {
          bContent += '&#xe642;'
        }
        this.$refs.good[k].innerHTML = gContent
        this.$refs.bad[k].innerHTML = bContent
      }
    },
    ...mapMutations(['changeDetail'])
  },
  mounted () {
    this.renderStars()
  },
  activated () {
    this.renderStars()
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .good
    color: #ffb436
    margin: 0
    font-size: .2rem
  .bad
    position: relative
    color: #ddd
    margin: 0
    font-size: .2rem
    right: .08rem
  .title
    overflow: hidden
    width: 100%
    padding: .24rem .26rem
    .icon
      color: #f65f53
  .recommand-box
    display: flex
    img
      height: 2rem
      width: 2rem
      padding: .1rem
    .info
      flex-grow: 1
      padding: 0 .1rem
      .place
        margin-top: .4rem
        font-size: .32rem
        height: .44rem
        line-height: .44rem
      .starlevel
        margin: .2rem 0 .1rem 0
        .comment
          margin-top: .1rem
          margin-left: .2rem
          color: #616161
          font-size: .24rem
          line-height: .34rem
      .price
        position: relative
        color: #616161
        font-size: .24rem
        .price-num
          line-height: .6rem
          font-size: .4rem
          height: .4rem
          color: $emphasizeColor
        .brief-location
          position: absolute
          top: 0
          right: 0
</style>
