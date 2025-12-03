<template>
  <section class="card">
    <div class="header">
      <h2 class="section-title">工具分类</h2>
      <p>快速定位常用工具类型</p>
    </div>
    <div class="grid categories">
      <article v-for="category in categories" :key="category.id" class="category-card">
        <h3>
          <Icon :icon="category.icon ?? 'solar:folder-with-files-bold-duotone'" />
          {{ category.title }}
        </h3>
        <p>{{ category.description }}</p>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { ToolCategory } from '@/types'
import { Icon } from '@iconify/vue'

interface Props {
  categories: ToolCategory[]
}

defineProps<Props>()
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.categories {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}
.category-card {
  padding: 1rem;
  border-radius: 1rem;
  background: #fff;
  border: 1px solid rgba(106, 90, 224, 0.12);
  box-shadow: 0 10px 30px rgba(101, 119, 166, 0.15);
}
.category-card h3 {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
</style>
