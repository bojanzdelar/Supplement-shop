<template>
  <div>
    <div class="bg-light text-center p-3">
      <h3 class="text-uppercase">{{ category.name }}</h3>
    </div>
    <div class="container mt-4">
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
      category: {},
      products: [],
    };
  },
  watch: {
    $route() {
      if (
        this.$route.name == this.$options.name &&
        Object.keys(this.category).length
      ) {
        this.getCategory();
        this.getProducts();
      }
    },
  },
  methods: {
    async getCategory() {
      const id = this.$route.params["id"];
      if (id !== "all") {
        const response = await axios.get(`/categories/${id}`);
        this.category = response.data;
      } else {
        this.category.name = "Products";
      }
      document.title = `${this.product.name} - ${document.title}`;
    },

    async getProducts() {
      const id = this.$route.params["id"];
      const path = id == "all" ? "/products" : `/products/category/${id}`;
      const response = await axios.get(path);
      this.products = response.data;
    },
  },
  created() {
    this.getCategory();
    this.getProducts();
  },
};
</script>
