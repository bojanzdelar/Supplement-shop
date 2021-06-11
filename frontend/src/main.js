import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App);

const instance = axios.create({
  baseURL: "http://localhost:5000/api",
});

app.use(router);
app.config.globalProperties.axios = instance;
app.mount("#app");
