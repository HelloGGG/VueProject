<template>
  <div class="icons border-bottom">
     <swiper :options="swiperOption">
      <swiper-slide v-for="(ls,index) in swiperSlides" :key="index">
        <div class="icon-warpper" v-for="(item, index) in ls" :key="index">
          <img :src="item.iconUrl" alt="">
          <p class="icon-desc">{{item.iconName}}</p>
        </div>
      </swiper-slide>
      <div class="swiper-pagination"  slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  props: {
    list: Array
  },
  data () {
    return {
      swiperOption: {
        pagination: {
          el: '.swiper-pagination'
        },
        loop: true
      }
    }
  },
  computed: {
    swiperSlides () {
      var pages = []
      this.list.forEach((item, index) => {
        var pageIndex = Math.floor(index / 8)
        if (!pages[pageIndex]) {
          pages[pageIndex] = []
          pages[pageIndex].push(item)
        } else {
          pages[pageIndex].push(item)
        }
      })
      return pages
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .icons >>> .swiper-slide
    display: flex
    flex-flow: row wrap
  .icons
    overflow: hidden
    padding: .2rem 0 .3rem 0
    background: #fff
    .icon-warpper
      width: 25%
      img
        display: block
        width: 1.1rem
        height 1.1rem
        margin: 0.1rem auto
      .icon-desc
        text-align: center
        font-size: 0.28rem
        margin-top: 0.1rem
        height: 0.36rem
        line-height: 0.36rem
        ellipsis()
</style>
