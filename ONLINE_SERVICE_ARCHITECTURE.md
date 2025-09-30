# DocxTPL Online - 在线文档生成服务平台

## 📋 项目概述

DocxTPL Online 是一个基于现有 docxtpl-mcp 项目扩展的在线 SaaS 平台，让用户能够通过 Web 界面管理模板、生成文档，并支持模板共享和交易。

### 核心特性
- 🌐 **多租户架构** - 支持多用户隔离和权限管理
- 📝 **模板管理** - 在线上传、编辑、版本控制
- 🚀 **API 访问** - RESTful API 和 GraphQL 支持
- 🤝 **模板市场** - 公共模板共享和交易
- 🔒 **安全认证** - JWT + OAuth2.0 支持
- 📊 **数据分析** - 使用统计和报表
- 💰 **计费系统** - 使用量计费和订阅制
- 🔌 **MCP 兼容** - 保持与原 MCP 协议兼容

## 🏗️ 系统架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                         前端应用层                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Web UI  │  │Mobile App│  │  API Docs │  │ Admin UI │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTPS
┌─────────────────────────┴───────────────────────────────────┐
│                      API 网关层 (Nginx)                      │
│            负载均衡 │ 限流 │ 缓存 │ SSL终端                   │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                      应用服务层                               │
│  ┌────────────────────────────────────────────────────┐     │
│  │              FastAPI Application                    │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │     │
│  │  │   Auth   │  │ Template │  │ Document │        │     │
│  │  │  Service │  │  Service │  │ Generator│        │     │
│  │  └──────────┘  └──────────┘  └──────────┘        │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │     │
│  │  │  Market  │  │  Billing │  │Analytics │        │     │
│  │  │  Service │  │  Service │  │  Service │        │     │
│  │  └──────────┘  └──────────┘  └──────────┘        │     │
│  └────────────────────────────────────────────────────┘     │
│                                                              │
│  ┌────────────────────────────────────────────────────┐     │
│  │            MCP Bridge Service                       │     │
│  │         (保持与MCP客户端兼容)                        │     │
│  └────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                        数据层                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │PostgreSQL│  │  Redis   │  │   S3/    │  │  Elastic │   │
│  │(主数据库) │  │  (缓存)  │  │  MinIO   │  │  Search  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                      任务队列层                               │
│              Celery + RabbitMQ/Redis                         │
│         异步任务 │ 定时任务 │ 批量处理                        │
└──────────────────────────────────────────────────────────────┘
```

## 💻 技术栈详细说明

### 后端技术栈

#### 核心框架
- **FastAPI** (v0.100+) - 高性能异步 Web 框架
- **SQLAlchemy** (v2.0+) - ORM 和数据库工具
- **Pydantic** (v2.0+) - 数据验证和序列化
- **Alembic** - 数据库迁移管理

#### 认证与安全
- **python-jose[cryptography]** - JWT token 生成和验证
- **passlib[bcrypt]** - 密码哈希
- **python-multipart** - 文件上传处理
- **authlib** - OAuth2.0 客户端和服务器

#### 任务队列
- **Celery** (v5.3+) - 分布式任务队列
- **celery-beat** - 定时任务调度
- **flower** - Celery 监控工具

#### 文档处理
- **docxtpl** - Word 模板处理（核心）
- **python-docx** - Word 文档操作
- **Jinja2** - 模板引擎
- **Pillow** - 图片处理

#### 存储和缓存
- **boto3** - AWS S3 客户端
- **minio** - MinIO 客户端（S3 兼容）
- **redis-py** - Redis 客户端
- **asyncpg** - PostgreSQL 异步驱动

#### API 文档和测试
- **pytest** - 测试框架
- **pytest-asyncio** - 异步测试支持
- **httpx** - HTTP 客户端测试
- **faker** - 测试数据生成

### 前端技术栈

#### 核心框架
- **React** (v18+) 或 **Vue 3** - UI 框架
- **TypeScript** (v5+) - 类型安全
- **Vite** - 构建工具
- **React Router** / **Vue Router** - 路由管理

#### 状态管理
- **Redux Toolkit** (React) 或 **Pinia** (Vue)
- **React Query** / **Vue Query** - 服务端状态管理

#### UI 组件库
- **Ant Design** (v5+) 或 **Element Plus**
- **TailwindCSS** - 实用优先的 CSS 框架
- **Monaco Editor** - 代码编辑器组件

#### 工具库
- **axios** - HTTP 客户端
- **dayjs** - 日期处理
- **react-hook-form** / **vee-validate** - 表单验证
- **recharts** / **echarts** - 图表库

### 基础设施

#### 容器化
- **Docker** - 容器化
- **Docker Compose** - 本地开发环境
- **Kubernetes** - 生产环境编排

#### 数据库
- **PostgreSQL 15+** - 主数据库
- **Redis 7+** - 缓存和会话存储
- **Elasticsearch 8+** - 全文搜索

#### 消息队列
- **RabbitMQ** 或 **Redis** - 消息代理

#### 监控和日志
- **Prometheus** - 指标收集
- **Grafana** - 可视化监控
- **ELK Stack** - 日志管理
- **Sentry** - 错误追踪

## 📂 项目结构

```
docxtpl-online/
├── backend/                    # 后端服务
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI 应用入口
│   │   ├── core/             # 核心配置
│   │   │   ├── config.py     # 配置管理
│   │   │   ├── security.py   # 安全相关
│   │   │   └── database.py   # 数据库连接
│   │   ├── api/              # API 路由
│   │   │   ├── v1/
│   │   │   │   ├── auth.py   # 认证接口
│   │   │   │   ├── templates.py
│   │   │   │   ├── documents.py
│   │   │   │   ├── market.py
│   │   │   │   └── users.py
│   │   │   └── v2/           # API 版本2
│   │   ├── models/           # 数据模型
│   │   │   ├── user.py
│   │   │   ├── template.py
│   │   │   ├── document.py
│   │   │   └── billing.py
│   │   ├── schemas/          # Pydantic 模式
│   │   │   ├── user.py
│   │   │   ├── template.py
│   │   │   └── document.py
│   │   ├── services/         # 业务逻辑
│   │   │   ├── auth_service.py
│   │   │   ├── template_service.py
│   │   │   ├── document_service.py
│   │   │   ├── storage_service.py
│   │   │   └── billing_service.py
│   │   ├── workers/          # Celery 任务
│   │   │   ├── __init__.py
│   │   │   ├── celery_app.py
│   │   │   ├── document_tasks.py
│   │   │   └── email_tasks.py
│   │   ├── mcp_bridge/       # MCP 协议桥接
│   │   │   ├── server.py
│   │   │   └── handlers.py
│   │   └── utils/            # 工具函数
│   │       ├── docx_processor.py
│   │       ├── validators.py
│   │       └── helpers.py
│   ├── migrations/            # Alembic 迁移
│   │   └── versions/
│   ├── tests/                # 测试
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── requirements.txt      # Python 依赖
│   ├── .env.example          # 环境变量示例
│   └── Dockerfile            # Docker 镜像
│
├── frontend/                  # 前端应用
│   ├── src/
│   │   ├── assets/           # 静态资源
│   │   ├── components/       # 通用组件
│   │   │   ├── Layout/
│   │   │   ├── Forms/
│   │   │   └── Charts/
│   │   ├── pages/           # 页面组件
│   │   │   ├── Home/
│   │   │   ├── Dashboard/
│   │   │   ├── Templates/
│   │   │   ├── Documents/
│   │   │   ├── Market/
│   │   │   └── Settings/
│   │   ├── services/        # API 服务
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   └── templates.ts
│   │   ├── store/           # 状态管理
│   │   │   ├── index.ts
│   │   │   ├── auth.ts
│   │   │   └── templates.ts
│   │   ├── hooks/           # 自定义 Hooks
│   │   ├── utils/           # 工具函数
│   │   ├── types/           # TypeScript 类型
│   │   ├── App.tsx          # 应用入口
│   │   └── main.tsx         # 主入口
│   ├── public/              # 公共文件
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── Dockerfile
│
├── docker/                   # Docker 配置
│   ├── docker-compose.yml   # 开发环境
│   ├── docker-compose.prod.yml
│   └── nginx/
│       └── nginx.conf
│
├── kubernetes/              # K8s 部署配置
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── scripts/                 # 部署和维护脚本
│   ├── deploy.sh
│   ├── backup.sh
│   └── migrate.sh
│
├── docs/                    # 项目文档
│   ├── API.md
│   ├── DEPLOYMENT.md
│   ├── DEVELOPMENT.md
│   └── USER_GUIDE.md
│
├── .github/                 # GitHub Actions
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── .gitignore
├── LICENSE
└── README.md
```

## 🗄️ 数据库设计

### 核心数据表

```sql
-- 用户表
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT true,
    is_superuser BOOLEAN DEFAULT false,
    email_verified BOOLEAN DEFAULT false,
    avatar_url VARCHAR(500),
    subscription_tier VARCHAR(50) DEFAULT 'free',
    api_key VARCHAR(255) UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- 模板表
