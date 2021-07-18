<template>
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th v-if="displayTotal">Total</th>
          <th>Deleted</th>
          <th v-if="actionsAvailable">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>
            <router-link
              :to="{ name: 'ProductDetails', params: { id: product.id } }"
              class="text-decoration-none"
            >
              {{ product.name }}
            </router-link>
          </td>
          <td>${{ product.price }}</td>
          <td>{{ product.quantity }}</td>
          <td v-if="displayTotal">${{ product.price * product.quantity }}</td>
          <td>
            <span v-if="product.deleted">Yes</span>
            <span v-else>No</span>
          </td>
          <td v-if="actionsAvailable">
            <button
              @click="edit(product.id)"
              class="btn text-dark text-uppercase me-2"
              data-bs-toggle="modal"
              data-bs-target="#modal"
            >
              <i class="bi bi-pencil"></i>
            </button>
            <button
              @click="remove(product.id)"
              class="btn text-uppercase"
              data-bs-toggle="modal"
              data-bs-target="#deleteModal"
            >
              <i class="bi bi-x-lg"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ProductsTable",
  props: {
    products: Array,
    displayTotal: Boolean,
    actionsAvailable: Boolean,
  },
  emits: {
    edit: null,
    remove: null,
  },
  methods: {
    edit(id) {
      this.$emit("edit", id);
    },

    remove(id) {
      this.$emit("remove", id);
    },
  },
};
</script>
