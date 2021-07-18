<template>
  <div class="card p-2">
    <router-link :to="{ name: 'ProductDetails', params: { id: id } }">
      <img :src="thumbnail" class="card-img-top" :alt="name" />
    </router-link>
    <div class="card-body">
      <router-link
        :to="{ name: 'ProductDetails', params: { id: id } }"
        class="text-decoration-none text-reset"
      >
        <h5 class="card-title">{{ name }}</h5>
      </router-link>
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
