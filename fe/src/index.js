import Vue from 'vue'
import App from './app'

// 创建vue app 实例
const app = new Vue({
    render: h => h(App)
})

// 挂在root dom
app.$mount('#app')

if (module.hot) {
    console.log(module.hot)
}