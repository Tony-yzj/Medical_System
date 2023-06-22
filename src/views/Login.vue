<template>
  <div class="login-container">
  <el-card class="login-box">
  <h1>浙大校医院快捷预约</h1>
  <el-form ref="loginForm" :model="loginForm" :rules="rules" label-width="0px">
  <h5>用户名/账号：</h5>
  <el-form-item prop="username">
  <el-input v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
  </el-form-item>
  <h5>密码：</h5>
  <el-form-item prop="password">
  <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" show-password></el-input>
  </el-form-item>
  <el-form-item>
  <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
  <!-- <el-button type="primary" @click="submitForm('loginForm')">注册</el-button> -->
  </el-form-item>
  </el-form>
  <!-- 添加二维码小标 -->
  <el-button type="text" @click="showQRCode">
   <img src="../assets/login_img/支付宝支付.svg" alt="qr_icon" width="20px" height="20px">
 </el-button>
 <el-button type="text" id="qrButton2" @click="showQRCode2">
   <img src="../assets/login_img/微信.svg" alt="qr_icon" width="20px" height="20px">
 </el-button>
  </el-card>
  <!-- 添加二维码弹窗 -->
  <!-- 使用element-ui的el-dialog组件来显示弹窗 -->
  <!-- 你需要传入一个visible.sync属性，表示弹窗的显示和隐藏 -->
  <!-- 你可以使用其他属性来自定义弹窗的样式，如title、width等 -->
  <!-- 详细的用法请参考element-ui的文档 -->
  <el-dialog title="支付宝登录" :visible.sync="qrVisible" width="27%">
    <!-- 使用qrcodejs2插件来显示二维码 -->
    <!-- 你需要传入一个text属性，表示二维码的内容 -->
    <!-- 你可以使用其他属性来自定义二维码的样式，如width、height、colorDark、colorLight等 -->
    <!-- 详细的用法请参考qrcodejs2的文档 -->
    <div id="qrCodeUrl"></div>
    <!-- 添加取消按钮 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="qrVisible = false">取消</el-button>
    </span>
  </el-dialog>
  <el-dialog title="微信登录" :visible.sync="qrVisible2" width="27%">
    <!-- 使用qrcodejs2插件来显示二维码 -->
    <!-- 你需要传入一个text属性，表示二维码的内容 -->
    <!-- 你可以使用其他属性来自定义二维码的样式，如width、height、colorDark、colorLight等 -->
    <!-- 详细的用法请参考qrcodejs2的文档 -->
    <div id="qrCodeUrl2"></div>
    <!-- 添加取消按钮 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="qrVisible2 = false">取消</el-button>
    </span>
  </el-dialog>
  </div>
  </template>
  
  <script>
  // 引入刚下载的qrcodejs2
  import QRCode from "qrcodejs2";
  export default {
  data() {
  return {
  loginForm: {
  username: "",
  password: "",
  },
  rules: {
  username: [
  { required: true, message: "请输入用户名", trigger: "blur" },
  { min: 3, max: 10, message: "长度在 3 到 10 个字符", trigger: "blur" },
  ],
  password: [
  { required: true, message: "请输入密码", trigger: "blur" },
  { min: 6, max: 20, message: "长度在 6 到 20 个字符", trigger: "blur" },
  ],
  },
  qrVisible: false, // 控制二维码弹窗的显示和隐藏
  qrVisible2: false,
  };
  },
  methods: {
  submitForm(formName) {
  this.$refs[formName].validate((valid) => {
  if (valid) {
  // 验证通过，发送请求
  // console.log(this.loginForm);
    // this.$message.success("登录成功");
    // this.$router.push("/");
    if (this.loginForm.username === "8848" && this.loginForm.password === "123456" || this.loginForm.username === "SE2023" && this.loginForm.password === "123456") {
      this.$message.success("登录成功");
      this.$router.push("/");
    } else {
      this.$message.error("账号/密码错误");
    }
  } else {
  // 验证失败，提示错误
  this.$message.error("请填写正确的表单信息");
  return false;
  }
  });
  },
  showQRCode() {
  // 切换二维码弹窗的状态
  this.qrVisible = !this.qrVisible;
  // 生成二维码
  this.$nextTick(function () {
  document.getElementById("qrCodeUrl").innerHTML = "";
  let qrCodeUrl = new QRCode("qrCodeUrl", {
  width: 200,
  height: 200,
  text:
  "https://open.weixin.qq.com/connect/qrconnect?appid=xxx&scope=xxx&redirect_uri=xxx&state=xxx&login_type=xxx&self_redirect=xxx",
  colorDark: "#000000",
  colorLight: "#fff",
  });
  });
  },
  showQRCode2() {
  // 切换二维码弹窗的状态
  this.qrVisible2 = !this.qrVisible2;
  // 生成二维码
  this.$nextTick(function () {
  document.getElementById("qrCodeUrl2").innerHTML = "";
  let qrCodeUrl = new QRCode("qrCodeUrl2", {
  width: 200,
  height: 200,
  text:
  "https://open.weixin.qq.com/connect/qrconnect?appid=xxx&scope=xxx&redirect_uri=xxx&state=xxx&login_type=xxx&self_redirect=xxx",
  colorDark: "#000000",
  colorLight: "#fff",
  });
  });
  },
  },
  };
  </script>
  
  <style lang="scss" scoped>
  .login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  // 设置背景图片
  background-image: url("../assets/login_img/login_bg.jpg");
  background-size: cover; // 背景图片自适应屏幕大小
  }
  .login-box {
  width: 400px;
  padding: 20px;
  }
  h1 {
  text-align: center;
  }
  /deep/ .dialog-footer {
  text-align: center;
  }
  /deep/ #qrCodeUrl > img {
  margin: 0 auto;
  }
  /deep/ #qrCodeUrl2 > img {
  margin: 0 auto;
  }
  </style>
 