<template>
  <div class="icons">
    <div class="icon-warpper" v-for="item in items" :key="item.id">
      <div class="icon">
        <img :src="item.iconUrl" alt="">
      </div>
      <p class="icon-desc">{{item.desc}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  data () {
    return {
      items: [
        {
          id: '0001',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/95/f3dd6c383aeb3b02.png',
          desc: '热门景点'
        }, {
          id: '0002',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/67/9a1678221b8e0e02.png',
          desc: '古镇'
        }, {
          id: '0003',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/50/26ffa31b56646402.png',
          desc: '亲子游'
        }, {
          id: '0004',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/20/831d62d2e1c7be02.png',
          desc: '名胜古迹'
        }, {
          id: '0005',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1804/ff/fdf170ee89594b02.png',
          desc: '嘉兴必游'
        }, {
          id: '0006',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/b8/c5dcdb58deec2402.png',
          desc: '虎踞峡'
        }, {
          id: '0007',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1803/8c/47630407f70e8302.png',
          desc: '横店影视城'
        }, {
          id: '0008',
          iconUrl: 'http://img1.qunarzz.com/piao/fusion/1804/95/8d02011d149bdb02.png',
          desc: '汽车票'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  .icons
    overflow: hidden
    width: 100%
    height: 0
    padding-bottom: 50.6%
    .icon-warpper
      float: left
      overflow: hidden
      width: 25%
      height: 0
      padding-bottom: 25%
      .icon
        overflow: hidden
        height: 0
        padding-bottom: 60%
        padding-top: 0.02rem
        img
          display: block
          width: 60%
          margin: 0.1rem auto
      .icon-desc
        overflow: hidden
        height: 0
        padding-bottom: 20%
        text-align: center
        padding-top: 0.2rem
</style>
