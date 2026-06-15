# Sources 命名規則

每份 source 檔案用 prefix 標示資料層級：

| Prefix | 類型 | 說明 | 範例 |
|--------|------|------|------|
| `primary-` | Primary | 官方來源：GitHub repo、官方文件、changelog | `primary-github-repo.md` |
| `secondary-` | Secondary | 社群來源：教學手冊、技術文章、評測 | `secondary-chihhung-blog.md` |
| `tool-` | Analysis tool | 工具產出：gitIngest、DeepWiki、gitDiagram 等 | `tool-gitingest.md` |

## 檔案內容格式

每個檔案開頭需包含：

```markdown
# Source: <標題>

**URL**: <來源網址>
**Fetched**: <YYYY-MM-DD>

（其餘為抓取的原始內容）
```
