import Vue from 'vue'
import App from './app'
import router from './routes'
import './plugins/post'

// 创建vue app 实例
const app = new Vue({
    router,
    render: h => h(App)
})

// 挂在root dom
app.$mount('#app')