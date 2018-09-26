<template>
  <div>
    <place-title>交通和到达</place-title>
    <div class="play-content">
      <div class="play-map">
        <img src="http://api.map.baidu.com/staticimage/v2?ak=D0ba2606b334fb2565df2646e9f8a479&center=120.494465,30.754749&width=370&height=200&zoom=14&scale=2&markers=120.494465,30.754749&markerStyles=-1,http://simg1.qunarzz.com/piao/images/map_icon.png" alt="">
      </div>
      <div
        v-for="(value, key, index) in transportation"
        :key="index"
      >
      <template v-if="key === 'routes'">
        <div
          v-for="(item, index) in value"
          :key="index+100"
        ></div>
        <p class="drive-route">{{item.rName}}</p>
        <p class="spec-route">{{item.ro[0]}}</p>
      </template>
      </div>
    </div>
    <div class="c-margin"></div>
  </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
export default {
  props: {
    transportation: Object
  },
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
