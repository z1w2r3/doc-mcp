# PPT 支持功能实施任务清单

## 📋 项目概述
为 docxtpl MCP 服务器增加 PowerPoint (PPT/PPTX) 支持,包括文档解析和生成功能。

## 🎯 需求分析

### 当前项目状态
- ✅ 已支持: DOCX 生成、DOCX/PDF/Excel 解析
- ✅ 技术栈: python-docx, pdfplumber, openpyxl
- ✅ MCP 架构: 完善的工具注册和错误处理机制
- 📂 发现: output 目录已有 PPT 文件样本

### PPT 功能需求
1. **解析功能** (优先级高)
   - 提取幻灯片内容(文本、标题、备注)
   - 提取表格数据
   - 提取元数据(作者、创建时间等)
   - 支持指定幻灯片范围解析

2. **生成功能** (优先级中)
   - 从模板生成 PPT
   - 支持动态内容填充
   - 支持循环生成多个幻灯片

## 📚 技术选型

### Python PPT 处理库对比

| 库名 | 解析 | 生成 | 复杂度 | 推荐度 |
|-----|------|------|--------|--------|
| **python-pptx** | ✅ 优秀 | ✅ 优秀 | 中等 | ⭐⭐⭐⭐⭐ |
| python-pptx-template | ❌ 无 | ✅ 模板 | 低 | ⭐⭐⭐ |
| PyPPTX | ✅ 基础 | ✅ 基础 | 高 | ⭐⭐ |

**选择**: `python-pptx`
- 功能全面,同时支持解析和生成
- 社区活跃,文档完善
- 与现有技术栈(python-docx)同源,API 相似
- 支持 PPTX 格式(Office 2007+)

## ✅ 实施计划

### 阶段 1: 环境准备
- [ ] 更新 requirements.txt 添加 python-pptx 依赖
- [ ] 测试依赖安装
- [ ] 研究 output 目录中的 PPT 样本文件

### 阶段 2: 解析功能实现 (优先)
- [ ] 实现 parse_ppt_document() 函数
  - [ ] 提取幻灯片内容(标题、文本)
  - [ ] 提取表格数据
  - [ ] 提取图片信息(数量、位置)
  - [ ] 提取元数据
  - [ ] 支持指定幻灯片范围
- [ ] 实现快速文本提取(扩展 extract_text_from_document)
- [ ] 实现元数据提取(扩展 get_document_metadata)

### 阶段 3: MCP 工具注册
- [ ] 在 list_tools() 中注册 parse_ppt_document 工具
- [ ] 更新 extract_text_from_document 支持 PPT
- [ ] 更新 get_document_metadata 支持 PPT
- [ ] 在 call_tool() 中实现工具路由

### 阶段 4: 生成功能实现 (可选)
- [ ] 设计 PPT 模板结构
- [ ] 实现 generate_ppt_document() 函数
- [ ] 支持 Jinja2 模板语法
- [ ] 在 generate_document 中集成 PPT 生成

### 阶段 5: 测试验证
- [ ] 测试 PPT 解析功能
  - [ ] 使用 output/江苏省智能建造试点项目.pptx 测试
  - [ ] 创建更多测试用例
- [ ] 测试边界情况和错误处理
- [ ] 性能测试(大文件处理)

### 阶段 6: 文档更新
- [ ] 更新 README.md 说明 PPT 功能
- [ ] 添加使用示例
- [ ] 更新 package.json keywords
- [ ] 创建演示脚本

## 📝 详细设计

### 1. parse_ppt_document 工具

**输入参数**:
```json
{
  "file_path": "string (必需) - PPT 文件绝对路径",
  "include_tables": "boolean (可选) - 是否提取表格, 默认 true",
  "include_images": "boolean (可选) - 是否提取图片信息, 默认 false",
  "slides": "string (可选) - 幻灯片范围, 如 '1-5' 或 'all', 默认 'all'"
}
```

