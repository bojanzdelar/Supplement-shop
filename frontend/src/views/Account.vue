<template>
  <div class="container mt-5">
    <h1 class="text-center">My account</h1>
    <hr />
    <div class="row">
      <div class="col-md-6">
        <h4>Order history</h4>
      </div>
      <div class="col-md-6">
        <h4>Account details</h4>
        <router-link
          to="/account/addresses"
          tag="button"
          class="btn btn-success text-uppercase text-dark"
        >
          View addresses
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Account",
};
</script>
