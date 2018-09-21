<template>
  <div>
    <div class="title">周末去哪儿</div>
    <div class="items-box border-bottom" v-for="item in list" :key="item.id">
      <div class="img-wrap">
        <img :src="item.imgUrl" alt="" class="pic">
      </div>
      <div class="info-box">
        <p class="info">{{item.name}}</p>
        <p class="desc">{{item.desc}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeWeekend',
  props: {
    list: Array
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .title
    height: .8rem;
    padding-left: .26rem;
    line-height: .8rem;
    color: #212121;
    background: #f5f5f5
  .img-wrap
    overflow: hidden
    width: 100%
    height: 0
    padding-bottom: 33.4%
    .pic
      width: 100%
  .info-box
    padding: .14rem .2rem .2rem .2rem
    .info
      font-size: .28rem
      line-height: 0.4rem
      height: 0.4rem
      color: #212121
      ellipsis()
    .desc
      font-size: .24rem
      line-height: 0.36rem
      height: 0.36rem
      color: #616161
      margin-top: 0.1rem
      margin-bottom: 0.2rem
      ellipsis()
</style>
