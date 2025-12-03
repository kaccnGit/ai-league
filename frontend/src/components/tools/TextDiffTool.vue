<template>
  <section class="interactive-card">
    <header>
      <h3>文本对比</h3>
      <p>快速比较两个片段差异，突出新增/删除行。</p>
    </header>
    <div class="diff-inputs">
      <div>
        <label>原文本</label>
        <el-input v-model="left" type="textarea" :rows="6" placeholder="粘贴旧版本内容" />
      </div>
      <div>
        <label>对比文本</label>
        <el-input v-model="right" type="textarea" :rows="6" placeholder="粘贴新版本内容" />
      </div>
    </div>
    <div class="actions">
      <el-button type="primary" @click="handleDiff" :loading="loading" :disabled="!left && !right">
        对比
      </el-button>
      <el-button text @click="clear">清空</el-button>
    </div>
    <div v-if="diff.length" class="diff-viewer">
      <p class="legend">
        <span class="added">新增</span>
        <span class="removed">删除</span>
        <span class="unchanged">未变化</span>
      </p>
      <ul>
        <li v-for="(line, index) in diff" :key="index" :class="line.type">
          <code>{{ prefix(line.type) }} {{ line.value || '·' }}</code>
        </li>
      </ul>
    </div>
    <p v-else-if="!loading" class="empty">暂无结果，先输入内容吧。</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { diffText } from '@/services/api'
import type { DiffLine } from '@/types'

const left = ref('')
const right = ref('')
const diff = ref<DiffLine[]>([])
const loading = ref(false)

const handleDiff = async () => {
  loading.value = true
  try {
    const { data } = await diffText({ left: left.value, right: right.value })
    diff.value = data.diff
  } catch (error) {
    console.error(error)
    diff.value = []
  } finally {
    loading.value = false
  }
}

const clear = () => {
  left.value = ''
  right.value = ''
  diff.value = []
}

const prefix = (type: DiffLine['type']) => {
  if (type === 'added') return '+'
  if (type === 'removed') return '-'
  return ' '
}
</script>

<style scoped>
.diff-inputs {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
.diff-viewer {
  border: 1px solid rgba(106, 90, 224, 0.15);
  border-radius: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.9);
  max-height: 260px;
  overflow: auto;
}
.diff-viewer ul {
  list-style: none;
  padding: 0;
  margin: 0;
  font-family: 'JetBrains Mono', Menlo, Consolas, monospace;
  font-size: 0.85rem;
}
.diff-viewer li {
  padding: 0.2rem 0.4rem;
  border-radius: 0.4rem;
  margin-bottom: 0.2rem;
}
.diff-viewer li code {
  background: transparent;
}
.diff-viewer li.added {
  background: rgba(52, 199, 89, 0.15);
  color: #20894d;
}
.diff-viewer li.removed {
  background: rgba(255, 99, 99, 0.15);
  color: #c0392b;
}
.diff-viewer li.unchanged {
  color: rgba(30, 30, 47, 0.7);
}
.legend {
  display: flex;
  gap: 0.5rem;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
}
.legend span {
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  font-weight: 600;
}
.legend .added {
  background: rgba(52, 199, 89, 0.15);
  color: #20894d;
}
.legend .removed {
  background: rgba(255, 99, 99, 0.15);
  color: #c0392b;
}
.legend .unchanged {
  background: rgba(30, 30, 47, 0.08);
}
.empty {
  color: rgba(30, 30, 47, 0.45);
  text-align: center;
}
</style>
