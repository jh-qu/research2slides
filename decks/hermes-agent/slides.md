---
theme: seriph
background: /hero-art.webp
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Hermes Agent 技術評估
mdc: true
---

# Hermes Agent

### 自我改進 AI Agent 框架技術評估

<div class="pt-12 text-gray-200">
  Nous Research ・ 技術評估報告 ・ 2026.06.12
</div>

---
layout: center
class: text-center
---

# 這個名字，不只是個名字

<div class="text-6xl mt-8">𓂀</div>

<div class="text-gray-600 mt-6 text-lg">
  Hermes・Hermès・Harness
</div>

---
layout: default
---

# Hermes — 眾神的信使

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-5xl mb-4">⚡</div>
    <p class="text-gray-800 leading-relaxed">
      在希臘神話中，<strong class="text-amber-600">赫爾墨斯（Hermēs）</strong>是奧林匹斯十二主神中最靈活的一位——身兼眾神信使、商業之神、邊界之神。
    </p>
    <p class="text-gray-800 leading-relaxed mt-4">
      他穿梭於神界與人界之間，傳遞訊息、調度資源，從不受邊界束縛。
    </p>
    <div class="mt-6 text-sm text-gray-600">
      讀音：英文 <span class="text-gray-700 font-mono">HUR-meez</span>・法文 <span class="text-gray-700 font-mono">air-MEZ</span>
    </div>
  </div>
  <div class="flex flex-col gap-4 justify-center">
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-yellow-700 font-bold mb-1">📨 信使</div>
      <div class="text-gray-700">在模型、工具與平台之間傳遞指令</div>
    </div>
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-blue-700 font-bold mb-1">🌐 邊界之神</div>
      <div class="text-gray-700">自由穿越 Telegram、Slack、Discord 等邊界</div>
    </div>
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-green-700 font-bold mb-1">⚡ 速度與智慧</div>
      <div class="text-gray-700">快速、可靠地執行與學習</div>
    </div>
  </div>
</div>

---
layout: default
---

# Hermès → Harness — 從馬具到 AI

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🐎</div>
    <div class="font-bold text-orange-700 mb-2">Hermès 愛馬仕</div>
    <div class="text-sm text-gray-700">
      1837 年，創辦人 Thierry Hermès 開設<strong class="text-gray-900">高級馬具工坊</strong>，專為貴族馴馬、駕馭烈馬
    </div>
  </div>
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🔧</div>
    <div class="font-bold text-blue-700 mb-2">Harness 馬具</div>
    <div class="text-sm text-gray-700">
      軟體工程中，<strong class="text-gray-900">Harness</strong> 指「測試框架或控制套件」——將難以預測的事物引導、馴服
    </div>
  </div>
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🤖</div>
    <div class="font-bold text-green-700 mb-2">Agent Harness</div>
    <div class="text-sm text-gray-700">
      <strong class="text-gray-900">駕馭大語言模型</strong>，將難以預測的 AI 引導發揮最大效能
    </div>
  </div>
</div>

<div class="mt-6 p-4 bg-gray-800 rounded-lg border border-gray-600 text-center">
  <span class="text-gray-100 text-sm">神話信使・奢華馬具・AI 框架——三個世界，同一個名字</span>
</div>

---
layout: two-cols
---

# 專案概覽

<v-clicks>

- **名稱**：Hermes Agent
- **開發方**：Nous Research
- **授權**：MIT（可免費商用）
- **定位**：「The self-improving AI agent」
- **主要語言**：Python 82.6%、TypeScript 13.4%

</v-clicks>

::right::

<div class="flex flex-col gap-6 mt-8 ml-8 text-center">
  <div>
    <div class="text-5xl font-bold text-blue-600">195K</div>
    <div class="text-gray-600 text-sm mt-1">GitHub Stars</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-green-600">34.1K</div>
    <div class="text-gray-600 text-sm mt-1">Forks</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-purple-600">1,415</div>
    <div class="text-gray-600 text-sm mt-1">Contributors</div>
  </div>
</div>

---
layout: default
---

# 核心特色：自我改進學習迴圈

<div class="text-gray-600 italic mb-6">
  「Creates skills from <strong>experience</strong>, improves them during use, builds a <strong>deepening model</strong> of who you are across sessions」
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">🧠</div>
    <strong>持久記憶</strong>
    <p class="text-sm text-gray-700 mt-2">跨對話累積知識，不需每次重頭開始，搭配全文搜尋回溯歷史</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">⚡</div>
    <strong>自動技能生成</strong>
    <p class="text-sm text-gray-700 mt-2">從複雜任務中自動提取可複用技能，累積組織專屬知識庫</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">👤</div>
    <strong>用戶建模</strong>
    <p class="text-sm text-gray-700 mt-2">持續理解使用者偏好，個人化回應方式與工作流程</p>
  </div>
