<template>
  <div class="home">
    <Carousel />
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
      products: {}
    }
  },
  methods: { 
    get_products() {
      axios.get("http://localhost:5000/api/product")
        .then((response) => {
          this.products = response.data;
        });
    },
    view_details(id) { 
      this.$router.push(`/products/${id}`);
    }
  },
  created() {
    this.get_products();
  }
};
</script>
