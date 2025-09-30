# 📄 docxtpl MCP Server

基于模型上下文协议 (MCP) 的 Word 文档生成服务器，使用 Python 的 docxtpl 库提供强大的模板功能。

[![npm version](https://img.shields.io/npm/v/docxtpl-mcp.svg)](https://www.npmjs.com/package/docxtpl-mcp)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![MCP Protocol](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 🚀 快速安装

### 方式 1：通过 Claude Code (推荐)
```bash
claude mcp add docxtpl npx docxtpl-mcp@latest
```

### 方式 2：直接使用 npx
```bash
# 无需安装，直接运行
npx docxtpl-mcp@latest
```

### 方式 3：全局安装
```bash
# 全局安装
npm install -g docxtpl-mcp

# 运行
docxtpl-mcp
```

### 方式 4：手动配置 Claude Desktop
在 Claude Desktop 配置文件（`~/.claude/config.json`）中添加：
```json
{
  "mcpServers": {
    "docxtpl": {
      "command": "npx",
      "args": ["docxtpl-mcp@latest"]
    }
  }
}
```

## ✨ 特性

- 🚀 **基于 MCP 协议** - 标准化的 AI 模型交互接口
- 📝 **强大的模板引擎** - 支持完整的 Jinja2 语法
- 🔄 **动态内容生成** - 条件渲染、循环、自定义过滤器
- 📊 **丰富的模板** - 内置发票、报告、合同、信函等模板
- 🛠️ **易于扩展** - 简单添加自定义模板和功能
- 🔒 **安全可靠** - 完善的错误处理和输入验证
- 📖 **文档解析** - 支持解析 DOCX、PDF 和 Excel 文档,提取结构化内容

## 📋 目录

- [快速开始](#快速开始)
- [安装](#安装)
- [配置](#配置)
- [使用方法](#使用方法)
- [可用工具](#可用工具)
- [模板示例](#模板示例)
- [API 文档](#api-文档)
- [开发指南](#开发指南)
- [故障排除](#故障排除)
- [贡献](#贡献)
- [许可证](#许可证)

## 📋 前置要求

- Node.js 14.0+ 和 npm（用于 npx）
- Python 3.10+ （自动检测，如未安装会提示）
- 支持 MCP 的 AI 客户端（如 Claude Desktop）

**注意**：首次运行时会自动安装 Python 依赖包，这可能需要几分钟时间。

## 📦 开发安装

如果您想从源代码运行或参与开发：

### 克隆仓库

```bash
# 克隆仓库
git clone https://github.com/yourusername/docxtpl-mcp.git
cd docxtpl-mcp

# 安装 Python 依赖
pip install -r requirements.txt

# 创建示例模板
python create_templates.py

# 直接运行服务器
python -m src.server
```

### 本地测试 npm 包

```bash
# 链接到全局
npm link

# 测试运行
npx docxtpl-mcp
```

## ⚙️ 配置

### 环境变量

复制 `.env.example` 到 `.env` 并根据需要修改：

```bash
cp .env.example .env
```

可配置项：

| 变量 | 默认值 | 描述 |
|-----|-------|-----|
| `TEMPLATE_DIR` | `templates` | 模板文件目录 |
| `OUTPUT_DIR` | `output` | 生成文档输出目录 |
| `MAX_FILE_SIZE_MB` | `50` | 最大文件大小限制（MB） |
| `DEBUG` | `false` | 启用调试日志 |

### Claude Desktop 配置

配置文件位置：
- **macOS/Linux**: `~/.claude/config.json`
- **Windows**: `%APPDATA%\Claude\config.json`

#### 使用 npm 包（推荐）
```json
{
  "mcpServers": {
    "docxtpl": {
      "command": "npx",
      "args": ["docxtpl-mcp@latest"]
    }
  }
}
```

#### 或从源代码运行
```json
{
  "mcpServers": {
    "docxtpl": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "/path/to/docxtpl-mcp",
      "env": {
        "TEMPLATE_DIR": "templates",
        "OUTPUT_DIR": "output"
      }
    }
  }
}
```

## 📖 使用方法

### 基本用法

1. **列出可用模板**
```
使用 list_templates 工具查看所有可用模板
```

2. **生成文档**
```
使用 generate_document 工具，提供模板名称和数据
```

3. **验证模板**
```
使用 validate_template 工具检查模板语法和所需变量
```

### 示例对话

**用户：** 帮我生成一份发票，客户是 ABC 公司，包含两个产品：软件许可证 10 个（单价 $99.99）和技术支持服务（$500）

**AI：** 我来帮您生成发票。让我使用发票模板创建文档...

[AI 调用 generate_document 工具]

**AI：** 发票已成功生成！
- 📄 文件：invoice_20240928_143022.docx
- 📁 位置：output/invoice_20240928_143022.docx
- 💰 总计：$1,649.89（含10%税费）

### 文档解析示例

**用户：** 帮我解析这个 PDF 文件 `/path/to/report.pdf`,提取所有文本和表格

**AI：** 好的,我来解析这个 PDF 文档...

[AI 调用 parse_pdf_document 工具]

**AI：** PDF 文档解析成功！
- 📄 文件：report.pdf
- 📄 总页数：15 页
- 📝 文本长度：12,450 字符
- 📊 表格数：3 个

解析结果已转换为结构化 JSON 格式,包含每页的文本内容和表格数据。

**用户：** 解析这个 Excel 文件 `/path/to/data.xlsx`,我只需要 "销售数据" 工作表

**AI：** 好的,我来解析 Excel 文件...

[AI 调用 parse_excel_document 工具]

**AI：** Excel 文档解析成功！
- 📄 文件：data.xlsx
- 📊 工作表总数：5
- 📋 已解析：销售数据
- 💼 单元格数：1,200
- 📐 公式数：15

解析结果包含工作表的所有单元格数据、公式和合并单元格信息。

## 🛠️ 可用工具

### 文档生成工具

#### 1. generate_document
生成 Word 文档

**参数：**
- `template_name` (string, 必需) - 模板文件名
- `context_data` (object, 必需) - 填充模板的数据
- `output_name` (string, 可选) - 输出文件名

**示例：**
```json
{
  "template_name": "invoice.docx",
  "context_data": {
    "company_name": "ABC Tech Inc.",
    "customer_name": "XYZ Corp",
    "items": [
      {
        "description": "Software License",
        "quantity": 10,
        "unit_price": 99.99,
        "total": 999.90
      }
    ],
    "total": 999.90
  },
  "output_name": "invoice_001"
}
```

### 2. list_templates
列出所有可用的 Word 模板

**参数：** 无

**返回：** 模板列表及其信息

### 3. validate_template
验证模板并提取所需变量

**参数：**
- `template_name` (string, 必需) - 模板文件名

**返回：** 模板中使用的变量列表

### 4. preview_template
使用示例数据预览模板

**参数：**
- `template_name` (string, 必需) - 模板文件名
- `sample_data` (object, 必需) - 示例数据

### 5. delete_document
删除生成的文档

**参数：**
- `document_id` (string, 必需) - 文档 ID

### 6. list_documents
列出所有已生成的文档

**参数：** 无

### 文档解析工具

#### 7. parse_docx_document
解析 DOCX 文档并提取结构化内容

**参数：**
- `file_path` (string, 必需) - DOCX 文件的绝对路径
- `include_tables` (boolean, 可选) - 是否提取表格 (默认: true)

**返回：** JSON 格式的结构化内容,包括:
- 文档元数据 (作者、创建时间等)
- 段落内容和样式
- 表格数据

**示例：**
```json
{
  "file_path": "/path/to/document.docx",
  "include_tables": true
}
```

#### 8. parse_pdf_document
解析 PDF 文档并提取文本、表格和元数据

**参数：**
- `file_path` (string, 必需) - PDF 文件的绝对路径
- `include_tables` (boolean, 可选) - 是否提取表格 (默认: true)
- `pages` (string, 可选) - 要解析的页面范围,如 "1-5" 或 "1,3,5" (默认: "all")

**返回：** JSON 格式的结构化内容,包括:
- PDF 元数据
- 每页的文本内容
- 每页的表格数据

**示例：**
```json
{
  "file_path": "/path/to/document.pdf",
  "include_tables": true,
  "pages": "1-10"
}
```

#### 9. extract_text_from_document
快速提取文档纯文本 (支持 DOCX 和 PDF)

**参数：**
- `file_path` (string, 必需) - 文档文件的绝对路径

**返回：** 文档的纯文本内容及统计信息

**示例：**
```json
{
  "file_path": "/path/to/document.docx"
}
```

#### 10. get_document_metadata
提取文档元数据信息

**参数：**
- `file_path` (string, 必需) - 文档文件的绝对路径 (DOCX、PDF 或 Excel)

**返回：** JSON 格式的元数据,包括:
- 文件基本信息 (文件名、大小、类型)
- 作者、标题、主题等
- 创建和修改时间
- 文档统计信息

**示例：**
```json
{
  "file_path": "/path/to/document.pdf"
}
```

#### 11. parse_excel_document
解析 Excel 文档 (XLSX/XLS) 并提取结构化内容

**参数：**
- `file_path` (string, 必需) - Excel 文件的绝对路径
- `sheet_name` (string, 可选) - 指定要解析的工作表名称 (默认: 解析所有工作表)
- `include_formulas` (boolean, 可选) - 是否包含单元格公式 (默认: true)

**返回：** JSON 格式的结构化内容,包括:
- Excel 元数据 (创建者、修改时间等)
- 工作表信息 (名称、行数、列数)
- 单元格数据
- 公式 (如果启用)
- 合并单元格信息

**示例：**
```json
{
  "file_path": "/path/to/data.xlsx",
  "sheet_name": "销售数据",
  "include_formulas": true
}
```

## 📋 模板示例

### 发票模板 (invoice.docx)

生成专业的商业发票：
- 公司和客户信息
- 商品明细表
- 自动计算小计、税费和总计
- 自定义备注和条款

### 报告模板 (report.docx)

创建结构化的业务报告：
- 封面和目录
- 执行摘要
- 章节和子章节
- 数据表格
- 结论和建议

### 合同模板 (contract.docx)

生成法律合同文档：
- 合同双方信息
- 条款和子条款
- 签名部分
- 日期和编号

### 信函模板 (letter.docx)

创建正式商务信函：
- 发件人和收件人信息
- 主题行
- 正文段落
- 附件和抄送

## 📚 API 文档

### 资源 URI

- `template://{name}` - 访问模板资源
- `document://{id}` - 访问生成的文档

### 提示模板

- `invoice_generator` - 发票生成提示
- `report_generator` - 报告生成提示

### 自定义过滤器

- `currency` - 格式化货币（例：1234.56 → $1,234.56）
- `date` - 格式化日期（例：2024-09-28 → September 28, 2024）

## 🔧 开发指南

### 添加自定义模板

1. 在 `templates/` 目录创建新的 .docx 文件
2. 使用 {{variable}} 语法插入变量
3. 使用 {% for %} 进行循环
4. 使用 {% if %} 进行条件判断

### 添加自定义过滤器

在 `src/server.py` 中注册新过滤器：

```python
def my_custom_filter(value):
    return value.upper()

jinja_env.filters['uppercase'] = my_custom_filter
```

### 运行测试

```bash
# 单元测试
pytest tests/

# 集成测试
pytest tests/integration/

# 覆盖率报告
pytest --cov=src tests/
```

## 🐛 故障排除

### 常见问题

**Q: 模板找不到怎么办？**
A: 确保模板文件在 `templates/` 目录下，且文件扩展名为 `.docx`

**Q: 生成的文档格式混乱？**
A: 检查模板中的 Jinja2 语法是否正确，使用 `validate_template` 工具验证

**Q: 如何处理大文件？**
A: 调整 `MAX_FILE_SIZE_MB` 环境变量，或考虑分批生成

### 错误代码

| 代码 | 描述 | 解决方案 |
|-----|------|---------|
| E001 | 模板未找到 | 检查模板路径和文件名 |
| E002 | 语法错误 | 验证 Jinja2 语法 |
| E003 | 数据类型错误 | 检查提供的数据格式 |
| E004 | 文件大小超限 | 减少内容或调整限制 |

## 🤝 贡献

我们欢迎各种形式的贡献！

### 如何贡献

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `style:` 代码格式
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议规范
- [python-docx-template](https://github.com/elapouya/python-docx-template) - 强大的 Word 模板引擎
- [Jinja2](https://jinja.palletsprojects.com/) - 优秀的模板语言

## 📞 联系方式

- 📧 邮件：dev@docxtpl-mcp.io
- 💬 讨论：[GitHub Discussions](https://github.com/yourusername/docxtpl-mcp/discussions)
- 🐛 问题：[Issue Tracker](https://github.com/yourusername/docxtpl-mcp/issues)

---

**⭐ 如果这个项目对您有帮助，请给个 Star！**

*Made with ❤️ by the docxtpl-mcp team*