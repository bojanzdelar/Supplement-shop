<template>
  <header
    class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow"
  >
    <router-link to="/" class="navbar-brand col-md-3 col-lg-2 me-0 px-3">
      MusclePharm
    </router-link>
    <button
      class="navbar-toggler position-absolute d-md-none collapsed"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#sidebarMenu"
      aria-controls="sidebarMenu"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="navbar-filler w-100"></div>
    <div class="navbar-nav">
      <div class="nav-item text-nowrap">
        <router-link @click="logOut" to="/" class="nav-link px-3">
          Sign out
        </router-link>
      </div>
    </div>
  </header>
</template>

<script>
import { createNamespacedHelpers } from "vuex";

const { mapActions } = createNamespacedHelpers("auth");

export default {
  name: "DashboardNavbar",
  methods: {
    ...mapActions(["logOut"]),
  },
};
</script>

<style scoped>
.navbar-brand {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  font-size: 1rem;
  background-color: rgba(0, 0, 0, 0.25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.25);
}

.navbar .navbar-toggler {
  top: 0.25rem;
  right: 1rem;
}

.navbar .form-control {
  padding: 0.75rem 1rem;
  border-width: 0;
  border-radius: 0;
}

.navbar-filler {
  height: 3rem;
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.1);
}
</style>
