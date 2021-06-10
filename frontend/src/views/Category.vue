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
          @details="view_details"
          class="col-lg-2"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
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
    get_products() {
      axios.get("http://localhost:5000/api/product").then((response) => {
        this.products = response.data.filter((product) => {
          const category = this.$route.params["id"];
          // if category equals to 0 display all products
          return category != 0
            ? product.category_id == this.$route.params["id"]
            : true;
        });
      });
    },
    view_details(id) {
      this.$router.push(`/products/${id}`);
    },
  },
  created() {
    this.get_products();
  },
  updated() {
    this.get_products();
  },
};
</script>
