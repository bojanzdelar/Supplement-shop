<template>
  <div>
    <h1>Orders</h1>
    <hr />
    <OrdersTable :orders="orders" @send="sendOrder" @deliver="deliverOrder" />
  </div>
</template>

<script>
import OrdersTable from "@/components/OrdersTable.vue";
import axios from "@/service/index.js";

export default {
  name: "DashboardOrders",
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

    async sendOrder(id) {
      const response = await axios.patch(`/orders/${id}/sent`);
      const data = response.data;
      this.orders[this.orders.findIndex((order) => order.id === id)].sent =
        data.sent;
    },

    async deliverOrder(id) {
      const response = await axios.patch(`/orders/${id}/delivered`);
      const data = response.data;
      this.orders[this.orders.findIndex((order) => order.id === id)].delivered =
        data.delivered;
    },
  },
  created() {
    this.getOrders();
  },
};
</script>
