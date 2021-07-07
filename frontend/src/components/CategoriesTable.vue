<template>
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="category in categories" :key="category.id">
          <td>{{ category.name }}</td>
          <td>
            <button
              @click="edit(category.id)"
              class="btn text-dark text-uppercase me-2"
              data-bs-toggle="modal"
              data-bs-target="#modal"
            >
              <i class="bi bi-pencil"></i>
            </button>
            <button
              @click="remove(category.id)"
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
  name: "CategoriesTable",
  props: {
    categories: Array,
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
