<template>
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>${{ product.price }}</td>
          <td>{{ product.quantity }}</td>
          <td>${{ product.price * product.quantity }}</td>
          <td>
            <button
              @click="edit(address.id)"
              class="btn text-dark text-uppercase me-2"
              data-bs-toggle="modal"
              data-bs-target="#modal"
            >
              <i class="bi bi-pencil"></i>
            </button>
            <button
              @click="remove(address.id)"
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
