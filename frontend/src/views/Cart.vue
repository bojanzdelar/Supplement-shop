<template>
  <div class="container mt-5">
    <div v-if="cartIsEmpty">
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
                @changed="changeQuantity"
                @remove="removeItem"
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
import CartRow from "@/components/CartRow.vue";

export default {
  name: "Cart",
  components: {
    CartRow,
  },
  data() {
    return {
      cart: [],
      logged: localStorage.getItem("access_token") !== null,
    };
  },
  computed: {
    cartIsEmpty() {
      return this.cart.length == 0;
    },
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

    changeQuantity(id, quantity) {
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].id == id) {
          this.cart[i].newQuantity = quantity;
          break;
        }
      }
    },

    updateQuantity() {
      if (this.logged) {
        for (let item of this.cart) {
          if ("newQuantity" in item) {
            item.quantity = item.newQuantity;
            delete item.newQuantity;
            this.axios.put(`/cart/${item.id}`, item);
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
      this.emitter.emit("updatedCart");
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
    this.getCart();

    this.emitter.on("loggedOut", () => {
      this.logged = false;
      this.getCart();
    });

    this.emitter.on("removedFromCart", (id) => {
      this.removeRemovedItem(id);
    });
  },
};
</script>
