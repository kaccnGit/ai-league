from __future__ import annotations

from app.models.tool import Tool, ToolCategory


TOOL_CATEGORIES: list[ToolCategory] = [
    ToolCategory(
        id="encode",
        title="在线转码",
        description="Base64、URL、Hash 等快速转换",
        icon="carbon:code-reference",
    ),
    ToolCategory(
        id="convert",
        title="格式转换",
        description="JSON、YAML、Markdown、表格互转",
        icon="solar:transfer-horizontal-bold-duotone",
    ),
    ToolCategory(
        id="media",
        title="图片 & 多媒体",
        description="压缩、裁剪、格式优化一站式完成",
        icon="solar:image-bold-duotone",
    ),
    ToolCategory(
        id="ops",
        title="效率&运维",
        description="正则测试、延迟探测、Webhook 调试",
        icon="ph:terminal-window-duotone",
    ),
]

TOOLS: list[Tool] = [
    Tool(
        id="base64-playground",
        name="Base64 Playground",
        description="实时编码/解码、粘贴即得结果，支持文本与文件。",
        category="encode",
        tags=["编码", "字符串", "安全"],
        url="https://base64.guru/converter/decode",
        icon="https://cdn.jsdelivr.net/gh/tabler/tabler-icons/icons/base64.svg",
        featured=True,
    ),
    Tool(
        id="json-format",
        name="JSON 格式化",
        description="可视化 JSON Diff、验证 Schema。",
        category="convert",
        tags=["JSON", "验证"],
        url="https://jsoncrack.com/editor",
        icon="https://jsoncrack.com/favicon.svg",
        featured=True,
    ),
    Tool(
        id="yaml-to-json",
        name="YAML ⇆ JSON",
        description="双向转换保留注释与排序，可下载结果。",
        category="convert",
        tags=["YAML", "转换"],
        url="https://www.json2yaml.com/",
    ),
    Tool(
        id="imgcompress",
        name="TinyPNG",
        description="智能压缩 PNG/JPG，支持批量拖拽。",
        category="media",
        tags=["图片", "压缩"],
        url="https://tinypng.com/",
    ),
    Tool(
        id="svg-optimizer",
        name="SVGOMG",
        description="可视化调节，导出最优 SVG。",
        category="media",
        tags=["SVG"],
        url="https://jakearchibald.github.io/svgomg/",
    ),
    Tool(
        id="cron-checker",
        name="Crontab Guru",
        description="快速验证 Cron 表达式并展示下次执行时间。",
        category="ops",
        tags=["运维", "调度"],
        url="https://crontab.guru/",
    ),
    Tool(
        id="webhook-sandbox",
        name="Webhook.site",
        description="捕获并调试任何 HTTP 请求，支持自定义响应。",
        category="ops",
        tags=["调试", "HTTP"],
        url="https://webhook.site/",
        featured=True,
    ),
]
