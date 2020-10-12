import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: () => import('./pages/blog')
    },
    {
        path: '/auth/login',
        component: () => import('./pages/auth/login')
    },
    {
        path: '/auth/register',
        component: () => import('./pages/auth/register')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router