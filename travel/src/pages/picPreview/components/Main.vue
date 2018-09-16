<template>
    <div class="main">
      <div class="pic-box" v-for="(url, index) in imgs" :key="index">
        <img :src="url"
          class="thumbnail"
          @click="handleBannerClick(index)"
        >
      </div>
      <gallery
        @close="handleClose"
        v-if="show"
        :imgs="imgs"
      ></gallery>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Gallery from 'common/Gallery'
export default {
  props: ['imgs', 'test'],
  name: 'PreviewMain',
  components: {
    Gallery
  },
  data () {
    return {
      show: false
    }
  },
  methods: {
    handleClose () {
      this.show = false
    },
    handleBannerClick (id) {
      this.show = true
      this.changeCurrentPic(id)
    },
    handleBackClick () {
      this.$router.push('/')
    },
    ...mapMutations(['changeCurrentPic'])
  }
}
</script>

<style lang="stylus" scoped>
  .main
    display: flex
    flex-flow: row wrap
    box-sizing: border-box
    background: #f5f5f5
    width: 100%
    padding: .1rem
    z-index: 1
    .pic-box
      display: block
      box-sizing: border-box
      width: 50%
      padding: 0.05rem
      .thumbnail
        width: 100%
</style>
