<template>
  <div>
    <preview-header></preview-header>
    <preview-main :imgs="imgs"></preview-main>
  </div>
</template>

<script>
import PreviewHeader from './components/Header'
import PreviewMain from './components/Main'
export default {
  name: 'PicPreview',
  components: {
    PreviewHeader,
    PreviewMain
  },
  data () {
    return {
      imgs: [
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg',
        'http://img1.qunarzz.com/sight/p0/1603/5d/5dd523afbdbb037c90.water.jpg_r_800x800_181ae7c9.jpg'
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
