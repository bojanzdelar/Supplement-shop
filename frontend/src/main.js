import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App);

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
});

instance.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  req.headers.Authorization = `Bearer ${token}`;
  return req;
});

app.use(router);
app.config.globalProperties.axios = instance;
app.mount("#app");

// instance.interceptors.request.use((config) => {
//   let token = localStorage.getItem("token");
//   Object.assign(config.headers, { Authorization: `Bearer ${token}` });
//   return config;
// });
