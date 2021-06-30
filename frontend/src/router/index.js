import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Category from "../views/Category.vue";
import ProductDetails from "../views/ProductDetails.vue";
import Search from "../views/Search.vue";
import Cart from "../views/Cart.vue";
import Checkout from "../views/Checkout.vue";
import CheckoutInformation from "../components/CheckoutInformation.vue";
import CheckoutShipping from "../components/CheckoutShipping.vue";
import CheckoutPayment from "../components/CheckoutPayment.vue";
import About from "../views/About.vue";
import Contact from "../views/Contact.vue";
import Registration from "../views/Registration.vue";
import Login from "../views/Login.vue";
import NotFound from "../views/NotFound.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/category/:id",
    name: "Category",
    component: Category,
  },
  {
    path: "/products/:id",
    name: "ProductDetails",
    component: ProductDetails,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/checkout",
    redirect: "/checkout/information",
    name: "Checkout",
    component: Checkout,
    children: [
      {
        path: "information",
        name: "CheckoutInformation",
        component: CheckoutInformation,
      },
      {
        path: "shipping",
        name: "CheckoutShipping",
        component: CheckoutShipping,
      },
      {
        path: "payment",
        name: "CheckoutPayment",
        component: CheckoutPayment,
      },
    ],
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/register",
    name: "Registration",
    component: Registration,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
