<template>
  <div class="card">
    <a @click="viewDetails" href="#">
      <img :src="thumbnail" class="card-img-top" :alt="name" />
    </a>
    <div class="card-body">
      <a @click="viewDetails" href="#" class="text-body text-decoration-none">
        <h5 class="card-title">{{ name }}</h5>
      </a>
      <p class="card-text">${{ price }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Product",
  props: {
    id: String,
    name: String,
    description: String,
    price: Number,
    thumbnail: String,
  },
  methods: {
    viewDetails() {
      this.$router.push(`/products/${this.id}`);
    },
  },
};
</script>