</div>

---
layout: default
---

# 多模型支援 — 200+ 模型，一套框架

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>

| 提供商 | 類型 |
|--------|------|
| OpenRouter | 多模型聚合平台 |
| Nous Portal | Nous 自家模型 |
| OpenAI | GPT 系列 |
| NVIDIA NIM | 企業級推論 |
| Hugging Face | 開源模型 |
| 自訂 Endpoint | 本地 / 私有雲 |

  </div>
  <div class="flex flex-col justify-center">
    <div class="p-4 bg-blue-900 bg-opacity-30 rounded-lg border border-blue-700">
      <div class="font-bold text-black mb-2">💡 對企業的意義</div>
      <p class="text-sm text-black">
        無需改動程式碼即可切換底層模型，降低廠商鎖定風險。未來若有更好或更便宜的模型，可隨時替換。
      </p>
    </div>
  </div>
</div>

---
layout: default
---

# 部署彈性 — 從個人到企業規模

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="border border-green-700 rounded-lg p-5">
    <h3 class="text-green-700 mb-4">🚀 輕量部署</h3>
    <ul class="space-y-2 text-sm">
      <li>✅ 本機終端機（立即可用）</li>
      <li>✅ $5/月 VPS（低成本驗證）</li>
      <li>✅ Docker 容器化</li>
      <li>✅ SSH 遠端機器</li>
    </ul>
  </div>
  <div class="border border-blue-700 rounded-lg p-5">
    <h3 class="text-blue-700 mb-4">🏢 企業部署</h3>
    <ul class="space-y-2 text-sm">
      <li>✅ GPU 叢集（Singularity）</li>
      <li>✅ Serverless（Modal）</li>
      <li>✅ 雲端沙箱（Daytona）</li>
      <li>✅ 多平台訊息閘道</li>
    </ul>
  </div>
</div>

---
layout: default
---

# 多平台整合 — 在現有工具中使用 AI

Agent 透過主流通訊平台操作，使用者不需學新介面

<div class="flex gap-4 mt-6 flex-wrap">
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">💬</div>
    <div class="text-sm mt-1">Telegram</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">🎮</div>
    <div class="text-sm mt-1">Discord</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">💼</div>
    <div class="text-sm mt-1">Slack</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">📱</div>
    <div class="text-sm mt-1">WhatsApp</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">🔒</div>
    <div class="text-sm mt-1">Signal</div>
  </div>
</div>

<div class="mt-6 p-4 bg-yellow-900 bg-opacity-30 rounded-lg border border-yellow-700 text-sm">
  📌 <strong>實際場景：</strong>工程師或業務人員直接在 Slack 發指令給 Agent，完成自動化任務，不需切換工具
</div>

---
layout: default
---

# 架構解析 — 三層設計

```mermaid {scale: 0.75}
flowchart TB
    subgraph IF["① 介面層"]
        direction TB
        cli["CLI / TUI"]
        msg["Telegram · Discord\nSlack · WhatsApp"]
        web["Web Dashboard"]
        ide["VS Code / Zed（ACP）"]
    end
    subgraph AG["② Agent 邏輯層"]
        direction TB
        aa["AIAgent\nrun_agent.py"]
        mt["model_tools.py\n動態工具派發"]
    end
    subgraph EX["③ 執行層"]
        direction TB
        local["Local · Docker · SSH"]
        cloud["Modal · Singularity\n（GPU 叢集）"]
    end
    IF --> AG --> EX
```

---
layout: default
---

# 架構解析 — Runtime Modes & 設定

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-sm font-bold text-gray-500 mb-3">四種啟動入口</div>

| Mode | Entry Point |
|------|-------------|
| CLI | `cli.py` |
| 訊息平台 Gateway | `gateway/run.py` |
| Editor (ACP) | VS Code / Zed 整合 |
| Web UI | 瀏覽器 Dashboard |

  </div>
  <div>
    <div class="text-sm font-bold text-gray-500 mb-3">HERMES_HOME（<span class="font-mono">~/.hermes/</span>）</div>
    <div class="flex flex-col gap-2 text-sm">
      <div class="p-2 bg-gray-100 rounded font-mono">config.yaml <span class="text-gray-500 font-sans">— 模型、工具設定</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">SOUL.md <span class="text-gray-500 font-sans">— Agent 人格定義</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">MEMORY.md <span class="text-gray-500 font-sans">— 長期記憶</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">.env <span class="text-gray-500 font-sans">— API 金鑰</span></div>
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# 深入解析

