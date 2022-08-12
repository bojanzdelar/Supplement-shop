<template>
  <div>
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Shipping method</th>
            <th>Shipping price</th>
            <th>Payment method</th>
            <th>Total product price</th>
            <th>Total price</th>
            <th>Sent</th>
            <th>Delivered</th>
            <th v-if="isAdmin">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr @click="select(order)" v-for="order in orders" :key="order.id">
            <td>{{ order.id }}</td>
            <td>{{ order.shipping_method.name }}</td>
            <td>${{ order.shipping_method.price.toFixed(2) }}</td>
            <td>{{ order.payment_method.name }}</td>
            <td>${{ order.total_product_price.toFixed(2) }}</td>
            <td>
              ${{
                (
                  order.shipping_method.price + order.total_product_price
                ).toFixed(2)
              }}
            </td>
            <td>
              <span v-if="order.sent">Yes</span>
              <span v-else>No</span>
            </td>
            <td>
              <span v-if="order.delivered">Yes</span>
              <span v-else>No</span>
            </td>
            <td v-if="isAdmin">
              <button @click="send(order.id)" class="btn btn-secondary me-2">
                <span v-if="order.sent">Mark as unsent</span>
                <span v-else>Mark as sent</span>
              </button>
              <button @click="deliver(order.id)" class="btn btn-secondary">
                <span v-if="order.delivered">Mark as undelivered</span>
                <span v-else>Mark as delivered</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="isOrderSelected" class="border p-3">
      <div class="mb-3">
        <h5>Shipping address</h5>
        <AddressesTable
          :addresses="[selectedOrder.shipping_address]"
          :actionsAvailable="false"
        />
      </div>
      <div class="mb-3">
        <h5>Billing address</h5>
        <AddressesTable
          :addresses="[selectedOrder.billing_address]"
          :actionsAvailable="false"
        />
      </div>
      <div>
        <h5>Products in order</h5>
        <ProductsTable
          :products="selectedOrder.products"
          :displayTotal="true"
          :actionsAvailable="false"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import AddressesTable from "@/components/AddressesTable.vue";
import ProductsTable from "@/components/ProductsTable.vue";
import axios from "@/service/index.js";

const { mapState } = createNamespacedHelpers("auth");

export default {
  name: "OrdersTable",
  components: {
    AddressesTable,
    ProductsTable,
  },
  props: {
    orders: Array,
  },
  emits: {
    send: null,
    deliver: null,
  },
  data() {
    return {
      selectedOrder: {},
    };
  },
  computed: {
    isOrderSelected() {
      return Object.entries(this.selectedOrder).length !== 0;
    },

    ...mapState(["isAdmin"]),
  },
  methods: {
    async getProducts(orderId) {
      const response = await axios.get(`/products/order/${orderId}`);
      return response.data;
    },

    async select(order) {
      this.selectedOrder.products = await this.getProducts(order.id);
    },

    send(orderId) {
      this.$emit("send", orderId);
    },

    deliver(orderId) {
      this.$emit("deliver", orderId);
    },
  },
};
</script>
