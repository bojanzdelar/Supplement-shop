<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-7">
        <h1>Musclepharm</h1>
        <CheckoutNav />
        <router-view />
      </div>
      <div class="col-lg-5">
        <CheckoutOrder />
      </div>
    </div>
  </div>
</template>

<script>
import CheckoutNav from "@/components/CheckoutNav.vue";
import CheckoutOrder from "@/components/CheckoutOrder.vue";

export default {
  name: "Checkout",
  components: {
    CheckoutNav,
    CheckoutOrder,
  },
};
</script>
