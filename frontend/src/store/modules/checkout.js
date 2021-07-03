const checkout = {
  namespaced: true,
  state: JSON.parse(localStorage.getItem("checkout")),
  getters: {},
  mutations: {
    setContact(state, contact) {
      state.contact = contact;
    },

    setShippingAddress(state, address) {
      state.shippingAddress = address;
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
    // order({ commit }) {
    // }
  },
};

export default checkout;
