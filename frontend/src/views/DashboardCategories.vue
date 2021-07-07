<template>
  <div>
    <h1>Categories</h1>
    <hr />
    <button
      @click="create"
      class="btn px-3 py-2"
      data-bs-toggle="modal"
      data-bs-target="#modal"
    >
      <i class="bi bi-plus-lg"></i>
    </button>
    <CategoriesModal
      :category="modal.category"
      :heading="modal.heading"
      :button="modal.button"
      @submitted="modal.handler"
    />
    <CategoriesTable :categories="categories" @edit="edit" @remove="remove" />
    <DeleteModal :entity="'category'" @confirmed="deleteCategory(id)" />
  </div>
</template>

<script>
import CategoriesModal from "@/components/CategoriesModal.vue";
import CategoriesTable from "@/components/CategoriesTable.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import axios from "@/service/index.js";

export default {
  name: "DashboardCategories",
  components: {
    CategoriesModal,
    CategoriesTable,
    DeleteModal,
  },
  data() {
    return {
      categories: [],
      modal: {},
      id: null,
    };
  },
  methods: {
    async getCategories() {
      const response = await axios.get("/category");
      this.categories = response.data;
    },

    async createCategory(newCategory) {
      const response = await axios.post("/category", newCategory);
      newCategory.id = response.data.id;
      this.categories.push(newCategory);
    },

    async updateCategory(newCategory) {
      const response = await axios.put(
        `/category/${newCategory.id}`,
        newCategory
      );
      this.categories[
        this.categories.findIndex((category) => category.id === newCategory.id)
      ] = response.data;
    },

    async deleteCategory(id) {
      await axios.delete(`/category/${id}`);
      this.categories.splice(
        this.categories.findIndex((category) => category.id === id),
        1
      );
    },

    create() {
      this.modal = {
        category: {},
        heading: "Add a new category",
        button: "Add category",
        handler: this.createCategory,
      };
    },

    edit(id) {
      this.modal = {
        category: this.categories.find((category) => category.id === id),
        heading: "Edit category",
        button: "Update category",
        handler: this.updateCategory,
      };
    },

    remove(id) {
      this.id = id;
    },
  },
  created() {
    this.getCategories();
  },
};
</script>
