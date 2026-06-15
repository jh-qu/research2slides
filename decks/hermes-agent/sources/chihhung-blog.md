# Source: Hermes Agent 生態系教學手冊

**URL**: https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/hermes-agent%E7%94%9F%E6%85%8B%E7%B3%BB%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/  
**Version covered**: v0.15.2  
**Fetched**: 2026-06-15  
**Language**: 繁體中文

## 定位與特色

Hermes 區別於傳統 ChatGPT 的關鍵：
- 跨對話持久記憶
- 自動技能學習迴圈
- 23+ 通訊平台原生支援
- 支援任意 OpenAI-compatible 模型（含免費 Nous Portal）
- MIT 授權開源

## 版本里程碑

| 版本 | 日期 | 重點 |
|------|------|------|
| v0.12.0 | 2026-04-30 | Autonomous Curator 自動技能維護 |
| v0.13.0 | 2026-05-07 | Multi-agent Kanban、`/goal` 跨回合目標追蹤 |
| v0.14.0 | 2026-05-16 | Foundation Release — PyPI 安裝、`hermes proxy` OpenAI 相容代理 |
| v0.15.0 | 2026-05-28 | Velocity Release — 代碼行數減 76%、Bitwarden 秘密管理、Skill Bundles |

## 系統架構

分層設計：

```
展示層（23 平台 + Web Dashboard）
  → API Gateway
  → Agent Core
  → 記憶層
  → 工具層（60+ 內建工具）
  → 資料層
```

支援多 Agent 協作、子代理平行委派、持久化 Kanban 看板管理。

## 核心機制

1. **Learning Loop**：複雜任務完成後自動回顧、提取經驗、封裝為可重用 Skill
2. **記憶系統**：短期（Context Window）→ 中期（FTS5 全文搜尋）→ 長期（MEMORY.md + 向量 DB）
3. **Tool Calling**：支援 MCP、6 種執行後端（本地/Docker/SSH/Modal/Daytona）
4. **模型路由**：支援 Anthropic、OpenAI、Qwen、xAI Grok 等 200+ 模型即時切換

## 部署

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**成本控制建議**：主模型用 Anthropic Claude，輔助模型用免費 Nous Portal MiMo v2 Pro。

## 企業級特性

- **Bitwarden 秘密管理**（v0.15.0）：統一 API Key 管理
- **Promptware 防禦**（v0.15.0）：Brainworm-class 攻擊防護
- **Multi-agent Kanban**：心跳監測、殭屍偵測、工作回收
- **多 Profile 隔離**：為不同團隊配置專屬 SOUL.md 與技能集

## 開發支援

- 自訂 Skill（Markdown 格式，支援社群共享）
- Plugin 系統：可擴展平台、模型 Provider、工具、Dashboard 元件
- 語音模式：CLI、Telegram、Discord Voice Channel
- Web 整合：FastAPI/Spring Boot 後端封裝、SSE 串流、React/Vue 前端
