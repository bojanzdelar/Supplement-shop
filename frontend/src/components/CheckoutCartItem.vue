<template>
  <div class="row align-items-center">
    <div class="col-2">
      <span
        class="
          position-relative
          top-0
          translate-middle
          p-2
          bg-secondary
          text-light
          rounded-circle
        "
      >
        {{ quantity }}
      </span>
      <img :src="thumbnail" class="img-fluid" :alt="name" />
    </div>
    <div class="col-8">
      <h6 class="fw-bold">{{ name }}</h6>
    </div>
    <div class="col-2">
      <p class="fw-bold">${{ price }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CheckoutCartItem",
  props: {
    name: String,
    quantity: Number,
    price: Number,
    thumbnail: String,
  },
};
</script>
