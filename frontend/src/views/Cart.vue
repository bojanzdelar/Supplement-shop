<template>
  <div class="container mt-5">
    <div v-if="isEmpty">
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
                v-for="item in cart"
                :key="item.id"
                :id="item.id"
                :product-id="item.product_id"
                :name="item.name"
                :quantity="item.quantity"
                :price="item.price"
                :thumbnail="item.thumbnail"
                @changed="changeItemQuantity"
                @remove="remove(item.id)"
                class="mb-1"
              />
            </tbody>
          </table>
          <button @click="update" class="btn btn-success">Update</button>
        </div>
        <div class="col-lg-4 bg-light">
          <p>Subtotal ${{ subtotal }}</p>
          <p>Shipping & taxes calculated at checkout</p>
          <router-link
            to="/checkout"
            tag="button"
            class="btn btn-success text-uppercase"
            aria-label="checkout"
          >
            Proceed to checkout
          </router-link>
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
