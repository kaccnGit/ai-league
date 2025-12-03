import type { AIResource, Tool, ToolCategory } from '@/types'

export const fallbackCategories: ToolCategory[] = [
  { id: 'encode', title: '在线转码', description: 'Base64、URL、Hash 等快速转换', icon: 'carbon:code-reference' },
  { id: 'convert', title: '格式转换', description: 'JSON、YAML、Markdown、表格互转', icon: 'solar:transfer-horizontal-bold-duotone' },
  { id: 'media', title: '图片 & 多媒体', description: '压缩、裁剪、格式优化', icon: 'solar:image-bold-duotone' },
  { id: 'ops', title: '效率&运维', description: '正则测试、延迟探测、Webhook 调试', icon: 'ph:terminal-window-duotone' }
]

export const fallbackTools: Tool[] = [
  {
    id: 'base64-playground',
    name: 'Base64 Playground',
    description: '实时编码/解码、粘贴即得结果。',
    category: 'encode',
    tags: ['编码', '字符串'],
    url: 'https://base64.guru/converter/decode',
    featured: true
  },
  {
    id: 'json-format',
    name: 'JSON 格式化',
    description: '校验 JSON、比对差异、导出结果。',
    category: 'convert',
    tags: ['JSON', '格式化'],
    url: 'https://jsoncrack.com/editor',
    featured: true
  }
]

export const fallbackAIResources: AIResource[] = [
  {
    id: 'openai-gpt4o',
    name: 'GPT-4o',
    provider: 'OpenAI',
    category: '通用对话',
    description: '多模态旗舰模型，适合通用编码、问答与智能体。',
    docs_url: 'https://platform.openai.com/docs',
    console_url: 'https://platform.openai.com/playground',
    tags: ['高级', '多模态'],
    difficulty: '进阶',
    highlight: true
  }
]
