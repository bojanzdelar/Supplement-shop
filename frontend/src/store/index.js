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
  if (mutation.type.startsWith("cart") && !state.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart.cart));
  }
});

store.subscribe((mutation, state) => {
  if (mutation.type.startsWith("checkout")) {
    localStorage.setItem("checkout", JSON.stringify(state.checkout));
  }
});

export default store;
