<template>
  <div class="container mt-5">
    <h1 class="text-center">Your orders</h1>
    <hr />
    <router-link to="/account" class="text-secondary text-decoration-none">
      Return to account details
    </router-link>
    <OrdersTable :orders="orders" />
  </div>
</template>

<script>
import OrdersTable from "@/components/OrdersTable.vue";
import axios from "@/service/index.js";

export default {
  name: "Orders",
  components: {
    OrdersTable,
  },
  data() {
    return {
      orders: [],
    };
  },
  methods: {
    async getOrders() {
      const response = await axios.get("/orders");
      this.orders = response.data;
    },
  },
  created() {
    this.getOrders();
  },
};
</script>