<div class="text-gray-400 mt-4 text-lg">六個值得關注的技術特色</div>

---
layout: default
---

# Agent 越用越聰明：Learning Loop

```mermaid
flowchart LR
    A["🎯 任務完成"] -->|"自動回顧"| B["📦 封裝 Skill\nskill_manage"]
    B -->|"Python 工具 + MD"| C["💾 MEMORY.md"]
    C -->|"Curator 維護"| D["🤖 Autonomous\nCurator"]
    D -->|"下次自動套用"| A
```

<div class="grid grid-cols-3 gap-2 mt-3">
  <div class="border border-green-600 rounded p-2 text-xs">✅ 重複任務零人工撰碼：同類需求第二次起自動套用</div>
  <div class="border border-green-600 rounded p-2 text-xs">✅ 部門隔離：多 Profile 各自維護專屬 Skill Bundle</div>
  <div class="border border-green-600 rounded p-2 text-xs">✅ 知識不腐化：Curator 自動合併 / 棄用過時 Skill</div>
</div>

<div class="mt-2 p-2 border border-red-500 rounded-lg text-xs text-red-700">
  ⚠️ 企業注意：自動生成的 Skill 無人工審核閘門，受監管環境需自建 code review 流程
</div>

---
layout: default
---

# `SOUL.md`：Agent 行為的版本控制單元

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-xs text-gray-400 mb-2">~/.hermes/SOUL.md</div>
    <div class="p-3 bg-gray-800 rounded text-xs font-mono text-green-300 leading-relaxed">
      # 身份<br>
      你是法務部門的 AI 助理。<br><br>
      # 行為邊界<br>
      不得提供具體法律建議。<br>
      回應需附加「請諮詢專業律師」。
    </div>
    <div class="mt-4 text-xs text-gray-500">啟動時注入 system prompt 前置區段</div>
    <div class="mt-3 p-2 bg-gray-100 rounded text-xs text-gray-700">
      → 可納入 Git 版控、PR review、CI/CD<br>
      ≈ <strong>IaC for Agent behavior</strong>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="border border-gray-300 rounded p-3 text-sm text-center">⚖️ 法務 Agent<br><span class="text-xs text-gray-500">合規語氣 + 免責提示</span></div>
    <div class="border border-gray-300 rounded p-3 text-sm text-center">🎧 客服 Agent<br><span class="text-xs text-gray-500">親切語氣 + 退款授權範圍</span></div>
    <div class="border border-gray-300 rounded p-3 text-sm text-center">🛠 工程 Agent<br><span class="text-xs text-gray-500">技術語氣 + 生產環境禁令</span></div>
  </div>
</div>

<div class="mt-3 p-3 border border-red-500 rounded-lg text-sm text-red-700">
  ⚠️ 純文字，無原生 ACL — 有 HERMES_HOME 寫入權限者可靜默修改人格，建議搭配 OS 層或 Secret Manager 保護
</div>

---
layout: default
---

# 記憶不中斷：三層記憶架構

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="flex flex-col gap-2">
    <div class="border border-blue-400 rounded-lg p-4">
      <div class="text-blue-500 font-bold text-sm mb-1">短期 — Context Window</div>
      <div class="text-xs text-gray-600">當前對話即時推理，會話結束即消失</div>
    </div>
    <div class="flex justify-center text-gray-400 text-xs">▼ 對話結束後寫入</div>
    <div class="border border-purple-400 rounded-lg p-4">
      <div class="text-purple-500 font-bold text-sm mb-1">中期 — SQLite FTS5 全文索引</div>
      <div class="text-xs text-gray-600">跨會話關鍵字召回，毫秒級查詢 ／ Honcho 管理</div>
    </div>
    <div class="flex justify-center text-gray-400 text-xs">▼ 重要資訊持久化</div>
    <div class="border border-green-400 rounded-lg p-4">
      <div class="text-green-500 font-bold text-sm mb-1">長期 — MEMORY.md + 向量 DB</div>
      <div class="text-xs text-gray-600">USER.md 記錄使用者偏好 ／ Skill 知識庫</div>
    </div>
  </div>
  <div class="flex flex-col gap-4 justify-center">
    <div class="p-4 bg-blue-50 rounded-lg border border-blue-200 text-sm">
      💡 <strong>實際場景</strong><br>
      <span class="text-gray-600">三週後繼續同一專案，無需重新交代背景</span>
    </div>
    <div class="p-4 bg-green-50 rounded-lg border border-green-200 text-sm">
      📋 <strong>稽核友善</strong><br>
      <span class="text-gray-600">MEMORY.md 為純文字，IT 可直接備份與審計</span>
    </div>
    <div class="p-3 border border-red-400 rounded-lg text-xs text-red-700">
      ⚠️ 記憶邊界由 AI 自主決定，企業需評估資料治理策略
    </div>
  </div>
