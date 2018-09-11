<template>
    <div class="header">
        <div class="header-left iconfont">&#xe624;</div>
        <div class="header-input iconfont">&#xe6fe;请输入城市/景点/游玩主题</div>
        <div class="header-right iconfont">城市&#xe64a;</div>
    </div>
</template>

<script>
export default {
  name: 'HomeHeader'
}
</script>

<style lang="stylus" scoped>
    @import '~styles/variable.styl';
    .header
      display: flex;
      flex-direction: row;
      height: 0.88rem;
      background: $bg;
      align-items: center;

      .header-left
        width: 0.8rem;
        text-align: center;
        color: #fff;

      .header-input
        width: 5.38rem;
        height: 0.6rem;
        border-radius: 0.06rem;
        text-indent: 0.2rem;
        color: #cecece;
        background: #fff;
        line-height: 0.6rem;
      .header-right
        width: 1.32rem;
        text-align: center;
        color: #fff;
</style>
