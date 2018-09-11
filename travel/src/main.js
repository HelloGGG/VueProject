// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// 移动端初始化
import '@/assets/reset.css'
// 解决移动端1px显示问题
import '@/assets/border.css'
// 解决移动端300ms点击延迟
import fastclick from 'fastclick'


Vue.config.productionTip = false
fastclick.attach(document.body)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
