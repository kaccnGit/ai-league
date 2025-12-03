export interface Tool {
  id: string
  name: string
  description: string
  category: string
  tags: string[]
  url: string
  icon?: string
  featured?: boolean
}

export interface ToolCategory {
  id: string
  title: string
  description: string
  icon?: string
}

export interface AIResource {
  id: string
  name: string
  provider: string
  category: string
  description: string
  docs_url: string
  console_url?: string
  tags: string[]
  difficulty: string
  highlight?: boolean
}

export type Base64Mode = 'encode' | 'decode'
export interface Base64RequestPayload {
  payload: string
  mode: Base64Mode
}
export interface Base64ResponsePayload {
  result: string
}

export type HashAlgorithm = 'md5' | 'sha1' | 'sha256' | 'sha512'
export interface HashRequestPayload {
  payload: string
  algorithm: HashAlgorithm
}
export interface HashResponsePayload {
  algorithm: HashAlgorithm
  hash: string
}

export type TimestampMode = 'unix_to_human' | 'human_to_unix'
export interface TimestampRequestPayload {
  value: string
  mode: TimestampMode
  timezone?: string
}
export interface TimestampResponsePayload {
  unix: number
  human: string
}

export interface JsonFormatPayload {
  payload: string
  indent?: number
}
export interface JsonFormatResponsePayload {
  formatted: string
  size: number
}

export type JsonYamlDirection = 'json_to_yaml' | 'yaml_to_json'
export interface JsonYamlPayload {
  payload: string
  direction: JsonYamlDirection
}
export interface JsonYamlResponsePayload {
  result: string
}

export interface ColorConvertPayload {
  value: string
}
export interface ColorConvertResponsePayload {
  hex: string
  rgb: string
  hsl: string
}

export type DiffLineType = 'added' | 'removed' | 'unchanged'
export interface TextDiffPayload {
  left: string
  right: string
}
export interface DiffLine {
  type: DiffLineType
  value: string
}
export interface TextDiffResponsePayload {
  diff: DiffLine[]
}
