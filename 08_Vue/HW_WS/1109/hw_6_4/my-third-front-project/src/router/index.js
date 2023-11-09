import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
// import OtherView from '@/views/OtherView.vue'
import StudentViews from '@/views/StudentViews.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'some',
      component: SomeView
    },
    {
      path: '/other',
      name: 'other',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/OtherView.vue')
    },
    {
      path: '/students',
      name:'students',
      component: StudentViews
    },
    {
      path: '/students/:name',
      name:'studentsname',
      component: StudentDetailView
    }
  ]
})

export default router
