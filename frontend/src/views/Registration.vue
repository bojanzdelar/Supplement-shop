<template>
  <div class="container">
    <div v-if="failed" class="col-lg-8 mx-auto alert alert-danger" role="alert">
      Username is already taken.
    </div>
    <form
      @submit.prevent="register(user)"
      class="row needs-validation"
      novalidate
    >
      <div class="col-lg-8 mx-auto">
        <div>
          <label for="validationCustom01" class="form-label">First name</label>
          <input
            v-model="user.first_name"
            type="text"
            class="form-control"
            id="validationCustom01"
            required
          />
          <div class="valid-feedback">Looks good!</div>
        </div>
        <div>
          <label for="validationCustom02" class="form-label">Last name</label>
          <input
            v-model="user.last_name"
            type="text"
            class="form-control"
            id="validationCustom02"
            required
          />
          <div class="valid-feedback">Looks good!</div>
        </div>
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
          <label for="validationCustomPasswordConfirmation" class="form-label">
            Password confirmation
          </label>
          <div class="input-group has-validation">
            <input
              v-model="user.password_confirmation"
              type="password"
              class="form-control"
              id="validationCustomPasswordConfirmation"
              aria-describedby="inputGroupPrepend"
              required
            />
            <div class="invalid-feedback">Please confirm your password.</div>
          </div>
        </div>
        <div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              value=""
              id="invalidCheck"
              required
            />
            <label class="form-check-label" for="invalidCheck">
              Agree to terms and conditions
            </label>
            <div class="invalid-feedback">
              You must agree before submitting.
            </div>
          </div>
        </div>
        <div>
          <input class="btn btn-success" type="submit" value="Register" />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Registration",
  data() {
    return {
      user: {},
      failed: false,
    };
  },
  methods: {
    register(user) {
      this.axios
        .post("/register", user)
        .then(() => {
          this.$router.push("/login");
        })
        .catch(() => {
          this.failed = true;
        });
    },
  },
};
</script>