</div>

---
layout: default
---

# Promptware 防禦：對抗記憶污染攻擊

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-xs text-gray-400 mb-3">攻擊鏈（Brainworm-class）</div>
    <div class="flex flex-col gap-2 text-sm">
      <div class="p-2 bg-red-50 border border-red-300 rounded">📄 外部內容（網頁、文件、工具輸出）</div>
      <div class="flex justify-center text-red-400 text-xs">▼ 混入惡意指令</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">💾 寫入 MEMORY.md / skill_manage</div>
      <div class="flex justify-center text-red-400 text-xs">▼ 持久化感染</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">🔁 跨會話持續執行攻擊者指令</div>
    </div>
    <div class="mt-3 p-2 bg-green-50 border border-green-400 rounded text-xs text-green-700">
      🛡 v0.15.0 在記憶寫入路徑前加入攔截驗證
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="text-xs text-gray-500 mb-1">企業導入前確認清單</div>
    <div class="p-3 border border-gray-300 rounded text-sm">□ 防禦是否覆蓋 MCP 工具輸出？</div>
    <div class="p-3 border border-gray-300 rounded text-sm">□ 是否有第三方滲透測試報告？</div>
    <div class="p-3 border border-gray-300 rounded text-sm">□ 觸發日誌是否可稽核？</div>
    <div class="mt-2 p-2 bg-gray-100 rounded text-xs text-gray-600">
      MIT 開源 — 企業可自行審計防禦實作原始碼
    </div>
  </div>
</div>

---
layout: two-cols
class: kanban-slide
---

# Multi-agent Kanban 自癒能力

```mermaid {scale: 0.6}
flowchart TD
    Master(["主代理"]) -->|"派生"| A["子代理 A"]
    Master -->|"派生"| B["子代理 B ⚠️"]
    Master -->|"派生"| C["子代理 C"]
    A & B & C -->|"狀態寫入"| KB[("📋 Kanban")]
    B -->|"心跳中斷"| Z["殭屍標記"]
    Z -->|"自動偵測"| R["任務回收"]
    R -->|"承接繼續"| C
```

::right::

<div class="flex flex-col gap-3 mt-24">
  <div class="border border-green-600 rounded p-3 text-sm">✅ 無人值守長任務：子代理失效不需人工介入</div>
  <div class="border border-green-600 rounded p-3 text-sm">✅ 任務狀態可審計：Kanban 提供完整生命週期記錄</div>
  <div class="border border-green-600 rounded p-3 text-sm">✅ 跨 session 持久化：配合 /goal 追蹤多日工作流</div>
  <div class="mt-4 p-2 border border-yellow-400 rounded text-xs text-yellow-700">
    ⚠️ v0.13.0 推出，尚無公開 benchmark — 建議 PoC 自行驗證可靠性
  </div>
</div>

<style>
.kanban-slide h1 {
  white-space: nowrap;
  overflow: visible;
}
</style>

---
layout: default
---

# v0.15 Velocity：更精簡的程式碼，更穩固的基礎

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="text-center flex flex-col justify-center">
    <div class="text-7xl font-bold text-blue-600">76%</div>
    <div class="text-gray-500 mt-2">程式碼削減</div>
    <div class="text-sm text-gray-400 mt-1">功能不減，架構收斂</div>
    <div class="mt-6 flex flex-col gap-2 text-xs text-gray-500">
      <div class="flex justify-between px-4"><span>v0.12</span><span>v0.13</span><span>v0.14</span><span class="text-blue-600 font-bold">v0.15</span></div>
      <div class="h-1 bg-gray-200 rounded mx-4 relative">
        <div class="absolute right-0 top-0 h-1 w-1/4 bg-blue-600 rounded"></div>
      </div>
      <div class="text-center">28 天四版迭代</div>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-3 bg-gray-100 rounded text-sm">
      <div class="text-gray-500 text-xs mb-1">重構前</div>
      四條平行執行路徑（CLI / Gateway / ACP / Web UI）各自維護
    </div>
    <div class="flex justify-center text-blue-400">▼ 收斂</div>
    <div class="p-3 bg-blue-50 border border-blue-300 rounded text-sm">
      <div class="text-blue-500 text-xs mb-1">重構後</div>
      單一 AIAgent 協調層統一入口
    </div>
    <div class="mt-2 flex flex-col gap-2 text-sm">
      <div class="border border-green-600 rounded p-2">✅ 安全審計範圍縮小</div>
      <div class="border border-green-600 rounded p-2">✅ Bitwarden 原生 API Key 管理</div>
    </div>
    <div class="p-2 border border-red-400 rounded text-xs text-red-700">
      ⚠️ 距 v0.14 僅 12 天 — PoC 前確認測試覆蓋率
    </div>
  </div>
