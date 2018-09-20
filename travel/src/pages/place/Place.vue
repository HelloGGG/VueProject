<template>
  <div>
    <place-header></place-header>
    <place-reference></place-reference>
  </div>
</template>

<script>
import PlaceHeader from './components/PlaceHeader'
import PlaceReference from './components/PlaceReference'
export default {
  name: 'Place',
  components: {
    PlaceHeader,
    PlaceReference
  }
}
</script>

<style lang="stylus" scoped>

</style>
