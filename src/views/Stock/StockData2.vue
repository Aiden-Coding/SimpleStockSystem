<template>
  <div class="homeward">
    <el-container class="main_container">
      <el-aside width="20%" class="{['absolute top-0 left-0 h-full']}">
        <div style="width: 100%; height: 100%">
          <div style="width: 100%; height: 95%">
            <el-table :data="tableData" style="width: 100%" height="100%">
              <el-table-column label="Date" width="75" fixed sortable>
                <template #header>
                  <span>代码</span>
                </template>
                <template #default="scope">
                  <p>{{ scope.row.date.name }}</p>
                  <p>{{ scope.row.date.code }}</p>
                </template>
              </el-table-column>

              <el-table-column prop="name" label="Name" width="60" show-overflow-tooltip sortable>
                <template #header>
                  <span>涨</span>
                </template>
              </el-table-column>
              <el-table-column
                prop="address"
                label="Address"
                width="60"
                show-overflow-tooltip
                sortable
              >
                <template #header>
                  <span>地址</span>
                </template>
              </el-table-column>
              <el-table-column prop="address" label="Address" width="60" show-overflow-tooltip>
                <template #header>
                  <span>地址</span>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div style="height: 5%">
            <el-pagination small layout="prev, pager, next" :total="50" />
          </div>
        </div>
      </el-aside>
      <el-main class="stock_main_1">
        <el-scrollbar>
          <StockData />
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import {
  ElContainer,
  ElMain,
  ElScrollbar,
  ElAside,
  ElTable,
  ElTableColumn,
  ElPagination
} from 'element-plus'
import StockData from './StockData.vue'
const tableData = [
  {
    date: { name: '美利云', code: '000815' },
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: { name: 'mei', code: '23' },
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: { name: 'mei', code: '23' },
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: { name: 'mei', code: '23' },
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  }
]
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
