#!/usr/bin/env python3
"""
测试文档解析功能
"""
import asyncio
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from src.server import DocxTemplateServer

async def test_parsing_functions():
    """测试文档解析功能"""
    print("🧪 开始测试文档解析功能\n")

    server = DocxTemplateServer()

    # 测试文件路径
    docx_file = "/Users/zhengwr/workspace/doc-mcp/templates/invoice.docx"
    output_docx = "/Users/zhengwr/workspace/doc-mcp/output/business_proposal_letter_2025.docx"

    print(f"📄 测试 DOCX 文件: {docx_file}\n")

    # 测试 1: 解析 DOCX 模板
    print("=" * 60)
    print("测试 1: parse_docx_document (模板文件)")
    print("=" * 60)
    result = await server.parse_docx_document(docx_file, include_tables=True)
    print(result[0].text[:500] + "..." if len(result[0].text) > 500 else result[0].text)
    print()

    # 测试 2: 提取文本
    print("=" * 60)
    print("测试 2: extract_text_from_document")
    print("=" * 60)
    result = await server.extract_text_from_document(docx_file)
    print(result[0].text[:500] + "..." if len(result[0].text) > 500 else result[0].text)
    print()

    # 测试 3: 获取元数据
    print("=" * 60)
    print("测试 3: get_document_metadata")
    print("=" * 60)
    result = await server.get_document_metadata(docx_file)
    print(result[0].text[:500] + "..." if len(result[0].text) > 500 else result[0].text)
    print()

    # 测试 4: 解析生成的文档
    if Path(output_docx).exists():
        print("=" * 60)
        print(f"测试 4: parse_docx_document (生成的文档)")
        print("=" * 60)
        result = await server.parse_docx_document(output_docx, include_tables=True)
        print(result[0].text[:500] + "..." if len(result[0].text) > 500 else result[0].text)
        print()

    # 测试 5: 错误处理 - 不存在的文件
    print("=" * 60)
    print("测试 5: 错误处理 (不存在的文件)")
    print("=" * 60)
    result = await server.parse_docx_document("/tmp/nonexistent.docx")
    print(result[0].text)
    print()

    # 测试 6: 错误处理 - 错误的文件格式
    print("=" * 60)
    print("测试 6: 错误处理 (错误的文件格式)")
    print("=" * 60)
    result = await server.parse_docx_document("/Users/zhengwr/workspace/doc-mcp/README.md")
    print(result[0].text)
    print()

    print("✅ 所有测试完成!")

if __name__ == "__main__":
    asyncio.run(test_parsing_functions())