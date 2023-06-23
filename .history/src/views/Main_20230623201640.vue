<!-- views/Main.vue -->
<template>
  <div class="container">
    <!-- 导航栏 -->
    <el-header class="header">
      <el-row type="flex" justify="space-between" align="middle">
        <el-col :span="4">
          <!-- logo -->
          <img src="../assets/logo.jpg" alt="logo" class="logo" />
        </el-col>
        <el-col :span="16">
          <!-- 菜单 -->
          <el-menu :default-active="activeMenu" @select="handleMenuSelect"
            mode="horizontal"
            router
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item index="/user">个人中心</el-menu-item>
            <el-menu-item index="/doctors">查询医生</el-menu-item>
            <el-menu-item index="/appointments">预约挂号</el-menu-item>
            <el-menu-item index="/records">查看预约信息</el-menu-item>
            <el-menu-item index="/online">在线问诊</el-menu-item>
            <el-menu-item index="/knowledge">康复系统</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="4">
          <!-- 用户信息 -->
          <div class="user-info">
          <!-- 使用el-dropdown组件 -->
          <el-dropdown trigger="click" @command="handleCommand">
          <!-- 头像作为触发元素 -->
          <el-avatar :src="avatar" size="large"></el-avatar>
          <!-- 下拉菜单 -->
          <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="edit">修改信息</el-dropdown-item>
          </el-dropdown-menu>
          </el-dropdown>
          <span class="username">{{ username }}</span>
            <el-button type="text" @click="logout">退出</el-button>
          </div>
        </el-col>
      </el-row>
    </el-header>

    <!-- 主内容 -->
    <el-main class="main">
      <!-- 路由出口 -->
      <router-view></router-view>
    </el-main>

    <!-- 底部 -->
    <el-footer class="footer">©2023 医院预约挂号系统</el-footer>
  </div>
</template>

<script>
export default {
  name: "Main",
  data() {
    return {
      avatar: require("../assets/user_img/avatar.jpg"),
      username: "蔡旭琨", // 模拟用户姓名
    };
  },
  methods: {
    logout() {
      // 模拟退出登录
      this.$message.success("退出成功");
      this.$router.push("/login");
    },
    handleCommand(command) {
    if (command === "edit") {
      this.editProfile();
      }
    },
    handleMenuSelect(index) {
      if (index === '/online') {
        window.open('http://192.168.43.89:8080', '_blank');
      }
      if (index === '/knowledge') {
        window.open('http://192.168.43.109:8080/home', '_blank');
      }
      if (index === '/usr') {
        window.open('http://192.168.43.109:8080/home', '_blank');
      }

    }
  },
};
</script>

<style scoped>
.container {
  height: 100vh;
}
.header {
  height: 60px;
}
.logo {
  width: 120px;
}
.user-info {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  justify-content: flex-end;
}
.main {
  padding: 20px;
}
.footer {
  height: 40px;
  line-height: 40px;
  text-align: center;
}
</style>
