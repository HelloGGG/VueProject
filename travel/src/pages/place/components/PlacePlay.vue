<template>
   <div>
     <place-title>特色玩法</place-title>
     <div
      v-for="(value, key, index) in play[0]"
      :key="key"
      class="play-item">
       <div class="img-wrapper">
        <img :src="value[index]" alt="">
        <div class="img-descri">{{value[index]}}</div>
       </div>
       <p class="play-words">展出江南古床的博物馆，面积约1200多平方米，内收数十张明、清、近代的江南古床精品。</p>
     </div>
   </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
import ListMore from 'common/ListMore'
export default {
  props: {
    play: Array
  },
  name: 'PlacePlay',
  components: {
    PlaceTitle,
    ListMore
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .c-margin
    componentMargin()
  .play-item
    padding: .2rem
    .img-wrapper
      position: relative
      height: 0
      width: 100%
      padding-bottom: 59.15%
      img
        width: 100%
    .img-descri
      position: absolute
      left: 0
      right: 0
      bottom: 0
      height: .6rem
      line-height: .6rem
      background: rgba(0, 0, 0, .6)
      color: #fff
      text-align: center
    .play-words
      comment()
      padding-top: .15rem
      font-size: .28rem
</style>
