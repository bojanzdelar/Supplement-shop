const auth = {
  namespaced: true,
  state: {
    logged: localStorage.getItem("access_token") !== null,
    user: JSON.parse(localStorage.getItem("user")) || null,
  },
  mutations: {
    loggedIn(state, [access_token, refresh_token, user]) {
      state.logged = true;
      state.user = user;
      localStorage.setItem("access_token", access_token);
      localStorage.setItem("refresh_token", refresh_token);
      localStorage.setItem("user", JSON.stringify(user));
      localStorage.removeItem("cart");
    },

    logOut(state) {
      state.logged = false;
      state.user = null;
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("user");
      localStorage.removeItem("cart");
    },
  },
  actions: {
    loggedIn({ commit, dispatch }, { access_token, refresh_token, user }) {
      commit("loggedIn", [access_token, refresh_token, user]);
      dispatch("cart/save", null, { root: true }).then(() => {
        dispatch("cart/get", null, { root: true });
      });
    },

    logOut({ commit, dispatch }) {
      commit("logOut");
      dispatch("cart/get", null, { root: true });
    },
  },
};

export default auth;
