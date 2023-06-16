<!-- views/UserCenter.vue -->
<template>
  <div class="home">
  <!-- 头像和用户名 -->
  <!-- 我的收藏 -->
  <div class="favorites">
  <h3>我的收藏</h3>
  <el-tabs v-model="activeTab" type="card">
  <el-tab-pane label="医生" name="doctors">
  <!-- 使用el-carousel组件 -->
  <el-carousel height="200px" arrow="always">
  <el-carousel-item v-for="doctor in favoriteDoctors" :key="doctor.id">
  <div class="doctor-card">
  <img :src="doctor.avatar" class="doctor-avatar" />
  <div class="doctor-info">
  <span class="doctor-name">{{ doctor.name }}</span>
  <span class="doctor-title">{{ doctor.title }}</span>
  <span class="doctor-department">{{ doctor.department }}</span>
  <span class="doctor-intro">{{ doctor.intro }}</span>
  </div>
  <div class="doctor-action">
  <el-button type="text" @click="unfavoriteDoctor(doctor.id)">取消收藏</el-button>
  </div>
  </div>
  </el-carousel-item>
  </el-carousel>
  </el-tab-pane>
  <el-tab-pane label="文章" name="articles">
  <el-carousel height="200px" arrow="always">
  <el-carousel-item v-for="article in favoriteArticles" :key="article.id">
  <div class="article-card">
  <img :src="article.image" class="article-image" />
  <div class="article-info">
  <span class="article-title">{{ article.title }}</span>
  <span class="article-author">{{ article.author }}</span>
  <span class="article-date">{{ article.date }}</span>
  <span class="article-summary">{{ article.summary }}</span>
  </div>
  <div class="article-action">
  <el-button type="text" @click="unfavoriteArticle(doctor.id)">取消收藏</el-button>
  </div>
  </div>
  </el-carousel-item>
  </el-carousel>
  </el-tab-pane>
  </el-tabs>
  </div>
  <!-- 我的消息 -->
  <div class="messages">
  <h3>我的消息</h3>
  <el-table :data="messages" border style="width: 100%">
  <el-table-column prop="content" label="内容"></el-table-column>
  <el-table-column prop="time" label="时间"></el-table-column>
  <el-table-column prop="status" label="状态"></el-table-column>
  <el-table-column label="操作">
  <template slot-scope="{ row }">
  <el-button type="text" @click.native.prevent.stop="
  markAsRead(row.id)
  ">标记已读</el-button
  >
  |
  <el-button type="text" @click.native.prevent.stop="
  deleteMessage(row.id)
  ">删除</el-button
  >
  </template>
  </el-table-column>
  </el-table>
  </div>
  </div>
 </template>
 
 <script>
 // 导入vue-horizontal-list组件
  import VueHorizontalList from "vue-horizontal-list";
 export default {
  name: "UserCenter",
  data() {
  return {
  // 模拟头像和用户名数据
  avatar: require("../assets/user_img/avatar.jpg"),
  username: "蔡旭琨",
  // 模拟收藏医生数据
  favoriteDoctors: [
  {
  id: 1,
  avatar: require("../assets/doctor_img/doctor_1.jpg"),
  name: "张三 ",
  title: "主任医师 ",
  department: "内科 ",
  intro: "张三医生是一位经验丰富的内科医师，擅长治疗各种内科疾病，尤其是心血管方面的问题。他曾在多个国际期刊上发表过论文，获得过多项荣誉和奖励。他对待患者耐心细致，深受好评。",
  },
  {
  id: 2,
  avatar: require("../assets/doctor_img/doctor_2.jpg"),
  name: "王五 ",
  title: "副主任医师 ",
  department: "外科 ",
  intro: "王五医生是一位技术精湛的外科医师，擅长进行各种外科手术，尤其是神经外科方面的操作。他曾在多个国际会议上做过报告，获得过多项专利和证书。他对待患者热情周到，深受信赖。",
  },
  ],
  // 模拟收藏文章数据
  favoriteArticles: [
  {
  id: 1,
  image: require("../assets/article_img/cold.jpg"),
  title: "如何预防感冒",
  author: "赵六",
  date: "2023-01-01",
  summary: "感冒是一种常见的呼吸道疾病，通常由病毒感染引起。感冒的症状包括发烧、咳嗽、流鼻涕、喉咙痛等。感冒虽然不是什么大病，但也会影响人们的工作和生活。本文将介绍如何预防感冒，以及感冒时如何进行自我护理。"
  },
  {
  id: 2,
  image: require("../assets/article_img/sleep.jpg"),
  title: "如何保持良好的睡眠习惯",
  author: "孙七",
  date: "2023-01-02",
  summary: "睡眠是人体必需的生理活动之一，对于保持身心健康有着重要的作用。睡眠不足或者睡眠质量差会导致精神萎靡、注意力不集中、免疫力下降等问题。本文将介绍如何保持良好的睡眠习惯，以及如何改善睡眠障碍。"
  },
  ],
  // 模拟消息数据
  messages: [
  {
  id: 1,
  content: "您预约的李四医生已经确认，请按时就诊。",
  time: "2023-01-03 10:00",
  status: "未读",
  },
  {
  id: 2,
  content: "您预约的王五医生已经取消，请重新预约。",
  time: "2023-01-04 11:00",
  status: "已读",
  },
  ],
  // 当前激活的标签页
  activeTab: "doctors",
  };
  },
  methods: {
  // 跳转到修改信息页面
  editProfile() {
  this.$router.push("/edit-profile");
  },
  // 取消收藏医生
  unfavoriteDoctor(id) {
  this.favoriteDoctors = this.favoriteDoctors.filter(
  (doctor) => doctor.id !== id
  );
  this.$message.success("取消收藏成功");
  },
  // 取消收藏文章
  unfavoriteArticle(id) {
  this.favoriteArticles = this.favoriteArticles.filter(
  (article) => article.id !== id
  );
  this.$message.success("取消收藏成功");
  },
  // 标记消息已读
  markAsRead(id) {
  const message = this.messages.find((message) => message.id === id);
  if (message.status === "未读") {
  message.status = "已读";
  this.$message.success("标记已读成功");
  }
  },
  // 删除消息
  deleteMessage(id) {
  this.messages = this.messages.filter((message) => message.id !== id);
  this.$message.success("删除消息成功");
  },
  },
 };
 </script>
 
 <style scoped>
 .home {
  padding: 20px;
 }
 .username {
  margin-left: 10px;
  font-size: 24px;
  font-weight:bold;
 }
 .favorites h3, .messages h3{
  font-weight:bold;
  margin-bottom:10px;
 }
 .doctor-card, .article-card{
  display:flex;
  align-items:center;
  justify-content:flex-start;
 }
 .doctor-avatar{
  width:auto;
  height:auto;
  max-width:200px;
  max-height:200px;
 }
 .article-image
 {
  width:auto;
  height:auto;
  max-width:300px;
  max-height:300px;
 }
 .doctor-info, .article-info{
  margin-left:auto;
  margin-right:auto;
  flex-direction: column;
  display: flex;
 }
 .article-title, .doctor-name{
  font-size: 24px;
 }
 .doctor-action, .article-action{
  margin-left:auto;
  margin-right:auto;
  align-self: flex-start;
 }
 </style>
 
 