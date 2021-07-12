<template>
  <div class="container mt-5">
    <div v-if="isEmpty">
      <p>You don't have any items in your cart.</p>
      <router-link to="/" class="btn btn-success">
        Continue shopping<i class="bi bi-chevron-right"></i>
      </router-link>
    </div>
    <div v-else>
      <h3 class="text-center mb-4">Your cart</h3>
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
                v-for="item in cart"
                :key="item.id"
                :id="item.id"
                :product-id="item.product_id"
                :name="item.name"
                :quantity="item.quantity"
                :price="item.price"
                :thumbnail="item.thumbnail"
                @changed="changeItemQuantity"
                @remove="remove(item.product_id)"
                class="mb-1"
              />
            </tbody>
          </table>
          <div class="d-flex justify-content-between my-4">
            <router-link to="/" tag="button" class="btn">
              <i class="bi bi-arrow-left-circle"></i> Continue shopping
            </router-link>
            <button @click="update" class="btn">
              <i class="bi bi-arrow-repeat"></i> Update
            </button>
          </div>
          <p>
            We processes all orders in USD. While the content of your cart is
            currently displayed in USD, the checkout will use USD at the most
            current exchange rate.
          </p>
        </div>
        <div class="col-lg-4 bg-light p-4 h-100">
          <div
            class="d-flex justify-content-between fw-bold text-uppercase mb-3"
          >
            <span>Subtotal</span>
            <span>${{ subtotal }}</span>
          </div>
          <p>Shipping & taxes calculated at checkout</p>
          <div class="d-grid">
            <router-link
              to="/checkout"
              tag="button"
              class="btn btn-success text-uppercase text-dark"
              aria-label="checkout"
            >
              Proceed to checkout
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import CartRow from "@/components/CartRow.vue";

const { mapState, mapGetters, mapMutations, mapActions } =
  createNamespacedHelpers("cart");

export default {
  name: "Cart",
  components: {
    CartRow,
  },
  computed: {
    ...mapState(["cart"]),
    ...mapGetters(["isEmpty", "subtotal"]),
  },
  methods: {
    ...mapMutations(["changeItemQuantity"]),
    ...mapActions(["update", "remove"]),
  },
};
</script>
