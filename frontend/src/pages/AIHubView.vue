<template>
  <div class="ai-page">
    <header class="page-header">
      <div>
        <h1>AI 模型集锦</h1>
        <p>覆盖国内外主流大模型，附带入门链接与控制台入口</p>
      </div>
    </header>
    <AIResourceGrid :resources="resources" @filter="handleFilter" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import AIResourceGrid from '@/components/AIResourceGrid.vue'
import { useCatalogStore } from '@/stores/catalog'

const catalog = useCatalogStore()
const { aiResources: resources } = storeToRefs(catalog)

const handleFilter = (params: Record<string, string | undefined>) => {
  const cleanParams = Object.fromEntries(
    Object.entries(params).filter(([, value]) => value)
  ) as Record<string, string>
  catalog.loadAIResources(cleanParams)
}

onMounted(() => {
  if (!resources.value.length) {
    catalog.loadAIResources()
  }
})
</script>

<style scoped>
.page-header {
  margin-bottom: 1.5rem;
}
</style>
