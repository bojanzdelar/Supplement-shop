<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <router-link to="/" class="navbar-brand">Musclepharm</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
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
                  <router-link to="/category/0" class="dropdown-item"
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
            <li class="nav-item">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/contact" class="nav-link">Contact</router-link>
            </li>
          </ul>
          <ul class="navbar-nav mb-2 mb-lg-0">
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
                <li v-if="!logged">
                  <div class="d-grid">
                    <router-link to="/login" class="btn btn-success">
                      Login
                    </router-link>
                  </div>
                </li>
                <li v-if="!logged">
                  <router-link to="/register" class="dropdown-item">
                    New user? <u>Register now</u>
                  </router-link>
                </li>
                <li v-if="logged" @click="logout" class="dropdown-item">
                  Logout
                </li>
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
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      categories: [],
      logged: false,
    };
  },
  methods: {
    getCategories() {
      this.axios.get("/category/").then((response) => {
        this.categories = response.data;
      });
    },
    logout() {
      this.emitter.emit("loggedOut");
      localStorage.removeItem("token");
    },
  },
  created() {
    this.getCategories();

    this.emitter.on("loggedIn", () => {
      this.logged = true;
    });

    this.emitter.on("loggedOut", () => {
      this.logged = false;
    });
  },
};
</script>
