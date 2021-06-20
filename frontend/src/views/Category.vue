<template>
  <div class="container">
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
      this.getProducts();
    },
  },
  methods: {
    getProducts() {
      const id = this.$route.params["id"];
      const path = id == "all" ? "/product" : `/category/${id}/products`;

      this.axios.get(path).then((response) => {
        this.products = response.data;
      });
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
