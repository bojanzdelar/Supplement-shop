<template>
  <div>
    <DashboardNavbar />
    <div class="container-fluid">
      <div class="row">
        <DashboardSidebar />
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 mt-4">
          <router-view />
        </main>
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
