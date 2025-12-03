# AI League 工具网站

一个聚合程序员常用工具与 AI 大模型资源的门户站，前端使用 Vue 3 + Element Plus，后端基于 FastAPI。

## 功能亮点
- 在线工具合集：转码、格式转换、图片与运维调试等分类导航与搜索。
- 内置工具：Base64、Hash、颜色编码、文本对比、时间戳、JSON 格式化/转换等站内即时完成，每个工具拥有独立二级页面。
- AI 资源导航：按厂商、用途筛选，附入门文档与控制台链接。
- 响应式设计：桌面/H5 同步适配，浅色渐变 + 玻璃拟态视觉。
- 简易数据层：暂存静态 JSON，可替换数据库或外部服务。

## 项目结构
```
./frontend   # Vue 3 + Vite 单页应用
./backend    # FastAPI 服务 (提供 /api 接口)
./docs       # 架构说明
```

## 快速开始
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API 将运行在 `http://localhost:8000`。

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Vite Dev Server 默认端口 `5173`，并代理 `/api` 到后端。

## 后续可扩展
1. 接入用户体系（登录/收藏/自定义清单）。
2. 将工具与 AI 资源落地数据库 + 管理后台。
3. 增加更多工具类型（电商、财税、设计等）。
4. 支持多语言与夜间主题切换。

欢迎继续完善！
