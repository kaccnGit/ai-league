from __future__ import annotations

from app.models.ai_resource import AIResource


AI_RESOURCES: list[AIResource] = [
    AIResource(
        id="openai-gpt4o",
        name="GPT-4o",
        provider="OpenAI",
        category="通用对话",
        description="多模态旗舰模型，适合通用编码、问答与智能体搭建。",
        docs_url="https://platform.openai.com/docs",
        console_url="https://platform.openai.com/playground",
        tags=["多模态", "高精度"],
        difficulty="进阶",
        highlight=True,
    ),
    AIResource(
        id="doubao-pro",
        name="豆包 Pro",
        provider="字节跳动",
        category="中文大模型",
        description="对中文任务强化，性价比高，适合产品化快速接入。",
        docs_url="https://www.volcengine.com/docs/82367/",
        console_url="https://www.volcengine.com/product/doubao",
        tags=["中文", "API"],
    ),
    AIResource(
        id="qwen2-coder",
        name="通义千问 Qwen2 Coder",
        provider="阿里云",
        category="代码助手",
        description="针对代码生成/补全优化，支持 32k+ 上下文。",
        docs_url="https://help.aliyun.com/zh/model-studio/user-guide/qwen2",
        console_url="https://modelscope.cn/",
        tags=["代码", "长上下文"],
        difficulty="进阶",
        highlight=True,
    ),
    AIResource(
        id="deepseek-chat",
        name="DeepSeek Chat",
        provider="DeepSeek",
        category="性价比",
        description="开放 API，推理与代码表现优秀，成本友好。",
        docs_url="https://api-docs.deepseek.com/",
        console_url="https://platform.deepseek.com/",
        tags=["低成本"],
    ),
    AIResource(
        id="dashscope-video",
        name="通义灵码视频",
        provider="阿里云",
        category="多模态",
        description="提供视频理解与生成 API，适合内容创作。",
        docs_url="https://help.aliyun.com/zh/model-studio/developer-reference/text-to-video",
        tags=["视频", "多模态"],
        difficulty="实验",
    ),
]
