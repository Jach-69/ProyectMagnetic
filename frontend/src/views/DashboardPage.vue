<template>
  <div class="dashboard-container">
    <SidebarMenu />
    <div class="dashboard-content">
      <router-view />
    </div>
  </div>
</template>

<script>
import SidebarMenu from '@/components/SidebarMenu.vue';

export default {
  components: {
    SidebarMenu
  }
};
</script>

<style scoped>
.dashboard-container {
  display: flex;
  height: 100vh;
}

.dashboard-content {
  flex-grow: 1;
  padding: 20px;
  background-color: #2c2c2c;
  color: white;
}
</style>
