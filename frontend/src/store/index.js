import { createStore } from "vuex";
import auth from "./modules/auth.js";
import cart from "./modules/cart.js";
import order from "./modules/order.js";

const store = createStore({
  modules: {
    auth,
    cart,
    order,
  },
});

store.subscribe((mutation, state) => {
  if (mutation.type.startsWith("cart") && !state.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart.cart));
  }
});

store.subscribe((mutation, state) => {
  if (mutation.type.startsWith("order")) {
    localStorage.setItem("order", JSON.stringify(state.order));
  }
});

export default store;
