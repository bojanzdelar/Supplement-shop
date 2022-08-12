<template>
  <div
    class="offcanvas offcanvas-end"
    tabindex="-1"
    id="cartBar"
    aria-labelledby="cartBarLabel"
  >
    <div class="offcanvas-header">
      <h4 id="cartBarLabel">Your cart</h4>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <div v-if="!isEmpty">
        <CartBarItem
          v-for="item in cart"
          :key="item.product_cart.id"
          :id="item.product_cart.id"
          :name="item.product_cart.name"
          :quantity="item.quantity"
          :price="item.product_cart.price"
          :thumbnail="item.product_cart.thumbnail"
          @remove="remove(item.product_cart.id)"
          class="mb-1"
        />
        <div class="d-grid gap-2">
          <p>Subtotal: ${{ subtotal }}</p>
          <router-link
            to="/checkout"
            tag="button"
            class="btn btn-success text-uppercase"
            data-bs-dismiss="offcanvas"
            aria-label="checkout"
          >
            Proceed to checkout
          </router-link>
          <router-link
            to="/cart"
            tag="button"
            class="btn btn-success text-uppercase"
            data-bs-dismiss="offcanvas"
            aria-label="viewCart"
          >
            View cart
          </router-link>
        </div>
      </div>
      <div v-else>You don't have any items in your cart.</div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import CartBarItem from "@/components/CartBarItem.vue";

const { mapState, mapGetters, mapActions } = createNamespacedHelpers("cart");

export default {
  name: "CartBar",
  components: {
    CartBarItem,
  },
  computed: {
    ...mapState(["cart"]),
    ...mapGetters(["isEmpty", "subtotal"]),
  },
  methods: {
    ...mapActions(["remove"]),
  },
};
</script>
