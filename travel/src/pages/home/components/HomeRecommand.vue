<template>
  <div>
    <div class="iconfont title"><span class="icon">&#xe616;</span> 猜你喜欢</div>
    <div class="recommand-box border-bottom" v-for="item in items" :key="item.id">
      <img :src="item.imgUrl" alt="">
      <div class="info">
        <p class="place">{{item.place}}</p>
        <p class="comment">{{item.comment}}</p>
        <button class="btn-detail">查看详情</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeRecommand',
  data () {
    return {
      items: [
        {
          id: '0001',
          imgUrl: 'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_200x200_3e4f203f.jpg',
          place: '乌镇',
          comment: '12799条评论'
        }, {
          id: '0002',
          imgUrl: 'http://img1.qunarzz.com/sight/p0/201401/10/c15067e404b3b7c84a93f62d89aebf33.jpg_200x200_96c23ef5.jpg',
          place: '云澜湾景区',
          comment: '725条评论'
        }, {
          id: '0003',
          imgUrl: 'http://img1.qunarzz.com/sight/p0/201302/05/7baaa81258670852c8d65eac.jpg_200x200_65d90332.jpg',
          place: '乌镇西栅',
          comment: '8043条评论'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  .title
    overflow: hidden
    width: 100%
    padding: 0.24rem 0.26rem
    .icon
      color: #f65f53
  .recommand-box
    display: flex
    img
      height: 2rem
      width: 2rem
      padding: 0.1rem
    .info
      flex-grow: 1
      padding: 0 0.1rem
      .place
        margin-top: 0.4rem
        font-size: 0.32rem
        height: 0.44rem
        line-height: 0.44rem
      .comment
        margin-top: 0.1rem
        color: #616161
        font-size: 0.24rem
        line-height: 0.34rem
      .btn-detail
        margin-top: 0.2rem
        color: orange
        padding: 0.08rem
        border-radius: 0.1rem
</style>
