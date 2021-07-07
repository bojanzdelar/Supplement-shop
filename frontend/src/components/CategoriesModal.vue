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
            <label for="name">Name</label>
            <input
              v-model="newCategory.name"
              type="text"
              id="name"
              class="form-control"
              aria-describedby="name"
              required
            />
          </div>
          <div class="modal-footer">
            <div>
              <input
                type="submit"
                tag="button"
                class="btn btn-success text-dark text-uppercase me-2"
                :value="button"
                data-bs-toggle="modal"
                data-bs-target="#modal"
              />
              <a
                href="#"
                class="text-reset text-decoration-none"
                data-bs-toggle="modal"
                data-bs-target="#modal"
              >
                Cancel
              </a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategoriesModal",
  props: {
    category: Object,
    heading: String,
    button: String,
  },
  emits: {
    submitted: null,
  },
  data() {
    return {
      newCategory: this.category ? { ...this.category } : {},
    };
  },
  watch: {
    category() {
      this.newCategory = this.category ? { ...this.category } : {};
    },
  },
  methods: {
    submit() {
      this.$emit("submitted", this.newCategory);
    },
  },
};
</script>
