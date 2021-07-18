<template>
  <div class="modal" id="deleteModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Confirm deletion</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <p>Are you sure you want to delete selected {{ entity }}?</p>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            data-bs-target="#deleteModal"
          >
            Close
          </button>
          <button
            @click="confirm"
            type="button"
            class="btn btn-primary"
            data-bs-dismiss="modal"
            data-bs-target="#deleteModal"
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DeleteModal",
  props: {
    entity: String,
  },
  emits: {
    confirmed: null,
  },
  methods: {
    confirm() {
      this.$emit("confirmed");
    },
  },
};
</script>
