<template>
   <div>
     <place-title>特色玩法</place-title>
     <div class="play-item">
       <div class="img-wrapper">
        <img src="http://img1.qunarzz.com/sight/p0/1412/97/7a82745eeab480370103365e5e8ce67e.water.jpg_710x420_9120f22e.jpg" alt="">
        <div class="img-descri">江南百床馆</div>
       </div>
       <p class="play-words">展出江南古床的博物馆，面积约1200多平方米，内收数十张明、清、近代的江南古床精品。</p>
     </div>
    <div class="play-item">
      <div class="img-wrapper">
        <img src="http://img1.qunarzz.com/sight/p0/1412/12/9c7c8d7e9f2a7c01132579813372ae90.water.jpg_710x420_34bbb9b4.jpg" alt="">
        <div class="img-descri">宏源泰染坊</div>
      </div>
      <p class="play-words">宏源泰染坊始创于宋元年间，原址在南栅，清光绪迁址于此，系蓝印花布制作基地，也是蓝印花布制品集散中心。在宏源泰染坊，可以欣赏到祖祖辈辈留下的手艺。</p>
    </div>
    <div class="play-item">
      <div class="img-wrapper">
        <img src="http://img1.qunarzz.com/sight/p0/1412/14/cc393146879adbaeb7700a54525a5278.water.jpg_710x420_3aa4183c.jpg" alt="">
        <div class="img-descri">小桥流水</div>
      </div>
      <p class="play-words">桥是江南水乡古镇不可或缺的，大多始建或重建于明清，有些桥还题有桥联。</p>
    </div>
    <div class="c-margin"></div>
   </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
import ListMore from 'common/ListMore'
export default {
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
