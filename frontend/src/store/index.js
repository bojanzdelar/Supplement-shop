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
    const accessToken = state.auth.tokens.accessToken;
    if (accessToken) {
      localStorage.setItem("access_token", accessToken);
    } else {
      localStorage.removeItem("access_token");
    }

    const refreshToken = state.auth.tokens.refreshToken;
    if (refreshToken) {
      localStorage.setItem("refresh_token", refreshToken);
    } else {
      localStorage.removeItem("refresh_token");
    }
  } else if (mutation.type.startsWith("cart") && !state.auth.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart.cart));
  } else if (mutation.type.startsWith("checkout")) {
    localStorage.setItem("checkout", JSON.stringify(state.checkout));
  }
});

export default store;
