<template>
  <div class="container my-5">
    <div class="row">
      <div class="col-lg-6 me-lg-5">
        <router-link to="/" class="text-dark text-decoration-none">
          <h1 class="mb-3">Musclepharm</h1>
        </router-link>
        <CheckoutNav class="mb-4" />
        <router-view />
      </div>
      <div class="col-lg-5 bg-light p-5">
        <CheckoutCart />
      </div>
    </div>
  </div>
</template>

<script>
import CheckoutNav from "@/components/CheckoutNav.vue";
import CheckoutCart from "@/components/CheckoutCart.vue";

export default {
  name: "Checkout",
  components: {
    CheckoutNav,
    CheckoutCart,
  },
};
</script>
