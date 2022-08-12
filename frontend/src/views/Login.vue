<template>
  <div class="container mt-5">
    <h3 class="text-center mb-4">My account</h3>
    <div class="row justify-content-center">
      <div class="col-md-4 border p-4 me-md-4 mb-4">
        <h5>Login</h5>
        <p>If you have an account with us, please log in.</p>
        <div v-if="failed" class="alert alert-danger" role="alert">
          Email and/or password is invalid.
        </div>
        <form @submit.prevent="login(user)" class="text-center row g-3">
          <div>
            <input
              v-model="user.email"
              type="text"
              class="form-control"
              placeholder="Email"
              aria-describedby="email"
              required
            />
          </div>
          <div>
            <input
              v-model="user.password"
              type="password"
              class="form-control"
              placeholder="Password"
              aria-describedby="password"
              required
            />
          </div>
          <div>
            <input
              class="btn btn-success text-dark text-uppercase"
              type="submit"
              value="Sign in"
            />
          </div>
          <p>Forgot your password?</p>
        </form>
      </div>
      <div class="col-md-4 border p-4 mb-4">
        <h5>New customer?</h5>
        <p>
          Registering for this site allows you to access your order status and
          history. We’ll get a new account set up for you in no time. For this
          will only ask you for information necessary to make the purchase
          process faster and easier
        </p>
        <router-link
          to="/account/register"
          class="btn btn-success text-dark text-uppercase"
        >
          Create an account
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
import axios from "@/service/index.js";

const { mapActions } = createNamespacedHelpers("auth");

export default {
  name: "Login",
  data() {
    return {
      user: {},
      failed: false,
    };
  },
  methods: {
    async login(user) {
      try {
        const response = await axios.post("/login", user);
        const data = response.data;
        this.loggedIn([data.access_token, data.refresh_token]);
        this.$router.back();
      } catch {
        this.failed = true;
      }
    },
    ...mapActions(["loggedIn"]),
  },
};
</script>
