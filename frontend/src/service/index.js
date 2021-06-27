import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
  // headers: {"Authorization": `Bearer ${token}}
});

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

export default instance;
