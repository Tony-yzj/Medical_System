<!-- views/Home.vue -->
<template>
  <div class="home">
  <!-- 登录按钮 -->
  <div class="login">
  <el-button type="primary" size="small" @click="goTo("http://192.168.43.109:8080/home")">登录</el-button>
  </div>
  <!-- 轮播图 -->
  <el-carousel height="400px" autoplayTimeout="3000" indicator-position="outside" navigation-enabled="true" arrow-key-nav="true">
  <el-carousel-item v-for="item in images" :key="item.id">
  <img :src="item.url" alt="image" class="image" />
  </el-carousel-item>
  </el-carousel>
  <!-- 介绍 -->
  <div class="intro">
  <h2>欢迎来到浙大校医院快捷预约系统</h2>
  <p>
  这是一个为浙大师生提供便捷、高效、安全的医疗预约服务的平台。你可以在这里查询医生的信息，预约你想要看的医生，查看你的预约记录，以及取消或修改你的预约。我们致力于为你提供最优质的医疗服务，让你享受健康和快乐的校园生活。
  </p>
  </div>
  <!-- 模块 -->
  <div class="modules">
  <!-- 修改justify和gutter属性 -->
  <el-row :gutter="100" justify="center">
  <el-col :span="6" v-for="module in modules" :key="module.id">
  <el-card :body-style="{ padding: '0px' }">
  <img :src="module.icon" class="icon" />
  <div style="padding: 14px;">
  <span>{{ module.name }}</span>
  <div class="bottom clearfix">
  <el-button type="text" @click="goTo(module.path)">进入</el-button>
  </div>
  </div>
  </el-card>
  </el-col>
  </el-row>
  </div>
  <!-- 新闻资讯 -->
  <div class="news">
  <h3>新闻资讯</h3>
  <ul>
  <li v-for="news in newsList" :key="news.id">
  <a :href="news.url">{{ news.title }}</a>
  <span>{{ news.date }}</span>
  </li>
  </ul>
  </div>
  </div>
 </template>
 
 <script>
 export default {
  name: "Home",
  data() {
  return {
  // 模拟轮播图数据
  images: [
  {
  id: 1,
  url: require("../assets/home_img/1.jpg"),
  },
  {
  id: 2,
  url: require("../assets/home_img/2.jpg"),
  },
  {
  id: 3,
  url: require("../assets/home_img/3.jpg"),
  },
  ],
  // 模拟模块数据
  modules: [
  {
  id: 1,
  name: "医生查询",
  icon: require("../assets/icon/医生.svg"),
  path: "/doctors",
  },
  {
  id: 2,
  name: "预约挂号",
  icon: require("../assets/icon/预约.svg"),
  path: "/appointments",
  },
  {
  id: 3,
  name: "预约记录",
  icon: require("../assets/icon/记录.svg"),
  path: "/records",
  },
  {
  id: 4,
  name: "康复系统",
  icon: require("../assets/icon/知识.svg"),
  path: "/knowledge",
  },
  ],
  // 模拟新闻资讯数据
  newsList: [
  {
  id: 1,
  title:
  "浙大校医院开展“爱眼日”义诊活动",
  url:
  "https://www.zju.edu.cn/yy/2023/0617/c105a2023/page.htm",
  date: "2023-05-17",
  },
  {
  id: 2,
  title:
  "浙大校医院与浙江省人民医院签署战略合作协议",
  url:
  "https://www.zju.edu.cn/yy/2023/0519/c105a2023/page.htm",
  date: "2023-05-19",
  },
  {
  id: 3,
  title:
  "浙大校医院荣获“全国文明单位”称号",
  url:
  "https://www.zju.edu.cn/yy/2023/0428/c105a2023/page.htm",
  date: "2023-04-28",
  },
  ],
  };
  },
  methods: {
  // 跳转到指定路径
  goTo(path) {
  this.$router.push(path);
  },
  },
 };
 </script>
 
 <style scoped>
 .home {
  padding: 20px;
  /* background-color: rgb(115, 185, 162); */
 }
 .image {
  width: 100%;
  height: 100%;
 }
 .intro {
  margin-top: 20px;
 }
 .modules {
  margin-top: 20px;
 }
 .icon {
  width: 100%;
 }
 .news {
  margin-top: 20px;
 }
 .news h3 {
  font-weight: bold;
 }
 .news ul {
  list-style-type:none;
 }
 .news li {
  display:flex;
  justify-content: space-between;
 }
 .news a {
  color:black;
 }
 .news span {
  color:#999;
 }
 .login {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-bottom: 20px;
 }
 
 /* 自定义轮播图导航样式 */
 .el-carousel__arrow--left i, .el-carousel__arrow--right i{
  font-size: 36px; /* 设置箭头大小 */
  color:white; /* 设置箭头颜色 */
 }
 
 .el-carousel__indicators{
  background-color:#f0f0f0; /* 设置指示器背景颜色 */
  border-radius:10px; /* 设置指示器圆角 */
 }
 
 .el-carousel__indicator{
  width:auto; /* 设置指示器宽度 */
  height:auto; /* 设置指示器高度 */
 }
 
 .el-carousel__button{
  width:auto; /* 设置指示器按钮宽度 */
  height:auto; /* 设置指示器按钮高度 */
 }
 
 .el-carousel__button:hover{
  background-color:#409eff; /* 设置指示器按钮悬停颜色 */
 }
 
 .el-carousel__button.is-active{
  background-color:#409eff; /* 设置指示器按钮激活颜色 */
 }
 
 </style>
 
 