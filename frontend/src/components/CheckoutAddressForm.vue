<template>
  <div class="row g-2">
    <div class="form-floating">
      <select
        class="form-select"
        v-if="logged"
        v-model="newAddress"
        id="savedAddress"
        aria-describedby="savedAddress"
      >
        <option
          v-for="address in savedAddresses"
          :key="address.id"
          :value="address"
        >
          {{ address.address }}, {{ address.city }} {{ address.ZIP_code }},
          {{ address.country }} ({{ address.first_name }}
          {{ address.last_name }})
        </option>
        <option :value="{}">Use a new address</option>
      </select>
      <label for="savedAddress">Saved addresses</label>
    </div>

    <div class="col-md-6 form-floating">
      <input
        :value="newAddress.first_name"
        @input="changeAddress(newAddress, 'first_name', $event)"
        type="text"
        id="firstName"
        class="form-control"
        aria-describedby="firstName"
        :required="required"
        :disabled="disabled"
      />
      <label for="firstName">First name</label>
    </div>
    <div class="col-md-6 form-floating">
      <input
        :value="newAddress.last_name"
        @input="changeAddress(newAddress, 'last_name', $event)"
        type="text"
        id="lastName"
        class="form-control"
        aria-describedby="lastName"
        :required="required"
        :disabled="disabled"
      />
      <label for="lastName">Last name</label>
    </div>
    <div class="form-floating">
      <input
        :value="newAddress.company"
        @input="changeAddress(newAddress, 'company', $event)"
        type="text"
        id="company"
        class="form-control"
        aria-describedby="company"
        :disabled="disabled"
      />
      <label for="company">Company (optional)</label>
    </div>
    <div class="form-floating">
      <input
        :value="newAddress.address"
        @input="changeAddress(newAddress, 'address', $event)"
        type="text"
        id="address"
        class="form-control"
        aria-describedby="address"
        :required="required"
        :disabled="disabled"
      />
      <label for="address">Address</label>
    </div>
    <div class="form-floating">
      <input
        :value="newAddress.apartment"
        @input="changeAddress(newAddress, 'apartment', $event)"
        type="text"
        id="apartment"
        class="form-control"
        aria-describedby="apartment"
        :disabled="disabled"
      />
      <label for="apartment">Apartment, suite, etc. (optional)</label>
    </div>
    <div class="form-floating">
      <input
        :value="newAddress.city"
        @input="changeAddress(newAddress, 'city', $event)"
        type="text"
        id="city"
        class="form-control"
        aria-describedby="city"
        :required="required"
        :disabled="disabled"
      />
      <label for="city">City</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        :value="newAddress.country"
        @input="changeAddress(newAddress, 'country', $event)"
        type="text"
        id="country"
        class="form-control"
        aria-describedby="country"
        :required="required"
        :disabled="disabled"
      />
      <label for="country">Country/region</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        :value="newAddress.state"
        @input="changeAddress(newAddress, 'state', $event)"
        type="text"
        id="state"
        class="form-control"
        aria-describedby="state"
        :required="required"
        :disabled="disabled"
      />
      <label for="state">State</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        :value="newAddress.ZIP_code"
        @input="changeAddress(newAddress, 'ZIP_code', $event)"
        type="text"
        id="zipCode"
        class="form-control"
        aria-describedby="zipCode"
        :required="required"
        :disabled="disabled"
      />
      <label for="zipCode">ZIP code</label>
    </div>
    <div class="form-floating">
      <input
        :value="newAddress.phone"
        @input="changeAddress(newAddress, 'phone', $event)"
        type="text"
        id="phone"
        class="form-control"
        aria-describedby="phone"
        :disabled="disabled"
      />
      <label for="phone">Phone (optional)</label>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import axios from "@/service/index.js";

const { mapState } = createNamespacedHelpers("auth");

export default {
  name: "CheckoutAddressForm",
  props: {
    address: Object,
    required: Boolean,
  },
  emits: {
    changed: null,
  },
  data() {
    return {
      savedAddresses: [],
      newAddress: this.address ? { ...this.address } : {},
    };
  },
  computed: {
    ...mapState(["logged"]),
  },
  watch: {
    logged() {
      this.getUserAddresses();
    },

    newAddress: {
      deep: true,
      handler() {
        this.$emit("changed", this.newAddress);
      },
    },
  },
  methods: {
    async getUserAddresses() {
      if (!this.logged) return;

      const response = await axios.get("/address/user");
      this.savedAddresses = response.data;
    },

    changeAddress(address, key, event) {
      if (this.newAddress.id !== undefined) {
        this.newAddress = {};
        return;
      }

      address["key"] = event.target.value;
    },
  },
  created() {
    this.getUserAddresses();
  },
};
</script>
