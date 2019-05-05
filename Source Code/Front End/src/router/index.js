import Vue from 'vue'
import Router from 'vue-router'
import i from '@/components/i'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'i',
      component: i
    },
    {
      path: '*',
      component: 'NotFound'
    }
  ]
})
