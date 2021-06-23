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

const emitter = mitt();

instance.interceptors.request.use((req) => {
  const access_token = localStorage.getItem("access_token");
  req.headers.Authorization = `Bearer ${access_token}`;
  return req;
});

// instance.interceptors.response.use(
//   (res) => res,
//   (error) => {
//     if (error.response.data.msg == "Token has expired") {
//       emitter.emit("loggedOut"); // FIXME: should refresh token and log out only if refresh token has expired
//     }
//     return error;
//   }
// );

app.use(router);
app.config.globalProperties.axios = instance;
app.config.globalProperties.emitter = emitter;
app.mount("#app");
