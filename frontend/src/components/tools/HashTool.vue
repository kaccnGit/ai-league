<template>
  <section class="interactive-card">
    <header>
      <h3>Hash 摘要计算</h3>
      <p>支持 MD5 / SHA 家族算法，可快速校验文件或字符串。</p>
    </header>
    <label>算法</label>
    <el-select v-model="algorithm" placeholder="选择算法">
      <el-option v-for="option in algorithmOptions" :key="option.value" :label="option.label" :value="option.value" />
    </el-select>
    <el-input
      v-model="input"
      type="textarea"
      placeholder="输入需要计算 Hash 的内容"
      :rows="4"
    />
    <el-button type="primary" @click="handleHash" :loading="loading" :disabled="!input">
      计算
    </el-button>
    <div class="result-block" v-if="result">
      <label>结果</label>
      <code>{{ result }}</code>
    </div>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { HashAlgorithm } from '@/types'
import { runHash } from '@/services/api'

const algorithm = ref<HashAlgorithm>('md5')
const algorithmOptions = [
  { label: 'MD5', value: 'md5' },
  { label: 'SHA-1', value: 'sha1' },
  { label: 'SHA-256', value: 'sha256' },
  { label: 'SHA-512', value: 'sha512' }
]
const input = ref('')
const result = ref('')
const loading = ref(false)
const error = ref('')

const handleHash = async () => {
  if (!input.value) return
  loading.value = true
  error.value = ''
  try {
    const { data } = await runHash({ payload: input.value, algorithm: algorithm.value })
    result.value = data.hash
  } catch (err) {
    console.error(err)
    error.value = 'Hash 计算失败'
  } finally {
    loading.value = false
  }
}
</script>
