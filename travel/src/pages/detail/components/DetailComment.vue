<template>
  <div class="wrapper">
     <div class="c-title border-bottom">
        用户评论
      </div>
      <div class="content border-bottom">
        <div class="starlevel-datetime">
            <div class="starlevel">
              <span class="all iconfont">&#xe642;&#xe642;&#xe642;&#xe642;
                 <span class="bad iconfont">&#xe642;</span>
              </span>
            </div>
            <div class="datetime">杂*人&nbsp;&nbsp;2017-07-29</div>
        </div>
        <div class="words" :class="{intercept: isActive }">
          嘉善云澜湾四季花海乐园位于嘉善云澜湾甜蜜小镇内。据说这里春有郁金香、樱花，夏季则是马鞭草、薰衣草，秋季菊花盛放，冬天腊梅盛开，一年四季各色花常开。乐园不同时节还会配合不同主题活动，如：恐龙展、艺术灯展等，任何时间段来这里游玩都不会失望的。我们来的时节正值夏季，正是薰衣草和马鞭草盛放的时节。 薰衣草的故乡在法国，记得《普罗旺斯的一年》这本书的封面就是一片薰衣草，让人记忆深刻。日本北海道也引种了薰衣草，电影《非诚勿扰》里的唯美花海也是引得无数游客前往观赏。没想到就在江浙沪周边竟然也有这么一大片薰衣草田。 薰衣草一直被视为纯洁、清净、保护、感恩与和平的象征，代表着幸福的源泉，都说薰衣草精油具有抗忧郁、镇定的作用，难怪身处这片薰衣草田内，内心感到很安定，心情也不禁愉悦起来。除了薰衣草，四季花海乐园内还有和薰衣草长得很像的马鞭草。传说中马鞭草被称为“有魔力的植物”，因为它柠檬味的清新会帮助唤醒你的身体和心灵。另外，各种各样其它不知名的花卉也很多，可以说处处是景，处处都可以拍照凹造型。四季花海乐园身处云澜湾甜蜜小镇内，在这里爱情的甜蜜肯定不会缺少。这家乐园也是很多新婚夫妇拍摄婚纱照的好场所，无论是童话风的小木屋还是蓝白相间的地中海风格建筑，还有各种颇具异国风情的大风车，或是日式风格的桥......都能在这座乐园里找到。 爱拍照、爱凹造型的女生来到这里肯定会流连忘返的，因为这里有太多适合拍照的场景。乐园里到处充满了“爱”的元素在这家乐园内，还有很多适合孩子游玩的项目，带孩子亲子活动或是带着老人来赏花、呼吸新鲜空气，享受天伦之乐，四季花海乐园都是一个不错的选择。
        </div>
        <list-more class="listmore-custom"
          v-show="listmodeShow"
          @click.native="handleListMoreClick"
        >&#xe62c;
        </list-more>
        <list-more class="listmore-custom"
          v-show="!listmodeShow"
          @click.native="handleListMoreClick"
        >&#xe62e;
        </list-more>
        <div class="pic-display">
          <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
          <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
          <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
          <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
           <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
           <div class="pic-wrap">
            <img src="https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg" alt="">
          </div>
        </div>
      </div>
      <list-more>查看全部评论 &#xe62d;</list-more>
  </div>
</template>

<script>
import ListMore from 'common/ListMore'
export default {
  name: 'DetailComment',
  components: {
    ListMore
  },
  data () {
    return {
      listmodeShow: false,
      isActive: true
    }
  },
  methods: {
    handleListMoreClick () {
      this.isActive = !this.isActive
      this.listmodeShow = !this.listmodeShow
    }
  }
}
</script>

<style lang="stylus" scoped>
  .intercept
    overflow: hidden
    height: 2.1rem
  .listmore-custom
    line-height: .48rem
  .all
    color: #ffb436
    margin: 0
    font-size: 0.05rem
  .bad
    color: #ddd
    margin: 0
    font-size: 0.1rem
  .c-title
    line-height: .88rem
    font-size: .3rem
    padding-left: .4rem
  .c-title::after
    content: ""
    position: absolute
    top: .32rem
    left: .2rem
    width: .07rem
    height: .25rem
    background: #1ba9ba
    border-radius: .05rem
  .content
    padding: .1rem .2rem .4rem .2rem
    .starlevel-datetime
      position: relative
      line-height: .6rem
    .datetime
      position: absolute
      top: 0
      right: 0
      font-size: .24rem
    .words
      line-height: .42rem
      font-size: .26rem
      color: #616161
      word-break: break-all
      word-wrap: break-word
    .pic-display
      display: flex
      flex-flow: row wrap
      .pic-wrap
        box-sizing: border-box
        width: 33.33%
        padding: .05rem
        img
          width: 100%
</style>
