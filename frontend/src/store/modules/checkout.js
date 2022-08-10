import axios from "@/service/index.js";

const checkout = {
  namespaced: true,
  state: JSON.parse(localStorage.getItem("checkout")),
  getters: {},
  mutations: {
    setCheckout(state, checkout) {
      state = checkout;
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
      state.shippingAddress.complete = complete;
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

    saveOrder({ state, rootState }, [shippingAdressId, billingAddressId]) {
      return axios.post("/orders", {
        email: rootState.auth.logged
          ? rootState.auth.data.email
          : state.contact,
        shipping_address_id: shippingAdressId,
        billing_address_id: billingAddressId,
        shipping_method_id: state.shippingMethod.id,
        payment_method_id: state.paymentMethod.id,
        sent: 0,
        delivered: 0,
      });
    },

    async saveProductsInOrder({ rootState }, orderId) {
      for (let item of rootState.cart.cart) {
        await axios.post("/products-in-order", {
          product_id: item.product_id,
          order_id: orderId,
          quantity: item.quantity,
        });
      }
    },

    async clear({ commit }) {
      commit("setCheckout", {});
    },

    async checkout({ dispatch, state }) {
      // check whether:
      // - shipping address already has an ID
      // - check whether billing address already has an ID
      // - shipping address is same as billing

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

      const order = await dispatch("saveOrder", [
        shippingAddressId,
        billingAddressId,
      ]);

      await dispatch("saveProductsInOrder", order.data.id);
      await dispatch("cart/clear", null, { root: true });
      await dispatch("clear");
    },
  },
};

export default checkout;
