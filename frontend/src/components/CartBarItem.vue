<template>
  <div class="card">
    <div class="row">
      <div class="col-3">
        <a @click="viewDetails" href="#" data-bs-dismiss="offcanvas">
          <img :src="thumbnail" class="img-fluid" :alt="name" />
        </a>
      </div>
      <div class="col-7">
        <div class="card-body">
          <a
            @click="viewDetails"
            href="#"
            class="text-body text-decoration-none"
            data-bs-dismiss="offcanvas"
          >
            <h6 class="card-title">{{ name }}</h6>
          </a>
          <p class="card-text">${{ price }} * {{ quantity }}</p>
        </div>
      </div>
      <div class="col-1">
        <button
          @click="$emit('remove', id)"
          type="button"
          class="btn-close text-reset"
          aria-label="Remove"
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CartBarItem",
  props: {
    id: Number,
    productId: String,
    name: String,
    quantity: Number,
    price: Number,
    thumbnail: String,
  },
  emits: {
    remove: null,
  },
  methods: {
    viewDetails() {
      this.$router.push(`/products/${this.productId}`);
    },
  },
};
</script>
