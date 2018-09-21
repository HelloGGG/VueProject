import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home/Home'
import City from '@/pages/city/City'
import Detail from '@/pages/detail/Detail'
import PicPreview from '@/pages/picPreview/PicPreview'
import Eval from '@/pages/eval/Eval'
import Place from '@/pages/place/Place'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/city',
      name: 'City',
      component: City
    }, {
      path: '/detail/:id',
      name: 'Detail',
      component: Detail
    }, {
      path: '/picPreview',
      name: 'PicPreview',
      component: PicPreview
    }, {
      path: '/evaluation',
      name: 'Eval',
      component: Eval
    }, {
      path: '/place/:id',
      name: 'Place',
      component: Place
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return {x: 0, y: 0}
  }
})
