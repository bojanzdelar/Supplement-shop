<template>
  <div class="container mt-5">
    <div v-if="failed" class="alert alert-danger" role="alert">
      Username is already taken.
    </div>
    <form @submit.prevent="register(user)" class="text-center">
      <div>
        <input
          v-model="user.first_name"
          type="text"
          class="form-control"
          placeholder="First Name"
          aria-describedby="firstName"
          required
        />
      </div>
      <div>
        <input
          v-model="user.last_name"
          type="text"
          class="form-control"
          placeholder="Last Name"
          aria-describedby="lastName"
          required
        />
      </div>
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
          id="validationCustomPassword"
          aria-describedby="inputGroupPrepend"
          required
        />
      </div>
      <div>
        <input
          class="form-check-input"
          type="checkbox"
          value=""
          id="subscribe"
        />
        <label class="form-check-label" for="subscribe">
          Subscribe to stay updated with new products and offers!
        </label>
      </div>
      <div>
        <input class="btn btn-success" type="submit" value="Submit" />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "@/service/index.js";

export default {
  name: "Registration",
  data() {
    return {
      user: {},
      failed: false,
    };
  },
  methods: {
    async register(user) {
      try {
        await axios.post("/register", user);
        this.$router.push("/login");
      } catch {
        this.failed = true;
      }
    },
  },
};
</script>
