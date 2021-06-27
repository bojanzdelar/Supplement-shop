import { createStore } from "vuex";
import axios from "@/service/index.js";

const store = createStore({
  state: {
    logged: localStorage.getItem("access_token") !== null,
    cart: [],
  },
  mutations: {
    logIn(state, [access_token, refresh_token]) {
      state.logged = true;
      // state.cart = [];
      localStorage.setItem("access_token", access_token);
      localStorage.setItem("refresh_token", refresh_token);
      localStorage.removeItem("cart");
    },

    logOut(state) {
      state.logged = false;
      state.cart = [];
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("cart");
    },

    setCart(state, cart) {
      state.cart = cart;
    },

    addToCart(state, [product, quantity]) {
      const index = state.cart.findIndex(
        (item) => item.product_id == product.id
      );
      if (index != -1) {
        state.cart[index].quantity += quantity;
        return;
      }

      state.cart.push({
        product_id: product.id,
        name: product.name,
        price: product.price,
        quantity: quantity,
        thumbnail: product.thumbnail,
      });
    },

    removeFromCart(state, id) {
      state.cart.splice(
        state.cart.findIndex((item) => item.product_id == id),
        1
      );
    },
  },
  actions: {
    logIn({ commit, state, dispatch }, [access_token, refresh_token]) {
      commit("logIn", [access_token, refresh_token]);
      if (state.logged) {
        dispatch("saveCart").then(() => {
          dispatch("getCart");
        });
      } else {
        dispatch("getCart");
      }
    },

    logOut({ commit, dispatch }) {
      commit("logOut");
      dispatch("getCart");
    },

    saveCart({ state }) {
      if (!state.cart) return Promise.resolve();

      axios.delete("/cart/user").then(() => {
        state.cart.forEach((item) => {
          axios.post("/cart", item).then();
        });

        return Promise.resolve();
      });
    },

    getCart({ commit, state }) {
      if (state.logged) {
        axios.get("/cart/user").then((response) => {
          commit("setCart", response.data);
        });
      } else {
        commit("setCart", JSON.parse(localStorage.getItem("cart")) || []);
      }
    },

    addToCart({ commit, state }, [product, quantity]) {
      if (state.logged) {
        axios
          .post("/cart", { product_id: product.id, quantity: quantity })
          .then(() => {
            commit("addToCart", [product, quantity]);
          });
      } else {
        commit("addToCart", [product, quantity]);
      }
    },

    removeFromCart({ commit, state }, id) {
      if (state.logged) {
        axios.delete(`/cart/${id}`).then(() => {
          commit("removeFromCart", id);
        });
      } else {
        commit("removeFromCart", id);
      }
    },
  },
  getters: {
    cartIsEmpty(state) {
      return state.cart.length == 0;
    },

    cartSubtotal(state, getters) {
      if (getters.cartIsEmpty) return;

      return state.cart
        .reduce((sum, curr) => {
          return sum + curr.price * curr.quantity;
        }, 0)
        .toFixed(2);
    },
  },
  modules: {},
});

store.subscribe((_, state) => {
  if (!state.logged) {
    localStorage.setItem("cart", JSON.stringify(state.cart));
  }
});

export default store;
