<template>
  <div class="calendar-month">
    <div class="select-wrapper">
      <select
        v-model="selectY"
        class="calendar-title"
      >
        <option
          :value="defaultCYear + i - 1"
          v-for="i in 1"
          :key="i"
        >
          {{defaultCYear + i - 1}}
        </option>
      </select>
      年
      <select
        v-model="selectM"
        class="calendar-title"
      >
        <option
          :value="i"
          v-for="i in 12"
          :key="i+20"
        >
          {{i}}
        </option>
      </select>
      月
    </div>
    <div class="calendar-content">
      <div class="t-header">
        <div class="t-item"
          v-for="(item, index) in week"
          :key="index+2000"
        >{{item}}</div>
        <div class="t-item disabled" v-for="item in blankNum" :key="item+500"></div>
        <div v-if="isDisabledFirst" class="t-item disabled" v-for="item in firstRowStart" :key="item+600">{{item}}</div>
        <div
          v-if="!isDisabledFirst"
          class="t-item"
          v-for="(item,index) in firstRowStart"
          :key="item+800"
          ref="validDay"
          @click="handleValidClick(index)">{{item}}</div>
        <div
          v-if="!isDisabledFirst"
          class="t-item"
          v-for="(day, index) in setSecondStartdays"
          :key="day+100"
          @click="handleValidClick(index + firstRowStart)"
          ref="validDay"
        >
          {{day}}
        </div>
         <div
          v-if="isDisabledFirst"
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
import { mapMutations } from 'vuex'
export default {
  props: {
    defaultCYear: Number,
    defaultCMonth: Number
  },
  name: 'Calendar',
  data () {
    return {
      week: ['日', '一', '二', '三', '四', '五', '六'],
      selectM: this.defaultCMonth,
      selectY: this.defaultCYear
    }
  },
  computed: {
    RealM () {
      return this.selectM - 1
    },
    currentYear () {
      var date = new Date()
      return date.getFullYear()
    },
    currentMonth () {
      var date = new Date()
      return date.getMonth()
    },
    isDisabledFirst () {
      return this.selectY < this.currentYear || (this.selectY === this.currentYear && this.RealM <= this.currentMonth)
    },
    getCurrentMonthdays () {
      var date = new Date(this.selectY, this.RealM, 1)
      // 获取当前月份天数
      var nextMonth = new Date(date.setMonth(date.getMonth() + 1))
      var lastday = new Date(nextMonth.setDate(nextMonth.getDate() - 1))
      return lastday.getDate()
    },
    getTrs () {
      return Math.ceil(this.getCurrentMonthdays / 7)
    },
    secondRowStart () {
      var date = new Date(this.selectY, this.RealM, 1)
      switch (date.getDay()) {
        case 0: return 8
        case 1: return 7
        case 2: return 6
        case 3: return 5
        case 4: return 4
        case 5: return 3
        case 6: return 2
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
        // 今年本月
        if (today.getFullYear() === this.selectY && today.getMonth() === this.RealM) {
          if (i === tadayNum) {
            temp.push('今天')
          }
          if (i >= this.secondRowStart && i < tadayNum) {
            temp.push(i)
          }
        } else {
          if (i >= this.secondRowStart) {
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
        // 今年本月,设置可订日期
        if (today.getFullYear() === this.selectY && today.getMonth() === this.RealM) {
          if (i > tadayNum) {
            temp.push(i)
          }
        }
      }
      return temp
    }
  },
  methods: {
    handleValidClick (index) {
      var today = new Date()
      if (today.getFullYear() === this.selectY && today.getMonth() === this.RealM) {
        for (let i = 0; i < this.setValidDays.length; i++) {
          i === index ? this.$refs.validDay[i].classList.add('active') : this.$refs.validDay[i].classList.remove('active')
        }
      } else {
        for (let i = 0; i < this.getCurrentMonthdays; i++) {
          i === index ? this.$refs.validDay[i].classList.add('active') : this.$refs.validDay[i].classList.remove('active')
        }
      }
      this.changeOtherDay(this.$refs.validDay[index].innerText)
      this.changeOtherMonth(this.selectM)
      this.$emit('closeCalendar')
    },
    ...mapMutations(['changeOtherDay', 'changeOtherMonth'])
  },
  updated () {
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .select-wrapper >>> .el-input__inner
    width: 2rem
  .disabled
    color: #9f9f9f
  .valid
    color: #212121
  .active
    background: $bg
  .select-wrapper
    line-height: .92rem
    text-align: center
    .calendar-title
      color: #212121
      font-size: .28rem
      line-height: .92rem
  .calendar-content
    width: 100%
    text-align: center
    padding-bottom: .2rem
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
