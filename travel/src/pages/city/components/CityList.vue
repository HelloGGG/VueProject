<template>
  <div class="city-list" ref="tab">
    <div class="wrapper">
      <div class="hot-city">
        <div class="title">热门城市</div>
        <div class="item-box">
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
          <div class="s-item">北京</div>
        </div>
      </div>
      <div class="sort">
        <div class="title">字母排序</div>
        <div class="item-box sort-padding">
          <div class="sort-item">A</div>
          <div class="sort-item">B</div>
          <div class="sort-item">C</div>
          <div class="sort-item">D</div>
          <div class="sort-item">E</div>
          <div class="sort-item">F</div>
          <div class="sort-item">G</div>
          <div class="sort-item">H</div>
          <div class="sort-item">I</div>
          <div class="sort-item">J</div>
          <div class="sort-item">K</div>
          <div class="sort-item">L</div>
          <div class="sort-item">M</div>
          <div class="sort-item">N</div>
          <div class="sort-item">O</div>
          <div class="sort-item">P</div>
          <div class="sort-item">Q</div>
          <div class="sort-item">R</div>
          <div class="sort-item">S</div>
          <div class="sort-item">T</div>
          <div class="sort-item">U</div>
          <div class="sort-item">V</div>
          <div class="sort-item">W</div>
          <div class="sort-item">X</div>
          <div class="sort-item">Y</div>
          <div class="sort-item">Z</div>
        </div>
      </div>
      <div class="alpha">
        <div class="title">A</div>
        <div class="item-box">
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
          <div class="alpha-item">安阳</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
export default {
  name: 'CityList',
  mounted () {
    this.scroll = new BScroll(this.$refs.tab)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .sort-padding
    padding: .3rem 0
  .city-list
    overflow: hidden
    position: absolute
    top: 1.48rem
    left: 0
    right: 0
    bottom: 0
    z-index: 3
    .title
      position: relative
      font-size: .24rem
      padding: .24rem .3rem
      background: #f5f5f5
    .item-box
      position: relative
      display: flex
      flex-flow: row wrap
      overflow: hidden
      .s-item
        hiddenLine()
        box-sizing: border-box
        width: 33.33%
        line-height: .9rem
        height: .9rem
        text-align: center
      .sort-item
        box-sizing: border-box
        width: 16.66%
        line-height: .9rem
        height: .9rem
        text-align: center
      .alpha-item
        hiddenLine()
        box-sizing: border-box
        width: 25%
        line-height: .9rem
        height: .9rem
        text-align: center
    .item-box
      .s-item:nth-child(3n), .alpha-item:nth-child(4n)
        border-right: none

</style>
