import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueQrcode from 'vue-qrcode'
import axios from 'axios'
import router from './router/index.js'
import App from './App.vue'

Vue.use(ElementUI)
Vue.use(VueQrcode)
Vue.prototype.$axios = axios
axios.defaults.baseURL = 'http://localhost:8080' // 这里根据你的实际地址修改

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
