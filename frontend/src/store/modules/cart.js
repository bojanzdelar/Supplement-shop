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

      return state.cart
        .reduce((sum, curr) => {
          return sum + curr.price * curr.quantity;
        }, 0)
        .toFixed(2);
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

    remove(state, id) {
      state.cart.splice(
        state.cart.findIndex((item) => item.product_id == id),
        1
      );
    },
  },
  actions: {
    save({ state }) {
      if (!state.cart) return Promise.resolve();

      axios.delete("/cart/user").then(() => {
        state.cart.forEach((item) => {
          axios.post("/cart", item).then();
        });

        return Promise.resolve();
      });
    },

    get({ commit, state }) {
      if (state.logged) {
        axios.get("/cart/user").then((response) => {
          commit("set", response.data);
        });
      } else {
        commit("set", JSON.parse(localStorage.getItem("cart")) || []);
      }
    },

    add({ commit, state }, [product, quantity]) {
      if (state.logged) {
        axios
          .post("/cart", { product_id: product.id, quantity: quantity })
          .then(() => {
            commit("add", [product, quantity]);
          });
      } else {
        commit("add", [product, quantity]);
      }
    },

    update({ commit, state }) {
      if (state.logged) {
        for (let item of state.cart) {
          if ("newQuantity" in item) {
            axios.put(`/cart/${item.id}`, item);
          }
        }
      }
      commit("update");
    },

    remove({ commit, state }, id) {
      if (state.logged) {
        axios.delete(`/cart/${id}`).then(() => {
          commit("remove", id);
        });
      } else {
        commit("remove", id);
      }
    },
  },
};

export default cart;
