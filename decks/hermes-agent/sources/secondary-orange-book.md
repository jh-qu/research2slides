# Source: 花叔《Hermes Agent 橙皮書 2.0》

**URL**: https://github.com/alchaincyf/hermes-agent-orange-book
**Version**: v2.0 (Hermes v0.16.0, 2026-06-07)
**Fetched**: 2026-06-23
**License**: MIT
**Note**: 本書為 21 節 / 6 部分，基於 Hermes v0.16.0 全量重寫，與 Noah 的官方文件互補。

## Meta

- 完整結構：21 節 / 6 部分
- PDF（中文）: https://github.com/alchaincyf/hermes-agent-orange-book/raw/main/Hermes-Agent%E6%A9%99%E7%9A%AE4%B9%A62.0-v260607.pdf
- 定位：繁體中文教學 + 企業導入視角（比官方文件更講敍事）

## 核心主張

> "第一個出廠就帶緮繩、而且緮繩會自己長大的 Agent"

**五大差異化能力**（與 OpenClaw / Claude Code 比）：
1. 自改進學習循環
2. 三層記憶
3. Skill 自動創建與進化
4. 持久化多 Agent 看板（Kanban）
5. 以 OS 為邊界的安全模型

## 21 節摘要

| 節 | 標題 | 內容摘要 |
|---|------|---------|
| §01 | 這是什麼 | Hermes 定位、Nous Research 初衷 |
| §02 | 一個大腦多張臉 | 多平台支援（23 個 messaging platform） |
| §03 | 專案概覽 | 架構、版本路線 |
| §04 | 自改進三引擎 | Skill / Memory / Curator 驅動的學習三引擎 |
| §05 | Curator | 7 天閒置自動整理 Skill 庫 |
| §06 | 最該學的是「不要學」 | 負面學習、避免學到錯誤模式 |
| §07 | 三層記憶 | Context / SQLite / MEMORY.md + 向量 DB |
| §08 | 會話搜索 | session_search 跨對話召回 |
| §09 | Skill 自動進化 | 自動封裝可復用技能 |
| §10 | 指揮一群 Agent | delegate_task / Kanban |
| §11 | 64 個工具 | 內建工具生態、Tool Gateway |
| §12 | MCP | Model Context Protocol，外部工具整合 |
| §13 | 23 個平台 | Telegram / Discord / Slack / LINE 等 |
| §14 | 三個接入面 | 桌面 App / 瀏覽器面板 / CLI |
| §15 | delegate_task | 多 Agent 派工模式 |
| §16 | Kanban | 多 Agent 看板平台詳解 |
| §17 | 八種協作模式 | fan-out / pipeline / review 等 |
| §18 | 部署方案 | Docker / VPS / 自托管 |
| §19 | 唯一邊界是 OS | 安全模型、Docker 沙箱、Gateway 白名單 |
| §20 | Promptware 防禦 | 記憶污染攻擊防護 |
| §21 | 能力邊界 | 什麼做不到、何時不用 Hermes |

## 與 research2slides 的關係

- slides.md 截稿日期 2026.06.12，cover Hermes ~v0.14/v0.15
- 橙皮書 2.0 基於 v0.16.0，多了：
  - 原生桌面 App（native desktop app）
  - 瀏覽器管理面板
  - 23 個 messaging platform
  - Kanban 平台詳解
  - v0.15/v0.16 安全改進細節
- 本書為繁體中文、有企業導入視角，適合補充投影片的「落地」、「場景」章節
