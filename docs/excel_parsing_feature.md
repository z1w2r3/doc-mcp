# Excel 解析功能实现说明

## 📋 功能概述

本次更新为 docxtpl-mcp 项目添加了完整的 Excel 文档解析功能,支持 XLSX 和 XLS 格式的 Excel 文件解析。

## ✨ 新增功能

### 1. parse_excel_document 工具

完整的 Excel 文档解析工具,提取结构化数据:

**功能特性:**
- ✅ 支持 .xlsx 和 .xls 格式
- ✅ 解析所有工作表或指定工作表
- ✅ 提取单元格数据(包括日期格式自动转换)
- ✅ 提取公式信息
- ✅ 识别合并单元格
- ✅ 提取工作簿元数据

**使用示例:**
```json
{
  "file_path": "/path/to/file.xlsx",
  "sheet_name": "销售数据",  // 可选,不指定则解析所有工作表
  "include_formulas": true    // 可选,默认 true
}
```

### 2. 扩展现有工具

#### extract_text_from_document
- 新增 Excel 支持 (.xlsx, .xls)
- 快速提取所有工作表的文本数据
- 使用 Tab 分隔的格式展示

#### get_document_metadata
- 新增 Excel 元数据提取
- 包括工作表信息、作者、创建时间等
- 统计单元格总数

## 🔧 技术实现

### 依赖库

添加了 `openpyxl>=3.0.0` 库,用于读取和解析 Excel 文件。

### 核心实现

1. **文件验证**
   - 文件存在性检查
   - 格式验证 (.xlsx, .xls)
   - 文件大小限制检查

2. **数据提取**
   - 使用 `load_workbook()` 加载工作簿
   - 遍历工作表提取单元格数据
   - 日期和时间自动转换为 ISO 格式
   - 公式提取(需要重新打开文件获取公式字符串)

3. **元数据处理**
   - 工作簿属性(创建者、标题、主题等)
   - 工作表统计信息
   - 单元格和公式计数

### 输出格式

解析结果采用 JSON 格式:

```json
{
  "metadata": {
    "filename": "example.xlsx",
    "file_size_mb": 0.5,
    "sheets_count": 3,
    "sheet_names": ["Sheet1", "Sheet2", "Sheet3"],
    "creator": "用户名",
    "created": "2025-01-01T00:00:00",
    "modified": "2025-01-15T12:30:00"
  },
  "sheets": [
    {
      "name": "Sheet1",
      "rows": 100,
      "columns": 10,
      "data": [
        ["Header1", "Header2", "Header3"],
        ["Value1", 123, "2025-01-01"],
        ...
      ],
      "merged_cells": ["A1:B1"],
      "formulas": {
        "D2": "=SUM(A2:C2)"
      }
    }
  ],
  "total_sheets_parsed": 1
}
```

## 📝 更新的文件

### 核心文件
- ✅ [src/server.py](../src/server.py) - 添加 Excel 解析逻辑
- ✅ [requirements.txt](../requirements.txt) - 添加 openpyxl 依赖

### 文档文件
- ✅ [README.md](../README.md) - 更新功能说明和示例

### 测试文件
- ✅ [test_excel_parsing.py](../test_excel_parsing.py) - 完整的测试脚本
- ✅ [demo_excel_parsing.py](../demo_excel_parsing.py) - 演示脚本

### 配置文件
- ✅ [package.json](../package.json) - 更新描述和关键词

## 🧪 测试

运行测试脚本:

```bash
# 完整测试
python test_excel_parsing.py

# 快速演示
python demo_excel_parsing.py
```

测试覆盖:
- ✅ 创建测试 Excel 文件
- ✅ 解析所有工作表
- ✅ 解析指定工作表
- ✅ 快速文本提取
- ✅ 元数据提取

## 🎯 使用场景

1. **数据分析**
   - 提取 Excel 中的表格数据进行分析
   - 转换 Excel 数据为 JSON 格式

2. **文档处理**
   - 批量读取 Excel 文件
   - 提取特定工作表的数据

3. **自动化工作流**
   - Excel 数据导入到其他系统
   - 报表数据提取和处理

4. **AI 辅助分析**
   - Claude 分析 Excel 数据
   - 基于 Excel 数据生成报告

## 🚀 后续优化方向

1. **性能优化**
   - 大文件分块读取
   - 并行处理多个工作表

2. **功能增强**
   - 图表信息提取
   - 样式和格式信息
   - 条件格式规则提取

3. **错误处理**
   - 更详细的错误信息
   - 损坏文件的容错处理

## 📚 相关资源

- [openpyxl 文档](https://openpyxl.readthedocs.io/)
- [Excel 文件格式规范](https://docs.microsoft.com/en-us/openspecs/office_standards/)
- [MCP 协议文档](https://modelcontextprotocol.io/)

## ✅ 完成状态

- [x] 添加 Python 依赖
- [x] 实现 parse_excel_document 工具
- [x] 扩展 extract_text_from_document 支持 Excel
- [x] 扩展 get_document_metadata 支持 Excel
- [x] 更新文档
- [x] 创建测试脚本
- [x] 代码语法验证

---

**实现日期:** 2025-09-30
**版本:** 0.4.0 (待发布)