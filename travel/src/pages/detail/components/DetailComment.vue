<template>
  <div class="wrapper">
     <div class="c-title border-bottom">用户评论</div>
      <comment
        v-for="user in commentList"
        :key="user.commentId"
        :user="user"
      ></comment>
      <router-link to="/evaluation">
        <list-more>查看全部评论 &#xe62d;</list-more>
      </router-link>
  </div>
</template>

<script>
import Comment from './Comment'
import ListMore from 'common/ListMore'
export default {
  props: {
    commentList: Array
  },
  name: 'DetailComment',
  components: {
    Comment,
    ListMore
  },
  data () {
    return {
    }
  }
}
</script>

<style lang="stylus" scoped>
  .c-title
    line-height: .88rem
    font-size: .3rem
    padding-left: .4rem
  .c-title::after
    content: ""
    position: absolute
    top: .32rem
    left: .2rem
    width: .07rem
    height: .25rem
    background: #1ba9ba
    border-radius: .05rem
</style>
