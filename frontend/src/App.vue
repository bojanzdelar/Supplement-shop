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

    this.emitter.on("loggedIn", () => {
      const cart = JSON.parse(localStorage.getItem("cart"));
      if (!cart) return;

      this.axios.delete("/cart/user");
      cart.forEach((item) => {
        this.axios.post("/cart", item);
      });
      localStorage.removeItem("cart");
    });
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
