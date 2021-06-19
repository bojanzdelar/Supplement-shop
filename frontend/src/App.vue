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
    if (localStorage.getItem("token")) {
      this.emitter.emit("loggedIn");
    } else {
      console.log("out");
      this.emitter.emit("loggedOut");
    }
  },
};
</script>
