<template>
  <form @submit.prevent="finishOrder">
    <ul class="list-group">
      <li class="list-group-item d-flex justify-content-between">
        <span v-if="logged">Contact: {{ user.email }}</span>
        <span v-else>Contact: {{ contact }}</span>
        <router-link to="/checkout/information" class="text-decoration-none">
          Change
        </router-link>
      </li>
      <li class="list-group-item d-flex justify-content-between">
        <span>
          Ship to: {{ shippingAddress.address }}, {{ shippingAddress.city }}
          {{ shippingAddress.ZIP_code }}, {{ shippingAddress.country }}
        </span>
        <router-link to="/checkout/information" class="text-decoration-none">
          Change
        </router-link>
      </li>
      <li class="list-group-item d-flex justify-content-between">
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
    <div class="list-group">
      <label v-for="method in methods" :key="method.id" class="list-group-item">
        <input
          type="radio"
          name="method"
          class="form-check-input"
          :value="method"
          v-model="payment"
          required
        />
        <span>{{ method.name }}</span>
      </label>
    </div>
    <h4>Billing address</h4>
    <p>Select the address that matches your card or payment method.</p>
    <div class="list-group">
      <label class="list-group-item">
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
      <label class="list-group-item">
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
      <div v-if="!sameAddress" class="list-group-item">
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
import { mapState, mapMutations } from "vuex";
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

    ...mapState("auth", ["logged", "user"]),
    ...mapState("checkout", ["contact", "shippingAddress", "shippingMethod"]),
  },
  methods: {
    getPaymentMethods() {
      axios.get("/payment-method").then((response) => {
        this.methods = response.data;
      });
    },

    finishOrder() {
      this.setPaymentMethod(this.payment);
      this.setSameAddress(this.sameAddress);
      window.alert("Your order has been received!");
      // this.$router.push("/");
    },

    ...mapMutations("checkout", [
      "setPaymentMethod",
      "setBillingAddress",
      "setSameAddress",
    ]),
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
