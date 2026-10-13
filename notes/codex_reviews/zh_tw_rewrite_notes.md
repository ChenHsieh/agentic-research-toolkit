已改寫 [docs/zh/index.html](/scratch/ch29576/agentic-research-toolkit/docs/zh/index.html) 與 [docs/zh/diagrams.js](/scratch/ch29576/agentic-research-toolkit/docs/zh/diagrams.js)，並確認 JavaScript 語法與 diff 格式正常。

統一用詞：

- coding agent：代理
- session：session
- 會直接噴錯的 bug：crash、缺 module、syntax error 類問題
- 表面正常、其實錯了的 bug：程式跑完但結果無效的問題
- check：check
- brief：brief
- job：job
- scheduler：scheduler
- status file：status file
- Git worktree：每個 session 獨立的工作目錄

英文原文我會建議作者日後斟酌重寫的地方：

- “It can be worse than a filter.” 比喻不夠明確，直接說「不只會漏掉錯誤，還可能把錯誤結果修成看似成功」更清楚。
- “The silent guess” 作為小標有記憶點，但研究語境裡 “An undocumented choice” 會更精準。
- “The agent examples are mine” 太像註腳式的補充，可改成較完整的一句，交代表格中的例子來自作者自己的使用經驗。