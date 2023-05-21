import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import User from '../views/UserCenter.vue'
import Doctor from '../views/Doctor.vue'
import Appointment from '../views/Appointment.vue'
import Department from "../views/Department.vue";

Vue.use(VueRouter)

const routes = [
  { path:'/', component: Home },
  { path:'/user', component: User },
  { path:'/login', component: Login},
  { path:'/doctors', component: Doctor},
  { path:'/appointments', component: Appointment,
  children: [
    {
      path: "/:department",
      name: "消化内科",
      component: Department,
    },
  ],
  }
]

const router = new VueRouter({
   routes
})

export default router
