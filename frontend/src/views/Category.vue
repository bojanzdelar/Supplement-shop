<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <Product
          v-for="product in products"
          :key="product.id"
          :id="product.id"
          :name="product.name"
          :description="product.description"
          :thumbnail="product.thumbnail"
          @details="viewDetails"
          class="col-sm-6 col-md-4 col-lg-3 col-xl-2"
        />
      </div>
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
  methods: {
    getProducts() {
      this.axios.get("/product").then((response) => {
        this.products = response.data.filter((product) => {
          const category = this.$route.params["id"];
          return category != 0 ? product.category_id == category : true;
        });
      });
    },
    viewDetails(id) {
      this.$router.push(`/products/${id}`);
    },
  },
  created() {
    this.getProducts();
  },
  updated() {
    this.getProducts();
  },
};
</script>
