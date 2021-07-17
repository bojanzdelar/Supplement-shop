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
              <div class="col-md-6">
                <label for="firstName">First name</label>
                <input
                  v-model="newAddress.first_name"
                  type="text"
                  id="firstName"
                  class="form-control"
                  aria-describedby="firstName"
                  required
                />
              </div>
              <div class="col-md-6">
                <label for="lastName">Last name</label>
                <input
                  v-model="newAddress.last_name"
                  type="text"
                  id="lastName"
                  class="form-control"
                  aria-describedby="lastName"
                  required
                />
              </div>
              <div>
                <label for="company">Company (optional)</label>
                <input
                  v-model="newAddress.company"
                  type="text"
                  id="company"
                  class="form-control"
                  aria-describedby="company"
                />
              </div>
              <div>
                <label for="address">Address</label>
                <input
                  v-model="newAddress.address"
                  type="text"
                  id="address"
                  class="form-control"
                  aria-describedby="address"
                  required
                />
              </div>
              <div>
                <label for="apartment">Apartment, suite, etc. (optional)</label>
                <input
                  v-model="newAddress.apartment"
                  type="text"
                  id="apartment"
                  class="form-control"
                  aria-describedby="apartment"
                />
              </div>
              <div>
                <label for="city">City</label>
                <input
                  v-model="newAddress.city"
                  type="text"
                  id="city"
                  class="form-control"
                  aria-describedby="city"
                  required
                />
              </div>
              <div class="col-md-4">
                <label for="country">Country/region</label>
                <input
                  v-model="newAddress.country"
                  type="text"
                  id="city"
                  class="form-control"
                  aria-describedby="country"
                  required
                />
              </div>
              <div class="col-md-4">
                <label for="state">State</label>
                <input
                  v-model="newAddress.state"
                  type="text"
                  id="city"
                  class="form-control"
                  aria-describedby="state"
                  required
                />
              </div>
              <div class="col-md-4">
                <label for="zipCode">ZIP code</label>
                <input
                  v-model="newAddress.ZIP_code"
                  type="number"
                  id="zipCode"
                  class="form-control"
                  aria-describedby="zipCode"
                  required
                />
              </div>
              <div>
                <label for="phone">Phone (optional)</label>
                <input
                  v-model="newAddress.phone"
                  type="text"
                  id="phone"
                  class="form-control"
                  aria-describedby="phone"
                />
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <div>
              <input
                type="submit"
                tag="button"
                class="btn btn-success text-dark text-uppercase me-2"
                :value="button"
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
import { Modal } from "bootstrap";

export default {
  name: "AddressesModal",
  props: {
    address: Object,
    heading: String,
    button: String,
  },
  emits: {
    submitted: null,
  },
  data() {
    return {
      modal: {},
      newAddress: this.address ? { ...this.address } : {},
    };
  },
  watch: {
    address() {
      this.newAddress = this.address ? { ...this.address } : {};
    },
  },
  methods: {
    submit() {
      this.$emit("submitted", this.newAddress);
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
