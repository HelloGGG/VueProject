<template>
  <div>
    <detail-header></detail-header>
    <detail-banner></detail-banner>
    <!-- <detail-list :list="list"></detail-list> -->
  </div>
</template>

<script>
import DetailBanner from './components/DetailBanner'
import DetailHeader from './components/DetailHeader'
import DetailList from './components/DetailList'
export default {
  name: 'Detail',
  components: {
    DetailBanner,
    DetailHeader,
    DetailList
  },
  data () {
    return {
      list: [
        {
          title: '成人票',
          children: [
            {
              title: '成人三日游',
              children: [{
                title: '某某旅游社提供'
              }]
            }
          ]
        }, {
          title: '儿童票'
        }, {
          title: '团体票'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  .content
    height: 20rem
</style>
