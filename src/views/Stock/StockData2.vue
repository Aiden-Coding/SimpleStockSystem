<template>
  <div class="homeward">
    <el-container class="main_container">
      <el-aside width="200px" class="{['absolute top-0 left-0 h-full']}" />
      <el-main class="stock_main_1">
        <el-scrollbar>
          <StockData />
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ElContainer, ElMain, ElScrollbar, ElAside } from 'element-plus'
import StockData from './StockData.vue'
</script>

<style scoped>
.homeward {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.main_container {
  height: 100%;
}
.main_container {
  height: 100%;
}
.el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.stock_main_1 {
  padding: 0;
}
</style>
