<template>
  <div>
    <place-title>温馨提示</place-title>
    <div class="tip-content">
      <p class="t-title">小贴士</p>
      <p class="spec-tip">1、门票一经售出，概不退换，景区门票当日一次使用有效，消码/打孔注消；东栅景区门票实行一票分检制，进入景区各小景点请主动出示门票；</p>
      <p class="spec-tip">2、门票、船票、导游票均可直接报销，不另开发票，敬请谅解；</p>
      <p class="spec-tip">3、请配合景区管理人员工作，爱护文物，讲究卫生，注意防火，禁止在禁烟场所吸烟；</p>
      <p class="spec-tip">4、进入景区请注意游览安全，并保管好随身物品，未成年人必须有成年人监护并保持随时照顾，勿在河边嬉水，攀登跨越栏杆，坐游船请勿超员；</p>
      <p class="spec-tip">5、为保障您的合法权益，请选择有正规营业执照的民宿和客栈入住；</p>
      <p class="spec-tip">6、如遇困难请及时向景区管理人员求助；</p>
    </div>
    <div class="c-margin"></div>
  </div>
</template>

<script>
import PlaceTitle from './PlaceTitle'
export default {
  name: 'PlaceTip',
  components: {
    PlaceTitle
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/minx.styl'
  .c-margin
    componentMargin()
  .tip-content
    padding: 0 .2rem
    .t-title
      font-weight: bold
      color: #333
      line-height: .42rem
      font-size: .28rem
    .spec-tip
      comment()
</style>
