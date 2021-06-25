<template>
  <div>
    <Navbar />
    <SearchBar />
    <CartBar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SearchBar from "@/components/SearchBar.vue";
import CartBar from "@/components/CartBar.vue";

export default {
  name: "App",
  components: {
    Navbar,
    SearchBar,
    CartBar,
  },
  mounted() {
    if (localStorage.getItem("access_token")) {
      this.emitter.emit("loggedIn");
    } else {
      this.emitter.emit("loggedOut");
    }
  },
};
</script>

<style>
.btn {
  border: 0 !important;
}

.btn-success {
  background-color: #87d700 !important;
}
</style>
