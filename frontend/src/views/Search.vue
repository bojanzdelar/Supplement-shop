<template>
  <div class="container mt-5">
    <div class="row">
      <Product
        v-for="product in products"
        :key="product.id"
        :id="product.id"
        :name="product.name"
        :description="product.description"
        :price="product.price"
        :thumbnail="product.thumbnail"
        @details="viewDetails"
        class="col-sm-6 col-md-4 col-lg-3 col-xl-2"
      />
    </div>
  </div>
</template>

<script>
import axios from "@/service/index.js";
import Product from "@/components/Product.vue";

export default {
  name: "Search",
  components: {
    Product,
  },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    async getProducts() {
      const response = await axios.get(
        `/product/search/${this.$route.query.q}`
      );
      this.products = response.data;
    },
    viewDetails(id) {
      this.$router.push(`/products/${id}`);
    },
  },
  watch: {
    $route() {
      this.getProducts();
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
