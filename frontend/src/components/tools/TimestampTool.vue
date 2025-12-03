<template>
  <section class="interactive-card">
    <header>
      <h3>时间戳转换</h3>
      <p>在 Unix 时间戳和人类可读的 ISO 时间之间互转，默认使用本地时区。</p>
    </header>
    <div class="dual-columns">
      <div class="column">
        <label>Unix 时间戳</label>
        <el-input-number v-model="unixValue" placeholder="例如 1714540800" :controls="false" />
        <el-button text @click="convertUnix" :loading="loading">转换为时间</el-button>
      </div>
      <div class="column">
        <label>ISO 时间</label>
        <el-input v-model="isoValue" placeholder="2024-05-01T12:00:00+08:00" />
        <el-button text @click="convertIso" :loading="loading">转换为时间戳</el-button>
      </div>
    </div>
    <el-alert type="success" v-if="result.human" :closable="false">
      ISO 时间：{{ result.human }}<br />
      Unix：{{ result.unix }}
    </el-alert>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { runTimestamp } from '@/services/api'

const unixValue = ref<number | null>(null)
const isoValue = ref('')
const loading = ref(false)
const error = ref('')
const result = ref({ human: '', unix: 0 })

const convertUnix = async () => {
  if (unixValue.value === null) return
  loading.value = true
  error.value = ''
  try {
    const { data } = await runTimestamp({
      mode: 'unix_to_human',
      value: String(unixValue.value)
    })
    result.value = data
    isoValue.value = data.human
  } catch (err) {
    console.error(err)
    error.value = '转换失败，请检查时间戳'
  } finally {
    loading.value = false
  }
}

const convertIso = async () => {
  if (!isoValue.value) return
  loading.value = true
  error.value = ''
  try {
    const { data } = await runTimestamp({
      mode: 'human_to_unix',
      value: isoValue.value
    })
    result.value = data
    unixValue.value = data.unix
  } catch (err) {
    console.error(err)
    error.value = '请按照 ISO 8601 格式输入时间'
  } finally {
    loading.value = false
  }
}
</script>
