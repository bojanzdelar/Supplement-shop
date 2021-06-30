import { createStore } from "vuex";
import auth from "./modules/auth.js";
import cart from "./modules/cart.js";

const store = createStore({
  modules: {
    auth,
    cart,
  },
});

store.subscribe((mutation, state) => {
  if (mutation.type.startsWith("cart") && !state.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart.cart));
  }
});

export default store;
