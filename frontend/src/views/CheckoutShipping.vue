<template>
  <form @submit.prevent="continueToPayment">
    <ul class="list-group mb-4">
      <li class="list-group-item d-flex justify-content-between p-3">
        <span v-if="logged">Contact: {{ data.email }}</span>
        <span v-else>Contact: {{ contact }}</span>
        <router-link to="/checkout/information" class="text-decoration-none">
          Change
        </router-link>
      </li>
      <li class="list-group-item d-flex justify-content-between p-3">
        <span>
          Ship to: {{ shippingAddress.address }}, {{ shippingAddress.city }}
          {{ shippingAddress.ZIP_code }}, {{ shippingAddress.country }}
        </span>
        <router-link to="/checkout/information" class="text-decoration-none">
          Change
        </router-link>
      </li>
    </ul>
    <h4>Shipping method</h4>
    <div class="list-group mb-4">
      <label
        v-for="method in methods"
        :key="method.id"
        class="list-group-item p-3"
      >
        <input
          type="radio"
          name="method"
          class="form-check-input"
          :value="method"
          v-model="shipping"
          required
        />
        <span>{{ method.name }}</span>
        <span class="float-end">
          <b>${{ method.price }}</b>
        </span>
      </label>
    </div>
    <div class="row">
      <div class="col-md-6 text-md-max-center">
        <router-link
          to="/checkout/information"
          class="text-decoration-none text-md-max-center"
        >
          <i class="bi bi-chevron-left"></i>
          Return to information
        </router-link>
      </div>
      <div class="col-md-6 d-md-max-grid text-end">
        <input
          type="submit"
          tag="button"
          class="btn btn-primary"
          value="Continue to payment"
        />
      </div>
    </div>
  </form>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import axios from "@/service/index.js";

export default {
  name: "CheckoutShipping",
  data() {
    return {
      methods: [],
      shipping: {},
    };
  },
  computed: {
    ...mapState("auth", ["logged", "data"]),
    ...mapState("checkout", ["contact", "shippingAddress", "shippingMethod"]),
  },
  methods: {
    async getShippingMethods() {
      const response = await axios.get("/shipping-methods");
      this.methods = response.data;
    },

    continueToPayment() {
      this.setShippingMethod(this.shipping);
      this.$router.push("/checkout/payment");
    },

    ...mapMutations("checkout", ["setShippingMethod"]),
  },
  created() {
    this.getShippingMethods();
    this.shipping = { ...this.shippingMethod };
  },
};
</script>

<style scoped>
@media (max-width: 768px) {
  .text-md-max-center {
    text-align: center;
  }

  .d-md-max-grid {
    display: grid !important;
  }
}
</style>
