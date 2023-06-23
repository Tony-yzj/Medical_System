<template>
  <div class="doctor">
  <!-- 搜索框 -->
  <el-input
  v-model="search"
  placeholder="请输入医生姓名或科室"
  clearable
  @clear="handleClear"
  @keyup.enter.native="handleSearch"
  >
  <el-button slot="append" icon="el-icon-search" @click="handleSearch"></el-button>
  </el-input>
  <!-- 折叠面板 -->
  <el-collapse v-model="activeNames">
  <el-collapse-item v-for="doctor in doctors" :key="doctor.id" :name="doctor.id">
  <!-- 面板标题 -->
  <template slot="title">
  <!-- 姓名 -->
  <span class="name">{{ doctor.name }}</span>
  <!-- 科室 -->
  <el-tag type="info">{{ doctor.department }}</el-tag>
  <!-- 职称 -->
  <el-tag type="success">{{ doctor.title }}</el-tag>
  <!-- 擅长 -->
  <span class="expertise">{{ getExpertise(doctor.department, doctor.id) }}</span>
  </template>
  <!-- 面板内容 -->
  <div class="content">
  <!-- 头像 -->
  <img :src="doctor.avatar" class="avatar" />
  <!-- 简介 -->
  <div class="description">{{ doctor.description }}</div>
  <!-- 预约情况 -->
  <div class="booking">
  <span>预约情况：</span>
  <el-progress :percentage="doctor.booked / doctor.total * 100" status="success"></el-progress>
  <span>{{ doctor.booked }} / {{ doctor.total }}</span>
  </div>
  <!-- 评价 -->
  <div class="rating">
  <span>评价：</span>
  <!-- 气泡卡片 -->
  <el-popover placement="top-start" trigger="hover" popper-class="rating-popover">
  <!-- 气泡内容 -->
  <ul>
  <li v-for="(comment, index) in doctor.comments" :key="index">{{ comment }}</li>
  </ul>
  <!-- 气泡触发元素 -->
  <el-rate slot="reference" v-model="doctor.rating" disabled></el-rate>
  </el-popover>
  </div>
  <!-- 预约按钮 -->
  <el-button type="primary" @click="handleBooking(doctor)">咨询请求</el-button>
  </div>
  </el-collapse-item>
  </el-collapse>
  </div>
 </template>
 
 <script>
 import axios from "axios";
 
 export default {
  name: "Doctor",
  data() {
  return {
  search: "", // 搜索关键字
  activeNames: [], // 激活的面板名称
  doctors: [], // 医生数据
  };
  },
  computed: {
   // 根据科室的名称返回对应的专长
   expertiseByDepartment() {
    return {
     '内科': ['感冒', '发烧', '头痛', '胃痛'],
     '外科': ['骨折', '关节炎', '创伤', '烧伤'],
     '儿科': ['儿童感冒', '儿童发烧', '异物吞咽', '儿童综合'],
     '妇产科':['孕吐', '分娩', '胎位矫正', '孕期不适'],
     '眼科': ['青光眼', '近视', '视力下降', '白内障'],
     // 其他科室和专长
    }
   }
  },
  methods: {
   // 获取医生数据的函数
   fetchDoctors() {
    // 使用axios从后端获取数据，实际情况可能不同
    axios
     .get(
      `https://jsonplaceholder.typicode.com/users?name_like=${this.search}`
     )
     .then((res) => {
      const data = res.data;
      // 更新医生数据，并添加一些模拟数据，实际情况可能不同
      this.doctors = data.map((item) => ({
       ...item,
       avatar:
        item.gender === "male"
         ? require("../assets/icon/男医生.svg")
         : require("../assets/icon/女医生.svg"),
       department: ["内科", "外科", "儿科", "妇产科", "眼科"][Math.floor(Math.random() * 5)],
       title: ["主任医师", "副主任医师", "主治医师", "住院医师"][Math.floor(Math.random() * 4)],
       description: item.company.catchPhrase,
       total: Math.floor(Math.random() * 10) + 10,
       booked: Math.floor(Math.random() * 10),
       rating: Math.floor(Math.random() * 3) + 3,
       comments: [
        "非常专业，态度很好",
        "解答了我的疑问，很有耐心",
        "诊断准确，治疗有效",
        "人很亲切，很有亲和力",
        "非常满意，推荐给大家",
       ].slice(0, Math.floor(Math.random() * 5) + 1),
      }));
     })
     .catch((error) => {
      // 查询失败时，弹出错误提示
      this.$message.error(error.message);
     });
   },
   // 处理搜索事件
   handleSearch() {
    this.fetchDoctors(); // 刷新数据
   },
   // 处理清空事件
   handleClear() {
    this.fetchDoctors(); // 刷新数据
   },
   // 处理预约事件
   handleBooking(doctor) {
    if(doctor.booked == doctor.total)
      this.$message.error(`${doctor.name}医生的咨询名额已满，暂不可预约`);
    else{
      doctor.booked = doctor.booked + 1;
      this.$message.success(`您已成功预约${doctor.name}医生咨询，详情请见信息`); // 弹出成功提示
    }
   },
   // 根据科室的名称返回对应的专长
   getExpertise(department, id) {
    return this.expertiseByDepartment[department][id%4] || [];
   }
  },
  created() {
   // 获取路由参数中的搜索关键字，如果有的话
   this.search = this.$route.query.search || "";
 
   // 获取医生数据
   this.fetchDoctors();
  },
 };
 </script>
 
 <style scoped>
 .doctor {
  margin: 20px;
 }
 .avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
 }
 .name {
  font-size: 24px;
  font-weight: bold;
 }
 .expertise {
  color: #666;
 }
 .description {
  margin-top: 10px;
 }
 .booking {
  margin-top: 10px;
 }
 .rating {
  margin-top: 10px;
 }
 .rating-popover {
  max-height: 200px;
  overflow-y: auto;
 }
 </style>
 
 