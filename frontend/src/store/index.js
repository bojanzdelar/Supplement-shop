import { createStore } from "vuex";
import auth from "./modules/auth.js";
import cart from "./modules/cart.js";
import checkout from "./modules/checkout.js";

const store = createStore({
  modules: {
    auth,
    cart,
    checkout,
  },
});

store.subscribe((mutation, state) => {
  if (mutation.type.startsWith("auth")) {
    localStorage.setItem("access_token", state.auth.tokens.accessToken);
    localStorage.setItem("refresh_token", state.auth.tokens.refreshToken);
  } else if (mutation.type.startsWith("cart") && !state.auth.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart.cart));
  } else if (mutation.type.startsWith("checkout")) {
    localStorage.setItem("checkout", JSON.stringify(state.checkout));
  }
});

export default store;