</div>

---
layout: default
---

# Tool Gateway — 一訂閱全工具齊備

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-sm font-bold text-gray-500 mb-3">隨 Nous Portal 訂閱包含</div>

| 工具 | 說明 |
|------|------|
| 🔍 Web 搜尋 + 擷取 | Firecrawl 無速率限制 |
| 🎨 圖片生成 | FLUX 2 / GPT-Image / Ideogram 等 9 款 |
| 🔊 文字轉語音 | OpenAI TTS 等多款 |
| 🌐 瀏覽器自動化 | 雲端無頭 Chrome（Browser Use） |

  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-4 bg-yellow-50 border border-yellow-400 rounded-lg text-sm">
      💡 <strong>不需另開帳號：</strong>不必分別申請 Firecrawl、FAL、Browser Use——Tool Gateway 統一路由
    </div>
    <div class="p-3 bg-gray-50 border border-gray-300 rounded-lg text-sm">
      🛠 企業自建：停用 gateway 改用內部基礎設施（<span class="font-mono text-xs">use_gateway: false</span>）
    </div>
    <div class="p-2 border border-red-300 rounded text-xs text-red-700">
      ⚠️ 付費功能：Nous Portal 免費方案不含 Tool Gateway
    </div>
  </div>
</div>

---
layout: default
---

# Plugin 系統 — 三種擴充類型

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="border border-blue-400 rounded-lg p-4">
    <div class="text-2xl mb-2">🔧</div>
    <div class="font-bold text-blue-600 mb-2">Tools / Hooks</div>
    <div class="text-sm text-gray-600">新增自訂工具 + 設置生命週期鉤子（logging、guardrails、webhooks）</div>
    <div class="mt-3 text-xs font-mono text-gray-400">hermes plugins install</div>
  </div>
  <div class="border border-purple-400 rounded-lg p-4">
    <div class="text-2xl mb-2">🧠</div>
    <div class="font-bold text-purple-600 mb-2">Memory Provider</div>
    <div class="text-sm text-gray-600">替換記憶後端：Honcho、Mem0、OpenViking、RetainDB 等跨 session 記憶</div>
    <div class="mt-3 text-xs font-mono text-gray-400">跨 session 個人化</div>
  </div>
  <div class="border border-green-400 rounded-lg p-4">
    <div class="text-2xl mb-2">📋</div>
    <div class="font-bold text-green-600 mb-2">Context Engine</div>
    <div class="text-sm text-gray-600">替換 context 管理，自訂檔案注入與壓縮策略</div>
    <div class="mt-3 text-xs font-mono text-gray-400">hermes plugins UI</div>
  </div>
</div>

<div class="mt-5 p-3 bg-gray-100 rounded text-sm text-gray-700">
  🔒 <strong>企業應用：</strong>Tools/Hooks plugin 可實作 <strong>guardrails</strong>——工具呼叫前後攔截審計，不需 fork 核心程式碼
</div>

---
layout: default
---

