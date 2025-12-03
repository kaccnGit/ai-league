import axios from 'axios'
import type {
  Base64RequestPayload,
  Base64ResponsePayload,
  ColorConvertPayload,
  ColorConvertResponsePayload,
  HashRequestPayload,
  HashResponsePayload,
  JsonFormatPayload,
  JsonFormatResponsePayload,
  JsonYamlPayload,
  JsonYamlResponsePayload,
  TextDiffPayload,
  TextDiffResponsePayload,
  TimestampRequestPayload,
  TimestampResponsePayload
} from '@/types'

const baseURL = import.meta.env.VITE_API_BASE ?? '/api'

export const api = axios.create({
  baseURL,
  timeout: 8000
})

export const fetchTools = (params?: Record<string, string>) => api.get('/tools', { params })
export const fetchToolCategories = () => api.get('/tools/categories')
export const fetchAIResources = (params?: Record<string, string>) => api.get('/ai', { params })
export const runBase64 = (payload: Base64RequestPayload) => api.post<Base64ResponsePayload>('/utils/base64', payload)
export const runHash = (payload: HashRequestPayload) => api.post<HashResponsePayload>('/utils/hash', payload)
export const runTimestamp = (payload: TimestampRequestPayload) => api.post<TimestampResponsePayload>('/utils/timestamp', payload)
export const formatJson = (payload: JsonFormatPayload) => api.post<JsonFormatResponsePayload>('/utils/json/format', payload)
export const convertJsonYaml = (payload: JsonYamlPayload) => api.post<JsonYamlResponsePayload>('/utils/json-yaml', payload)
export const convertColor = (payload: ColorConvertPayload) => api.post<ColorConvertResponsePayload>('/utils/color/convert', payload)
export const diffText = (payload: TextDiffPayload) => api.post<TextDiffResponsePayload>('/utils/text/diff', payload)
