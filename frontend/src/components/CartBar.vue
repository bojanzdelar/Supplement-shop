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
      <CartBarItem
        v-for="item in $store.state.cart"
        :key="item.id"
        :id="item.id"
        :product-id="item.product_id"
        :name="item.name"
        :quantity="item.quantity"
        :price="item.price"
        :thumbnail="item.thumbnail"
        @remove="$store.dispatch('removeFromCart', item.id)"
        class="mb-1"
      />
      <div class="d-grid gap-2">
        <p>Subtotal: ${{ $store.getters.cartSubtotal }}</p>
        <button class="btn btn-success text-uppercase">
          Proceed to checkout
        </button>
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
  </div>
</template>

<script>
import CartBarItem from "@/components/CartBarItem.vue";

export default {
  name: "CartBar",
  components: {
    CartBarItem,
  },
};
</script>
