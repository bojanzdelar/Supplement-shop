const auth = {
  namespaced: true,
  state: {
    logged: localStorage.getItem("access_token") !== null,
    user: JSON.parse(localStorage.getItem("user")) || null,
    isAdmin: localStorage.getItem("user")
      ? JSON.parse(localStorage.getItem("user")).user_type_id === 1
      : false,
  },
  mutations: {
    loggedIn(state, [access_token, refresh_token, user]) {
      state.logged = true;
      state.user = user;
      state.isAdmin = user.user_type_id === 1;
      localStorage.setItem("access_token", access_token);
      localStorage.setItem("refresh_token", refresh_token);
      localStorage.setItem("user", JSON.stringify(user));
      localStorage.removeItem("cart");
    },

    logOut(state) {
      state.logged = false;
      state.user = null;
      state.isAdmin = false;
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("user");
      localStorage.removeItem("cart");
    },
  },
  actions: {
    async loggedIn(
      { commit, dispatch },
      { access_token, refresh_token, user }
    ) {
      commit("loggedIn", [access_token, refresh_token, user]);
      await dispatch("cart/save", null, { root: true });
      await dispatch("cart/get", null, { root: true });
    },

    logOut({ commit, dispatch }) {
      commit("logOut");
      dispatch("cart/get", null, { root: true });
    },
  },
};

export default auth;
