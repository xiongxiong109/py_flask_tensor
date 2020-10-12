import Vue from 'vue'
import axios from 'axios'

const post = {}

post.install = function(Vue, options) {
    Vue.prototype.$post = function() {
        return axios.post(...arguments)
    }
}

Vue.use(post)