# Word 模板使用说明

## 可用模板列表

### 1. invoice.docx - 发票模板
**必需变量：**
- company_name: 公司名称
- company_address: 公司地址
- company_email: 公司邮箱
- company_phone: 公司电话
- customer_name: 客户名称
- customer_address: 客户地址
- customer_email: 客户邮箱
- invoice_number: 发票号
- invoice_date: 开票日期
- due_date: 到期日期
- items: 商品列表 (数组)
  - description: 商品描述
  - quantity: 数量
  - unit_price: 单价
  - total: 小计
- subtotal: 小计金额
- tax_rate: 税率
- tax_amount: 税额
- total: 总计
- notes: 备注
- terms: 条款

### 2. report.docx - 报告模板
**必需变量：**
- report_title: 报告标题
- report_subtitle: 副标题
- author_name: 作者姓名
- department: 部门
- report_date: 报告日期
- executive_summary: 执行摘要
- sections: 章节列表 (数组)
  - title: 章节标题
  - content: 章节内容
  - subsections: 子章节 (可选)
  - table: 数据表 (可选)
- conclusions: 结论
- recommendations: 建议列表 (数组)
- appendices: 附录

### 3. contract.docx - 合同模板
**必需变量：**
- contract_type: 合同类型
- contract_number: 合同编号
- contract_date: 合同日期
- party1_name: 甲方全称
- party1_address: 甲方地址
- party1_short_name: 甲方简称
- party2_name: 乙方全称
- party2_address: 乙方地址
- party2_short_name: 乙方简称
- whereas_clause: 鉴于条款
- clauses: 条款列表 (数组)
  - title: 条款标题
  - content: 条款内容
  - subclauses: 子条款 (可选)
- party1_signatory: 甲方签字人
- party1_title: 甲方职务
- party2_signatory: 乙方签字人
- party2_title: 乙方职务
- signature_date1: 甲方签字日期
- signature_date2: 乙方签字日期

### 4. letter.docx - 信函模板
**必需变量：**
- sender_name: 发件人姓名
- sender_address: 发件人地址
- sender_city: 发件人城市
- sender_state: 发件人州/省
- sender_zip: 发件人邮编
- sender_email: 发件人邮箱
- sender_phone: 发件人电话
- letter_date: 信函日期
- recipient_name: 收件人姓名
- recipient_title: 收件人职务
- recipient_company: 收件人公司
- recipient_address: 收件人地址
- recipient_city: 收件人城市
- recipient_state: 收件人州/省
- recipient_zip: 收件人邮编
- salutation: 称呼
- body_paragraphs: 正文段落 (数组)
- closing: 结束语
- sender_title: 发件人职务

**可选变量：**
- subject: 主题
- enclosures: 附件列表 (数组)
- cc_list: 抄送列表 (数组)

## 使用示例

### 生成发票
```json
{
  "template_name": "invoice.docx",
  "context_data": {
    "company_name": "ABC Tech Inc.",
    "company_address": "123 Main St, Suite 100",
    "company_email": "info@abctech.com",
    "company_phone": "+1-234-567-8900",
    "customer_name": "XYZ Corp",
    "customer_address": "456 Oak Ave",
    "customer_email": "billing@xyzcorp.com",
    "invoice_number": "INV-2024-001",
    "invoice_date": "2024-09-28",
    "due_date": "2024-10-28",
    "items": [
      {
        "description": "Software License",
        "quantity": 10,
        "unit_price": 99.99,
        "total": 999.90
      },
      {
        "description": "Support Service",
        "quantity": 1,
        "unit_price": 500.00,
        "total": 500.00
      }
    ],
    "subtotal": 1499.90,
    "tax_rate": 10,
    "tax_amount": 149.99,
    "total": 1649.89,
    "notes": "Thank you for your business!",
    "terms": "Payment due within 30 days"
  }
}
```

## 自定义过滤器

模板中可以使用以下自定义过滤器：

- **currency**: 格式化为货币显示（例：{{amount|currency}} → $1,234.56）
- **date**: 格式化日期（例：{{date|date}} → September 28, 2024）

## 注意事项

1. 所有模板文件必须放在 `templates` 目录下
2. 模板文件必须是 .docx 格式
3. 使用 {{variable}} 语法插入变量
4. 使用 {% for %} 语法进行循环
5. 使用 {% if %} 语法进行条件判断
6. 生成的文档会保存在 `output` 目录下
