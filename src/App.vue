<template>
  <div id="app">
    <Main/>
    <!-- 或者使用<router-view/>来显示路由组件 -->
    <!-- <router-view/> -->
  </div>
</template>

<script>
import Login from './views/Login.vue'
import Main from './views/Main.vue'
import Home from './views/Home.vue'
import User from './views/UserCenter.vue'
import Doctor from './views/Doctor.vue'
import Appointment from './views/Appointment.vue'
import Records from './views/Records.vue'

export default {
  name: 'App',
  components: {
    Login,
    Main,
    User,
    Home,
    Doctor,
    Appointment,
    Records,
  }
}
</script>

<style>

</style>

