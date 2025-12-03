<template>
  <section class="interactive-card">
    <header>
      <h3>JSON ⇆ YAML</h3>
      <p>开发常用格式互转，保持键顺序与中文可读性。</p>
    </header>
    <label>方向</label>
    <el-radio-group v-model="direction" size="small">
      <el-radio-button label="json_to_yaml">JSON → YAML</el-radio-button>
      <el-radio-button label="yaml_to_json">YAML → JSON</el-radio-button>
    </el-radio-group>
    <el-input
      v-model="input"
      type="textarea"
      placeholder="输入 JSON 或 YAML 内容"
      :rows="6"
    />
    <el-button type="primary" @click="handleConvert" :loading="loading" :disabled="!input">
      转换
    </el-button>
    <el-input
      v-model="output"
      type="textarea"
      readonly
      placeholder="转换结果"
      :rows="6"
    />
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { JsonYamlDirection } from '@/types'
import { convertJsonYaml } from '@/services/api'

const direction = ref<JsonYamlDirection>('json_to_yaml')
const input = ref('')
const output = ref('')
const loading = ref(false)
const error = ref('')

const handleConvert = async () => {
  if (!input.value) return
  loading.value = true
  error.value = ''
  try {
    const { data } = await convertJsonYaml({ payload: input.value, direction: direction.value })
    output.value = data.result
  } catch (err) {
    console.error(err)
    error.value = '转换失败，请检查输入格式'
  } finally {
    loading.value = false
  }
}
</script>
