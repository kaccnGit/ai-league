import { defineStore } from 'pinia'
import type { AIResource, Tool, ToolCategory } from '@/types'
import { fetchAIResources, fetchToolCategories, fetchTools } from '@/services/api'
import { fallbackAIResources, fallbackCategories, fallbackTools } from '@/data/fallback'

interface CatalogState {
  tools: Tool[]
  categories: ToolCategory[]
  aiResources: AIResource[]
  loading: boolean
  error: string | null
}

export const useCatalogStore = defineStore('catalog', {
  state: (): CatalogState => ({
    tools: [],
    categories: [],
    aiResources: [],
    loading: false,
    error: null
  }),
  actions: {
    async bootstrap() {
      if (this.categories.length === 0) {
        await this.loadCategories()
      }
      if (this.tools.length === 0) {
        await this.loadTools()
      }
      if (this.aiResources.length === 0) {
        await this.loadAIResources()
      }
    },
    async loadTools(params?: Record<string, string>) {
      this.loading = true
      try {
        const { data } = await fetchTools(params)
        this.tools = data
      } catch (error) {
        this.error = '无法加载工具列表，已降级到内置数据'
        console.error(error)
        this.tools = fallbackTools
      } finally {
        this.loading = false
      }
    },
    async loadCategories() {
      try {
        const { data } = await fetchToolCategories()
        this.categories = data
      } catch (error) {
        console.error(error)
        this.categories = fallbackCategories
      }
    },
    async loadAIResources(params?: Record<string, string>) {
      this.loading = true
      try {
        const { data } = await fetchAIResources(params)
        this.aiResources = data
      } catch (error) {
        this.error = '无法加载 AI 资源，已使用本地数据'
        console.error(error)
        this.aiResources = fallbackAIResources
      } finally {
        this.loading = false
      }
    }
  }
})
