<template>
  <div class="container mt-5">
    <div v-if="$store.getters.cartIsEmpty">
      <p>You don't have any items in your cart.</p>
      <router-link to="/" class="btn btn-success">
        Continue shopping<i class="bi bi-chevron-right"></i>
      </router-link>
    </div>
    <div v-else>
      <h5 class="text-center">Your cart</h5>
      <div class="row">
        <div class="col-lg-8">
          <table class="table align-middle">
            <thead class="bg-light text-uppercase">
              <tr>
                <th></th>
                <th colspan="2">Product</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              <CartRow
                v-for="item in $store.state.cart"
                :key="item.id"
                :id="item.id"
                :product-id="item.product_id"
                :name="item.name"
                :quantity="item.quantity"
                :price="item.price"
                :thumbnail="item.thumbnail"
                @changed="changeQuantity"
                @remove="$store.dispatch('removeFromCart', item.id)"
                class="mb-1"
              />
            </tbody>
          </table>
          <button @click="updateQuantity" class="btn btn-success">
            Update
          </button>
        </div>
        <div class="col-lg-4"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/service/index.js";
import CartRow from "@/components/CartRow.vue";

export default {
  name: "Cart",
  components: {
    CartRow,
  },
  methods: {
    changeQuantity(id, quantity) {
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].id == id) {
          this.cart[i].newQuantity = quantity;
          break;
        }
      }
    },

    updateQuantity() {
      if (this.$store.state.logged) {
        for (let item of this.cart) {
          if ("newQuantity" in item) {
            item.quantity = item.newQuantity;
            delete item.newQuantity;
            axios.put(`/cart/${item.id}`, item);
          }
        }
      } else {
        for (let item of this.cart) {
          if ("newQuantity" in item) {
            item.quantity = item.newQuantity;
            delete item.newQuantity;
          }
        }
        localStorage.setItem("cart", JSON.stringify(this.cart));
      }
    },
  },
};
</script>
