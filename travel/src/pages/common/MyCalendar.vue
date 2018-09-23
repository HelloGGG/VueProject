<template>
  <div class="calendar">
    <div class="calendar-close iconfont">&#xe61a;</div>
    <div class="calendar-header border-bottom">选择时间</div>
    <div class="months">
       <calendar
      v-for="(month, index) in months"
      :key="index"
      :month="month"
      ></calendar>
    </div>
  </div>
</template>

<script>
import Calendar from './Calendar'
export default {
  name: 'MyCalendar',
  components: {
    Calendar
  },
  data () {
    return {
      months: [
        {
          year: 2018,
          month: 8
        }, {
          year: 2018,
          month: 9
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  .calendar
    position: fixed
    left: 0
    right: 0
    bottom: 0
    background: #fff
    z-index: 200
    .calendar-header
      line-height: 1rem
      font-size: .34rem
      text-align: center
      color: #212121
    .calendar-close
      position: absolute
      right: 0
      top: 0
      width: .88rem
      height: 1rem
      color: #9e9e9e
      font-size: .4rem
      line-height: 1rem
      text-align: center
    .months
      overflow-x: hidden
      overflow-y: auto
      min-height: 5.4rem
      max-height: 6.5rem
      position: relative
      width: 100%
</style>
