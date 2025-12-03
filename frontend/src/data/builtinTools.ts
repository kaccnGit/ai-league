export interface BuiltinTool {
  id: string
  name: string
  slogan: string
  description: string
  tags: string[]
  icon: string
  component: () => Promise<any>
}

export const builtinTools: BuiltinTool[] = [
  {
    id: 'color-converter',
    name: '颜色编码转换',
    slogan: 'Hex / RGB / HSL 一键互转',
    description: '支持拾色器输入及各色值制式互转，快速拷贝色值。',
    tags: ['颜色', '设计'],
    icon: 'solar:palette-linear',
    component: () => import('@/components/tools/ColorConverter.vue')
  },
  {
    id: 'json-formatter',
    name: 'JSON 格式化',
    slogan: '校验 + 格式化 + 压缩',
    description: '内置格式化/压缩选项与字节统计，方便开发调试。',
    tags: ['JSON', '格式化'],
    icon: 'ph:brackets-curly-bold',
    component: () => import('@/components/tools/JsonFormatter.vue')
  },
  {
    id: 'json-yaml',
    name: 'JSON ⇆ YAML',
    slogan: '保持键顺序与中文可读',
    description: '适合在配置文件与接口入参之间快速互转。',
    tags: ['配置', 'YAML'],
    icon: 'mdi:code-json',
    component: () => import('@/components/tools/JsonYamlTool.vue')
  },
  {
    id: 'base64',
    name: 'Base64 编解码',
    slogan: '支持中文与多语言',
    description: '粘贴即得结果，常用编码场景开箱即用。',
    tags: ['编码'],
    icon: 'ph:code-bold',
    component: () => import('@/components/tools/Base64Tool.vue')
  },
  {
    id: 'hash',
    name: 'Hash 计算',
    slogan: 'MD5 / SHA 系列',
    description: '校验签名、比对文件，提供常见 Hash 算法。',
    tags: ['安全', '校验'],
    icon: 'mdi:shield-lock-outline',
    component: () => import('@/components/tools/HashTool.vue')
  },
  {
    id: 'timestamp',
    name: '时间戳转换',
    slogan: 'Unix ↔ ISO8601',
    description: '自动适配本地时区，适合排查时间问题。',
    tags: ['时间'],
    icon: 'solar:clock-circle-linear',
    component: () => import('@/components/tools/TimestampTool.vue')
  },
  {
    id: 'text-diff',
    name: '文本对比',
    slogan: '行级差异高亮',
    description: '突出新增/删除/未变行，方便快速对比文本。',
    tags: ['Diff'],
    icon: 'mdi:compare',
    component: () => import('@/components/tools/TextDiffTool.vue')
  }
]

export const getBuiltinTool = (slug: string) => builtinTools.find((tool) => tool.id === slug)
