<template>
    <div class="header">
        <div class="header-left iconfont">&#xe624;</div>
        <div class="header-input iconfont">&#xe6fe;请输入城市/景点/游玩主题</div>
        <div class="header-right iconfont">{{city}}&#xe64a;</div>
    </div>
</template>

<script>
export default {
  name: 'HomeHeader',
  props: {
    city: String
  }
}
</script>

<style lang="stylus" scoped>
    @import '~styles/variable.styl';
    .header
      display: flex;
      flex-direction: row;
      width: 100%;
      height: 0.88rem;
      background: $bg;
      align-items: center;

      .header-left
        width: 0.7rem;
        text-align: center;
        color: #fff;

      .header-input
        flex-grow: 1
        height: 0.6rem;
        border-radius: 0.06rem;
        text-indent: 0.2rem;
        color: #cecece;
        background: #fff;
        line-height: 0.6rem;

      .header-right
        width: 1.28rem;
        text-align: center;
        color: #fff;
</style>
