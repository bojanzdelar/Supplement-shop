<template>
  <tr>
    <td>
      <button
        @click="$emit('remove', id)"
        type="button"
        class="btn-close text-reset"
        aria-label="Remove"
      ></button>
    </td>
    <td>
      <a @click="viewDetails" href="#">
        <img :src="thumbnail" class="img-fluid thumbnail" :alt="name" />
      </a>
    </td>
    <td>
      <a @click="viewDetails" href="#" class="text-body text-decoration-none">
        {{ name }}
      </a>
    </td>
    <td>${{ price }}</td>
    <td>
      <input
        type="number"
        v-model.number="newQuantity"
        min="1"
        :max="quantityAvailable"
        maxlength="1"
        class="form-control"
      />
    </td>
    <td>${{ (price * quantity).toFixed(2) }}</td>
  </tr>
</template>

<script>
import axios from "@/service/index.js";

export default {
  name: "CartRow",
  props: {
    id: Number,
    productId: String,
    name: String,
    quantity: Number,
    price: Number,
    thumbnail: String,
  },
  emits: {
    changed: null,
    remove: null,
  },
  data() {
    return {
      newQuantity: this.quantity,
      quantityAvailable: 1,
    };
  },
  watch: {
    newQuantity(val) {
      if (val <= this.quantityAvailable) {
        this.$emit("changed", this.id, val);
      } else {
        window.alert(
          "There aren't enough products for you! Please pick a smaller quantity"
        );
        this.newQuantity = this.quantity;
      }
    },
  },
  methods: {
    getQuantityAvailable() {
      axios.get(`/product/${this.productId}/quantity`).then((response) => {
        this.quantityAvailable = response.data.quantity;
      });
    },

    viewDetails() {
      this.$router.push(`/products/${this.productId}`);
    },
  },
  created() {
    this.getQuantityAvailable();
  },
};
</script>

<style scoped>
.thumbnail {
  width: 100px;
}

.form-control {
  width: 75px;
}
</style>
