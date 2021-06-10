<template>
  <div class="container">
    <form class="row needs-validation" novalidate>
      <div class="col-lg-8 mx-auto">
        <div>
          <label for="validationCustomUsername" class="form-label">
            Username
          </label>
          <div class="input-group has-validation">
            <span class="input-group-text" id="inputGroupPrepend">@</span>
            <input
              v-model="user.username"
              type="text"
              class="form-control"
              id="validationCustomUsername"
              aria-describedby="inputGroupPrepend"
              required
            />
            <div class="invalid-feedback">Please choose a username.</div>
          </div>
        </div>
        <div>
          <label for="validationCustomPassword" class="form-label">
            Password
          </label>
          <div class="input-group has-validation">
            <input
              v-model="user.password"
              type="password"
              class="form-control"
              id="validationCustomPassword"
              aria-describedby="inputGroupPrepend"
              required
            />
            <div class="invalid-feedback">Please enter a password.</div>
          </div>
        </div>
        <div>
          <button class="btn btn-success" type="submit">Login</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      user: {},
    };
  },
};
</script>