# 企業可靠性：多層模型保障

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="flex flex-col gap-3">
    <div class="border border-blue-400 rounded p-3 text-sm">
      <div class="font-bold text-blue-600 mb-1">🗺 Provider Routing</div>
      <div class="text-gray-600">依成本、速度、品質排序多個提供商，支援白名單 / 黑名單過濾</div>
    </div>
    <div class="border border-orange-400 rounded p-3 text-sm">
      <div class="font-bold text-orange-600 mb-1">🔄 Fallback Providers</div>
      <div class="text-gray-600">主要模型出錯時自動切換備援，視覺 / 壓縮任務有獨立 fallback</div>
    </div>
    <div class="border border-green-400 rounded p-3 text-sm">
      <div class="font-bold text-green-600 mb-1">🔑 Credential Pools</div>
      <div class="text-gray-600">多組 API Key 輪替，達速率上限自動換鑰，不中斷服務</div>
    </div>
    <div class="border border-purple-400 rounded p-3 text-sm">
      <div class="font-bold text-purple-600 mb-1">⚡ Prompt Caching</div>
      <div class="text-gray-600">跨 session 1 小時前綴快取（Claude / OpenRouter / Nous Portal），永遠開啟</div>
    </div>
  </div>
  <div class="flex flex-col justify-center gap-4">
    <div class="p-4 bg-blue-50 border border-blue-200 rounded-lg text-sm">
      💡 <strong>SLA 保障</strong><br>
      <span class="text-gray-600">供應商限速或故障時零介入自動切換，服務不中斷</span>
    </div>
    <div class="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
      💰 <strong>成本控管</strong><br>
      <span class="text-gray-600">Prompt caching 降低重複 context token 費用；Credential Pools 防單鑰達限</span>
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# 實際落地案例

<div class="text-gray-400 mt-4 text-lg">遊戲營運 AI Bot — 自然語言查 BigQuery 的實戰驗證</div>

---
layout: default
---

# 遊戲營運 Bot：用中文提問，Bot 自動出報告

<div class="text-gray-600 text-sm italic mb-4">
  Hermes Agent + BigQuery，遊戲運營同仁無需寫 SQL，直接提問得到完整對比分析
</div>

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="text-xs text-gray-400 mb-2">對話實例</div>
    <div class="bg-gray-900 rounded-lg p-4">
      <div class="text-gray-400 text-xs mb-3">使用者 · 14:32</div>
      <div class="bg-blue-600 rounded-lg px-3 py-2 text-white text-right mb-4 text-sm ml-8">
        黃金週與卡片最終戰成效交叉比對一下
      </div>
      <div class="text-gray-400 text-xs mb-1">RD7 Bot · 14:35</div>
      <div class="bg-gray-700 rounded-lg p-3 text-xs text-green-300 leading-relaxed">
        <span class="text-white font-bold">FXC 最終戰 × 黃金週 BP 交叉比對 (非CN)</span><br>
        查詢區間：2026/4/1 – 5/4<br><br>
        <span class="text-yellow-300 font-bold">結論先講：</span><br>
        FXC 最終戰仍是營收主力，BP 營收占 88%。Round B 日均較 Round A 下滑 28.5%…
      </div>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="text-xs text-gray-500 font-bold mb-1">Bot 在這次對話做了什麼？</div>
    <div class="border border-amber-400 rounded-lg p-3">
      <div class="text-amber-600 font-bold text-sm mb-1">🗣 理解需求</div>
      <div class="text-gray-700 text-xs">把「黃金週 vs 卡片最終戰」翻成可查的條件</div>
    </div>
    <div class="border border-blue-400 rounded-lg p-3">
      <div class="text-blue-600 font-bold text-sm mb-1">🔍 查資料</div>
      <div class="text-gray-700 text-xs">自動到 BigQuery 跑日均、營收、買家重疊</div>
    </div>
    <div class="border border-green-400 rounded-lg p-3">
      <div class="text-green-600 font-bold text-sm mb-1">📊 做對比，下結論</div>
      <div class="text-gray-700 text-xs">Round A vs B 日均公平對比，用人話解釋數字</div>
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# 資料準備

<div class="text-gray-400 mt-4 text-lg">Bot 要懂業務，得先給它正確的『地圖』和『字典』</div>

<div class="text-gray-500 text-sm mt-2">DATA · KNOWLEDGE · QUERIES</div>

---
layout: default
---

# Bot 要餵的三類知識

<div class="text-gray-600 text-sm italic mb-5">少了哪一塊都會卡住：表結構、能跑的範例、聽得懂的詞彙</div>

<div class="grid grid-cols-3 gap-4">
  <div class="border border-blue-400 rounded-lg overflow-hidden">
    <div class="bg-blue-700 px-4 py-3 text-white font-bold text-sm">01 · 數據儀表</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">BigQuery 表的中文名、用途、寫入頻率、欄位語意。Bot 才知道「要打開哪張表」。</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">DailyUserInfoSnapshot · GameAccount · ...</div>
    </div>
  </div>
  <div class="border border-amber-400 rounded-lg overflow-hidden">
    <div class="bg-amber-700 px-4 py-3 text-white font-bold text-sm">02 · 歷史 Query 範例</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">把過去寫過的查 SQL 收進來。Bot 用最像的範本改造，避免從零亂湊。</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">計算 DAU · 計算營收 · 留存 · 重疊買家</div>
    </div>
  </div>
  <div class="border border-green-400 rounded-lg overflow-hidden">
    <div class="bg-green-700 px-4 py-3 text-white font-bold text-sm">03 · 一般營運知識</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">縮寫、行話、人話對映：DAU 是什麼、員工要不要排除、CN 什麼定義…</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">DAU = 日活躍 · DNU = 新玩家 · DOU = 老玩家</div>
    </div>
  </div>
