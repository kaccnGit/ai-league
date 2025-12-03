<template>
  <section class="interactive-card">
    <header>
      <h3>JSON 格式化 & 校验</h3>
      <p>粘贴 JSON 文本，一键格式化、压缩或校验结构。</p>
    </header>
    <el-input
      v-model="input"
      type="textarea"
      placeholder='{"hello":"world"}'
      :rows="6"
    />
    <div class="controls">
      <label>缩进</label>
      <el-input-number v-model="indent" :min="0" :max="8" />
    </div>
    <div class="actions">
      <el-button type="primary" @click="format('pretty')" :loading="loading" :disabled="!input">格式化</el-button>
      <el-button text @click="format('compact')" :loading="loading" :disabled="!input">压缩</el-button>
    </div>
    <el-input
      v-model="output"
      type="textarea"
      readonly
      placeholder="格式化结果"
      :rows="6"
    />
    <el-alert v-if="statusMessage" :type="statusType" :closable="false">
      {{ statusMessage }}
    </el-alert>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { formatJson } from '@/services/api'

const input = ref('')
const output = ref('')
const indent = ref(2)
const loading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')

const format = async (mode: 'pretty' | 'compact') => {
  if (!input.value) return
  loading.value = true
  statusMessage.value = ''
  try {
    const indentParam = mode === 'compact' ? 0 : indent.value
    const { data } = await formatJson({ payload: input.value, indent: indentParam })
    output.value = data.formatted
    statusType.value = 'success'
    statusMessage.value = `格式化成功，输出大小 ${data.size} 字节`
  } catch (err) {
    console.error(err)
    statusType.value = 'error'
    statusMessage.value = 'JSON 解析失败，请检查语法'
  } finally {
    loading.value = false
  }
}
</script>
