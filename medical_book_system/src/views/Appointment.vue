<template>
    <div class="appointment">
      <side-bar></side-bar>
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  import SideBar from "./SideBar.vue";
  export default {
    components: {
      SideBar,
    },
  };
  </script>
  
  <style scoped>
  .appointment {
    display: flex;
  }
  </style>
  