<template>
  <form @submit.prevent="continueToShipping">
    <div class="row g-2">
      <div class="d-flex justify-content-between">
        <h5>Contact information</h5>
        <p v-if="!logged">
          Already have an account?
          <router-link to="/account/login" class="text-decoration-none">
            Log in
          </router-link>
        </p>
      </div>
      <div v-if="!logged" class="form-floating mb-4">
        <input
          v-model="contact"
          id="email"
          class="form-control"
          aria-describedby="email"
          required
        />
        <label for="email">Email</label>
      </div>
      <div v-else class="mb-4">
        <div>{{ data.name }} ({{ data.email }})</div>
        <a @click="logOut" href="#" class="text-decoration-none">Log out</a>
      </div>
      <h5>Shipping Address</h5>
      <CheckoutAddressForm
        :address="shippingAddress"
        :required="true"
        @changed="shippingAddress = $event"
        class="mb-4"
      />
      <div class="col-md-6 text-md-max-center">
        <router-link to="/cart" class="text-decoration-none text-md-max-center">
          <i class="bi bi-chevron-left"></i>
          Return to cart
        </router-link>
      </div>
      <div class="col-md-6 d-md-max-grid text-end">
        <input
          type="submit"
          tag="button"
          class="btn btn-primary"
          value="Continue to shipping"
        />
      </div>
    </div>
  </form>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";
import CheckoutAddressForm from "@/components/CheckoutAddressForm.vue";

export default {
  name: "CheckoutInformation",
  components: {
    CheckoutAddressForm,
  },
  computed: {
    contact: {
      get() {
        return this.$store.state.checkout.contact;
      },
      set(value) {
        this.setContact(value);
      },
    },

    shippingAddress: {
      get() {
        return this.$store.state.checkout.shippingAddress;
      },
      set(value) {
        this.setShippingAddress(value);
      },
    },

    ...mapState("auth", ["logged", "data"]),
  },
  methods: {
    continueToShipping() {
      this.setShippingAddressComplete(true);
      this.$router.push("/checkout/shipping");
    },

    ...mapMutations("checkout", [
      "setContact",
      "setShippingAddress",
      "setShippingAddressComplete",
    ]),
    ...mapActions("auth", ["logOut"]),
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
