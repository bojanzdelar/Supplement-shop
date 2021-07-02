<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item">
        <router-link to="/cart">Cart</router-link>
      </li>
      <li class="breadcrumb-item">
        <span v-if="page !== 'information'">
          <router-link to="/checkout/information">Information</router-link>
        </span>
        <span v-else>Information</span>
      </li>
      <li class="breadcrumb-item">
        <span v-if="page !== 'shipping'">
          <router-link to="/checkout/shipping">Shipping</router-link>
        </span>
        <span v-else>Shipping</span>
      </li>
      <li class="breadcrumb-item">
        <span v-if="page !== 'payment'">
          <router-link to="/checkout/payment">Payment</router-link>
        </span>
        <span v-else>Payment</span>
      </li>
    </ol>
  </nav>
</template>

<script>
export default {
  name: "CheckoutNav",
  computed: {
    page() {
      const path = this.$route.path.split("/");
      return path[path.length - 1];
    },
  },
};
</script>
