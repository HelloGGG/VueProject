<template>
  <div>
    <detail-banner></detail-banner>
  </div>
</template>

<script>
import DetailBanner from './components/DetailBanner'
export default {
  name: 'Detail',
  components: {
    DetailBanner
  },
  data () {
    return {
      show: true
    }
  },
  methods: {
    handleClose () {

    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
