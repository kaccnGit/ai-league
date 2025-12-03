<template>
  <section class="interactive-card">
    <header>
      <h3>色值转换</h3>
      <p>支持 Hex / RGB / HSL 互转，同时提供实时预览。</p>
    </header>
    <div class="color-inputs">
      <el-input v-model="colorValue" placeholder="#6a5ae0 或 rgb(106,90,224)" clearable />
      <el-color-picker v-model="pickerValue" @change="handlePickerChange" />
    </div>
    <div class="actions">
      <el-button type="primary" @click="handleConvert" :loading="loading" :disabled="!colorValue">
        立即转换
      </el-button>
      <el-button text @click="reset">重置</el-button>
    </div>
    <el-card v-if="result" shadow="hover" class="result-card">
      <p><strong>Hex：</strong>{{ result.hex }}</p>
      <p><strong>RGB：</strong>{{ result.rgb }}</p>
      <p><strong>HSL：</strong>{{ result.hsl }}</p>
    </el-card>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { convertColor } from '@/services/api'
import type { ColorConvertResponsePayload } from '@/types'

const colorValue = ref('#6a5ae0')
const pickerValue = ref('#6a5ae0')
const result = ref<ColorConvertResponsePayload | null>(null)
const loading = ref(false)
const error = ref('')

const handlePickerChange = (value: string) => {
  if (value) {
    colorValue.value = value
  }
}

const handleConvert = async () => {
  if (!colorValue.value) {
    return
  }
  loading.value = true
  error.value = ''
  try {
    const { data } = await convertColor({ value: colorValue.value })
    result.value = data
    pickerValue.value = data.hex
  } catch (err) {
    console.error(err)
    error.value = '无法识别该色值，请检查格式'
    result.value = null
  } finally {
    loading.value = false
  }
}

const reset = () => {
  colorValue.value = '#6a5ae0'
  pickerValue.value = '#6a5ae0'
  result.value = null
  error.value = ''
}
</script>

<style scoped>
.color-inputs {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.color-inputs :deep(.el-color-picker) {
  margin-left: auto;
}
.result-card {
  background: rgba(106, 90, 224, 0.05);
  border: 1px dashed rgba(106, 90, 224, 0.4);
}
</style>
