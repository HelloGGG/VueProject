<template>
  <div>
    <div class="iconfont title"><span class="icon">&#xe616;</span> 猜你喜欢</div>
      <router-link tag="div"
      class="recommand-box border-bottom"
      v-for="item in list"
      :key="item.id"
      :to="'/detail/' + item.id"
      >
        <img :src="item.imgUrl" alt="">
        <div class="info">
          <p class="place">{{item.place}}</p>
          <p class="comment">{{item.comment}}</p>
          <button class="btn-detail">查看详情</button>
        </div>
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeRecommand',
  props: {
    list: Array
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
