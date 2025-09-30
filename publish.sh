#!/bin/bash

echo "📦 准备发布 docxtpl-mcp 到 npm..."
echo "================================"

# 运行验证脚本
echo "🔍 验证包完整性..."
node scripts/prepublish.cjs

if [ $? -ne 0 ]; then
    echo "❌ 验证失败，请修复问题后再试"
    exit 1
fi

# 检查是否登录
echo ""
echo "🔐 检查 npm 登录状态..."
npm whoami 2>/dev/null

if [ $? -ne 0 ]; then
    echo "📝 需要登录 npm"
    echo "请运行: npm login"
    echo ""
    echo "如果还没有 npm 账号，请先在 https://www.npmjs.com 注册"
    exit 1
fi

# 显示当前版本
CURRENT_VERSION=$(node -p "require('./package.json').version")
echo "📌 当前版本: v$CURRENT_VERSION"

# 询问是否继续
echo ""
read -p "是否继续发布? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "🚫 取消发布"
    exit 0
fi

# 发布
echo ""
echo "🚀 发布到 npm..."
npm publish

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 发布成功！"
    echo ""
    echo "🎉 用户现在可以通过以下方式使用："
    echo "   claude mcp add docxtpl npx docxtpl-mcp@latest"
    echo "   npx docxtpl-mcp@latest"
    echo ""
    echo "📦 查看包信息："
    echo "   https://www.npmjs.com/package/docxtpl-mcp"
else
    echo ""
    echo "❌ 发布失败"
    echo "可能的原因："
    echo "1. 包名已存在 - 需要更改包名或获取权限"
    echo "2. 网络问题 - 请重试"
    echo "3. 权限问题 - 确保已登录正确账号"
fi