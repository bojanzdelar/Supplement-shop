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
    async getOrderPrice(id) {
      const response = await axios.get(`/orders/${id}/price`);
      return response.data;
    },

    async getOrders() {
      const response = await axios.get("/orders/user");
      const data = response.data;

      for (let order of data) {
        const { shipping_price, total_product_price } =
          await this.getOrderPrice(order.id);

        order.shipping_price = shipping_price;
        order.total_product_price = total_product_price;
      }

      this.orders = data;
    },
  },
  created() {
    this.getOrders();
  },
};
</script>