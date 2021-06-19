<template>
  <div class="container">
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
            <button @click="addToCart" class="btn btn-success">
              Add to cart
            </button>
          </div>
        </div>
      </div>
    </div>
    <CommentSection />
  </div>
</template>

<script>
import CommentSection from "@/components/CommentSection.vue";

export default {
  name: "ProductDetails",
  components: {
    CommentSection,
  },
  data() {
    return {
      product: {},
      cart: {
        product_id: this.$route.params["id"],
        quantity: 1,
      },
      logged: false,
    };
  },
  methods: {
    getProduct() {
      this.axios
        .get(`/product/${this.$route.params["id"]}`)
        .then((response) => {
          this.product = response.data;
        });
    },
    addToCart() {
      if (!this.token) {
        window.alert("You must be signed in to add products to cart!");
        return;
      }
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
      this.axios.post("/cart", this.cart);
      this.emitter.emit("addedToCart");
    },
  },
  created() {
    this.getProduct();

    this.emitter.on("loggedIn", () => {
      this.logged = true;
    });

    this.emitter.on("loggedOut", () => {
      this.logged = false;
    });
  },
};
</script>