**输出格式**:
```json
{
  "metadata": {
    "filename": "string",
    "file_size_mb": "number",
    "total_slides": "number",
    "author": "string",
    "title": "string",
    "created": "datetime",
    "modified": "datetime"
  },
  "slides": [
    {
      "slide_number": "number",
      "title": "string",
      "shapes": [
        {
          "shape_type": "text|table|picture",
          "text": "string",
          "position": {"x": 0, "y": 0}
        }
      ],
      "tables": [
        {
          "rows": "number",
          "columns": "number",
          "data": [[]]
        }
      ],
      "notes": "string"
    }
  ],
  "statistics": {
    "total_text_length": "number",
    "total_tables": "number",
    "total_images": "number"
  }
}
```

### 2. 扩展现有工具

**extract_text_from_document**:
- 添加 `.pptx` 格式支持
- 提取所有幻灯片的文本内容
- 格式: `=== Slide 1 ===\nTitle\nContent\n\n`

**get_document_metadata**:
- 添加 `.pptx` 格式支持
- 提取 PPT 核心属性

### 3. PPT 生成功能(可选)

使用 python-pptx-template 或自定义实现:
```python
# 模板变量示例
{{title}}  # 幻灯片标题
{{content}}  # 内容文本
{% for item in items %}  # 循环生成幻灯片
```

## 🔧 实施要点

### 简单性原则
- 每个任务尽可能简单
- 复用现有代码模式(参考 Excel 解析实现)
- 最小化代码变更范围
- 优先实现核心功能,高级功能可后续迭代

### 代码复用
参考现有实现:
- `parse_excel_document`: 结构化数据提取模式
- `parse_pdf_document`: 分页处理和范围解析
- `extract_text_from_document`: 多格式支持模式

### 错误处理
- 文件存在性验证
- 格式验证(.pptx)
- 大小限制检查
- 中文错误提示

## 📊 成功标准

- [ ] python-pptx 依赖安装成功
- [ ] parse_ppt_document 工具正常工作
- [ ] 支持 PPTX 格式解析
- [ ] 返回结构化 JSON 数据
- [ ] 完善的错误处理
- [ ] 文档说明完整
- [ ] 通过所有测试用例

## 🚀 后续优化方向

- [ ] PPT 模板生成功能
- [ ] 图片内容提取和转换
- [ ] 幻灯片布局识别
- [ ] 支持旧版 PPT 格式(.ppt)
- [ ] 批量转换功能
- [ ] 幻灯片预览生成

---

## 📋 任务待办 (Todo Items)

### 阶段 1: 环境准备
- [ ] 添加 python-pptx 到 requirements.txt
- [ ] 测试依赖安装
- [ ] 分析样本 PPT 文件

### 阶段 2: 核心实现
- [ ] 实现 parse_ppt_document() 基础功能
- [ ] 实现幻灯片内容提取
- [ ] 实现表格数据提取
- [ ] 扩展 extract_text_from_document 支持 PPT
- [ ] 扩展 get_document_metadata 支持 PPT

### 阶段 3: MCP 集成
- [ ] 注册 parse_ppt_document 工具
- [ ] 更新 call_tool() 路由
- [ ] 实现错误处理

### 阶段 4: 测试和文档
- [ ] 创建测试脚本
- [ ] 使用样本文件测试
- [ ] 更新 README.md
- [ ] 更新版本号

---

## ✅ 实施总结

### 已完成的工作

**阶段 1: 环境准备** ✅
- ✅ 添加 `python-pptx>=0.6.21` 到 requirements.txt
- ✅ 验证依赖安装成功 (已安装 python-pptx 1.0.2)
- ✅ 分析样本 PPT 文件 (24 张幻灯片, 93.07 MB)

**阶段 2: 核心实现** ✅
- ✅ 实现 `parse_ppt_document()` 函数
  - 提取幻灯片标题和文本内容
  - 提取表格数据
  - 提取图片信息 (位置和尺寸)
  - 提取备注内容
  - 支持指定幻灯片范围 (all, 1-5, 1,3,5)
- ✅ 扩展 `extract_text_from_document` 支持 .pptx
  - 按幻灯片组织文本输出
  - 包含标题、内容和备注
- ✅ 扩展 `get_document_metadata` 支持 .pptx
  - 提取核心属性 (作者、创建时间等)
  - 提取幻灯片尺寸和数量
  - 统计形状和表格数量

