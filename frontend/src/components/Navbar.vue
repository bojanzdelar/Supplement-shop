<template>
  <div>
    <NavbarMenu :categories="categories" />
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark pt-4 pb-3">
      <div class="container">
        <div
          class="navbar-toggler"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#navbarMenu"
          aria-controls="navbarMenu"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="bi bi-list"></i>
          <!-- <span class="navbar-toggler-icon"></span> -->
        </div>
        <router-link to="/" class="navbar-brand">
          <img
            src="../assets/images/logo/MPLogo.svg"
            width="100"
            height="50"
            class="d-inline-block align-text-top"
          />
        </router-link>
        <div class="collapse navbar-collapse" id="navbar">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle text-uppercase"
                href="#"
                id="shopDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Shop
              </a>
              <ul class="dropdown-menu" aria-labelledby="shopDropdown">
                <li>
                  <router-link to="/category/all" class="dropdown-item"
                    >All Products</router-link
                  >
                </li>
                <li v-for="category in categories" :key="category.id">
                  <router-link
                    :to="{
                      name: 'Category',
                      params: { id: category.id },
                    }"
                    class="dropdown-item"
                  >
                    {{ category.name }}
                  </router-link>
                </li>
              </ul>
            </li>
            <li class="nav-item text-uppercase">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
            <li class="nav-item text-uppercase">
              <router-link to="/contact" class="nav-link">Contact</router-link>
            </li>
          </ul>
        </div>
        <ul class="navbar-nav list-group-horizontal mb-2 mb-lg-0">
          <li class="nav-item">
            <a
              href="#"
              class="nav-link"
              data-bs-toggle="offcanvas"
              data-bs-target="#searchBar"
              aria-controls="searchBar"
            >
              <i class="bi bi-search"></i>
            </a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="settingsDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <i class="bi bi-gear"></i>
            </a>
            <ul class="dropdown-menu" aria-labelledby="settingsDropdown">
              <li v-if="logged" @click="logOut" class="dropdown-item">
                Logout
              </li>
              <div v-else>
                <li>
                  <div class="d-grid">
                    <router-link
                      to="/login"
                      tag="button"
                      class="btn btn-success"
                    >
                      Login
                    </router-link>
                  </div>
                </li>
                <li>
                  <router-link to="/register" class="dropdown-item">
                    New user? <u>Register now</u>
                  </router-link>
                </li>
              </div>
            </ul>
          </li>
          <li class="nav-item">
            <a
              href="#"
              class="nav-link"
              data-bs-toggle="offcanvas"
              data-bs-target="#cartBar"
              aria-controls="cartBar"
            >
              <i class="bi bi-cart"></i>
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import axios from "@/service/index.js";
import NavbarMenu from "@/components/NavbarMenu.vue";

const { mapState, mapActions } = createNamespacedHelpers("auth");

export default {
  name: "Navbar",
  components: {
    NavbarMenu,
  },
  data() {
    return {
      categories: [],
    };
  },
  computed: {
    ...mapState(["logged"]),
  },
  methods: {
    getCategories() {
      axios.get("/category/").then((response) => {
        this.categories = response.data;
      });
    },
    ...mapActions(["logOut"]),
  },
  created() {
    this.getCategories();
  },
};
</script>

<style scoped>
@media (max-width: 992px) {
  .navbar-nav.list-group-horizontal .nav-item {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
}
</style>
