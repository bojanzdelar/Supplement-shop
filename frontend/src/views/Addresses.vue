<template>
  <div class="container mt-5">
    <h1 class="text-center">Your addresses</h1>
    <hr />
    <div class="d-flex justify-content-between mb-4">
      <router-link to="/account" class="text-secondary text-decoration-none">
        Return to account details
      </router-link>
      <button
        @click="create"
        class="btn px-3 py-2"
        data-bs-toggle="modal"
        data-bs-target="#modal"
      >
        <i class="bi bi-plus-lg"></i> (Create new)
      </button>
    </div>
    <AddressesModal
      :address="modal.address"
      :heading="modal.heading"
      :button="modal.button"
      @submitted="modal.handler"
    />
    <AddressesTable
      :addresses="addresses"
      :actionsAvailable="true"
      @edit="edit"
      @remove="remove"
    />
    <DeleteModal :entity="'address'" @confirmed="deleteAddress(id)" />
  </div>
</template>

<script>
import AddressesModal from "@/components/AddressesModal.vue";
import AddressesTable from "@/components/AddressesTable.vue";
import DeleteModal from "@/components/DeleteModal.vue";
import axios from "@/service/index.js";

export default {
  name: "Addresses",
  components: {
    AddressesModal,
    AddressesTable,
    DeleteModal,
  },
  data() {
    return {
      addresses: [],
      modal: {},
      id: null,
    };
  },
  methods: {
    async getAdresses() {
      const response = await axios.get("/address/user");
      this.addresses = response.data;
    },

    async createAddress(newAddress) {
      const response = await axios.post("/address", newAddress);
      newAddress.id = response.data.id;
      this.addresses.push(newAddress);
    },

    async updateAddress(newAddress) {
      const response = await axios.put(`/address/${newAddress.id}`, newAddress);
      this.addresses[
        this.addresses.findIndex((address) => address.id === newAddress.id)
      ] = response.data;
    },

    async deleteAddress(id) {
      await axios.delete(`/address/${id}`);
      this.addresses.splice(
        this.addresses.findIndex((address) => address.id === id),
        1
      );
    },

    create() {
      this.modal = {
        address: {},
        heading: "Add a new address",
        button: "Add address",
        handler: this.createAddress,
      };
    },

    edit(id) {
      this.modal = {
        address: this.addresses.find((address) => address.id === id),
        heading: "Edit address",
        button: "Update address",
        handler: this.updateAddress,
      };
    },

    remove(id) {
      this.id = id;
    },
  },
  created() {
    this.getAdresses();
  },
};
</script>
