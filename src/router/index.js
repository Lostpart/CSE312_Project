import { createRouter, createWebHistory } from 'vue-router'
import hello from '../views/hello.vue'


const routes = [
  {
   path: '/',
   name:'hello',
   component: hello
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
