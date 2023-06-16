<!-- Booking.vue -->
<template>
    <div class="booking">
    <!-- 预约表单 -->
    <el-form :model="form" label-width="100px" @submit.native.prevent="handleSubmit">
    <!-- 隐藏的医生id -->
    <input type="hidden" v-model="form.doctor" />
    <!-- 显示的医生姓名 -->
    <el-form-item label="医生">
    {{ getDoctorNameById(form.doctor) }}
    </el-form-item>
    <!-- 选择日期 -->
    <el-form-item label="日期">
    <el-date-picker
    v-model="form.date"
    type="date"
    placeholder="选择日期"
    :picker-options="datePickerOptions"
    ></el-date-picker>
    </el-form-item>
    <!-- 选择时间 -->
    <el-form-item label="时间">
    <el-time-select
    v-model="form.time"
    placeholder="选择时间"
    :picker-options="timePickerOptions"
    ></el-time-select>
    </el-form-item>
    <!-- 提交按钮 -->
    <el-form-item>
    <el-button type="primary" native-type="submit">提交</el-button>
    </el-form-item>
    </el-form>
    <!-- 预约结果 -->
    <div v-if="result">
    <div v-if="result.success" class="success">
    <h3>预约成功</h3>
    <p>您已成功预约{{ result.doctor }}医生</p>
    <p>预约日期：{{ result.date }}</p>
    <p>预约时间：{{ result.time }}</p>
    </div>
    <div v-else class="error">
    <h3>预约失败</h3>
    <p>{{ result.message }}</p>
    </div>
    </div>
    </div>
   </template>
   
   <script>
   import axios from "axios";
   
   export default {
    name: "Booking",
    props: {
     doctorId: {
      type: String,
      default: "",
     },
    },
    data() {
     return {
      form: {
       doctor: this.doctorId, // 默认选择传入的医生id
       date: "",
       time: "",
      },
      doctors: [], // 医生数据
      result: null, // 预约结果
     };
    },
    computed: {
     // 日期选择器的选项
     datePickerOptions() {
      return {
       // 禁用今天之前的日期
       disabledDate(date) {
        return date.getTime() < Date.now() - 8.64e7;
       },
      };
     },
     // 时间选择器的选项
     timePickerOptions() {
      return {
       // 只显示整点和半点
       format: "HH:mm",
       start: "08:00",
       step: "00:30",
       end: "17:30",
      };
     },
    },
    methods: {
     // 获取医生数据的函数
     fetchDoctors() {
      // 使用axios从后端获取数据，实际情况可能不同
      axios
       .get("https://jsonplaceholder.typicode.com/users")
       .then((res) => {
        const data = res.data;
        // 更新医生数据，并添加一些模拟数据，实际情况可能不同
        this.doctors = data.map((item) => ({
         ...item,
         name: item.name + "医生",
        }));
       })
       .catch((error) => {
        // 查询失败时，弹出错误提示
        this.$message.error(error.message);
       });
     },
     // 处理提交事件
     handleSubmit() {
      // 检查表单是否完整
      if (!this.form.doctor || !this.form.date || !this.form.time) {
       this.$message.warning("请填写完整的预约信息");
       return;
      }
      // 使用axios向后端发送预约请求，实际情况可能不同
      axios
       .post("https://jsonplaceholder.typicode.com/posts", this.form)
       .then((res) => {
        const data = res.data;
        // 模拟预约成功或失败的结果，实际情况可能不同
        if (Math.random() > 0.5) {
         this.result = {
          success: true,
          doctor: this.getDoctorNameById(data.doctor),
          date: data.date,
          time: data.time,
         };
         this.$message.success("预约成功");
        } else {
         this.result = {
          success: false,
          message: "预约失败，请稍后重试",
         };
         this.$message.error("预约失败");
        }
       })
       .catch((error) => {
        // 预约失败时，弹出错误提示
        this.result = {
         success: false,
         message: error.message,
        };
        this.$message.error(error.message);
       });
     },
     // 根据医生id获取医生姓名的函数
     getDoctorNameById(id) {
      const doctor = this.doctors.find((item) => item.id === id);
      return doctor ? doctor.name : "";
     },
    },
    mounted() { // 注意这里使用mounted而不是created钩子函数，因为需要等待组件渲染完成才能获取传入的属性值
     // 获取医生数据
     this.fetchDoctors();
    },
   };
   </script>
   
   <style scoped>
   .booking {
    margin: 20px;
   }
   .success {
    color: green;
   }
   .error {
    color: red;
   }
   </style>
   
   