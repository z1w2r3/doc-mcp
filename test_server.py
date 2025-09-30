#!/usr/bin/env python
"""
测试 docxtpl MCP 服务器的功能

这个脚本模拟 MCP 客户端，测试服务器的各种功能。
"""

import json
import asyncio
from datetime import datetime
from pathlib import Path

# 导入服务器模块
from src.server import DocxTemplateServer


async def test_list_templates(server):
    """测试列出模板功能"""
    print("\n📋 测试：列出所有模板")
    print("-" * 50)

    result = await server.list_templates()
    print(result[0].text)
    return len(result) > 0


async def test_validate_template(server):
    """测试模板验证功能"""
    print("\n✅ 测试：验证模板")
    print("-" * 50)

    result = await server.validate_template("invoice.docx")
    print(result[0].text)
    return "Variables Found" in result[0].text


async def test_generate_invoice(server):
    """测试生成发票文档"""
    print("\n💰 测试：生成发票")
    print("-" * 50)

    context_data = {
        "company_name": "测试科技有限公司",
        "company_address": "北京市朝阳区科技路 123 号",
        "company_email": "info@testtech.com",
        "company_phone": "+86-10-12345678",
        "customer_name": "客户公司",
        "customer_address": "上海市浦东新区商务路 456 号",
        "customer_email": "customer@client.com",
        "invoice_number": "INV-2024-TEST-001",
        "invoice_date": datetime.now().date().isoformat(),
        "due_date": datetime(2024, 10, 31).date().isoformat(),
        "items": [
            {
                "description": "软件开发服务",
                "quantity": 1,
                "unit_price": 50000,
                "total": 50000
            },
            {
                "description": "技术支持服务（年度）",
                "quantity": 1,
                "unit_price": 12000,
                "total": 12000
            },
            {
                "description": "培训服务（3天）",
                "quantity": 3,
                "unit_price": 3000,
                "total": 9000
            }
        ],
        "subtotal": 71000,
        "tax_rate": 6,
        "tax_amount": 4260,
        "total": 75260,
        "notes": "感谢您的业务合作！本发票为测试生成。",
        "terms": "付款期限：30天内"
    }

    result = await server.generate_document(
        "invoice.docx",
        context_data,
        "test_invoice"
    )
    print(result[0].text)
    return "successfully" in result[0].text


async def test_generate_report(server):
    """测试生成报告文档"""
    print("\n📊 测试：生成报告")
    print("-" * 50)

    context_data = {
        "report_title": "2024年第三季度业务分析报告",
        "report_subtitle": "市场趋势与业绩评估",
        "author_name": "张三",
        "department": "战略规划部",
        "report_date": datetime.now().date().isoformat(),
        "executive_summary": """本季度公司业绩表现优异，营收同比增长25%，达到1.5亿元。
        主要增长动力来自新产品线的成功推出和市场份额的扩大。
        然而，我们也面临着供应链压力和成本上升的挑战。""",
        "sections": [
            {
                "title": "市场分析",
                "content": "本季度市场整体呈现积极增长态势，行业规模扩大15%...",
                "subsections": [
                    {
                        "number": 1,
                        "title": "竞争格局",
                        "content": "市场竞争日趋激烈，主要竞争对手..."
                    },
                    {
                        "number": 2,
                        "title": "客户需求",
                        "content": "客户需求向高端化、个性化方向发展..."
                    }
                ]
            },
            {
                "title": "财务表现",
                "content": "本季度财务指标全面达标，营收和利润双增长...",
                "table": {
                    "title": "关键财务指标",
                    "headers": ["指标", "本季度", "同比增长"]
                }
            },
            {
                "title": "运营效率",
                "content": "通过流程优化和技术升级，运营效率提升20%..."
            }
        ],
        "conclusions": """第三季度的业绩证明了我们战略的正确性。
        新产品线的成功和市场份额的增长为未来发展奠定了坚实基础。
        但我们需要密切关注成本控制和供应链管理。""",
        "recommendations": [
            "加大研发投入，保持产品创新优势",
            "优化供应链管理，降低成本压力",
            "扩大销售团队，进一步提升市场份额",
            "加强数字化转型，提高运营效率"
        ],
        "appendices": "详细财务数据和市场调研报告见附录文档。"
    }

    result = await server.generate_document(
        "report.docx",
        context_data,
        "test_report"
    )
    print(result[0].text)
    return "successfully" in result[0].text


