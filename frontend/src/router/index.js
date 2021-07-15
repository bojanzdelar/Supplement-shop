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
        meta: {
          title: "Home page",
        },
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
        meta: {
          title: "Search",
        },
      },
      {
        path: "/cart",
        name: "Cart",
        component: () => import("../views/Cart.vue"),
        meta: {
          title: "Cart",
        },
      },
      {
        path: "/account",
        name: "Account",
        component: () => import("../views/Account.vue"),
        meta: {
          requiresAuth: true,
          title: "Account",
        },
      },
      {
        path: "/account/register",
        name: "Registration",
        component: () => import("../views/Registration.vue"),
        meta: {
          requiresGuest: true,
          title: "Registration",
        },
      },
      {
        path: "/account/login",
        name: "Login",
        component: () => import("../views/Login.vue"),
        meta: {
          requiresGuest: true,
          title: "Login",
        },
      },
      {
        path: "/account/orders",
        name: "Orders",
        component: () => import("../views/Orders.vue"),
        meta: {
          requiresAuth: true,
          title: "Orders",
        },
      },
      {
        path: "/account/addresses",
        name: "Addresses",
        component: () => import("../views/Addresses.vue"),
        meta: {
          requiresAuth: true,
          title: "Addresses",
        },
      },
      {
        path: "/about",
        name: "About",
        component: () => import("../views/About.vue"),
        meta: {
          title: "About",
        },
      },
      {
        path: "/contact",
        name: "Contact",
        component: () => import("../views/Contact.vue"),
        meta: {
          title: "Contact",
        },
      },
      {
        path: "/:pathMatch(.*)*",
        name: "NotFound",
        component: () => import("../views/NotFound.vue"),
      },
    ],
  },
  {
    path: "/checkout",
    redirect: "/checkout/information",
    name: "Checkout",
    component: () => import("../views/Checkout.vue"),
    beforeEnter: () => {
      if (store.getters["cart/isEmpty"]) return "/";
    },
    children: [
      {
        path: "information",
        name: "CheckoutInformation",
        component: () => import("../views/CheckoutInformation.vue"),
        meta: {
          title: "Checkout - Information",
        },
      },
      {
        path: "shipping",
        name: "CheckoutShipping",
        component: () => import("../views/CheckoutShipping.vue"),
        beforeEnter: () => {
          if (
            !store.state.checkout.shippingAddress ||
            !store.state.checkout.shippingAddress.complete
          )
            return "/checkout/information";
        },
        meta: {
          title: "Checkout - Shipping",
        },
      },
      {
        path: "payment",
        name: "CheckoutPayment",
        component: () => import("../views/CheckoutPayment.vue"),
        beforeEnter: () => {
          if (!store.state.checkout.shippingMethod) return "/checkout/shipping";
        },
        meta: {
          title: "Checkout - Payment",
        },
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
        meta: {
          title: "Dashboard - orders",
        },
      },
      {
        path: "/dashboard/products",
        name: "DashboardProducts",
        component: () => import("../views/DashboardProducts.vue"),
        meta: {
          title: "Dashboard - products",
        },
      },
      {
        path: "/dashboard/categories",
        name: "DashboardCategories",
        component: () => import("../views/DashboardCategories.vue"),
        meta: {
          title: "Dashboard - categories",
        },
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
    (to.meta.requiresGuest && store.state.auth.logged) ||
    (to.meta.requiresAdmin && !store.state.auth.isAdmin)
  ) {
    return "/";
  }
});

router.beforeEach((to) => {
  document.title = process.env.VUE_APP_TITLE;
  if (to.meta.title) {
    document.title += ` - ${to.meta.title}`;
  }
});

export default router;
