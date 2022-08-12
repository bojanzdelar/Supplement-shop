<template>
  <div class="d-flex flex-column min-vh-100">
    <Navbar />
    <SearchBar />
    <CartBar v-if="!isAdmin" />
    <router-view />
    <div class="flex-grow-1"></div>
    <Footer />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Navbar from "@/components/Navbar.vue";
import SearchBar from "@/components/SearchBar.vue";
import CartBar from "@/components/CartBar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Buyer",
  components: {
    Navbar,
    SearchBar,
    CartBar,
    Footer,
  },
  computed: {
    ...mapState("auth", ["isAdmin"]),
  },
  methods: {
    ...mapActions("cart", ["get"]),
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

.bg-light {
  background-color: #f5f5f5 !important;
}
</style>
