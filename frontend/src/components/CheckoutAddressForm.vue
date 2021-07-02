<template>
  <div class="row">
    <div class="col-md-6 form-floating">
      <input
        v-model="newAddress.first_name"
        type="text"
        id="firstName"
        class="form-control"
        aria-describedby="firstName"
        :required="required"
      />
      <label for="firstName">First name</label>
    </div>
    <div class="col-md-6 form-floating">
      <input
        v-model="newAddress.last_name"
        type="text"
        id="lastName"
        class="form-control"
        aria-describedby="lastName"
        :required="required"
      />
      <label for="lastName">Last name</label>
    </div>
    <div class="form-floating">
      <input
        v-model="newAddress.company"
        type="text"
        id="company"
        class="form-control"
        aria-describedby="company"
      />
      <label for="company">Company (optional)</label>
    </div>
    <div class="form-floating">
      <input
        v-model="newAddress.address"
        type="text"
        id="address"
        class="form-control"
        aria-describedby="address"
        :required="required"
      />
      <label for="address">Address</label>
    </div>
    <div class="form-floating">
      <input
        v-model="newAddress.apartment"
        type="text"
        id="apartment"
        class="form-control"
        aria-describedby="apartment"
      />
      <label for="apartment">Apartment, suite, etc. (optional)</label>
    </div>
    <div class="form-floating">
      <input
        v-model="newAddress.city"
        type="text"
        id="city"
        class="form-control"
        aria-describedby="city"
        :required="required"
      />
      <label for="city">City</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        v-model="newAddress.country"
        type="text"
        id="city"
        class="form-control"
        aria-describedby="country"
        :required="required"
      />
      <label for="country">Country/region</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        v-model="newAddress.state"
        type="text"
        id="city"
        class="form-control"
        aria-describedby="state"
        :required="required"
      />
      <label for="state">State</label>
    </div>
    <div class="col-md-4 form-floating">
      <input
        v-model="newAddress.ZIP_code"
        type="text"
        id="zipCode"
        class="form-control"
        aria-describedby="zipCode"
        :required="required"
      />
      <label for="zipCode">ZIP code</label>
    </div>
    <div class="form-floating">
      <input
        v-model="newAddress.phone"
        type="text"
        id="phone"
        class="form-control"
        aria-describedby="phone"
      />
      <label for="phone">Phone (optional)</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "CheckoutAdressForm",
  props: {
    address: Object,
    required: Boolean,
  },
  emits: {
    changed: null,
  },
  data() {
    return {
      newAddress: this.address ? { ...this.address } : {},
    };
  },
  watch: {
    newAddress: {
      deep: true,
      handler() {
        this.$emit("changed", this.newAddress);
      },
    },
  },
};
</script>
