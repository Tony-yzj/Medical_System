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
        activeIndex: "digest",
        isCollapse: false,
        menu: [
          {
            index: "internal medicine",
            label: "内科",
            children: [
              { index: "digest", label: "消化内科" },
              { index: "neurology", label: "神经内科" },
              { index: "respiratory", label: "呼吸内科" },
              { index: "cardio", label: "心血管内科" },
            ],
          },
          {
            index: "surgery",
            label: "外科",
            children: [
              { index: "general", label: "普外科" },
              { index: "neurosurgery", label: "神经外科" },
              { index: "orthopedics", label: "骨科" },
              { index: "urology", label: "泌尿外科" },
            ],
          },
          {
            index: "pediatrics",
            label: "儿科",
            children: [
              { index: "pediatric-internal", label: "小儿内科" },
              { index: "pediatric-surgery", label: "小儿外科" },
              { index: "pediatric-neuro", label: "小儿神经科" },
              { index: "pediatric-cardio", label: "小儿心脏科" },
            ],
          },
        ],
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        this.$router.push({ path: '/appointments/' + key});
      },
    },
  };
  </script>
  
  <style scoped>
  .sidebar {
    width: 200px;
  }
  </style>
  