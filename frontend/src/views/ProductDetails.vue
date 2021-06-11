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
        <button class="btn btn-success">Add to cart</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductDetails",
  data() {
    return {
      product: {},
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
  },
  created() {
    this.getProduct();
  },
};
</script>
