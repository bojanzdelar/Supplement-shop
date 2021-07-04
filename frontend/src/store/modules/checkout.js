import axios from "@/service/index.js";

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
    saveShippingAddress({ state }) {
      return axios.post("/address", state.shippingAddress);
    },

    saveBillingAddress({ state }) {
      return axios.post("/address", state.billingAddress);
    },

    saveOrder({ state }, [shippingAdressId, billingAddressId]) {
      return axios.post("/orders", {
        email: state.contact,
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
        await axios.post("/product-in-order", {
          product_id: item.product_id,
          order_id: orderId,
          quantity: item.quantity,
        });
      }
    },

    async checkout({ dispatch }) {
      const [shippingAddress, billingAddress] = await Promise.all([
        dispatch("saveShippingAddress"),
        dispatch("saveBillingAddress"),
      ]);

      const order = await dispatch("saveOrder", [
        shippingAddress.data.id,
        billingAddress.data.id,
      ]);

      await dispatch("saveProductsInOrder", order.data.id);

      await dispatch("cart/clear", null, { root: true });
    },
  },
};

export default checkout;
