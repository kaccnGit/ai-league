<template>
  <div class="app-shell">
    <AppHeader />
    <main>
      <router-view />
    </main>
    <FooterBar />
  </div>
</template>

<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import FooterBar from '@/components/FooterBar.vue'
</script>
