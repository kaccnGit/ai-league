import { createRouter, createWebHistory } from 'vue-router'

const HomeView = () => import('@/pages/HomeView.vue')
const ToolsView = () => import('@/pages/ToolsView.vue')
const ToolDetailView = () => import('@/pages/ToolDetailView.vue')
const AIHubView = () => import('@/pages/AIHubView.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/tools', component: ToolsView },
    { path: '/tools/:toolId', component: ToolDetailView },
    { path: '/ai', component: AIHubView }
  ],
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router
