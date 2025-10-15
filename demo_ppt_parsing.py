#!/usr/bin/env python
"""
PowerPoint 解析功能演示脚本

演示如何使用 docxtpl-mcp 服务器解析 PowerPoint 文档
"""
import asyncio
import json
from pathlib import Path
from src.server import DocxTemplateServer


async def demo_ppt_parsing():
    """演示 PowerPoint 解析功能"""

    print("=" * 80)
    print("📊 PowerPoint 解析功能演示")
    print("=" * 80)
    print()

    server = DocxTemplateServer()

    # 使用样本文件
    sample_file = Path("output/江苏省智能建造试点项目.pptx").absolute()

    if not sample_file.exists():
        print("❌ 样本文件不存在,请将 PPT 文件放在 output 目录下")
        return

    print(f"📄 样本文件: {sample_file.name}")
    print(f"📏 文件大小: {sample_file.stat().st_size / (1024*1024):.2f} MB")
    print()

    # 演示 1: 快速文本提取
    print("=" * 80)
    print("演示 1: 快速文本提取 (extract_text_from_document)")
    print("=" * 80)

    result = await server.extract_text_from_document(file_path=str(sample_file))
    print(result[0].text[:1000])  # 只显示前1000个字符
    print("... (输出已截断)")
    print()

    # 演示 2: 提取元数据
    print("=" * 80)
    print("演示 2: 提取元数据 (get_document_metadata)")
    print("=" * 80)

    result = await server.get_document_metadata(file_path=str(sample_file))
    print(result[0].text)
    print()

    # 演示 3: 解析指定幻灯片
    print("=" * 80)
    print("演示 3: 解析指定幻灯片范围 (parse_ppt_document)")
    print("=" * 80)
    print("解析幻灯片 1-3...")

    # 注意: 由于样本文件较大 (93MB),可能超过默认限制
    # 这里演示如何使用 API,实际使用时请确保文件大小在限制范围内
    print()
    print("⚠️  注意: 样本文件较大,可能超过默认的 50 MB 限制")
    print("💡 提示: 可以通过设置环境变量 MAX_FILE_SIZE_MB 调整限制")
    print()

    # 演示 API 调用方式
    print("API 调用示例:")
    print("-" * 80)
    api_example = {
        "tool": "parse_ppt_document",
        "arguments": {
            "file_path": "/path/to/presentation.pptx",
            "include_tables": True,
            "include_images": False,
            "slides": "1-5"
        }
    }
    print(json.dumps(api_example, indent=2, ensure_ascii=False))
    print("-" * 80)
    print()

    # 演示不同的幻灯片范围选项
    print("幻灯片范围选项:")
    print("  - 'all'      : 解析所有幻灯片")
    print("  - '1-5'      : 解析第 1-5 张幻灯片")
    print("  - '1,3,5'    : 解析第 1、3、5 张幻灯片")
    print("  - '10'       : 仅解析第 10 张幻灯片")
    print()

    print("=" * 80)
    print("✅ 演示完成!")
    print("=" * 80)
    print()
    print("💡 使用提示:")
    print("1. parse_ppt_document   - 获取完整的结构化数据 (幻灯片、表格、图片)")
    print("2. extract_text_from_document - 快速提取纯文本内容")
    print("3. get_document_metadata - 仅获取文档元数据")
    print()
    print("📚 更多信息请参阅 README.md")


if __name__ == "__main__":
    asyncio.run(demo_ppt_parsing())