</div>

---
layout: default
---

# 數據儀表｜DailyUserInfoSnapshot

<div class="text-gray-600 text-sm italic mb-4">非即時主表，覆蓋玩家屬性 + 每日聚合，是 Bot 跑分析的第一站</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">TABLE METADATA</div>
    <div class="flex flex-col gap-2">
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">table_id</span><span class="font-mono text-gray-700">preprocessed_bklog.<br>DailyUserInfoSnapshot</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">中文表名</span><span class="text-gray-700">日結玩家聚合資訊</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">table_type</span><span class="text-gray-700">Intermediate</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">write_frequency</span><span class="text-gray-700">Daily</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">business_domain</span><span class="text-gray-700">玩家</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">partitions</span><span class="font-mono text-gray-700">BQDate</span></div>
    </div>
  </div>
  <div>
    <div class="text-xs text-gray-400 font-bold mb-2">BOT 最常用的欄位</div>
    <div class="flex flex-col divide-y divide-gray-100 text-xs">
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BQDate</span><span class="text-gray-600">日期 partition（REQUIRED）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">UserID</span><span class="text-gray-600">玩家 ID</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">Country</span><span class="text-gray-600">主要市場：CN/JP/TW/US/VN/Others</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">VipLV</span><span class="text-gray-600">當日最高 VIP</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">GameLevel</span><span class="text-gray-600">當日最高遊戲等級</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BuyNumber</span><span class="text-gray-600">營收（不需排除員工）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">EndBalance</span><span class="text-gray-600">持有通算金幣（金幣水位）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">UserType</span><span class="text-gray-600">30日活躍 / 新進 / 30日回流</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">LastBuyDate</span><span class="text-gray-600">180 天內最近一次購買</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BPBuyNumber</span><span class="text-gray-600">付費 BP 儲值金額</span></div>
    </div>
  </div>
</div>

---
layout: default
---

# 歷史 Query 範例

<div class="text-gray-600 text-sm italic mb-4">把過去寫得不錯的 SQL 收進來，Bot 找最像的當範本改</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">計算 DAU &nbsp;·&nbsp; dim: BQDate</div>
    <pre class="bg-gray-50 rounded p-3 text-xs font-mono leading-snug"><span class="text-gray-400 italic">/* 非即時資料 → 用 DailyUserInfoSnapshot */</span>
<span class="text-gray-400 italic">/* 非營收資料 → 排除員工 */</span>
<span class="text-blue-600">SELECT</span> BQDate,
  <span class="text-purple-600">count</span>(<span class="text-blue-600">distinct</span> UserID) <span class="text-blue-600">AS</span> DAU
<span class="text-blue-600">FROM</span> <span class="text-green-600">`DailyUserInfoSnapshot`</span>
<span class="text-blue-600">WHERE</span> BQDate <span class="text-blue-600">BETWEEN</span> <span class="text-amber-600">'2025-08-08'</span>
  <span class="text-blue-600">AND</span> <span class="text-amber-600">'2025-08-10'</span>
  <span class="text-blue-600">AND</span> UserID <span class="text-blue-600">NOT IN</span> (
    <span class="text-blue-600">SELECT</span> UserID <span class="text-blue-600">FROM</span> <span class="text-green-600">`GameAccount`</span>
  )
<span class="text-blue-600">GROUP BY</span> BQDate
<span class="text-blue-600">ORDER BY</span> BQDate</pre>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">計算營收 &nbsp;·&nbsp; dim: BQDate</div>
    <pre class="bg-gray-50 rounded p-3 text-xs font-mono leading-snug"><span class="text-gray-400 italic">/* 非即時資料 → 用 DailyUserInfoSnapshot */</span>
<span class="text-gray-400 italic">/* 營收資料 → 不需排除員工 */</span>
<span class="text-blue-600">SELECT</span> BQDate,
  <span class="text-purple-600">sum</span>(BuyNumber) <span class="text-blue-600">AS</span> BuyNumber
<span class="text-blue-600">FROM</span> <span class="text-green-600">`DailyUserInfoSnapshot`</span>
<span class="text-blue-600">WHERE</span> BQDate <span class="text-blue-600">BETWEEN</span> <span class="text-amber-600">'2025-08-08'</span>
  <span class="text-blue-600">AND</span> <span class="text-amber-600">'2025-08-10'</span>
