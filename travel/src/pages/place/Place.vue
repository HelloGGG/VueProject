<template>
  <div>
    <place-header></place-header>
    <place-reference></place-reference>
    <place-play></place-play>
    <place-tip></place-tip>
    <place-transport></place-transport>
  </div>
</template>

<script>
import PlaceHeader from './components/PlaceHeader'
import PlaceReference from './components/PlaceReference'
import PlacePlay from './components/PlacePlay'
import PlaceTip from './components/PlaceTip'
import PlaceTransport from './components/PlaceTransport'
export default {
  name: 'Place',
  components: {
    PlaceHeader,
    PlaceReference,
    PlacePlay,
    PlaceTip,
    PlaceTransport
  }
}
</script>

<style lang="stylus" scoped>

</style>
