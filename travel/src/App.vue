<template>
  <div id="app">
    <keep-alive exclude="Place">
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="stylus">
</style>
