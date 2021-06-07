<template>
  <div class="home">
    <Carousel />
    <div class="container">
      <div class="row">
        <Product v-for="index in 6" :key="index" class="col-lg-3" />
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
};
</script>
