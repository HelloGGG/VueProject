<template>
  <div class="container" @click="handleContainerClick">
    <div class="content">
        <swiper :options="swiperOption" ref="mySwiper">
        <swiper-slide v-for="(item, index) in imgs" :key="index">
          <img class="gallery-pic" :src="item" alt="">
        </swiper-slide>
        <div class="swiper-pagination"  slot="pagination"></div>
      </swiper>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imgs: Array
  },
  name: 'Gallery',
  data () {
    return {
      swiperOption: {
        pagination: {
          el: '.swiper-pagination',
          type: 'fraction'
        },
        observeParents: true,
        observer: true,
        autoHeight: true
      }
    }
  },
  computed: {
    swiper () {
      return this.$refs.mySwiper.swiper
    }
  },
  methods: {
    handleContainerClick () {
      this.$emit('close')
    }
  },
  mounted () {
    this.swiper.slideTo(this.$store.state.currentPic, 0, false)
  }
}
</script>

<style lang="stylus" scoped>
  .container >>> .swiper-pagination
    bottom: 0.5rem
    color: #fff
  .container >>> .swiper-container
    position: static
    overflow: visible
  .container
    display: flex
    flex-direction: colmun
    align-items: center
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    background: #000
    z-index: 100
    .content
      width: 100%
      .gallery-pic
        width: 100%
</style>
