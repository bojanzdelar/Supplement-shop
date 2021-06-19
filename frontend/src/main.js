import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios";
import router from "./router";
import mitt from "mitt";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

const app = createApp(App);

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
});

instance.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  req.headers.Authorization = `Bearer ${token}`;
  return req;
});

const emitter = mitt();

app.use(router);
app.config.globalProperties.axios = instance;
app.config.globalProperties.emitter = emitter;
app.mount("#app");
