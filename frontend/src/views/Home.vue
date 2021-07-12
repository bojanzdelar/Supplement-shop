<template>
  <div>
    <Carousel />
    <div class="container mt-5">
      <h3 class="text-center text-uppercase">Popular products</h3>
      <div class="row my-5">
        <Product
          v-for="product in products"
          :key="product.id"
          :id="product.id"
          :name="product.name"
          :description="product.description"
          :price="product.price"
          :thumbnail="product.thumbnail"
          class="col-6 col-md-4 col-lg-3 col-xl-2"
        />
      </div>
      <div class="text-center">
        <router-link
          to="/category/all"
          tag="button"
          class="btn btn-success text-uppercase text-dark"
        >
          View all products
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/service/index.js";
import Carousel from "@/components/Carousel.vue";
import Product from "@/components/Product.vue";

export default {
  name: "Home",
  components: {
    Carousel,
    Product,
  },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    async getProducts() {
      const response = await axios.get("/product/popular/6");
      this.products = response.data;
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
