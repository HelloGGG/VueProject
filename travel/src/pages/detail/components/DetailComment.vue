<template>
  <div class="wrapper">
     <div class="c-title border-bottom">用户评论</div>
      <comment
        v-for="user in users"
        :key="user.id"
        :user="user"
      ></comment>
      <list-more>查看全部评论 &#xe62d;</list-more>
  </div>
</template>

<script>
import Comment from './Comment'
import ListMore from 'common/ListMore'
export default {
  name: 'DetailComment',
  components: {
    Comment,
    ListMore
  },
  data () {
    return {
      users: [
        {
          id: '0001',
          name: 'ze*o',
          stars: 4,
          date: '2018-09-15',
          words: '嘉善云澜湾四季花海乐园位于嘉善云澜湾甜蜜小镇内。据说这里春有郁金香、樱花，夏季则是马鞭草、薰衣草，秋季菊花盛放，冬天腊梅盛开，一年四季各色花常开。乐园不同时节还会配合不同主题活动，如：恐龙展、艺术灯展等，任何时间段来这里游玩都不会失望的。我们来的时节正值夏季，正是薰衣草和马鞭草盛放的时节。 薰衣草的故乡在法国，记得《普罗旺斯的一年》这本书的封面就是一片薰衣草，让人记忆深刻。日本北海道也引种了薰衣草，电影《非诚勿扰》里的唯美花海也是引得无数游客前往观赏。没想到就在江浙沪周边竟然也有这么一大片薰衣草田。 薰衣草一直被视为纯洁、清净、保护、感恩与和平的象征，代表着幸福的源泉，都说薰衣草精油具有抗忧郁、镇定的作用，难怪身处这片薰衣草田内，内心感到很安定，心情也不禁愉悦起来。除了薰衣草，四季花海乐园内还有和薰衣草长得很像的马鞭草。传说中马鞭草被称为“有魔力的植物”，因为它柠檬味的清新会帮助唤醒你的身体和心灵。另外，各种各样其它不知名的花卉也很多，可以说处处是景，处处都可以拍照凹造型。四季花海乐园身处云澜湾甜蜜小镇内，在这里爱情的甜蜜肯定不会缺少。这家乐园也是很多新婚夫妇拍摄婚纱照的好场所，无论是童话风的小木屋还是蓝白相间的地中海风格建筑，还有各种颇具异国风情的大风车，或是日式风格的桥......都能在这座乐园里找到。 爱拍照、爱凹造型的女生来到这里肯定会流连忘返的，因为这里有太多适合拍照的场景。乐园里到处充满了“爱”的元素在这家乐园内，还有很多适合孩子游玩的项目，带孩子亲子活动或是带着老人来赏花、呼吸新鲜空气，享受天伦之乐，四季花海乐园都是一个不错的选择。',
          imgs: [
            'https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg_228x168_3d478b45.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/41/63f27534b902e002.jpg_228x168_df8d84a8.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg_228x168_74b451eb.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/da/d7fa96263201ca02.jpg_228x168_01388bed.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/e0/2b067041a9c4ea02.jpg_228x168_81c3e2ed.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/78/d72656ff4fb4ae02.jpg_228x168_81a75221.jpg'
          ]
        }, {
          id: '0002',
          name: 'Ali*e',
          stars: 5,
          date: '2018-09-12',
          words: '路线安排很合理，导游热情，解说详细有趣，自由度也很高，100％纯玩团，非常靠谱，很愉快的旅程。东栅比较小，不过景点很集中，西栅很大，夜景确实很棒！我们在西栅是走进去，最后自费游船出来，可以直接观夜景，很舒服！',
          imgs: [
            'https://imgs.qunarzz.com/piao/fusion/1808/c0/014d956dda6cc302.jpg_228x168_9dff9040.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/89/ba65c157375fb002.jpg_228x168_422e486f.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/b0/4081febd4a563d02.jpg_228x168_e496fe27.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/47/c977125c06b01602.jpg_228x168_e8c442d0.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/c3/cffc02490806c802.jpg_228x168_2dd9fa49.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/e3/160d053b57b78302.jpg_228x168_abcd29fb.jpg'
          ]
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
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
</style>
