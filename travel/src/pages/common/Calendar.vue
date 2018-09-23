<template>
  <div class="calendar-month">
    <div class="calendar-title">{{month.year}}年{{month.month+1}}月</div>
    <div class="calendar-content">
      <div class="t-header">
        <div class="t-item"
          v-for="(item, index) in week"
          :key="index+2000"
        >{{item}}</div>
        <div class="t-item disabled" v-for="item in blankNum" :key="item+500"></div>
        <div class="t-item disabled" v-for="item in firstRowStart" :key="item+600">{{item}}</div>
        <div
          class="t-item disabled"
          v-for="day in setSecondStartdays"
          :key="day+100"
        >
          {{day}}
        </div>
        <div
          class="t-item valid"
          v-for="(day, index) in setValidDays"
          :key="index"
          @click="handleValidClick(index)"
          ref="validDay"
        >
          {{day}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    month: Object
  },
  name: 'Calendar',
  data () {
    return {
      week: ['日', '一', '二', '三', '四', '五', '六']
    }
  },
  computed: {
    getCurrentMonthdays () {
      var date = new Date(this.month.year, this.month.month, 1)
      // 获取当前月份天数
      var nextMonth = new Date(date.setMonth(date.getMonth() + 1))
      var lastday = new Date(nextMonth.setDate(nextMonth.getDate() - 1))
      return lastday.getDate()
    },
    getTrs () {
      return Math.ceil(this.getCurrentMonthdays / 7)
    },
    secondRowStart () {
      var date = new Date(this.month.year, this.month.month, 1)
      switch (date.getDay()) {
        case 0:
          return 8
        case 1:
          return 7
        case 2:
          return 6
        case 3:
          return 5
        case 4:
          return 4
        case 5:
          return 3
        case 6:
          return 2
        default: break
      }
    },
    blankNum () {
      return 7 - (this.secondRowStart - 1)
    },
    firstRowStart () {
      return this.secondRowStart - 1
    },
    setSecondStartdays () {
      var temp = []
      var today = new Date()
      var tadayNum = today.getDate()
      for (let i = 1; i <= this.getCurrentMonthdays; i++) {
        if (today.getFullYear() === this.month.year && today.getMonth() === this.month.month) {
          if (i === tadayNum) {
            temp.push('今天')
          }
          if (i >= this.secondRowStart && i < tadayNum) {
            temp.push(i)
          }
        }
      }
      return temp
    },
    setValidDays () {
      var temp = []
      var today = new Date()
      var tadayNum = today.getDate()
      for (let i = 1; i <= this.getCurrentMonthdays; i++) {
        if (today.getFullYear() === this.month.year && today.getMonth() === this.month.month) {
          if (i > tadayNum) {
            temp.push(i)
          }
        } else {
          temp.push(i)
        }
      }
      return temp
    }
  },
  methods: {
    handleValidClick (index) {
      for (let i = 0; i < this.setValidDays.length; i++) {
        i === index ? this.$refs.validDay[i].classList.add('active') : this.$refs.validDay[i].classList.remove('active')
      }
    }
  },
  updated () {
  },
  mounted () {
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .disabled
    color: #9f9f9f
  .valid
    color: #212121
  .active
    background: $bg
  .calendar-title
    color: #212121
    font-size: .28rem
    line-height: .92rem
    text-align: center
  .calendar-content
    width: 100%
    text-align: center
    .t-header, .t-specific
      display: flex
      flex-flow: row wrap
      .t-item
        box-sizing: border-box
        display: block
        padding: .1rem
        width: 14.28%
        line-height: .85rem
        height: .85rem
        border-radius: .1rem
</style>
