# npm 发布指南 - docxtpl MCP

## 发布前检查清单

✅ **已完成的准备工作**：
- [x] 创建 package.json 配置文件
- [x] 创建 bin/index.js Node.js 入口脚本
- [x] 创建 scripts/install.cjs 自动安装脚本
- [x] 创建 scripts/prepublish.cjs 验证脚本
- [x] 创建 .npmignore 文件
- [x] 添加 LICENSE 文件
- [x] 更新 README.md 添加 npm 使用说明
- [x] 本地测试通过

## 发布步骤

### 1. 确认本地测试通过
```bash
# 验证包完整性
node scripts/prepublish.cjs

# 测试版本
npm test

# 测试本地链接
npm link
npx docxtpl-mcp --version
```

### 2. 登录 npm
```bash
npm login
# 输入用户名、密码和邮箱
```

### 3. 发布到 npm
```bash
# 第一次发布
npm publish

# 后续更新版本
npm version patch  # 或 minor / major
npm publish
```

### 4. 验证发布
```bash
# 等待几分钟后测试
npx docxtpl-mcp@latest --version
```

## 使用方式

发布成功后，用户可以通过以下方式使用：

### Claude Code 添加
```bash
claude mcp add docxtpl npx docxtpl-mcp@latest
```

### 直接运行
```bash
npx docxtpl-mcp@latest
```

### 全局安装
```bash
npm install -g docxtpl-mcp
docxtpl-mcp
```

## 版本管理

- **patch** (0.1.0 → 0.1.1): 修复 bug
- **minor** (0.1.0 → 0.2.0): 新功能，向后兼容
- **major** (0.1.0 → 1.0.0): 重大更改，可能不兼容

## 更新流程

1. 修改代码
2. 更新版本：`npm version patch/minor/major`
3. 推送到 Git：`git push --tags`
4. 发布到 npm：`npm publish`

## 注意事项

1. **包名唯一性**：`docxtpl-mcp` 必须在 npm 上唯一
2. **Python 依赖**：用户需要 Python 3.10+
3. **首次运行**：会自动安装 Python 依赖
4. **模板文件**：自动包含在 npm 包中

## 故障排除

### 发布权限问题
```bash
npm whoami  # 检查登录状态
npm owner ls docxtpl-mcp  # 查看包所有者
```

### 包名冲突
如果包名已存在，需要：
1. 更改 package.json 中的 name
2. 使用作用域包名：`@username/docxtpl-mcp`

### 测试发布
可以先发布到本地 registry 测试：
```bash
npm pack  # 创建 .tgz 文件
npm install -g ./docxtpl-mcp-0.1.0.tgz  # 本地安装测试
```

---

📝 **提示**：发布前确保已经在 https://www.npmjs.com/ 注册账号。