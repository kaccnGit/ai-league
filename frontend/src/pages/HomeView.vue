<template>
  <div class="home">
    <HeroSection />
    <ToolCategoryGrid :categories="categories" />
    <section class="card" v-if="featuredTools.length">
      <div class="header">
        <h2 class="section-title">精选工具</h2>
        <RouterLink to="/tools">查看全部 →</RouterLink>
      </div>
      <div class="grid tool-grid">
        <article v-for="tool in featuredTools" :key="tool.id" class="tool-card">
          <h3>{{ tool.name }}</h3>
          <p>{{ tool.description }}</p>
          <div class="tags">
            <el-tag v-for="tag in tool.tags" :key="tag" size="small" effect="plain">{{ tag }}</el-tag>
          </div>
        </article>
      </div>
    </section>
    <section class="card">
      <div class="header">
        <h2 class="section-title">内置工具索引</h2>
        <RouterLink to="/tools">查看更多 →</RouterLink>
      </div>
      <div class="tool-index">
        <article v-for="tool in builtinPreview" :key="tool.id" class="index-item">
          <h3>{{ tool.name }}</h3>
          <p>{{ tool.slogan }}</p>
          <RouterLink :to="`/tools/${tool.id}`">进入工具 →</RouterLink>
        </article>
      </div>
    </section>
    <section class="card" v-if="highlightAI.length">
      <div class="header">
        <h2 class="section-title">AI 快速入口</h2>
        <RouterLink to="/ai">发现更多 →</RouterLink>
      </div>
      <div class="grid ai-grid">
        <article v-for="item in highlightAI" :key="item.id" class="ai-card highlight">
          <p class="badge">{{ item.provider }}</p>
          <h3>{{ item.name }}</h3>
          <p>{{ item.description }}</p>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import HeroSection from '@/components/HeroSection.vue'
import ToolCategoryGrid from '@/components/ToolCategoryGrid.vue'
import { useCatalogStore } from '@/stores/catalog'
import { RouterLink } from 'vue-router'
import { builtinTools } from '@/data/builtinTools'

const catalog = useCatalogStore()
const { categories, tools, aiResources } = storeToRefs(catalog)

const featuredTools = computed(() => tools.value.filter((tool) => tool.featured))
const highlightAI = computed(() => aiResources.value.filter((item) => item.highlight))
const builtinPreview = computed(() => builtinTools.slice(0, 4))

onMounted(() => {
  catalog.bootstrap()
})
</script>

<style scoped>
.tool-grid {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}
.ai-grid {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}
.tool-card,
.ai-card {
  background: #fff;
  border: 1px solid rgba(106, 90, 224, 0.12);
  padding: 1.25rem;
  border-radius: 1rem;
}
.tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tool-index {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}
.index-item {
  border: 1px solid rgba(106, 90, 224, 0.12);
  border-radius: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.9);
}
.index-item p {
  color: rgba(30, 30, 47, 0.75);
}
</style>