async def test_list_documents(server):
    """测试列出生成的文档"""
    print("\n📚 测试：列出所有生成的文档")
    print("-" * 50)

    result = await server.list_documents()
    print(result[0].text)
    return True


async def test_preview_template(server):
    """测试预览模板功能"""
    print("\n👀 测试：预览模板")
    print("-" * 50)

    sample_data = {
        "sender_name": "李四",
        "sender_address": "北京市海淀区中关村大街1号",
        "sender_city": "北京",
        "sender_state": "北京",
        "sender_zip": "100080",
        "sender_email": "lisi@example.com",
        "sender_phone": "010-12345678",
        "letter_date": datetime.now().date().isoformat(),
        "recipient_name": "王五",
        "recipient_title": "总经理",
        "recipient_company": "示例公司",
        "recipient_address": "上海市黄浦区南京东路100号",
        "recipient_city": "上海",
        "recipient_state": "上海",
        "recipient_zip": "200001",
        "salutation": "王总",
        "subject": "关于合作提案的函",
        "body_paragraphs": [
            "很高兴有机会向贵公司提出这份合作提案。",
            "基于我们之前的讨论，我相信这个合作将为双方带来巨大价值。",
            "期待您的回复，希望我们能够尽快推进此事。"
        ],
        "closing": "此致敬礼",
        "sender_title": "业务发展经理"
    }

    result = await server.preview_template("letter.docx", sample_data)
    print(result[0].text)
    return "successfully" in result[0].text


async def run_all_tests():
    """运行所有测试"""
    print("\n" + "="*60)
    print("🧪 开始测试 docxtpl MCP 服务器")
    print("="*60)

    # 创建服务器实例
    server = DocxTemplateServer()

    # 测试结果统计
    tests = [
        ("列出模板", test_list_templates),
        ("验证模板", test_validate_template),
        ("生成发票", test_generate_invoice),
        ("生成报告", test_generate_report),
        ("预览模板", test_preview_template),
        ("列出文档", test_list_documents),
    ]

    results = {}

    for test_name, test_func in tests:
        try:
            success = await test_func(server)
            results[test_name] = "✅ 通过" if success else "❌ 失败"
        except Exception as e:
            results[test_name] = f"❌ 错误: {str(e)}"
            print(f"\n错误详情: {e}")

    # 打印测试结果摘要
    print("\n" + "="*60)
    print("📊 测试结果摘要")
    print("="*60)

    for test_name, result in results.items():
        print(f"{test_name}: {result}")

    # 统计通过率
    passed = sum(1 for r in results.values() if "✅" in r)
    total = len(results)
    pass_rate = (passed / total) * 100

    print("\n" + "-"*60)
    print(f"通过率: {passed}/{total} ({pass_rate:.1f}%)")

    if pass_rate == 100:
        print("🎉 所有测试通过！")
    elif pass_rate >= 80:
        print("⚠️ 大部分测试通过，但仍有问题需要修复。")
    else:
        print("❌ 测试失败较多，请检查代码。")

    print("="*60)

    # 清理测试文件（可选）
    output_dir = Path("output")
    test_files = list(output_dir.glob("test_*"))
    if test_files:
        print(f"\n🧹 找到 {len(test_files)} 个测试文件")
        # for f in test_files:
        #     f.unlink()
        #     print(f"  删除: {f.name}")


if __name__ == "__main__":
    # 运行测试
    asyncio.run(run_all_tests())