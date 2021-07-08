import { createRouter, createWebHistory } from "vue-router";
import store from "../store/index.js";

const routes = [
  {
    path: "/",
    name: "Buyer",
    component: () => import("../views/Buyer.vue"),
    children: [
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
        meta: { requiresAuth: true },
      },
      {
        path: "/account/register",
        name: "Registration",
        component: () => import("../views/Registration.vue"),
        meta: { requiresGuest: true },
      },
      {
        path: "/account/login",
        name: "Login",
        component: () => import("../views/Login.vue"),
        meta: { requiresGuest: true },
      },
      {
        path: "/account/orders",
        name: "Orders",
        component: () => import("../views/Orders.vue"),
        meta: { requiresAuth: true },
      },
      {
        path: "/account/addresses",
        name: "Addresses",
        component: () => import("../views/Addresses.vue"),
        meta: { requiresAuth: true },
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
    ],
  },
  {
    path: "/dashboard",
    redirect: "/dashboard/orders",
    name: "Dashboard",
    component: () => import("../views/Dashboard.vue"),
    meta: { requiresAdmin: true },
    children: [
      {
        path: "/dashboard/orders",
        name: "DashboardOrders",
        component: () => import("../views/DashboardOrders.vue"),
      },
      {
        path: "/dashboard/products",
        name: "DashboardProducts",
        component: () => import("../views/DashboardProducts.vue"),
      },
      {
        path: "/dashboard/categories",
        name: "DashboardCategories",
        component: () => import("../views/DashboardCategories.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to) => {
  if (
    (to.meta.requiresAuth || to.meta.requiresAdmin) &&
    !store.state.auth.logged
  ) {
    return "/account/login";
  } else if (
    (to.meta.requiresAdmin || to.meta.requiresGuest) &&
    store.state.auth.logged
  ) {
    return "/";
  }
});

export default router;
