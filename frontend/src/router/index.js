import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/category/:id",
    name: "Category",
    component: () => import("../views/Category.vue"),
  },
  {
    path: "/products/:id",
    name: "ProductDetails",
    component: () => import("../views/ProductDetails.vue"),
  },
  {
    path: "/search",
    name: "Search",
    component: () => import("../views/Search.vue"),
  },
  {
    path: "/cart",
    name: "Cart",
    component: () => import("../views/ProductDetails.vue"),
  },
  {
    path: "/checkout",
    redirect: "/checkout/information",
    name: "Checkout",
    component: () => import("../views/Checkout.vue"),
    children: [
      {
        path: "information",
        name: "CheckoutInformation",
        component: () => import("../views/CheckoutInformation.vue"),
      },
      {
        path: "shipping",
        name: "CheckoutShipping",
        component: () => import("../views/CheckoutShipping.vue"),
      },
      {
        path: "payment",
        name: "CheckoutPayment",
        component: () => import("../views/CheckoutPayment.vue"),
      },
    ],
  },
  {
    path: "/account",
    name: "Account",
    component: () => import("../views/Account.vue"),
  },
  {
    path: "/account/register",
    name: "Registration",
    component: () => import("../views/Registration.vue"),
  },
  {
    path: "/account/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/account/orders",
    name: "Orders",
    component: () => import("../views/Orders.vue"),
  },
  {
    path: "/account/addresses",
    name: "Addresses",
    component: () => import("../views/Addresses.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
  {
    path: "/contact",
    name: "Contact",
    component: () => import("../views/Contact.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../views/NotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
