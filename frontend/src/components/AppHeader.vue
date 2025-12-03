<template>
  <header class="app-header">
    <div class="brand">
      <span class="logo">⚡</span>
      <div>
        <p class="title">AI League</p>
        <p class="subtitle">程序员效率宇宙</p>
      </div>
    </div>
    <nav :class="['nav-links', { open: mobileMenu }]">
      <RouterLink to="/" @click="closeMenu">首页</RouterLink>
      <RouterLink to="/tools" @click="closeMenu">工具集</RouterLink>
      <RouterLink to="/ai" @click="closeMenu">AI 集锦</RouterLink>
    </nav>
    <button class="nav-toggle" @click="mobileMenu = !mobileMenu">
      <span />
      <span />
      <span />
    </button>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const mobileMenu = ref(false)
const closeMenu = () => {
  mobileMenu.value = false
}
</script>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(106, 90, 224, 0.15);
  position: sticky;
  top: 0;
  backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.9);
  z-index: 20;
}
.brand {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}
.logo {
  font-size: 1.65rem;
}
.title {
  font-weight: 700;
  margin: 0;
}
.subtitle {
  margin: 0;
  font-size: 0.75rem;
  opacity: 0.7;
}
.nav-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}
.nav-links a {
  font-weight: 500;
  color: inherit;
}
.nav-links a.router-link-active {
  color: var(--accent-color);
  font-weight: 600;
}
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 0.2rem;
  background: none;
  border: none;
  cursor: pointer;
}
.nav-toggle span {
  width: 1.5rem;
  height: 2px;
  background: currentColor;
}

@media (max-width: 720px) {
  .nav-links {
    position: absolute;
    top: 64px;
    right: 1rem;
    flex-direction: column;
    background: rgba(255, 255, 255, 0.95);
    padding: 1rem;
    border-radius: 0.75rem;
    box-shadow: 0 10px 40px rgba(23, 32, 90, 0.15);
    display: none;
  }
  .nav-links.open {
    display: flex;
  }
  .nav-toggle {
    display: flex;
  }
}
</style>
