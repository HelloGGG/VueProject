<template>
  <div class="alpha-bet">
    <div class="alpha">A</div>
    <div class="alpha">B</div>
    <div class="alpha">C</div>
    <div class="alpha">D</div>
    <div class="alpha">E</div>
    <div class="alpha">F</div>
    <div class="alpha">G</div>
    <div class="alpha">H</div>
    <div class="alpha">I</div>
    <div class="alpha">J</div>
    <div class="alpha">K</div>
    <div class="alpha">L</div>
    <div class="alpha">M</div>
    <div class="alpha">N</div>
    <div class="alpha">O</div>
    <div class="alpha">P</div>
    <div class="alpha">Q</div>
    <div class="alpha">R</div>
    <div class="alpha">S</div>
    <div class="alpha">T</div>
    <div class="alpha">U</div>
    <div class="alpha">V</div>
    <div class="alpha">W</div>
    <div class="alpha">X</div>
    <div class="alpha">Y</div>
    <div class="alpha">Z</div>
  </div>
</template>

<script>
export default {
  name: 'CityAlphaBet'  
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variable.styl'
  .alpha-bet
    display: flex
    flex-flow: column wrap
    align-items: center
    position: absolute
    right: 0
    top: 3.5rem
    width: .2rem
    z-index: 10
    margin-right: .1rem
    .alpha
     line-height: .3rem
     margin:.02rem 0
     color: $bg
</style>
