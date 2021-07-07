<template>
  <div>
    <Navbar />
    <SearchBar />
    <CartBar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import Navbar from "@/components/Navbar.vue";
import SearchBar from "@/components/SearchBar.vue";
import CartBar from "@/components/CartBar.vue";
import Footer from "@/components/Footer.vue";

const { mapActions } = createNamespacedHelpers("cart");

export default {
  name: "Buyer",
  components: {
    Navbar,
    SearchBar,
    CartBar,
    Footer,
  },
  methods: {
    ...mapActions(["get"]),
  },
  created() {
    this.get();
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