<span class="text-blue-600">GROUP BY</span> BQDate
<span class="text-blue-600">ORDER BY</span> BQDate</pre>
  </div>
</div>

---
layout: default
---

# 一般營運知識｜給 Bot 的字典

<div class="text-gray-600 text-sm italic mb-4">把行話、縮寫、規則寫清楚，Bot 才不會把「新進」當「活躍」回給你</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">INDICATORS</div>
    <div class="flex flex-col divide-y divide-gray-100 text-xs">
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DAU</span><span class="text-gray-600">日活躍玩家數 (Daily Active Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DNU</span><span class="text-gray-600">每日新玩家數 (Daily New Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DOU</span><span class="text-gray-600">每日老玩家數 (Daily Old Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">BP 營收</span><span class="text-gray-600">付費 BP 儲值金額（BPBuyNumber）</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">黑鑽</span><span class="text-gray-600">BlackDiamondTag 標示的高價值玩家</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">金幣水位</span><span class="text-gray-600">EndBalance：玩家當日持有通算金幣量</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">30日活躍</span><span class="text-gray-600">前 30 天內有上線紀錄的玩家</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">30日回流</span><span class="text-gray-600">前 30 天有過上線、但今日不是新進</span></div>
    </div>
  </div>
  <div class="pt-4">
    <div class="text-xs text-gray-400 font-bold mb-3">BOT 預設遵守的營運規則</div>
    <div class="flex flex-col gap-2">
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">非即時數據需求：一律走 DailyUserInfoSnapshot</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">非營收查詢：UserID 排除 GameAccount 員工帳號</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">營收查詢：不需排除員工</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">Country = Others 時，看 CountryDetail 取精準國家</div>
      <div class="p-2 bg-gray-50 border-l-2 border-amber-400 rounded-r text-xs text-gray-700">通算金幣 = Coin + 25000 × Gem（贈幣同口徑）</div>
      <div class="p-2 bg-gray-50 border-l-2 border-green-400 rounded-r text-xs text-gray-700">回答先給結論，再附支持的數字與 SQL</div>
    </div>
  </div>
</div>

---
layout: default
---

# 評估結論

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="border border-green-700 rounded-lg p-5">
    <h3 class="text-green-700 mb-3">✅ 優勢</h3>
    <ul class="space-y-2 text-sm">
      <li>社群規模龐大（191K stars），成熟度高</li>
      <li>MIT 授權，可自由商用與修改</li>
      <li>多模型支援，降低廠商鎖定風險</li>
      <li>部署彈性高，PoC 成本極低</li>
      <li>自我改進機制，長期使用價值遞增</li>
    </ul>
  </div>
  <div class="border border-yellow-700 rounded-lg p-5">
    <h3 class="text-yellow-700 mb-3">⚠️ 注意事項</h3>
    <ul class="space-y-2 text-sm">
      <li>尚無公開效能基準測試資料</li>
      <li>Python 為主，需具備相關技術資源</li>
      <li>功能複雜，導入學習曲線較高</li>
      <li>企業資料安全政策需另行評估</li>
    </ul>
  </div>
</div>

<div class="mt-5 p-4 bg-blue-900 bg-opacity-40 rounded-lg border border-blue-600">
  <span class="text-white">🎯 <strong>建議：</strong>值得列為內部 AI Agent 基礎框架候選，建議以 $5 VPS 進行一個月 PoC 驗證，成本極低風險可控</span>
</div>

---
layout: default
---

# 資料來源

<div class="flex flex-col gap-4 mt-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">GitHub Repo</div>
    <div class="font-mono text-sm">github.com/NousResearch/hermes-agent</div>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">官方文件</div>
    <div class="font-mono text-sm">hermes-agent.nousresearch.com/docs</div>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">繁中教學手冊（chihhung, v0.15.2）</div>
    <div class="font-mono text-sm">chihhung.github.io/Blog/posts/教學/ai開發/hermes-agent生態系教學手冊</div>
  </div>
  <div class="border border-blue-300 rounded-lg p-4">
    <div class="text-xs text-blue-400 mb-1">DeepWiki — code-level 架構分析</div>
    <div class="font-mono text-sm">deepwiki.com/NousResearch/hermes-agent</div>
  </div>
</div>

---
layout: center
class: text-center
---

# 謝謝

<div class="text-gray-600 mt-4 text-sm">
  報告日期：2026.06.12
</div>
