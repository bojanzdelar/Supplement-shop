const auth = {
  namespaced: true,
  state: {
    logged: localStorage.getItem("access_token") !== null,
  },
  mutations: {
    loggedIn(state, [access_token, refresh_token]) {
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
  },
  actions: {
    loggedIn({ commit, dispatch }, { access_token, refresh_token }) {
      commit("loggedIn", [access_token, refresh_token]);
      dispatch("cart/save").then(() => {
        dispatch("cart/get");
      });
    },

    logOut({ commit, dispatch }) {
      commit("logOut");
      dispatch("cart/get");
    },
  },
};

export default auth;
