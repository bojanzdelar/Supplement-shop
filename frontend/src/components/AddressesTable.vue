<template>
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>First name</th>
          <th>Last name</th>
          <th>Company</th>
          <th>Address</th>
          <th>Apartment</th>
          <th>City</th>
          <th>County</th>
          <th>State</th>
          <th>ZIP code</th>
          <th>Phone</th>
          <th v-if="actionsAvailable">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="address in addresses" :key="address.id">
          <td>{{ address.first_name }}</td>
          <td>{{ address.last_name }}</td>
          <td>{{ address.company }}</td>
          <td>{{ address.address }}</td>
          <td>{{ address.apartment }}</td>
          <td>{{ address.city }}</td>
          <td>{{ address.country }}</td>
          <td>{{ address.state }}</td>
          <td>{{ address.zip_code }}</td>
          <td>{{ address.phone }}</td>
          <td v-if="actionsAvailable">
            <button
              @click="edit(address.id)"
              class="btn text-dark text-uppercase me-2"
              data-bs-toggle="modal"
              data-bs-target="#modal"
            >
              <i class="bi bi-pencil"></i>
            </button>
            <button
              @click="remove(address.id)"
              class="btn text-uppercase"
              data-bs-toggle="modal"
              data-bs-target="#deleteModal"
            >
              <i class="bi bi-x-lg"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "AddressesTable",
  props: {
    addresses: Array,
    actionsAvailable: Boolean,
  },
  emits: {
    edit: null,
    remove: null,
  },
  methods: {
    edit(id) {
      this.$emit("edit", id);
    },

    remove(id) {
      this.$emit("remove", id);
    },
  },
};
</script>
