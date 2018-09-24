<template>
  <div>
    <div class="mask" @click="handleMaskClick"></div>
    <div class="calendar">
      <div class="calendar-close iconfont" @click="handleMaskClick">&#xe61a;</div>
      <div class="calendar-header border-bottom">选择时间</div>
      <div class="months">
        <calendar
          @closeCalendar="handleCloseCalendar"
          :defaultCYear="currentYear"
          :defaultCMonth="currentMonth"
        ></calendar>
      </div>
    </div>
  </div>
</template>

<script>
import Calendar from './Calendar'
export default {
  props: {
    currentYear: Number,
    currentMonth: Number
  },
  name: 'MyCalendar',
  components: {
    Calendar
  },
  data () {
    return {
    }
  },
  methods: {
    handleMaskClick () {
      this.$emit('showCalendar', false)
      this.optionClose = true
    },
    handleCloseCalendar () {
      this.$emit('showCalendar', false)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .mask
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    background: rgba(0, 0, 0, .6)
    z-index: 150
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
      z-index: 200
</style>
