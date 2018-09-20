<template>
  <div>
    <place-title>交通和到达</place-title>
    <div class="play-content">
      <div class="play-map">
        <img src="http://api.map.baidu.com/staticimage/v2?ak=D0ba2606b334fb2565df2646e9f8a479&center=120.494465,30.754749&width=370&height=200&zoom=14&scale=2&markers=120.494465,30.754749&markerStyles=-1,http://simg1.qunarzz.com/piao/images/map_icon.png" alt="">
      </div>
      <p class="drive-route">自驾路线</p>
      <p class="spec-route">1、上海</p>
      <p class="spec-route">（1）从上海浦东机场上高速，走申嘉湖高速（S32→S12），在乌镇出口下，全程105公里左右。</p>
      <p class="spec-route">（2）从上海出发，走沪杭高速（A8）新命名沪昆高速【G60】（过嘉兴东下一站转）→乍嘉苏高速（苏嘉杭高速）→常台高速）【G15W】苏州方向（到观音桥转）→申嘉湖高速【S12】湖州方向→乌镇出口下。全程140公里左右。</p>
      <p class="spec-route">2、杭州</p>
      <p class="spec-route">（1）走沪杭高速新命名沪昆高速【G60】往上海方向开，从桐乡的高桥出口下，走迎宾大道，往桐乡方向开，在桐乡绕城公路一个立交桥处有乌镇方向的指示牌，看指示牌转即可。（优先推荐）</p>
      <p class="spec-route">（2）沪杭高速新命名沪昆高速【G60】到长安或屠甸出口下（或者走320国道）到桐乡，再经桐乡到达乌镇。 80公里左右。</p>
      <p class="spec-route">（3）杭州湾跨海大桥（沈海高速【G15】）→乍嘉苏高速【S11】（苏嘉杭高速）→申嘉湖高速【S12】乌镇出口下。</p>
      <p class="spec-route">3、苏州到乌镇</p>
      <p class="spec-route">（1）走乍嘉苏高速（常台高速）【G15W】到与申嘉湖高速【S12】的交叉口（观音桥），转上申嘉湖高速【S12】（湖州方向），到乌镇出口下。80公里左右。</p>
      <p class="spec-route">（2）走乍嘉苏高速（常台高速）【G15W】（也叫苏嘉杭高速）到嘉兴开发区出口（或者一级公路，苏州--吴江--嘉兴--乌镇）到乌镇。 100公里左右。</p>
      <p class="spec-route">4、南京</p>
      <p class="spec-route">（2）走杭宁高速（长深高速【G25】）（往杭州方向）→申嘉湖高速【S12】（往嘉兴、上海方向）乌镇出口下。300公里左右。</p>
    </div>
    <div class="c-margin"></div>
  </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
export default {
  name: 'PlaceTransport',
  components: {
    PlaceTitle
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .c-margin
    componentMargin()
  .play-content
    padding: .2rem
    .play-map
      height: 0
      width: 100%
      padding-bottom: 59.15%
      img
        width: 100%
    .drive-route
      padding-top: .1rem
      font-weight: bold
      line-height: .42rem
      color: #333
      font-size: .28rem
    .spec-route
      comment()
      font-size: .28rem
</style>
