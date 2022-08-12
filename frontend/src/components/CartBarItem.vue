<template>
  <div class="card">
    <div class="row">
      <div class="col-3">
        <router-link
          :to="{ name: 'ProductDetails', params: { id } }"
          data-bs-dismiss="offcanvas"
        >
          <img :src="thumbnail" class="card-img-top" :alt="name" />
        </router-link>
      </div>
      <div class="col-7">
        <div class="card-body">
          <router-link
            :to="{ name: 'ProductDetails', params: { id } }"
            class="text-decoration-none text-reset"
            data-bs-dismiss="offcanvas"
          >
            <h6 class="card-title">{{ name }}</h6>
          </router-link>
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
    id: String,
    name: String,
    quantity: Number,
    price: Number,
    thumbnail: String,
  },
  emits: {
    remove: null,
  },
};
</script>