**阶段 3: MCP 集成** ✅
- ✅ 在 list_tools() 注册 parse_ppt_document 工具
- ✅ 在 call_tool() 添加路由处理
- ✅ 实现完整的错误处理
  - 文件存在性验证
  - 格式验证 (.pptx)
  - 大小限制检查
  - 中文错误提示

**阶段 4: 测试和文档** ✅
- ✅ 创建测试脚本 (test_ppt_parsing.py)
  - 测试 parse_ppt_document 功能
  - 测试 extract_text_from_document 扩展
  - 测试 get_document_metadata 扩展
  - 测试错误处理
- ✅ 创建演示脚本 (demo_ppt_parsing.py)
- ✅ 更新 README.md
  - 添加 PowerPoint 特性说明
  - 添加 parse_ppt_document 工具文档
  - 添加使用示例
  - 更新其他工具的格式支持说明
- ✅ 更新 package.json
  - 版本号: 0.4.1 → 0.5.0
  - 描述更新包含 PowerPoint
  - 添加关键词: powerpoint, pptx, presentation

### 技术亮点

1. **API 一致性**
   - 与现有文档解析工具保持相同的设计模式
   - 参数命名和返回格式统一
   - 复用验证和错误处理逻辑

2. **功能完整性**
   - ✅ 结构化解析 (parse_ppt_document)
   - ✅ 快速文本提取 (extract_text_from_document)
   - ✅ 元数据提取 (get_document_metadata)
   - ✅ 幻灯片范围控制
   - ✅ 可选的表格和图片信息

3. **代码质量**
   - 简洁清晰的实现
   - 完善的类型注解
   - 详细的中文错误提示
   - 与现有代码风格保持一致

### 功能对比

| 功能 | DOCX | PDF | Excel | PowerPoint |
|-----|------|-----|-------|-----------|
| **结构化解析** | ✅ | ✅ | ✅ | ✅ |
| **快速文本提取** | ✅ | ✅ | ✅ | ✅ |
| **元数据提取** | ✅ | ✅ | ✅ | ✅ |
| **表格提取** | ✅ | ✅ | ✅ | ✅ |
| **范围控制** | - | ✅ (页面) | ✅ (工作表) | ✅ (幻灯片) |
| **图片信息** | - | - | - | ✅ |

### 测试结果

✅ **所有测试通过**:
- parse_ppt_document: 正常解析 PPT 文档
- extract_text_from_document: 成功提取 1,589 字符
- get_document_metadata: 成功提取元数据 (24 张幻灯片)
- 错误处理: 正确处理不存在的文件

⚠️ **已知限制**:
- 默认文件大小限制: 50 MB (可通过 MAX_FILE_SIZE_MB 环境变量调整)
- 仅支持 .pptx 格式 (不支持旧版 .ppt)

### 使用示例

```python
# 解析 PowerPoint 文档
result = await server.parse_ppt_document(
    file_path="/path/to/presentation.pptx",
    include_tables=True,
    include_images=False,
    slides="1-5"
)

# 快速文本提取
result = await server.extract_text_from_document(
    file_path="/path/to/presentation.pptx"
)

# 提取元数据
result = await server.get_document_metadata(
    file_path="/path/to/presentation.pptx"
)
```

### 代码统计

- **新增工具**: 1 个 (parse_ppt_document)
- **扩展工具**: 2 个 (extract_text_from_document, get_document_metadata)
- **新增代码**: ~250 行
- **新增依赖**: 1 个 (python-pptx)
- **新增文件**: 3 个 (测试、演示、分析脚本)

### 后续优化方向

- [ ] 支持旧版 PPT 格式 (.ppt)
- [ ] 图片内容提取和 Base64 编码
- [ ] 幻灯片布局和样式信息
- [ ] 幻灯片缩略图生成
- [ ] 批量处理多个文件
- [ ] 性能优化 (大文件流式处理)
- [ ] PPT 模板生成功能 (可选)

---
**创建时间**: 2025-10-15
**完成时间**: 2025-10-15
**状态**: ✅ 已完成
