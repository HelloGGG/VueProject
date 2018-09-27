<template>
   <div>
     <place-title>特色玩法</place-title>
     <div
      v-for="(value, index) in play"
      :key="index"
      class="play-item">
       <div class="img-wrapper">
        <img :src="value.img" alt="">
        <div class="img-descri">{{value.info}}</div>
       </div>
       <p class="play-words">{{value.text}}</p>
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
