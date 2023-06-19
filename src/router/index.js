import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import User from '../views/UserCenter.vue'
import Doctor from '../views/Doctor.vue'
import Appointment from '../views/Appointment.vue'
import Records from "../views/Records.vue"
import Digest from '../views/Department/Digest.vue'
import Neurology from '../views/Department/Neurology.vue'
import Respiratory from '../views/Department/Respiratory.vue'
import Cardiovascular from '../views/Department/Cardiovascular.vue'
import General from '../views/Department/General.vue'
import Neurosurgery from '../views/Department/Neurosurgery.vue'
import Orthopedics from '../views/Department/Orthopedics.vue'
import Urology from '../views/Department/Urology.vue'
import PediatricInternal from '../views/Department/PediatricInternal.vue'
import PediatricSurgery from '../views/Department/PediatricSurgery.vue'
import PediatricNeurology from '../views/Department/PediatricNeurology.vue'
import PediatricCardio from '../views/Department/PediatricCardio.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/user', component: User },
  { path: '/login', component: Login },
  { path: '/doctors', component: Doctor },
  { path:'/records', component: Records},
  {
    path: '/appointments',
    component: Appointment,
    children: [
      //消化内科 神经内科 呼吸内科 心血管内科
      { path: 'digest', component: Digest },
      { path: 'neurology', component: Neurology },
      { path: 'respiratory', component: Respiratory },
      { path: 'cardio', component: Cardiovascular },
      { path: '', component: Digest},
      //普外科 神经外科 骨科 泌尿外科
      { path: 'general', component: General },
      { path: 'neurosurgery', component: Neurosurgery },
      { path: 'orthopedics', component: Orthopedics },
      { path: 'urology', component: Urology },
      //小儿内科 小儿外科 小儿神经科 小儿心脏科
      { path: 'pediatric-internal', component: PediatricInternal },
      { path: 'pediatric-surgery', component: PediatricSurgery },
      { path: 'pediatric-neuro', component: PediatricNeurology },
      { path: 'pediatric-cardio', component: PediatricCardio },
    ],
  },
]

const router = new VueRouter({
  routes
})

// 解决重复点击路由报错问题
const orignPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return orignPush.call(this, location).catch(err => err)
}

export default router
