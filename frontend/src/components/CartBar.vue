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
      <CartItem
        v-for="item in cart"
        :key="item.id"
        :id="item.id"
        :product-id="item.product_id"
        :name="item.name"
        :quantity="item.quantity"
        :price="item.price"
        :thumbnail="item.thumbnail"
        @remove="removeItem"
        class="mb-1"
      />
      <div class="d-grid gap-2">
        <p>Subtotal: ${{ subtotal }}</p>
        <button class="btn btn-success text-uppercase">
          Proceed to checkout
        </button>
        <button class="btn btn-success text-uppercase">View cart</button>
      </div>
    </div>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem.vue";

export default {
  name: "CartBar",
  components: {
    CartItem,
  },
  data() {
    return {
      cart: [],
    };
  },
  computed: {
    subtotal() {
      if (this.cart.length == 0) return;

      return this.cart
        .reduce((sum, curr) => {
          return sum + curr.price * curr.quantity;
        }, 0)
        .toFixed(2);
    },
  },
  methods: {
    getCart() {
      this.axios.get("/cart/user").then((response) => {
        this.cart = response.data;
      });
    },
    removeItem(id) {
      this.axios.delete(`/cart/${id}`).then(() => {
        for (let i = 0; i < this.cart.length; i++) {
          if (this.cart[i].id == id) {
            this.cart.splice(i, 1);
            break;
          }
        }
      });
    },
  },
  created() {
    this.getCart();

    this.emitter.on("loggedIn", () => {
      this.getCart();
    });

    this.emitter.on("loggedOut", () => {
      this.cart = [];
    });

    this.emitter.on("addedToCart", () => {
      this.getCart();
    });
  },
};
</script>
