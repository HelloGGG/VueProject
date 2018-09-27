<template>
  <div>
    <place-header></place-header>
    <place-reference :reference="reference"></place-reference>
    <place-play :play="play"></place-play>
    <place-tip :tips="tips"></place-tip>
    <!-- <place-transport :transportation="transportation"></place-transport> -->
  </div>
</template>

<script>
import PlaceHeader from './components/PlaceHeader'
import PlaceReference from './components/PlaceReference'
import PlacePlay from './components/PlacePlay'
import PlaceTip from './components/PlaceTip'
import PlaceTransport from './components/PlaceTransport'
import axios from 'axios'
export default {
  name: 'Place',
  components: {
    PlaceHeader,
    PlaceReference,
    PlacePlay,
    PlaceTip,
    PlaceTransport
  },
  data () {
    return {
      reference: [],
      play: [],
      tips: [],
      transportation: {},
      latestUrl: ''
    }
  },
  methods: {
    getPlaceData () {
      axios.get('api/placeInfo?url=' + this.$store.state.place).then(this.getPlaceDataSucc)
    },
    getPlaceDataSucc (res) {
      if (res) {
        this.reference = res.data.reference
        this.tips = res.data.tips
        this.transportation = res.data.transportation
        this.play = res.data.play
      }
    }
  },
  mounted () {
    this.getPlaceData()
    this.latestUrl = this.$store.state.place
  },
  activated () {
    if (this.latestUrl !== this.$store.state.place) {
      this.getPlaceData()
      console.log(this.$store.state.place)
      this.latestUrl = this.$store.state.place
    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
