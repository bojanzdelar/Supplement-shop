import axios from "@/service/index.js";

const checkout = {
  namespaced: true,
  state: JSON.parse(localStorage.getItem("checkout")) || {},
  getters: {},
  mutations: {
    resetState(state) {
      Object.keys(state).forEach((key) => delete state[key]);
    },

    setShippingProvided(state, provided) {
      state.shippingProvided = provided;
    },

    setContact(state, contact) {
      state.contact = contact;
    },

    setShippingAddress(state, address) {
      state.shippingAddress = address;
    },

    setShippingAddressComplete(state, complete) {
      state.shippingAddressComplete = complete;
    },

    setBillingAddress(state, address) {
      state.billingAddress = address;
    },

    setSameAddress(state, equal) {
      state.sameAddress = equal;
    },

    setShippingMethod(state, method) {
      state.shippingMethod = method;
    },

    setPaymentMethod(state, method) {
      state.paymentMethod = method;
    },
  },
  actions: {
    saveShippingAddress({ state }) {
      return axios.post("/addresses", state.shippingAddress);
    },

    saveBillingAddress({ state }) {
      return axios.post("/addresses", state.billingAddress);
    },

    saveOrder({ state, rootState }, [shippingAddressId, billingAddressId]) {
      const products = rootState.cart.cart.map((item) => {
        return {
          product_id: item.product_cart.id,
          quantity: item.quantity,
        };
      });

      return axios.post("/orders", {
        email: rootState.auth.logged
          ? rootState.auth.data.email
          : state.contact,
        shipping_address_id: shippingAddressId,
        billing_address_id: billingAddressId,
        shipping_method_id: state.shippingMethod.id,
        payment_method_id: state.paymentMethod.id,
        sent: 0,
        delivered: 0,
        products: products,
      });
    },

    async clear({ commit }) {
      commit("resetState");
      localStorage.removeItem("checkout");
    },

    async checkout({ dispatch, state }) {
      let shippingAddressId = state.shippingAddress.id;
      let billingAddressId = state.sameAddress
        ? shippingAddressId
        : state.billingAddress.id;

      if (shippingAddressId === undefined) {
        const response = await dispatch("saveShippingAddress");
        shippingAddressId = response.data.id;
        if (state.sameAddress) {
          billingAddressId = shippingAddressId;
        }
      }

      if (billingAddressId === undefined) {
        const response = await dispatch("saveBillingAddress");
        billingAddressId = response.data.id;
      }

      await dispatch("saveOrder", [shippingAddressId, billingAddressId]);
      await dispatch("cart/clear", null, { root: true });
      await dispatch("clear");
    },
  },
};

export default checkout;
