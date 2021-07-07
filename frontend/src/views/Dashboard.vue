<template>
  <div>
    <DashboardNavbar />
    <div class="container-fluid">
      <div class="row">
        <DashboardSidebar />
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import DashboardNavbar from "@/components/DashboardNavbar.vue";
import DashboardSidebar from "@/components/DashboardSidebar.vue";

export default {
  name: "Dashboard",
  components: {
    DashboardSidebar,
    DashboardNavbar,
  },
};
</script>
