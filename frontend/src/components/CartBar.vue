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
  data() {
    return {
      cart: [],
      logged: localStorage.getItem("access_token") !== null,
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
      if (this.logged) {
        this.axios.get("/cart/user").then((response) => {
          this.cart = response.data;
        });
      } else {
        this.cart = JSON.parse(localStorage.getItem("cart")) || [];
      }
    },

    removeItem(id) {
      if (this.logged) {
        this.axios.delete(`/cart/${id}`).then(() => {
          this.emitter.emit("removedFromCart", id);
        });
      } else {
        let updatedCart = JSON.parse(localStorage.getItem("cart"));
        updatedCart.splice(
          updatedCart.findIndex((item) => item.id == id),
          1
        );
        localStorage.setItem("cart", JSON.stringify(updatedCart));
        this.emitter.emit("removedFromCart", id);
      }
    },

    removeRemovedItem(id) {
      this.cart.splice(
        this.cart.findIndex((item) => item.id == id),
        1
      );
    },
  },
  created() {
    this.emitter.on("loggedIn", () => {
      this.logged = true;
      this.getCart();
    });

    this.emitter.on("loggedOut", () => {
      this.logged = false;
      this.getCart();
    });

    this.emitter.on("addedToCart", () => {
      this.getCart();
    });

    this.emitter.on("updatedCart", () => {
      this.getCart();
    });

    this.emitter.on("removedFromCart", (id) => {
      this.removeRemovedItem(id);
    });
  },
};
</script>
