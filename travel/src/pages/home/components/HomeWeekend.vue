<template>
  <div>
    <div class="title">周末去哪儿</div>
    <div class="items-box border-bottom" v-for="item in items" :key="item.id">
      <div class="img-wrap">
        <img :src="item.imgUrl" alt="" class="pic">
      </div>
      <div class="info-box">
        <p class="info">{{item.info}}</p>
        <p class="desc">{{item.desc}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeWeekend',
  data () {
    return {
      items: [{
        id: '0001',
        imgUrl: 'http://img1.qunarzz.com/sight/source/1505/f1/c2066187e1b26c.jpg_r_640x214_e4c882f0.jpg',
        info: '嘉兴必游TOP10',
        desc: '小桥，流水，人家'
      }, {
        id: '0002',
        imgUrl: 'http://img1.qunarzz.com/sight/source/1505/69/490fe2414dfc35.jpg_r_640x214_b642009a.jpg',
        info: '回味儿童趣',
        desc: '小鬼当家，闹不停'
      }]
    }
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
    background: red
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
