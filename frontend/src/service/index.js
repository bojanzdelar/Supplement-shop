import axios from "axios";
import store from "../store/index.js";

const URL = "http://127.0.0.1:5000/api";

const instance = axios.create({
  baseURL: URL,
});

instance.interceptors.request.use((req) => {
  const accessToken = localStorage.getItem("access_token");
  if (accessToken) {
    req.headers.Authorization = `Bearer ${accessToken}`;
  }
  return req;
});

instance.interceptors.response.use(
  (res) => res,
  async (error) => {
    if (error.response.status === 401) {
      const refreshToken = store.state.auth.tokens.refreshToken;
      const response = await axios.post(`${URL}/refresh`, null, {
        headers: { Authorization: `Bearer ${refreshToken}` },
      });
      const accessToken = response.data.access_token;
      store.commit("auth/refreshToken", accessToken);
      error.config.headers.Authorization = `Bearer ${accessToken}`;
      return axios(error.config);
    } else {
      return Promise.reject(error);
    }
  }
);

export default instance;
