<template>
    <div class="sidebar">
      <el-menu
        :default-active="activeIndex"
        :collapse="isCollapse"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @select="handleSelect"
      >
        <el-submenu v-for="(item, index) in menu" :key="index" :index="item.index">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>{{ item.label }}</span>
          </template>
          <el-menu-item
            v-for="(child, i) in item.children"
            :key="i"
            :index="child.index"
            >{{ child.label }}</el-menu-item
          >
        </el-submenu>
      </el-menu>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeIndex: "1-1",
        isCollapse: false,
        menu: [
          {
            index: "1",
            label: "内科",
            children: [
              { index: "1-1", label: "消化内科" },
              { index: "1-2", label: "神经内科" },
              { index: "1-3", label: "呼吸内科" },
              { index: "1-4", label: "心血管内科" },
            ],
          },
          {
            index: "2",
            label: "外科",
            children: [
              { index: "2-1", label: "普通外科" },
              { index: "2-2", label: "神经外科" },
              { index: "2-3", label: "骨科" },
              { index: "2-4", label: "泌尿外科" },
            ],
          },
          {
            index: "3",
            label: "儿科",
            children: [
              { index: "3-1", label: "小儿内科" },
              { index: "3-2", label: "小儿外科" },
              { index: "3-3", label: "小儿神经科" },
              { index: "3-4", label: "小儿心脏科" },
            ],
          },
        ],
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        this.$router.push({ name: key });
      },
    },
  };
  </script>
  
  <style scoped>
  .sidebar {
    width: 200px;
  }
  </style>
  