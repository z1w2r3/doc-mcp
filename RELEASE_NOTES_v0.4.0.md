# Release Notes - v0.4.0

## 🎉 新增 Excel 解析功能

发布日期: 2025-09-30

### ✨ 新功能

#### 1. Excel 文档解析支持

添加了完整的 Excel (XLSX/XLS) 文档解析功能,现在可以像解析 DOCX 和 PDF 一样解析 Excel 文件!

**新增工具:**
- `parse_excel_document` - 解析 Excel 文档并提取结构化内容
  - 支持 .xlsx 和 .xls 格式
  - 可解析所有工作表或指定工作表
  - 提取单元格数据、公式、合并单元格信息
  - 提取工作簿元数据(作者、创建时间等)

**扩展的工具:**
- `extract_text_from_document` - 现在支持 Excel 文件快速文本提取
- `get_document_metadata` - 现在支持提取 Excel 文件元数据

### 📊 使用示例

```javascript
// 解析整个 Excel 文件
{
  "file_path": "/path/to/data.xlsx"
}

// 解析指定工作表
{
  "file_path": "/path/to/data.xlsx",
  "sheet_name": "销售数据",
  "include_formulas": true
}
```

### 🔧 技术改进

- 添加 `openpyxl>=3.0.0` 依赖用于 Excel 解析
- 自动转换日期格式为 ISO 标准格式
- 支持公式提取和显示
- 识别并标记合并单元格

### 📝 输出格式

解析结果包含:
- 工作簿元数据(文件名、大小、创建者、修改时间等)
- 每个工作表的详细信息(名称、行数、列数)
- 所有单元格数据
- 公式映射表
- 合并单元格范围

### 🧪 测试

添加了完整的测试脚本:
- `test_excel_parsing.py` - 完整功能测试
- `demo_excel_parsing.py` - 快速演示脚本

### 📚 文档更新

- 更新 README.md 添加 Excel 解析说明和示例
- 新增 `docs/excel_parsing_feature.md` 详细功能文档
- 更新工具描述以反映 Excel 支持

### 🎯 使用场景

1. **数据分析** - 提取 Excel 表格数据进行 AI 分析
2. **文档处理** - 批量读取和转换 Excel 文件
3. **自动化工作流** - Excel 数据导入到其他系统
4. **报表生成** - 基于 Excel 数据生成报告

### 🔄 升级指南

从 v0.3.0 升级到 v0.4.0:

```bash
# 使用 npx (推荐)
npx docxtpl-mcp@latest

# 或更新全局安装
npm update -g docxtpl-mcp

# 或在 Claude Code 中更新
claude mcp update docxtpl
```

首次运行会自动安装 `openpyxl` Python 依赖包。

### 🐛 已知问题

- 超大 Excel 文件(>50MB)的解析可能较慢
- 不支持解析图表和嵌入对象
- 仅提取单元格格式的基本信息

### 📈 统计

- 新增代码: ~200 行
- 新增测试: 2 个文件
- 文档更新: 3 个文件
- 新增依赖: 1 个 (openpyxl)

### 🙏 感谢

感谢所有用户的反馈和建议!

---

**完整变更日志**: [v0.3.0...v0.4.0](https://github.com/yourusername/docxtpl-mcp/compare/v0.3.0...v0.4.0)