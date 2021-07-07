<template>
  <nav
    id="sidebarMenu"
    class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse"
  >
    <div class="position-sticky pt-3">
      <ul class="nav flex-column">
        <div class="nav-item">
          <router-link to="/dashboard/orders" class="nav-link">
            <i class="bi bi-cart me-1"></i>
            Orders
          </router-link>
        </div>
        <div class="nav-item">
          <router-link to="/dashboard/products" class="nav-link">
            <i class="bi bi-list-ul me-1"></i>
            Products
          </router-link>
        </div>
        <div class="nav-item">
          <router-link to="/dashboard/categories" class="nav-link">
            <i class="bi bi-cart me-1"></i>
            Categories
          </router-link>
        </div>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "DashboardSidebar",
};
</script>

<style scoped>
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.1);
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 5rem;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}
</style>
