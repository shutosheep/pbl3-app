import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Search from "../components/Search.vue";
import Info from "../components/Info.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/search",
    name: "search",
    component: Search,
  },
  {
    path: "/info",
    name: "info",
    component: Info,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
