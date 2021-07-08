<template>
  <div>
    <h1>Products</h1>
    <hr />
    <button
      @click="create"
      class="btn px-3 py-2"
      data-bs-toggle="modal"
      data-bs-target="#modal"
    >
      <i class="bi bi-plus-lg"></i>
    </button>
    <ProductsModal
      :product="modal.product"
      :categories="categories"
      :heading="modal.heading"
      :button="modal.button"
      @submitted="modal.handler"
    />
    <ProductsTable :products="products" @edit="edit" @remove="remove" />
    <DeleteModal :entity="'product'" @confirmed="deleteProduct(id)" />
  </div>
</template>

<script>
import ProductsModal from "@/components/ProductsModal.vue";
import ProductsTable from "@/components/ProductsTable.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import axios from "@/service/index.js";

export default {
  name: "DashboardProducts",
  components: {
    ProductsModal,
    ProductsTable,
    DeleteModal,
  },
  data() {
    return {
      products: [],
      categories: [],
      modal: {},
      id: null,
    };
  },
  methods: {
    async getProducts() {
      const response = await axios.get("/product");
      this.products = response.data;
    },

    async getCategories() {
      const response = await axios.get("/category");
      this.categories = response.data;
    },

    async createProduct(newProduct, selectedCategories) {
      const response = await axios.post("/product", newProduct);
      newProduct.id = response.data.id;
      await this.setProductCategories(newProduct.id, selectedCategories);
      this.products.push(newProduct);
    },

    async updateProduct(newProduct, selectedCategories) {
      const response = await axios.put(`/product/${newProduct.id}`, newProduct);
      await this.setProductCategories(newProduct.id, selectedCategories);
      this.products[
        this.products.findIndex((product) => product.id === newProduct.id)
      ] = response.data;
    },

    async deleteProduct(id) {
      await axios.delete(`/product/${id}`);
      this.products.splice(
        this.products.findIndex((product) => product.id === id),
        1
      );
    },

    async setProductCategories(product_id, selectedCategories) {
      console.log(product_id, selectedCategories);

      await axios.delete(`/product-in-category/${product_id}`);

      for (let category of selectedCategories) {
        await axios.post("/product-in-category", {
          product_id: product_id,
          category_id: category,
        });
      }
    },

    create() {
      this.modal = {
        product: {},
        heading: "Add a new product",
        button: "Add product",
        handler: this.createProduct,
      };
    },

    edit(id) {
      this.modal = {
        product: this.products.find((product) => product.id === id),
        heading: "Edit product",
        button: "Update product",
        handler: this.updateProduct,
      };
    },

    remove(id) {
      this.id = id;
    },
  },
  created() {
    this.getProducts();
    this.getCategories();
  },
};
</script>