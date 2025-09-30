#!/usr/bin/env python3
"""
文档解析功能演示脚本
展示新增的 4 个解析工具
"""
import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from src.server import DocxTemplateServer

async def demo():
    """演示文档解析功能"""

    print("=" * 70)
    print("📖 docxtpl-mcp v0.3.0 - 文档解析功能演示")
    print("=" * 70)
    print()

    server = DocxTemplateServer()

    # 测试文件路径
    docx_template = "/Users/zhengwr/workspace/doc-mcp/templates/invoice.docx"

    # =========================================================================
    # 演示 1: parse_docx_document - 完整解析 DOCX 文档
    # =========================================================================
    print("📄 演示 1: 完整解析 DOCX 文档")
    print("-" * 70)
    print(f"文件: {docx_template}")
    print()

    result = await server.parse_docx_document(docx_template, include_tables=True)
    output = result[0].text

    # 提取 JSON 部分
    if "```json" in output:
        json_start = output.find("```json") + 7
        json_end = output.find("```", json_start)
        json_str = output[json_start:json_end].strip()
        data = json.loads(json_str)

        print("✅ 解析成功!")
        print(f"   - 文件大小: {data['metadata']['file_size_mb']} MB")
        print(f"   - 作者: {data['metadata']['author']}")
        print(f"   - 段落数: {data['content']['paragraph_count']}")
        print(f"   - 表格数: {data['content']['table_count']}")
        print()

        # 显示前3个段落
        print("   前 3 个段落:")
        for i, para in enumerate(data['content']['paragraphs'][:3], 1):
            print(f"   {i}. [{para['style']}] {para['text'][:50]}...")

    print()

    # =========================================================================
    # 演示 2: extract_text_from_document - 快速文本提取
    # =========================================================================
    print("📝 演示 2: 快速文本提取")
    print("-" * 70)
    print(f"文件: {docx_template}")
    print()

    result = await server.extract_text_from_document(docx_template)
    output = result[0].text

    # 提取统计信息
    if "字符数:" in output:
        lines = output.split('\n')
        for line in lines:
            if '字符数:' in line or '单词数:' in line or '行数:' in line:
                print(f"   {line.strip()}")

    print()

    # =========================================================================
    # 演示 3: get_document_metadata - 提取元数据
    # =========================================================================
    print("📋 演示 3: 提取文档元数据")
    print("-" * 70)
    print(f"文件: {docx_template}")
    print()

    result = await server.get_document_metadata(docx_template)
    output = result[0].text

    if "```json" in output:
        json_start = output.find("```json") + 7
        json_end = output.find("```", json_start)
        json_str = output[json_start:json_end].strip()
        metadata = json.loads(json_str)

        print("✅ 元数据提取成功!")
        print(f"   - 文件名: {metadata['filename']}")
        print(f"   - 文件类型: {metadata['file_type']}")
        print(f"   - 大小: {metadata['file_size_mb']} MB")
        print(f"   - 作者: {metadata['author']}")
        if 'statistics' in metadata:
            stats = metadata['statistics']
            print(f"   - 段落数: {stats['paragraphs']}")
            print(f"   - 表格数: {stats['tables']}")
            print(f"   - 章节数: {stats['sections']}")

    print()

    # =========================================================================
    # 演示 4: 错误处理
    # =========================================================================
    print("⚠️  演示 4: 错误处理")
    print("-" * 70)
    print("测试: 解析不存在的文件")
    print()

    result = await server.parse_docx_document("/tmp/nonexistent.docx")
    print(f"   {result[0].text}")

    print()
    print("=" * 70)
    print("✅ 演示完成!")
    print()
    print("💡 提示:")
    print("   - 这些工具现在可以通过 MCP 协议在 Claude Desktop 中使用")
    print("   - 支持格式: DOCX 和 PDF")
    print("   - 输出格式: 结构化 JSON")
    print()
    print("🚀 使用方法:")
    print("   1. 重启 Claude Desktop 以加载新工具")
    print("   2. 使用工具名称调用:")
    print("      - parse_docx_document")
    print("      - parse_pdf_document")
    print("      - extract_text_from_document")
    print("      - get_document_metadata")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(demo())