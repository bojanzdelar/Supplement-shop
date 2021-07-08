<template>
  <div>
    <CheckoutCartItem
      v-for="item in cart"
      :key="item.id"
      :name="item.name"
      :quantity="item.quantity"
      :price="item.price"
      :thumbnail="item.thumbnail"
      class="mb-1"
    />
    <hr />
    <div class="d-flex justify-content-between">
      <span>Subtotal: </span>
      <span>${{ subtotal }}</span>
    </div>
    <div class="d-flex justify-content-between">
      <span>Shipping: </span>
      <span v-if="shippingMethod">${{ shippingMethod.price }}</span>
      <span v-else>Calculated at next step</span>
    </div>
    <hr />
    <div class="d-flex justify-content-between">
      <span>Total: </span>
      <span v-if="shippingMethod">
        USD ${{ (subtotal + shippingMethod.price).toFixed(2) }}
      </span>
      <span v-else> USD ${{ subtotal }} </span>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import CheckoutCartItem from "@/components/CheckoutCartItem.vue";

export default {
  name: "CheckoutCart",
  components: {
    CheckoutCartItem,
  },
  computed: {
    ...mapState("cart", ["cart"]),
    ...mapState("checkout", ["shippingMethod"]),
    ...mapGetters("cart", ["subtotal"]),
  },
};
</script>
