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
        class="col-6 col-md-4 col-lg-3 col-xl-2"
      />
    </div>
  </div>
</template>

<script>
import axios from "@/service/index.js";
import Product from "@/components/Product.vue";

export default {
  name: "Category",
  components: {
    Product,
  },
  data() {
    return {
      products: {},
    };
  },
  watch: {
    $route() {
      if (this.$route.name == this.$options.name) {
        this.getProducts();
      }
    },
  },
  methods: {
    async getProducts() {
      const id = this.$route.params["id"];
      const path = id == "all" ? "/product" : `/category/${id}/products`;

      this.products = await axios.get(path);
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
