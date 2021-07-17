<template>
  <form @submit.prevent="finishOrder">
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
      <li class="list-group-item d-flex justify-content-between p-3">
        <span>
          Method: {{ shippingMethod.name }} ·
          <b>${{ shippingMethod.price }}</b>
        </span>
        <router-link to="/checkout/shipping" class="text-decoration-none">
          Change
        </router-link>
      </li>
    </ul>
    <h4>Payment method</h4>
    <p>All transactions are secure and encrypted.</p>
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
          v-model="payment"
          required
        />
        <span class="ms-2">{{ method.name }}</span>
      </label>
    </div>
    <h4>Billing address</h4>
    <p>Select the address that matches your card or payment method.</p>
    <div class="list-group mb-4">
      <label class="list-group-item p-3">
        <input
          type="radio"
          name="address"
          class="form-check-input"
          v-model="sameAddress"
          :value="true"
          required
        />
        Same as shipping address
      </label>
      <label class="list-group-item p-3">
        <input
          type="radio"
          name="address"
          class="form-check-input"
          v-model="sameAddress"
          :value="false"
          required
        />
        Use a different billing address
      </label>
      <div v-if="!sameAddress" class="list-group-item bg-light p-4">
        <CheckoutAddressForm
          :address="billingAddress"
          :required="!sameAddress"
          @changed="billingAddress = $event"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 text-md-max-center">
        <router-link
          to="/checkout/shipping"
          class="text-decoration-none text-md-max-center"
        >
          <i class="bi bi-chevron-left"></i>
          Return to shipping
        </router-link>
      </div>
      <div class="col-md-6 d-md-max-grid text-end">
        <input
          type="submit"
          tag="button"
          class="btn btn-primary"
          value="Pay now"
        />
      </div>
    </div>
  </form>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";
import axios from "@/service/index.js";
import CheckoutAddressForm from "@/components/CheckoutAddressForm.vue";

export default {
  name: "CheckoutPayment",
  components: {
    CheckoutAddressForm,
  },
  data() {
    return {
      methods: [],
      payment: {},
      sameAddress: false,
    };
  },
  computed: {
    billingAddress: {
      get() {
        return this.$store.state.checkout.billingAddress;
      },
      set(value) {
        this.setBillingAddress(value);
      },
    },

    ...mapState("auth", ["logged", "data"]),
    ...mapState("checkout", ["contact", "shippingAddress", "shippingMethod"]),
  },
  methods: {
    async getPaymentMethods() {
      const response = await axios.get("/payment-method");
      this.methods = response.data;
    },

    async finishOrder() {
      this.setPaymentMethod(this.payment);
      this.setSameAddress(this.sameAddress);

      try {
        this.checkout();
        window.alert("Your order has been received!");
        this.$router.push("/");
      } catch (error) {
        window.alert(error);
      }
    },

    ...mapMutations("checkout", [
      "setPaymentMethod",
      "setBillingAddress",
      "setSameAddress",
    ]),
    ...mapActions("checkout", ["checkout"]),
  },
  created() {
    this.getPaymentMethods();
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
