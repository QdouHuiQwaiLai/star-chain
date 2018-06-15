import Vue from 'vue'
import router from './router'
import App from './App.vue'
import Vuex from 'vuex'
import './my-axios' // 封装axios

Vue.use(VueRouter)


new Vue({
    el: '#app',
    router,
    template: '<App />',
    components: {
        App
    },
    created: function() {
        // this.$router.push('/login')
    }
})

