<template>
  <div class="card">
    <img :src="thumbnail" class="card-img-top" :alt="name" />
    <div class="card-body">
      <h5 class="card-title">{{ name }}</h5>
      <!-- <p class="card-text">{{description}}</p> -->

      <button @click="$emit('details', id)" class="btn btn-primary">
        View details
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Product",
  emits: ["details"],
  props: {
    id: Number,
    name: String,
    description: String,
    price: Number,
    quantity: Number,
    thumbnail: String,
    category: String,
  },
};
</script>
