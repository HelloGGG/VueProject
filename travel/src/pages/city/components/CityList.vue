<template>
  <div class="city-list" ref="tab">
    <div class="wrapper">
      <div>
        <div class="current-city">
          <div class="title">当前城市</div>
          <div class="item-box">
            <div class="s-item"
            >{{this.city}}</div>
          </div>
        </div>
      </div>
      <div class="hot-city">
        <div class="title">热门城市</div>
        <div class="item-box">
          <div class="s-item"
            v-for="item in hotCities"
            :key="item.id"
            @click="handleCityClick(item.name)"
          >{{item.name}}</div>
        </div>
      </div>
      <div class="sort">
        <div class="title">字母排序</div>
        <div class="item-box sort-padding">
          <div class="sort-item"
            v-for="(item, key) in cities"
            :key="key"
            @click="handleClick"
            >{{key}}</div>
        </div>
      </div>
      <div class="alpha">
        <div
          v-for="(item, key) in cities"
          :key="key"
          :ref="key">
          <div class="title">{{key}}</div>
          <div class="item-box">
            <div class="alpha-item"
             v-for="cl in item"
             :key="cl.id"
             @click="handleCityClick(cl.name)"
             >{{cl.name}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
import {mapState, mapMutations} from 'vuex'

export default {
  props: {
    cities: Object,
    hotCities: Array,
    letter: String
  },
  data () {
    return {
      character: ''
    }
  },
  name: 'CityList',
  computed: {
    ...mapState(['city'])
  },
  methods: {
    handleClick (e) {
      this.character = e.target.innerText
      var element = this.$refs[this.character][0]
      this.scroll.scrollToElement(element)
    },
    handleCityClick (city) {
      this.changeCurrentCity(city)
      this.$router.push('./')
    },
    ...mapMutations([
      'changeCurrentCity'
    ])
  },
  watch: {
    letter () {
      if (this.letter) {
        var element = this.$refs[this.letter][0]
        this.scroll.scrollToElement(element)
      }
    }
  },
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
    z-index: 10
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
        ellipsis()
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
        ellipsis()
    .item-box
      .s-item:nth-child(3n), .alpha-item:nth-child(4n)
        border-right: none

</style>
