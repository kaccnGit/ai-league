<template>
  <div class="tools-page">
    <header class="page-header">
      <div>
        <p class="eyebrow">程序员效率中心</p>
        <h1>在线工具宇宙</h1>
        <p>集成 Base64、Hash、JSON、YAML、时间戳等高频工具，告别到处找小网站。</p>
      </div>
    </header>
    <section class="card tool-board">
      <div class="header">
        <h2 class="section-title">内置工具索引</h2>
        <p>选择任意工具进入二级页面，支持无限扩展</p>
      </div>
      <div class="index-grid">
        <article v-for="tool in builtinTools" :key="tool.id" class="index-card">
          <div class="card-head">
            <Icon :icon="tool.icon" />
            <div>
              <h3>{{ tool.name }}</h3>
              <p class="slogan">{{ tool.slogan }}</p>
            </div>
          </div>
          <p class="summary">{{ tool.description }}</p>
          <div class="tags">
            <el-tag v-for="tag in tool.tags" :key="tag" effect="plain" size="small">{{ tag }}</el-tag>
          </div>
          <el-button type="primary" @click="$router.push(`/tools/${tool.id}`)">打开工具</el-button>
        </article>
      </div>
    </section>
    <ToolList :tools="tools" :categories="categories" :loading="loading" @filter="handleFilter" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'
import ToolList from '@/components/ToolList.vue'
import { useCatalogStore } from '@/stores/catalog'
import { builtinTools } from '@/data/builtinTools'

const catalog = useCatalogStore()
const { tools, categories, loading } = storeToRefs(catalog)

const handleFilter = (params: Record<string, string | undefined>) => {
  const cleanParams = Object.fromEntries(
    Object.entries(params).filter(([, value]) => value)
  ) as Record<string, string>
  catalog.loadTools(cleanParams)
}

onMounted(async () => {
  if (!categories.value.length) {
    await catalog.loadCategories()
  }
  await catalog.loadTools()
})
</script>

<style scoped>
.page-header {
  margin-bottom: 1.5rem;
}
.eyebrow {
  font-size: 0.85rem;
  letter-spacing: 0.2rem;
  text-transform: uppercase;
  color: rgba(30, 30, 47, 0.5);
  margin-bottom: 0.4rem;
}
.tool-board {
  margin-bottom: 1.5rem;
}
.tool-board .header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tool-board .header p {
  margin: 0;
  color: rgba(30, 30, 47, 0.6);
}
.index-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}
.index-card {
  border: 1px solid rgba(106, 90, 224, 0.1);
  border-radius: 1rem;
  padding: 1.25rem;
  background: rgba(255, 255, 255, 0.95);
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  box-shadow: 0 14px 30px rgba(80, 82, 124, 0.12);
}
.card-head {
  display: flex;
  gap: 0.8rem;
  align-items: center;
}
.card-head svg {
  width: 32px;
  height: 32px;
  color: var(--accent-color);
}
.slogan {
  color: var(--accent-color);
  margin: 0;
  font-weight: 600;
}
.summary {
  margin: 0;
  color: rgba(30, 30, 47, 0.75);
}
.tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}
</style>
