<template>
  <div class="container mt-5">
    <h3 class="text-center">My account</h3>
    <div class="row justify-content-center">
      <div class="col-md-4">
        <h5>Login</h5>
        <p>If you have an account with us, please log in.</p>
        <div v-if="failed" class="alert alert-danger" role="alert">
          Username and/or password is invalid.
        </div>
        <form @submit.prevent="login(user)" class="text-center">
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
            <input class="btn btn-success" type="submit" value="Sign in" />
          </div>
          <p>Forgot your password?</p>
        </form>
      </div>
      <div class="col-md-4">
        <h5>New customer?</h5>
        <p>
          Registering for this site allows you to access your order status and
          history. We’ll get a new account set up for you in no time. For this
          will only ask you for information necessary to make the purchase
          process faster and easier
        </p>
        <router-link to="/register" class="btn btn-success">
          Create an account
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      user: {},
      failed: false,
    };
  },
  methods: {
    login(user) {
      this.axios
        .post("/login", user)
        .then((response) => {
          localStorage.setItem("access_token", response.data["access_token"]);
          localStorage.setItem("refresh_token", response.data["refresh_token"]);
          this.saveCart();
          this.emitter.emit("loggedIn");
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
          this.failed = true;
        });
    },

    saveCart() {
      const cart = JSON.parse(localStorage.getItem("cart"));
      if (!cart) return;

      this.axios.delete("/cart/user");
      cart.forEach((item) => {
        this.axios.post("/cart", item);
      });
      localStorage.removeItem("cart");
    },
  },
};
</script>
