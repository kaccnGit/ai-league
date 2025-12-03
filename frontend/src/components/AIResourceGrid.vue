<template>
  <section class="card">
    <div class="filters">
      <el-select v-model="provider" placeholder="厂商" clearable filterable>
        <el-option v-for="option in providerOptions" :key="option.value" :label="option.label" :value="option.value" />
      </el-select>
      <el-select v-model="category" placeholder="类别" clearable filterable>
        <el-option v-for="option in categoryOptions" :key="option.value" :label="option.label" :value="option.value" />
      </el-select>
      <el-select v-model="difficulty" placeholder="难度" clearable>
        <el-option
          v-for="option in difficultyOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </el-select>
      <el-button plain @click="applyFilter">筛选</el-button>
    </div>
    <div v-if="resources.length" class="grid ai-grid">
      <article v-for="item in resources" :key="item.id" class="ai-card" :class="{ highlight: item.highlight }">
        <small class="badge">{{ item.provider }} · {{ item.category }}</small>
        <h3>{{ item.name }}</h3>
        <p>{{ item.description }}</p>
        <div class="tags">
          <el-tag v-for="tag in item.tags" :key="tag" size="small" effect="plain">{{ tag }}</el-tag>
        </div>
        <div class="links">
          <a :href="item.docs_url" target="_blank">文档</a>
          <a v-if="item.console_url" :href="item.console_url" target="_blank">控制台</a>
        </div>
      </article>
    </div>
    <p v-else class="empty">暂无数据，可尝试更换筛选条件</p>
  </section>
</template>

<script setup lang="ts">
import type { AIResource } from '@/types'
import { computed, ref } from 'vue'

interface Props {
  resources: AIResource[]
}

const props = defineProps<Props>()
const emit = defineEmits<{
  filter: [{ provider?: string; category?: string; difficulty?: string }]
}>()

const provider = ref<string | null>(null)
const category = ref<string | null>(null)
const difficulty = ref<string | null>(null)

const providerOptions = computed(() =>
  Array.from(new Set(props.resources.map((item) => item.provider))).map((label) => ({ label, value: label }))
)
const categoryOptions = computed(() =>
  Array.from(new Set(props.resources.map((item) => item.category))).map((label) => ({ label, value: label }))
)
const difficultyOptions = [
  { label: '入门', value: '入门' },
  { label: '进阶', value: '进阶' },
  { label: '实验', value: '实验' }
]

const applyFilter = () => {
  emit('filter', {
    provider: provider.value || undefined,
    category: category.value || undefined,
    difficulty: difficulty.value || undefined
  })
}
</script>

<style scoped>
.filters {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}
.filters :deep(.el-select) {
  min-width: 180px;
}
.filters :deep(.el-button) {
  align-self: center;
}
.ai-grid {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}
ai-card,
.ai-card {
  border-radius: 1.2rem;
  background: #fff;
  border: 1px solid rgba(106, 90, 224, 0.12);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.ai-card.highlight {
  border-color: rgba(106, 90, 224, 0.55);
  box-shadow: 0 20px 40px rgba(106, 90, 224, 0.2);
}
.badge {
  color: rgba(30, 30, 47, 0.6);
}
.tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}
.links {
  display: flex;
  gap: 1rem;
}
.links a {
  color: var(--accent-color);
}
.empty {
  text-align: center;
  color: rgba(30, 30, 47, 0.55);
}
</style>
