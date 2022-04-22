import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import MessagesView from "../pages/MessagesView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import MomentsView from "../views/MomentsView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/square",
    name: "square",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/SquareView.vue"),
  },
  {
    path: "/messages",
    name: "messages",
    component: MessagesView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/moments",
    name: "moments",
    component: MomentsView,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
