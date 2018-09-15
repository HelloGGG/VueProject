<template>
  <div>
    <div class="search">
      <div class="domestic"
        :class="{activate: isActivate}"
        @click="handleClick">
        境内
        </div>
      <div class="overseas"
        :class="{activate: !isActivate}"
        @click="handleClick">
        境外·港澳台
        </div>
      <input
      class="search-input"
      type="text"
      placeholder="搜索"
      v-model="keyword"
      @click="handleInputClick"
      >
    </div>
    <div class="search-content"
      v-show="resultShow"
      ref="tab">
      <ul class="result">
        <li class="search-item border-bottom"
            v-for="(item, index) in result"
            :key="index"
            @click="handleCityClick(item)"
        >{{item}}</li>
        <li class="search-item border-bottom"
            v-show="helpTip"
        >
          没有匹配结果
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
export default {
  name: 'CitySearch',
  props: {
    show: Boolean,
    cities: Object
  },
  data () {
    return {
      isActivate: true,
      keyword: '',
      resultShow: this.show,
      result: []
    }
  },
  computed: {
    helpTip () {
      return !this.result.length
    }
  },
  methods: {
    handleClick () {
      this.isActivate = !this.isActivate
      this.$emit('changeAjax', this.isActivate, true)
      this.resultShow = false
    },
    handleInputClick () {
      this.$emit('changeList', false)
      this.resultShow = true
    },
    handleCityClick (city) {
      this.$store.commit('changeCurrentCity', city)
      this.$router.push('/')
    }
  },
  watch: {
    keyword () {
      this.result = []
      for (let i in this.cities) {
        this.cities[i].forEach((value, index) => {
          if (value.name.indexOf(this.keyword) > -1 || value.spell.indexOf(this.keyword) > -1) {
            this.result.push(value.name)
          }
        })
      }
      if (!this.keyword.length) {
        this.result = []
      }
    }
  },
  mounted () {
    this.scroll = new BScroll(this.$refs.tab)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .activate
    color: $bg
    background: #fff
  .search
    position: relative
    display: flex
    height: .4rem
    line-height: .4rem
    background: $bg
    padding: 0 1rem .2rem 1rem
    color: #fff
    text-align: center
    .domestic, .overseas, .search-input
      width: 33.33%
      border: 1px solid #fff
      height: .4rem
      line-height: .4rem
    .overseas
      border-left: none
      border-right: none
    .search-input
      text-align: center
  .search-content
    overflow: hidden
    position: absolute
    top: 1.48rem
    left: 0
    right: 0
    bottom: 0
    background: #fff
    .search-item
      color: #666
      text-align: left
      line-height: .6rem
      padding-left: .2rem
</style>
