import Vue from 'vue'
import axios from 'axios'
import { Indicator } from 'mint-ui'

Vue.prototype.$axios = axios

//添加请求拦截器
axios.interceptors.request.use(config => {
    Indicator.open()
    return config
  }, error => {
    Indicator.close()
    return Promise.reject(error)
  })
  //添加响应拦截器
  axios.interceptors.response.use(response => {
    Indicator.close()
    return response
  }, error => {
    Indicator.close()
    return Promise.reject(error)
  })

// 请求基础路径
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

// 带cookie请求
axios.defaults.withCredentials = true