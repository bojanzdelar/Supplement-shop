<template>
  <div>
    <Carousel />
    <div class="container mt-5">
      <h3 class="text-center text-uppercase">Featured products</h3>
      <div class="row mt-5">
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
    </div>
  </div>
</template>

<script>
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
    getProducts() {
      this.axios.get("/product").then((response) => {
        this.products = response.data;
      });
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
