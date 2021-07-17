import jwt_decode from "jwt-decode";

const auth = {
  namespaced: true,
  state: {
    logged: false,
    isAdmin: false,
    tokens: {
      accessToken: localStorage.getItem("access_token"),
      refreshToken: localStorage.getItem("refresh_token"),
    },
  },
  mutations: {
    initialize(state) {
      const accessToken = state.tokens.accessToken;
      if (accessToken) {
        const decoded = jwt_decode(accessToken);
        state.logged = true;
        state.isAdmin = decoded.isAdmin;
      } else {
        state.logged = false;
        state.isAdmin = false;
      }
    },

    refreshToken(state, accessToken) {
      state.tokens.accessToken = accessToken;
    },

    loggedIn(state, [access_token, refresh_token]) {
      state.tokens = {
        accessToken: access_token,
        refreshToken: refresh_token,
      };
    },

    logOut(state) {
      state.tokens = {};
    },
  },
  actions: {
    async loggedIn({ commit, dispatch }, [access_token, refresh_token]) {
      console.log("yo");

      commit("loggedIn", [access_token, refresh_token]);
      commit("initialize");
      await dispatch("cart/save", null, { root: true });
      await dispatch("cart/get", null, { root: true });
    },

    logOut({ commit, dispatch }) {
      commit("logOut");
      commit("initialize");
      dispatch("cart/get", null, { root: true });
    },
  },
};

export default auth;
