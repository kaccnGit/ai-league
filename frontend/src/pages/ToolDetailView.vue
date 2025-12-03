<template>
  <div class="tool-detail" v-if="tool">
    <section class="card hero">
      <div>
        <p class="eyebrow">AI League · 内置工具</p>
        <h1>{{ tool.name }}</h1>
        <p class="slogan">{{ tool.slogan }}</p>
        <p class="desc">{{ tool.description }}</p>
        <div class="tags">
          <el-tag v-for="tag in tool.tags" :key="tag" effect="light">{{ tag }}</el-tag>
        </div>
      </div>
      <el-button link type="primary" @click="$router.push('/tools')">← 返回工具索引</el-button>
    </section>
    <component :is="toolComponent" v-if="toolComponent" />
  </div>
  <div v-else class="tool-detail">
    <section class="card hero">
      <h1>工具不存在</h1>
      <p>请检查链接是否正确，或回到索引重新选择。</p>
      <el-button type="primary" @click="$router.push('/tools')">前往工具索引</el-button>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { defineAsyncComponent } from 'vue'
import { getBuiltinTool } from '@/data/builtinTools'

const route = useRoute()

const tool = computed(() => getBuiltinTool(route.params.toolId as string))

const toolComponent = computed(() => {
  if (!tool.value) return null
  return defineAsyncComponent(tool.value.component)
})
</script>

<style scoped>
.tool-detail {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.hero {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}
.eyebrow {
  font-size: 0.85rem;
  letter-spacing: 0.2rem;
  text-transform: uppercase;
  color: rgba(30, 30, 47, 0.5);
}
.slogan {
  font-size: 1.2rem;
  color: var(--accent-color);
}
.desc {
  color: rgba(30, 30, 47, 0.75);
}
.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
</style>
