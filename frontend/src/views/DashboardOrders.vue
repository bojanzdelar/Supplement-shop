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
    async getOrderPrice(id) {
      const response = await axios.get(`/orders/${id}/price`);
      return response.data;
    },

    async getOrders() {
      const response = await axios.get("/orders");
      const data = response.data;

      for (let order of data) {
        const { shipping_price, total_product_price } =
          await this.getOrderPrice(order.id);

        order.shipping_price = shipping_price;
        order.total_product_price = total_product_price;
      }

      this.orders = data;
    },

    async sendOrder(id) {
      const response = await axios.patch(`/orders/${id}/send`);
      const data = response.data;
      this.orders[this.orders.findIndex((order) => order.id === id)].sent =
        data.sent;
    },

    async deliverOrder(id) {
      const response = await axios.patch(`/orders/${id}/deliver`);
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
