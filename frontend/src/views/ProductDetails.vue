<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-6">
        <img :src="product.image" alt="product.name" class="img-fluid" />
      </div>
      <div class="col-md-6">
        <h2>{{ product.name }}</h2>
        <p>${{ product.price }}</p>
        <p>{{ product.description }}</p>
        <div class="row">
          <div class="col-3">
            <input
              v-model.number="cart.quantity"
              type="number"
              min="1"
              :max="product.quantity"
              class="form-control"
              required
            />
          </div>
          <div class="col-9 d-grid">
            <button @click="validate" class="btn btn-success">
              Add to cart
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import axios from "@/service/index.js";

const { mapActions } = createNamespacedHelpers("cart");

export default {
  name: "ProductDetails",
  data() {
    return {
      product: {},
      cart: {
        product_id: this.$route.params["id"],
        quantity: 1,
      },
    };
  },
  watch: {
    $route() {
      if (this.$route.name == this.$options.name) {
        this.getProduct();
      }
    },
  },
  methods: {
    async getProduct() {
      const response = await axios.get(`/product/${this.$route.params["id"]}`);
      this.product = response.data;
    },

    validate() {
      if (this.cart.quantity < 1) {
        window.alert("Quantity of product must be at least 1");
        return;
      }
      if (this.cart.quantity > this.product.quantity) {
        window.alert(
          "There aren't enough products for you! Please pick a smaller quantity"
        );
        return;
      }

      this.add([this.product, this.cart.quantity]);
    },

    ...mapActions(["add"]),
  },
  created() {
    this.getProduct();
  },
};
</script>
