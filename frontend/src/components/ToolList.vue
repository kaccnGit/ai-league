<template>
  <section class="card tool-list">
    <div class="filters">
      <el-input v-model="keywords" placeholder="搜索工具 / 标签" clearable />
      <el-select v-model="currentCategory" placeholder="选择分类" clearable filterable>
        <el-option
          v-for="option in categoryOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </el-select>
      <el-button plain @click="emitFilter">应用</el-button>
    </div>
    <div v-if="loading" class="skeleton-list">
      <el-skeleton
        v-for="i in 4"
        :key="i"
        animated
        :rows="3"
        class="skeleton-item"
      />
    </div>
    <div v-else-if="tools.length" class="grid tool-grid">
      <article v-for="tool in tools" :key="tool.id" class="tool-card">
        <div class="tool-head">
          <h3>{{ tool.name }}</h3>
          <el-tag size="small" type="info" effect="light">{{ tool.category }}</el-tag>
        </div>
        <p>{{ tool.description }}</p>
        <div class="tags">
          <el-tag v-for="tag in tool.tags" :key="tag" size="small" effect="plain">{{ tag }}</el-tag>
        </div>
        <a :href="tool.url" target="_blank" rel="noreferrer">立即前往 →</a>
      </article>
    </div>
    <p v-else class="empty">暂无符合条件的工具</p>
  </section>
</template>

<script setup lang="ts">
import type { Tool, ToolCategory } from '@/types'
import { computed, ref } from 'vue'

interface Props {
  tools: Tool[]
  categories: ToolCategory[]
  loading?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  filter: [{ q?: string; category?: string }]
}>()

const keywords = ref('')
const currentCategory = ref<string | null>(null)

const categoryOptions = computed(() =>
  props.categories.map((cat) => ({ label: cat.title, value: cat.id }))
)

const emitFilter = () => {
  emit('filter', { q: keywords.value || undefined, category: currentCategory.value || undefined })
}
</script>

<style scoped>
.filters {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}
.filters :deep(.el-input),
.filters :deep(.el-select) {
  min-width: 200px;
}
.filters :deep(.el-button) {
  align-self: center;
}
.tool-grid {
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}
.tool-card {
  background: #fff;
  border-radius: 1rem;
  padding: 1.25rem;
  border: 1px solid rgba(106, 90, 224, 0.12);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.tool-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}
.tool-card a {
  color: var(--accent-color);
  font-weight: 600;
  margin-top: auto;
}
.skeleton-list {
  display: grid;
  gap: 1rem;
}
.skeleton-item {
  border-radius: 1rem;
  padding: 1rem;
  border: 1px solid rgba(106, 90, 224, 0.08);
}
.empty {
  text-align: center;
  color: rgba(30, 30, 47, 0.5);
}
</style>
