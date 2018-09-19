<template>
  <div>
    <eval-header></eval-header>
    <eval-main
      v-for="user in users"
      :key="user.id"
      :user="user"
    ></eval-main>
    <div
    class="top-wrapper"
    @click="handleTopClick"
    v-show="isTopShow"
    ><div class="iconfont toTop">&#xe635;</div></div>
  </div>
</template>

<script>
import EvalHeader from './components/EvalHeader'
import EvalMain from './components/EvalMain'
export default {
  name: 'Eval',
  components: {
    EvalHeader,
    EvalMain
  },
  data () {
    return {
      isTopShow: false,
      users: [
        {
          id: '0001',
          name: 'ze*o',
          avatar: 'http://img1.qunarzz.com/ucenter/headshot/201308/12/ace6614d44a8f26f7c43c4d7.jpg',
          stars: 4,
          date: '2018-08-15',
          words: '嘉善云澜湾四季花海乐园位于嘉善云澜湾甜蜜小镇内。据说这里春有郁金香、樱花，夏季则是马鞭草、薰衣草，秋季菊花盛放，冬天腊梅盛开，一年四季各色花常开。乐园不同时节还会配合不同主题活动，如：恐龙展、艺术灯展等，任何时间段来这里游玩都不会失望的。我们来的时节正值夏季，正是薰衣草和马鞭草盛放的时节。 薰衣草的故乡在法国，记得《普罗旺斯的一年》这本书的封面就是一片薰衣草，让人记忆深刻。日本北海道也引种了薰衣草，电影《非诚勿扰》里的唯美花海也是引得无数游客前往观赏。没想到就在江浙沪周边竟然也有这么一大片薰衣草田。 薰衣草一直被视为纯洁、清净、保护、感恩与和平的象征，代表着幸福的源泉，都说薰衣草精油具有抗忧郁、镇定的作用，难怪身处这片薰衣草田内，内心感到很安定，心情也不禁愉悦起来。除了薰衣草，四季花海乐园内还有和薰衣草长得很像的马鞭草。传说中马鞭草被称为“有魔力的植物”，因为它柠檬味的清新会帮助唤醒你的身体和心灵。另外，各种各样其它不知名的花卉也很多，可以说处处是景，处处都可以拍照凹造型。四季花海乐园身处云澜湾甜蜜小镇内，在这里爱情的甜蜜肯定不会缺少。这家乐园也是很多新婚夫妇拍摄婚纱照的好场所，无论是童话风的小木屋还是蓝白相间的地中海风格建筑，还有各种颇具异国风情的大风车，或是日式风格的桥......都能在这座乐园里找到。 爱拍照、爱凹造型的女生来到这里肯定会流连忘返的，因为这里有太多适合拍照的场景。乐园里到处充满了“爱”的元素在这家乐园内，还有很多适合孩子游玩的项目，带孩子亲子活动或是带着老人来赏花、呼吸新鲜空气，享受天伦之乐，四季花海乐园都是一个不错的选择。',
          imgs: [
            'https://imgs.qunarzz.com/piao/fusion/1809/64/465358a580b9ab02.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/41/63f27534b902e002.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/f8/3740cfbf50896502.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/da/d7fa96263201ca02.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/e0/2b067041a9c4ea02.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1809/78/d72656ff4fb4ae02.jpg'
          ]
        }, {
          id: '0002',
          name: 'Ali*e',
          stars: 5,
          date: '2018-07-28',
          avatar: 'http://img1.qunarzz.com/ucenter/portrait/1806/3b/1b850fa6e9eefdea.jpg',
          words: '路线安排很合理，导游热情，解说详细有趣，自由度也很高，100％纯玩团，非常靠谱，很愉快的旅程。东栅比较小，不过景点很集中，西栅很大，夜景确实很棒！我们在西栅是走进去，最后自费游船出来，可以直接观夜景，很舒服！',
          imgs: [
            'https://imgs.qunarzz.com/piao/fusion/1808/c0/014d956dda6cc302.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/89/ba65c157375fb002.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/b0/4081febd4a563d02.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/47/c977125c06b01602.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/c3/cffc02490806c802.jpg',
            'https://imgs.qunarzz.com/piao/fusion/1808/e3/160d053b57b78302.jpg'
          ]
        }, {
          id: '0003',
          name: '塞*野',
          stars: 5,
          date: '2018-07-05',
          avatar: 'http://qcommons.qunar.com/headshot/headshotsById/148458871.png',
          words: '那么南栅一定会非常适合，这里的节奏很慢，生活很静，你仿佛能够看到，几十年来这里居民不变的生活状态","content":"去过东栅、西栅和南栅，说实话，南栅才是人们心中想象的古镇模样，宁静的小巷弄，织毛衣的老奶奶，骑着自行车叮当响的老爷爷，很有生活的味道。清晨早点铺子炊烟袅袅，一晚豆浆、一张烤饼、一根油条都是满满的幸福。\n南栅不收取门票，悠然自得，虽然不大但是比起商业化严重的西栅，个人认为美上十倍。一条直直的小弄，巷弄两旁是居民屋，亭台楼阁，临水而建，房屋老旧，有的甚至有百年历史，屋内依然存放的当年生活的家具。\n南栅商家不多，一些特产小店，剩下的都是街坊邻居，自家的屋子也腾出来做个小店面，爱好古玩的爷爷，在小铺子里收集了不少好东西。\n在这里没有嘈杂和随处的叫卖声，鲜有游客，你可以安静的感受江南水乡的韵律。这里的的房屋都是木制楼阁，格局不大，但是五脏俱全，设计雅致，大厅，阁楼，院子这是大户的配备，一般人家大门较窄，空间局促，这体现着江南生活的精细。\n地址：嘉兴市桐乡市乌镇南大街内。距离西栅步行30分钟，东栅车程10分钟。\n交通：公交350,两元，三轮车，或者步行。\n美食：乌镇有很多地道小食，姑嫂饼、乌米糕、白水鱼、羊肉、三白酒等等。\n住宿：可以选择在景区外，这样去东南西北栅都比较方便。\n门票：免费\n总结：来到乌镇所有人都会直奔西栅，当然如果是第一来也是要去感受的，但是南栅未被开发，确实是乌镇最原汁原味的老街，如果你也不喜欢灯红酒绿，那么南栅一定会非常适合，这里的节奏很慢，生活很静，你仿佛能够看到，几十年来这里居民不变的生活状态，一砖一瓦，一巷一弄似乎都不曾被岁月带走。如果你想感受最地道淳朴的乌镇特色，南栅是不二之选。',
          imgs: [
            'http://img1.qunarzz.com/travel/d0/1707/11/edb41f2f09399bb5.jpg',
            'http://img1.qunarzz.com/travel/d8/1707/73/41ed28bfe97e1fb5.jpg',
            'http://img1.qunarzz.com/travel/d6/1707/9a/4fb7a369946d43b5.jpg',
            'http://img1.qunarzz.com/travel/d2/1707/cb/b7316c62ef0e2db5.jpg',
            'http://img1.qunarzz.com/travel/d8/1707/2e/f09fcc3752a126b5.jpg',
            'http://img1.qunarzz.com/travel/d5/1707/b6/70f724f4aaa370b5.jpg',
            'http://img1.qunarzz.com/travel/d1/1707/6f/8017812366f3cdb5.jpg',
            'http://img1.qunarzz.com/travel/d3/1707/33/d343c8583eaa9eb5.jpg'
          ]
        }
      ]
    }
  },
  methods: {
    handleTopClick () {
      window.scrollTo(0, 0)
    },
    handleScroll () {
      let top = document.documentElement.scrollTop
      this.isTopShow = top > 150
    }
  },
  activated () {
    window.addEventListener('scroll', this.handleScroll)
  },
  deactivated () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .top-wrapper
    position: fixed
    display: flex
    align-items: center
    justify-content: center
    bottom: 1.5rem
    right: .2rem
    background: #fff
    line-height: 1rem
    width: 1rem
    border-radius: .5rem
    .toTop
      font-size: .8rem
      border-radius: .4rem
      color: $bg
      z-index: 100
</style>
