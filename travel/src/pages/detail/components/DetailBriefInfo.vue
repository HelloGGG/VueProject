<template>
  <div class="container">
    <div class="info">
      <div class="info-sorce border-rightbottom">
        <div class="top">
          <span class="num">4.9</span>
          分 很棒
        </div>
        <div class="bottom">12924评论  66条攻略</div>
        <div class="arrow-r iconfont custom_c">&#xe62d;</div>
      </div>
      <div class="info-intro  border-bottom">
        <div class="top">景点简介</div>
        <div class="bottom">开放时间/贴士</div>
        <div class="arrow-r iconfont custom_c">&#xe62d;</div>
      </div>
    </div>
    <div class="address border-bottom"><span class="iconfont custom_c">&#xe6d1;</span> 
    浙江省嘉兴市桐乡市乌镇石佛南路18号
    <div class="arrow-r iconfont custom_c">&#xe62d;</div>
    </div>
  </div>  
</template>

<script>
export default {
  
}
</script>

<style lang="stylus" scoped>
  .custom_c
    color: #9e9e9e
  .arrow-r
    position: absolute
    top: .28rem
    right: .2rem
  .container
    position: relative
    box-sizing: border-box
    width: 100%
    border-radius: .2rem .2rem 0 0
    padding: .1rem
    margin-top: -.1rem
    z-index: 10
    background: #fff
    .info
      .info-sorce, .info-intro
        float: left
        box-sizing: border-box
        width: 50%
        padding: .15rem
        .top
          position: relative
          height: .44rem
          line-height: .44rem
          color: #ff8300
          margin-bottom: .1rem
          .num
            font-size: .44rem
        .bottom
          position: relative
          font-size: .24rem
          color: #9e9e9e
          margin-bottom: .1rem
      .info-intro
        .top
          color: #333
    .address
      clear: both
      position: relative
      margin-top: .1rem
      line-height: .76rem
      height: .76rem
      padding-left: .1rem
      .arrow-r
        top: 0
</style>