CREATE TABLE templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    tags TEXT[],
    file_path VARCHAR(500),
    file_size INTEGER,
    thumbnail_url VARCHAR(500),
    variables JSONB,  -- 存储模板变量信息
    schema JSONB,     -- 存储字段验证规则
    is_public BOOLEAN DEFAULT false,
    is_featured BOOLEAN DEFAULT false,
    price DECIMAL(10, 2) DEFAULT 0,
    usage_count INTEGER DEFAULT 0,
    rating DECIMAL(3, 2),
    version INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, name, version)
);

-- 模板版本表
CREATE TABLE template_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id UUID REFERENCES templates(id) ON DELETE CASCADE,
    version_number INTEGER NOT NULL,
    file_path VARCHAR(500),
    changelog TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id)
);

-- 文档生成记录表
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    template_id UUID REFERENCES templates(id),
    document_name VARCHAR(255),
    file_path VARCHAR(500),
    file_size INTEGER,
    input_data JSONB,
    generation_time_ms INTEGER,
    status VARCHAR(50), -- pending, processing, completed, failed
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE
);

-- 模板共享表
CREATE TABLE template_shares (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id UUID REFERENCES templates(id) ON DELETE CASCADE,
    shared_by UUID REFERENCES users(id),
    shared_with UUID REFERENCES users(id),
    permission VARCHAR(50), -- view, use, edit
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 模板市场交易表
CREATE TABLE marketplace_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id UUID REFERENCES templates(id),
    buyer_id UUID REFERENCES users(id),
    seller_id UUID REFERENCES users(id),
    price DECIMAL(10, 2),
    commission DECIMAL(10, 2),
    payment_method VARCHAR(50),
    transaction_id VARCHAR(255),
    status VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- API 使用记录表
CREATE TABLE api_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    endpoint VARCHAR(255),
    method VARCHAR(10),
    request_body_size INTEGER,
    response_body_size INTEGER,
    status_code INTEGER,
    response_time_ms INTEGER,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 用户订阅表
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    plan_name VARCHAR(100),
    price_monthly DECIMAL(10, 2),
    document_limit INTEGER,
    storage_limit_mb INTEGER,
    api_rate_limit INTEGER,
    features JSONB,
    status VARCHAR(50), -- active, cancelled, expired
    started_at TIMESTAMP WITH TIME ZONE,
    ends_at TIMESTAMP WITH TIME ZONE,
    cancelled_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX idx_templates_user_id ON templates(user_id);
CREATE INDEX idx_templates_is_public ON templates(is_public);
CREATE INDEX idx_templates_category ON templates(category);
CREATE INDEX idx_documents_user_id ON documents(user_id);
CREATE INDEX idx_documents_template_id ON documents(template_id);
CREATE INDEX idx_documents_status ON documents(status);
CREATE INDEX idx_api_usage_user_id ON api_usage(user_id);
CREATE INDEX idx_api_usage_created_at ON api_usage(created_at);

-- 创建触发器更新 updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_templates_updated_at BEFORE UPDATE ON templates
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

## 🔐 API 设计

### RESTful API 端点

#### 认证相关
```
POST   /api/v1/auth/register        # 用户注册
POST   /api/v1/auth/login           # 用户登录
POST   /api/v1/auth/refresh         # 刷新 token
POST   /api/v1/auth/logout          # 用户登出
POST   /api/v1/auth/forgot-password # 忘记密码
POST   /api/v1/auth/reset-password  # 重置密码
GET    /api/v1/auth/verify-email    # 邮箱验证
```

#### 用户管理
```
GET    /api/v1/users/me             # 获取当前用户信息
PUT    /api/v1/users/me             # 更新用户信息
DELETE /api/v1/users/me             # 删除账号
GET    /api/v1/users/me/api-keys    # 获取 API 密钥
POST   /api/v1/users/me/api-keys    # 生成新 API 密钥
DELETE /api/v1/users/me/api-keys/{key_id} # 删除 API 密钥
```

#### 模板管理
```
GET    /api/v1/templates            # 获取模板列表
POST   /api/v1/templates            # 创建新模板
GET    /api/v1/templates/{id}       # 获取模板详情
PUT    /api/v1/templates/{id}       # 更新模板
DELETE /api/v1/templates/{id}       # 删除模板
POST   /api/v1/templates/{id}/duplicate # 复制模板
GET    /api/v1/templates/{id}/variables # 获取模板变量
POST   /api/v1/templates/{id}/validate  # 验证模板
GET    /api/v1/templates/{id}/versions  # 获取版本历史
POST   /api/v1/templates/{id}/share     # 共享模板
```

#### 文档生成
```
POST   /api/v1/documents/generate   # 生成文档
GET    /api/v1/documents            # 获取文档列表
GET    /api/v1/documents/{id}       # 获取文档详情
GET    /api/v1/documents/{id}/download # 下载文档
DELETE /api/v1/documents/{id}       # 删除文档
POST   /api/v1/documents/batch      # 批量生成文档
```

#### 模板市场
```
GET    /api/v1/marketplace          # 浏览市场模板
GET    /api/v1/marketplace/{id}     # 模板详情
POST   /api/v1/marketplace/{id}/purchase # 购买模板
POST   /api/v1/marketplace/{id}/rate     # 评价模板
GET    /api/v1/marketplace/categories    # 获取分类
GET    /api/v1/marketplace/trending      # 热门模板
```

#### 统计分析
```
GET    /api/v1/analytics/usage      # 使用统计
GET    /api/v1/analytics/documents  # 文档统计
GET    /api/v1/analytics/api        # API 使用统计
GET    /api/v1/analytics/storage    # 存储使用情况
```

### GraphQL API

```graphql
type Query {
  # 用户相关
  me: User
  user(id: ID!): User

  # 模板相关
  templates(
    filter: TemplateFilter
    pagination: PaginationInput
  ): TemplateConnection!

  template(id: ID!): Template

  # 文档相关
  documents(
    filter: DocumentFilter
    pagination: PaginationInput
  ): DocumentConnection!

  document(id: ID!): Document

  # 市场相关
  marketplace(
    category: String
    search: String
    pagination: PaginationInput
  ): MarketplaceConnection!
}

type Mutation {
  # 认证
  register(input: RegisterInput!): AuthPayload!
  login(input: LoginInput!): AuthPayload!

  # 模板操作
  createTemplate(input: CreateTemplateInput!): Template!
  updateTemplate(id: ID!, input: UpdateTemplateInput!): Template!
  deleteTemplate(id: ID!): Boolean!

  # 文档生成
  generateDocument(input: GenerateDocumentInput!): Document!

  # 市场交易
  purchaseTemplate(templateId: ID!): Transaction!
}

type Subscription {
  documentGenerated(userId: ID!): Document!
  templateUpdated(templateId: ID!): Template!
}
```

## 🚀 部署方案

### 开发环境部署

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/docxtpl-online.git
cd docxtpl-online

# 2. 设置环境变量
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 3. 启动 Docker Compose
docker-compose up -d

# 4. 运行数据库迁移
docker-compose exec backend alembic upgrade head

# 5. 创建超级用户
docker-compose exec backend python scripts/create_superuser.py

# 6. 访问应用
# 前端: http://localhost:3000
# 后端: http://localhost:8000
# API 文档: http://localhost:8000/docs
```

### 生产环境部署 (Kubernetes)

```yaml
# deployment.yaml 示例
apiVersion: apps/v1
kind: Deployment
metadata:
  name: docxtpl-backend
  namespace: docxtpl
spec:
  replicas: 3
  selector:
    matchLabels:
      app: docxtpl-backend
  template:
    metadata:
      labels:
        app: docxtpl-backend
    spec:
      containers:
      - name: backend
        image: docxtpl/backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: docxtpl-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: docxtpl-secrets
              key: redis-url
        - name: S3_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: docxtpl-secrets
              key: s3-access-key
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### CI/CD 流程 (GitHub Actions)

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r backend/requirements.txt
        pip install -r backend/requirements-dev.txt

    - name: Run tests
      run: |
        cd backend
        pytest tests/ --cov=app --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./backend/coverage.xml

  build-and-push:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push backend
      uses: docker/build-push-action@v4
      with:
        context: ./backend
        push: true
        tags: docxtpl/backend:latest

    - name: Build and push frontend
      uses: docker/build-push-action@v4
      with:
        context: ./frontend
        push: true
        tags: docxtpl/frontend:latest

  deploy:
    needs: build-and-push
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to Kubernetes
      uses: azure/k8s-deploy@v4
      with:
        manifests: |
          kubernetes/deployment.yaml
          kubernetes/service.yaml
        images: |
          docxtpl/backend:latest
          docxtpl/frontend:latest
```

## 📈 监控和运维

### 监控指标

```yaml
# prometheus-rules.yaml
groups:
  - name: docxtpl_alerts
    rules:
    - alert: HighErrorRate
      expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
      for: 5m
      annotations:
        summary: "High error rate detected"
        description: "Error rate is above 5% for 5 minutes"

    - alert: HighResponseTime
      expr: http_request_duration_seconds{quantile="0.99"} > 2
      for: 5m
      annotations:
        summary: "High response time"
        description: "99th percentile response time is above 2s"

    - alert: LowDiskSpace
      expr: node_filesystem_avail_bytes / node_filesystem_size_bytes < 0.1
      for: 5m
      annotations:
        summary: "Low disk space"
        description: "Less than 10% disk space remaining"
```

### 日志管理

```python
# backend/app/core/logging.py
import logging
from pythonjsonlogger import jsonlogger

def setup_logging():
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logHandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

    # 添加请求 ID 到日志
    import contextvars
    request_id = contextvars.ContextVar('request_id', default=None)

    class RequestIdFilter(logging.Filter):
        def filter(self, record):
            record.request_id = request_id.get()
            return True

    logger.addFilter(RequestIdFilter())
```

## 🔒 安全措施

### 安全清单

- [x] **认证和授权**
  - JWT token 认证
  - OAuth2.0 支持 (Google, GitHub)
  - 基于角色的访问控制 (RBAC)
  - API 密钥管理

- [x] **数据保护**
  - 密码使用 bcrypt 哈希
  - 敏感数据加密存储
  - HTTPS 强制使用
  - SQL 注入防护 (使用 ORM)

- [x] **文件安全**
  - 文件类型验证
  - 文件大小限制
  - 病毒扫描集成
  - 安全的文件存储路径

- [x] **API 安全**
  - 速率限制
  - CORS 配置
  - 请求大小限制
  - API 版本控制

- [x] **监控和审计**
  - 访问日志记录
  - 异常监控 (Sentry)
  - 安全事件告警
  - 定期安全审计

## 💰 商业模式

### 订阅计划

| 特性 | 免费版 | 基础版 | 专业版 | 企业版 |
|------|--------|--------|--------|--------|
| 价格/月 | $0 | $9.99 | $29.99 | 联系销售 |
| 文档生成/月 | 10 | 100 | 1000 | 无限 |
| 模板数量 | 3 | 20 | 100 | 无限 |
| 存储空间 | 100MB | 1GB | 10GB | 自定义 |
| API 访问 | ❌ | ✅ | ✅ | ✅ |
| 自定义域名 | ❌ | ❌ | ✅ | ✅ |
| 优先支持 | ❌ | Email | Email + Chat | 24/7 专属 |
| 模板市场收入 | 70% | 80% | 90% | 95% |

### 收入来源

1. **订阅收入** - 月度/年度订阅
2. **交易佣金** - 模板市场交易抽成 (5-30%)
3. **API 使用费** - 按使用量计费
4. **企业定制** - 私有化部署和定制开发
5. **增值服务** - 模板定制、培训、咨询

## 📊 关键性能指标 (KPIs)

### 技术指标
- API 响应时间 < 200ms (p95)
- 文档生成时间 < 5秒 (普通文档)
- 系统可用性 > 99.9%
- 并发用户支持 > 10,000

### 业务指标
- 月活跃用户 (MAU)
- 付费转化率
- 客户获取成本 (CAC)
- 用户生命周期价值 (LTV)
- 月度经常性收入 (MRR)

## 🗺️ 开发路线图

### 第一阶段 (MVP) - 3个月
- [x] 基础用户认证系统
- [x] 模板上传和管理
- [x] 文档生成 API
- [x] 简单的 Web 界面
- [ ] 基础计费系统

### 第二阶段 (增强) - 2个月
- [ ] 模板市场功能
- [ ] 高级模板编辑器
- [ ] 批量文档生成
- [ ] API 文档和 SDK
- [ ] 多语言支持

### 第三阶段 (扩展) - 2个月
- [ ] AI 辅助模板创建
- [ ] 团队协作功能
- [ ] 高级分析仪表板
- [ ] Webhook 集成
- [ ] 移动应用

### 第四阶段 (优化) - 持续
- [ ] 性能优化
- [ ] 安全加固
- [ ] 用户体验改进
- [ ] 新功能迭代

## 🚦 快速开始指南

### 后端开发

```bash
# 1. 设置 Python 虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 安装依赖
cd backend
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 3. 设置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库等

# 4. 运行数据库迁移
alembic upgrade head

# 5. 启动开发服务器
uvicorn app.main:app --reload --port 8000

# 6. 运行测试
pytest tests/
```

### 前端开发

```bash
# 1. 安装依赖
cd frontend
npm install

# 2. 设置环境变量
cp .env.example .env.local
# 编辑 .env.local，配置 API 端点等

# 3. 启动开发服务器
npm run dev

# 4. 构建生产版本
npm run build

# 5. 运行测试
npm test
```

### Docker 开发环境

```bash
# 构建并启动所有服务
docker-compose up --build

# 查看日志
docker-compose logs -f backend
docker-compose logs -f frontend

# 进入容器
docker-compose exec backend bash
docker-compose exec frontend sh

# 清理环境
docker-compose down -v
```

## 📝 代码示例

### 后端 API 示例

```python
# backend/app/api/v1/templates.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.template import Template
from app.schemas.template import TemplateCreate, TemplateResponse
from app.services.template_service import TemplateService

router = APIRouter(prefix="/templates", tags=["templates"])

@router.post("/", response_model=TemplateResponse)
async def create_template(
    *,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    file: UploadFile = File(...),
    name: str,
    description: str = None,
    category: str = None,
    is_public: bool = False
):
    """
    创建新模板
    """
    service = TemplateService(db)

    # 验证文件类型
    if not file.filename.endswith('.docx'):
        raise HTTPException(
            status_code=400,
            detail="Only .docx files are allowed"
        )

    # 创建模板
    template = await service.create_template(
        user_id=current_user.id,
        file=file,
        name=name,
        description=description,
        category=category,
        is_public=is_public
    )

    return template

@router.get("/", response_model=List[TemplateResponse])
async def list_templates(
    *,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    skip: int = 0,
    limit: int = 20,
    category: str = None,
    is_public: bool = None
):
    """
    获取模板列表
    """
    service = TemplateService(db)
    templates = await service.list_templates(
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        category=category,
        is_public=is_public
    )
    return templates

@router.post("/{template_id}/generate", response_model=DocumentResponse)
async def generate_document(
    *,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    template_id: str,
    data: dict
):
    """
    使用模板生成文档
    """
    service = TemplateService(db)

    # 检查权限
    template = await service.get_template(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")

    if template.user_id != current_user.id and not template.is_public:
        raise HTTPException(status_code=403, detail="Access denied")

    # 生成文档
    document = await service.generate_document(
        template_id=template_id,
        user_id=current_user.id,
        data=data
    )

    return document
```

### 前端组件示例

```tsx
// frontend/src/pages/Templates/TemplateList.tsx
import React, { useState, useEffect } from 'react';
import { Card, Button, Table, Space, Modal, message } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';
import { useQuery, useMutation } from 'react-query';

import { templateApi } from '@/services/api';
import { Template } from '@/types';

const TemplateList: React.FC = () => {
  const navigate = useNavigate();
  const [selectedTemplate, setSelectedTemplate] = useState<Template | null>(null);

  // 获取模板列表
  const { data: templates, isLoading, refetch } = useQuery(
    'templates',
    () => templateApi.list(),
    {
      onError: (error) => {
        message.error('Failed to load templates');
      }
    }
  );

  // 删除模板
  const deleteMutation = useMutation(
    (id: string) => templateApi.delete(id),
    {
      onSuccess: () => {
        message.success('Template deleted successfully');
        refetch();
      },
      onError: () => {
        message.error('Failed to delete template');
      }
    }
  );

  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Category',
      dataIndex: 'category',
      key: 'category',
    },
    {
      title: 'Created',
      dataIndex: 'created_at',
      key: 'created_at',
      render: (date: string) => new Date(date).toLocaleDateString(),
    },
    {
      title: 'Public',
      dataIndex: 'is_public',
      key: 'is_public',
      render: (isPublic: boolean) => (isPublic ? 'Yes' : 'No'),
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (_, record: Template) => (
        <Space>
          <Button
            icon={<EditOutlined />}
            onClick={() => navigate(`/templates/${record.id}/edit`)}
          >
            Edit
          </Button>
          <Button
            danger
            icon={<DeleteOutlined />}
            onClick={() => handleDelete(record.id)}
          >
            Delete
          </Button>
        </Space>
      ),
    },
  ];

  const handleDelete = (id: string) => {
    Modal.confirm({
      title: 'Delete Template',
      content: 'Are you sure you want to delete this template?',
      onOk: () => deleteMutation.mutate(id),
    });
  };

  return (
    <Card
      title="My Templates"
      extra={
        <Button
          type="primary"
          icon={<PlusOutlined />}
          onClick={() => navigate('/templates/new')}
        >
          New Template
        </Button>
      }
    >
      <Table
        columns={columns}
        dataSource={templates}
        loading={isLoading}
        rowKey="id"
      />
    </Card>
  );
};

