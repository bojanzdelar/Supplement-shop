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
            return sum + curr.price * curr.quantity;
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

    changeItemQuantity(state, [id, quantity]) {
      for (let item of state.cart) {
        if (item.product_id === id) {
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
        state.cart.findIndex((item) => item.product_id == product_id),
        1
      );
    },

    clear(state) {
      state.cart = [];
    },
  },
  actions: {
    async save({ state }) {
      if (!state.cart) return;

      await axios.delete("/carts/user");

      for (let item of state.cart) {
        await axios.post("/carts", item);
      }

      localStorage.removeItem("cart");
    },

    async get({ commit, rootState }) {
      if (rootState.auth.logged) {
        const response = await axios.get("/carts/user");
        commit("set", response.data);
      } else {
        commit("set", JSON.parse(localStorage.getItem("cart")) || []);
      }
    },

    async add({ commit, rootState }, [product, quantity]) {
      if (rootState.auth.logged) {
        await axios.post("/carts", {
          product_id: product.id,
          quantity: quantity,
        });
      }
      commit("add", [product, quantity]);
    },

    async update({ commit, state, rootState }) {
      if (rootState.auth.logged) {
        for (let item of state.cart) {
          if ("newQuantity" in item) {
            await axios.put(`/carts/${item.product_id}`, item);
          }
        }
      }
      commit("update");
    },

    async remove({ commit, rootState }, productId) {
      if (rootState.auth.logged) {
        await axios.delete(`/carts/${productId}`);
      }
      commit("remove", productId);
    },

    async clear({ commit, rootState }) {
      if (rootState.auth.logged) {
        await axios.delete("/carts/user");
      }
      commit("clear");
    },
  },
};

export default cart;
