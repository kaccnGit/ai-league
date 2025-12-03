# AI League 工具门户架构

## 总览
- **Mono Repo**：根目录下包含 `frontend/` (Vue 3 + Vite) 与 `backend/` (FastAPI)。
- **API / UI 解耦**：FastAPI 暴露 `/api` 命名空间，前端使用 Axios 调用。
- **数据驱动**：工具、AI 资源等通过结构化 JSON/TS 文件与 Pydantic 模型定义，易于扩展。
- **跨端体验**：响应式布局 + 移动端导航折叠，保证 H5 可用。

## 前端
- **技术栈**：Vite + Vue 3 + TypeScript + Vue Router + Pinia。
- **UI 框架**： [Element Plus](https://element-plus.org/) + `@iconify/vue`，并叠加浅色渐变/玻璃拟态定制样式。
- **样式**：CSS 变量 + PostCSS 自动前缀，部分定制化 utility class 确保主题一致。
- **目录结构**：
  - `src/pages`：Home、Tools、AI Hub 等页面。
  - `src/components`：Hero、ToolCard、CategoryTabs 等基础组件。
  - `src/data`：内置静态资源（后续可改为 API 动态获取）。
  - `src/stores`：Pinia 状态管理，缓存工具分类、AI 列表。
- **路由设计**：
  - `/` 首页（概览 + 呼吁 + 工具索引预览）。
  - `/tools` 工具中心索引：展示内置工具卡片 + 外链工具集。
  - `/tools/:toolId` 单工具页面（如 `/tools/color-converter`），按需懒加载实际组件，方便水平扩展。
  - `/ai` AI 模型导航：按用途/厂商分栏、入门资料链接。

## 后端
- **框架**：FastAPI + Uvicorn。
- **结构**：
  - `app/main.py`：入口、路由注册、CORS。
  - `app/api`：路由模块 (`tools.py`, `ai.py`, `health.py`)。
  - `app/models`：Pydantic schemas。
  - `app/data`：当前使用静态数据，后续可替换数据库。
- **功能**：
  - `GET /api/tools` 支持按分类、关键字过滤。
  - `GET /api/ai` 支持按提供商、能力过滤。
  - `GET /api/health` 健康检查，供部署监控。
  - `POST /api/utils/*` 一组实用工具 API：
    - `/base64` 编解码
    - `/hash` 常见 Hash 计算
    - `/timestamp` Unix ↔ ISO 时间互转
    - `/json/format` JSON 格式化/压缩
    - `/json-yaml` JSON 与 YAML 双向转换
    - `/color/convert` Hex/RGB/HSL 互转
    - `/text/diff` 行级文本对比

## 开发体验
1. `frontend`: `npm install && npm run dev`。
2. `backend`: 建议 `uvicorn app.main:app --reload`。
3. 提供 `Makefile` / `justfile` 统一脚本（后续可补）。

此文档将随实现同步更新。
