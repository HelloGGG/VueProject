<template>
  <div>
    <div class="ticket-kind border-bottom"
        v-for="(item, index) in list"
        :key="index"
    >
      <span class="ticket-icon"></span>
      {{item.title}}
      <div class="children"
        v-if="item.children"
      >
        <detail-list :list="item.children"></detail-list>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    list: Array
  },
  name: 'DetailList'
}
</script>

<style lang="stylus" scoped>
  .children
    padding: 0 .2rem
  .ticket-kind
    width: 100%
    line-height: .88rem
    font-size: .32rem
    align-items: center
    padding: 0 .2rem
    flex-flow: raw wrap
    .ticket-icon
      display: inline-block;
      width: .36rem;
      height: .36rem;
      background: url(http://s.qunarzz.com/piao/image/touch/sight/detail.png) 0 -.45rem no-repeat;
      margin-right: .05rem;
      background-size: .4rem 3rem;
</style>
