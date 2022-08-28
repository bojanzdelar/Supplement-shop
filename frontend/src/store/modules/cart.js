import axios from "@/service/index.js";

const cart = {
  namespaced: true,
  state: {
    cart: [],
  },
  getters: {
    isEmpty(state) {
      return state.cart.length == 0;
    },

    subtotal(state, getters) {
      if (getters.cartIsEmpty) return;

      return parseFloat(
        state.cart
          .reduce((sum, curr) => {
            return sum + curr.product_cart.price * curr.quantity;
          }, 0)
          .toFixed(2)
      );
    },
  },
  mutations: {
    set(state, cart) {
      state.cart = cart;
    },

    add(state, [product, quantity]) {
      const index = state.cart.findIndex(
        (item) => item.product_cart.id == product.id
      );
      if (index != -1) {
        state.cart[index].quantity += quantity;
        return;
      }

      state.cart.push({
        product_cart: product,
        quantity: quantity,
      });
    },

    changeItemQuantity(state, [id, quantity]) {
      for (let item of state.cart) {
        if (item.product_cart.id === id) {
          item.newQuantity = quantity;
        }
      }
    },

    update(state) {
      state.cart.forEach((item) => {
        if ("newQuantity" in item) {
          item.quantity = item.newQuantity;
          delete item.newQuantity;
        }
      });
    },

    remove(state, product_id) {
      state.cart.splice(
        state.cart.findIndex((item) => item.product_cart.id == product_id),
        1
      );
    },

    clear(state) {
      state.cart = [];
    },
  },
  actions: {
    async save({ state, rootState, rootGetters }) {
      if (!state.cart || rootState.auth.isAdmin) return;

      await axios.delete("/carts");

      for (let item of state.cart) {
        await axios.post("/carts", {
          user_id: rootGetters["auth/userId"],
          product_id: item.product_cart.id,
          quantity: item.quantity,
        });
      }

      localStorage.removeItem("cart");
    },

    async get({ commit, rootState, rootGetters }) {
      if (rootState.auth.logged) {
        const response = await axios.get(
          `/carts/${rootGetters["auth/userId"]}`
        );
        commit("set", response.data);
      } else {
        commit("set", JSON.parse(localStorage.getItem("cart")) || []);
      }
    },

    async add({ commit, rootState, rootGetters }, [product, quantity]) {
      if (rootState.auth.logged) {
        await axios.post("/carts", {
          user_id: rootGetters["auth/userId"],
          product_id: product.id,
          quantity: quantity,
        });
      }
      commit("add", [product, quantity]);
    },

    async update({ commit, state, rootState, rootGetters }) {
      if (rootState.auth.logged) {
        for (let item of state.cart) {
          if ("newQuantity" in item) {
            await axios.patch(
              `/carts/${rootGetters["auth/userId"]}/${item.product_cart.id}`,
              { quantity: item.newQuantity }
            );
          }
        }
      }
      commit("update");
    },

    async remove({ commit, rootState, rootGetters }, productId) {
      if (rootState.auth.logged) {
        await axios.delete(`/carts/${rootGetters["auth/userId"]}/${productId}`);
      }
      commit("remove", productId);
    },

    async clear({ commit, rootState }) {
      if (rootState.auth.logged) {
        await axios.delete("/carts");
      }
      commit("clear");
    },
  },
};

export default cart;