export default TemplateList;
```

### MCP 桥接代码示例

```python
# backend/app/mcp_bridge/server.py
import asyncio
from typing import Dict, Any, List
from mcp.server import Server
import mcp.types as types

from app.services.template_service import TemplateService
from app.services.document_service import DocumentService

class MCPBridge:
    """
    MCP 协议桥接器，将 MCP 请求转换为 API 调用
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.server = Server("docxtpl-online")
        self.template_service = TemplateService()
        self.document_service = DocumentService()
        self.setup_handlers()

    def setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> List[types.Tool]:
            return [
                types.Tool(
                    name="generate_document",
                    description="Generate document from template",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "template_id": {
                                "type": "string",
                                "description": "Template ID"
                            },
                            "data": {
                                "type": "object",
                                "description": "Template data"
                            }
                        },
                        "required": ["template_id", "data"]
                    }
                ),
                types.Tool(
                    name="list_templates",
                    description="List available templates",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "Filter by category"
                            }
                        }
                    }
                )
            ]

        @self.server.call_tool()
        async def call_tool(
            name: str,
            arguments: Dict[str, Any]
        ) -> List[types.TextContent]:
            # 验证 API 密钥
            user = await self.authenticate(self.api_key)
            if not user:
                return [types.TextContent(
                    type="text",
                    text="Authentication failed"
                )]

            if name == "generate_document":
                result = await self.document_service.generate(
                    user_id=user.id,
                    template_id=arguments["template_id"],
                    data=arguments["data"]
                )
                return [types.TextContent(
                    type="text",
                    text=f"Document generated: {result['document_id']}"
                )]

            elif name == "list_templates":
                templates = await self.template_service.list(
                    user_id=user.id,
                    category=arguments.get("category")
                )
                return [types.TextContent(
                    type="text",
                    text=f"Found {len(templates)} templates"
                )]

    async def authenticate(self, api_key: str):
        # 验证 API 密钥并返回用户
        # 实现省略
        pass

    async def run(self):
        # 启动 MCP 服务器
        await self.server.run()
```

## 🤝 团队和贡献

### 核心团队角色
- **项目负责人** - 整体架构和产品方向
- **后端开发** - API 和业务逻辑开发
- **前端开发** - UI/UX 实现
- **DevOps** - 部署和运维
- **QA** - 测试和质量保证

### 贡献指南
1. Fork 项目仓库
2. 创建功能分支
3. 提交代码并编写测试
4. 创建 Pull Request
5. 代码审查和合并

## 📚 参考资源

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

---

**注意**: 这是一个完整的技术架构文档，可以作为新项目的开发指南。请根据实际需求进行调整和优化。

如有任何问题或需要进一步的技术细节，请随时询问！