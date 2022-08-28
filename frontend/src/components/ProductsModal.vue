<template>
  <div class="modal" id="modal" tabindex="-1">
    <div class="modal-dialog modal-dialog-scrollable modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ heading }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form @submit.prevent="submit" class="border p-3">
          <div class="modal-body">
            <div class="row g-4">
              <div>
                <label for="name">Name</label>
                <input
                  v-model="newProduct.name"
                  type="text"
                  id="name"
                  class="form-control"
                  aria-describedby="name"
                  required
                />
              </div>
              <div>
                <label for="description">Description</label>
                <textarea
                  v-model="newProduct.description"
                  id="description"
                  rows="3"
                  class="form-control"
                  aria-describedby="description"
                />
              </div>
              <div class="col-6">
                <label for="price">Price</label>
                <input
                  v-model="newProduct.price"
                  type="number"
                  step="0.01"
                  id="name"
                  class="form-control"
                  aria-describedby="price"
                  required
                />
              </div>
              <div class="col-6">
                <label for="quantity">Quantity</label>
                <input
                  v-model="newProduct.quantity"
                  type="number"
                  id="name"
                  class="form-control"
                  aria-describedby="quantity"
                  required
                />
              </div>
              <div>
                <label for="thumbnail">Thumbnail URL</label>
                <input
                  v-model="newProduct.thumbnail"
                  type="text"
                  id="name"
                  class="form-control"
                  aria-describedby="thumbnail"
                />
              </div>
              <div>
                <label for="image">Image URL</label>
                <input
                  v-model="newProduct.image"
                  type="text"
                  id="image"
                  class="form-control"
                  aria-describedby="image"
                />
              </div>
              <div>
                <label for="categories">Categories</label>
                <select
                  v-model="selectedCategories"
                  class="form-select"
                  id="categories"
                  multiple
                >
                  <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                  >
                    {{ category.name }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <div>
              <a
                href="#"
                class="text-reset text-decoration-none me-4"
                data-bs-toggle="modal"
                data-bs-target="#modal"
              >
                Cancel
              </a>
              <input
                type="submit"
                tag="button"
                class="btn btn-secondary"
                :value="button"
              />
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from "bootstrap";
import axios from "@/service/index.js";

export default {
  name: "ProductsModal",
  props: {
    product: Object,
    categories: Array,
    heading: String,
    button: String,
  },
  emits: {
    submitted: null,
  },
  data() {
    return {
      modal: {},
      newProduct: this.product ? { ...this.product } : {},
      selectedCategories: [],
    };
  },
  watch: {
    product() {
      this.newProduct = this.product ? { ...this.product } : {};
      if (Object.keys(this.product).length) {
        this.getProductCategories();
      }
    },
  },
  methods: {
    async getProductCategories() {
      const response = await axios.get(
        `/categories/product/${this.product.id}`
      );
      this.selectedCategories = response.data.map((category) => category.id);
    },

    submit() {
      this.$emit("submitted", this.newProduct, this.selectedCategories);
      this.modal.hide();
    },
  },
  mounted() {
    /* bad practice to use JS DOM methods when using frontend
      framework, should be done with wrapper library like BootstrapVue
      (at the time it wasnt available for Vue 3) */
    this.modal = new Modal(document.querySelector("#modal"));
  },
};
</script>
