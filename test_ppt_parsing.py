#!/usr/bin/env python
"""
测试 PPT 解析功能
"""
import asyncio
import json
from pathlib import Path
from src.server import DocxTemplateServer

async def test_parse_ppt_document():
    """测试 parse_ppt_document 功能"""
    print("=" * 80)
    print("测试 1: parse_ppt_document - 解析样本 PPT 文件")
    print("=" * 80)

    server = DocxTemplateServer()
    sample_file = str(Path("output/江苏省智能建造试点项目.pptx").absolute())

    # 测试解析前 3 张幻灯片
    result = await server.parse_ppt_document(
        file_path=sample_file,
        include_tables=True,
        include_images=True,
        slides="1-3"
    )

    print(result[0].text)
    print("\n")


async def test_extract_text_from_ppt():
    """测试 extract_text_from_document 对 PPT 的支持"""
    print("=" * 80)
    print("测试 2: extract_text_from_document - 快速文本提取")
    print("=" * 80)

    server = DocxTemplateServer()
    sample_file = str(Path("output/江苏省智能建造试点项目.pptx").absolute())

    result = await server.extract_text_from_document(file_path=sample_file)

    print(result[0].text)
    print("\n")


async def test_get_ppt_metadata():
    """测试 get_document_metadata 对 PPT 的支持"""
    print("=" * 80)
    print("测试 3: get_document_metadata - 提取 PPT 元数据")
    print("=" * 80)

    server = DocxTemplateServer()
    sample_file = str(Path("output/江苏省智能建造试点项目.pptx").absolute())

    result = await server.get_document_metadata(file_path=sample_file)

    print(result[0].text)
    print("\n")


async def test_parse_all_slides():
    """测试解析所有幻灯片"""
    print("=" * 80)
    print("测试 4: parse_ppt_document - 解析所有幻灯片")
    print("=" * 80)

    server = DocxTemplateServer()
    sample_file = str(Path("output/江苏省智能建造试点项目.pptx").absolute())

    result = await server.parse_ppt_document(
        file_path=sample_file,
        include_tables=True,
        include_images=False,
        slides="all"
    )

    # 只显示摘要信息
    text = result[0].text
    lines = text.split('\n')
    for line in lines[:20]:  # 显示前20行
        print(line)
    print("\n... (完整输出已省略)")
    print("\n")


async def test_error_handling():
    """测试错误处理"""
    print("=" * 80)
    print("测试 5: 错误处理 - 不存在的文件")
    print("=" * 80)

    server = DocxTemplateServer()

    result = await server.parse_ppt_document(
        file_path="/nonexistent/file.pptx",
        include_tables=True,
        include_images=False,
        slides="all"
    )

    print(result[0].text)
    print("\n")


async def main():
    """运行所有测试"""
    print("\n🚀 开始 PPT 解析功能测试\n")

    await test_parse_ppt_document()
    await test_extract_text_from_ppt()
    await test_get_ppt_metadata()
    await test_parse_all_slides()
    await test_error_handling()

    print("=" * 80)
    print("✅ 所有测试完成!")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
