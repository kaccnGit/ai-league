<template>
  <section class="interactive-card">
    <header>
      <h3>Base64 编解码</h3>
      <p>快速对文本进行 Base64 编码或解码，支持中文与多语言。</p>
    </header>
    <div class="controls">
      <label>模式</label>
      <el-radio-group v-model="mode" size="small">
        <el-radio-button label="encode">编码</el-radio-button>
        <el-radio-button label="decode">解码</el-radio-button>
      </el-radio-group>
    </div>
    <el-input
      v-model="input"
      type="textarea"
      placeholder="粘贴原始文本..."
      :rows="4"
    />
    <div class="actions">
      <el-button type="primary" @click="handleTransform" :loading="loading" :disabled="!input">
        执行
      </el-button>
      <el-button text @click="clearAll">清空</el-button>
    </div>
    <el-input
      v-model="output"
      type="textarea"
      readonly
      placeholder="结果将在此展示"
      :rows="4"
    />
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Base64Mode } from '@/types'
import { runBase64 } from '@/services/api'

const input = ref('')
const output = ref('')
const mode = ref<Base64Mode>('encode')
const loading = ref(false)
const error = ref('')

const handleTransform = async () => {
  if (!input.value) return
  loading.value = true
  error.value = ''
  try {
    const { data } = await runBase64({ payload: input.value, mode: mode.value })
    output.value = data.result
  } catch (err) {
    console.error(err)
    error.value = '转换失败，请确认输入内容是否正确'
  } finally {
    loading.value = false
  }
}

const clearAll = () => {
  input.value = ''
  output.value = ''
  error.value = ''
}
</script>
