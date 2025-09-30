#!/bin/bash

# docxtpl MCP 服务器启动脚本

echo "🚀 启动 docxtpl MCP 服务器..."
echo "================================"

# 检查 Python 版本
python_version=$(python --version 2>&1 | grep -oP '\d+\.\d+' | head -n 1)
echo "✅ Python 版本: $python_version"

# 检查必要的目录
if [ ! -d "templates" ]; then
    echo "📁 创建模板目录..."
    mkdir templates
fi

if [ ! -d "output" ]; then
    echo "📁 创建输出目录..."
    mkdir output
fi

# 检查模板文件
template_count=$(ls -1 templates/*.docx 2>/dev/null | wc -l)
if [ "$template_count" -eq 0 ]; then
    echo "⚠️  没有找到模板文件，正在创建示例模板..."
    python create_templates.py
fi

echo "📄 找到 $template_count 个模板文件"

# 启动服务器
echo "================================"
echo "🎯 服务器正在启动..."
echo "📍 模板目录: templates/"
echo "📍 输出目录: output/"
echo "================================"
echo ""

# 运行服务器
python -m src.server