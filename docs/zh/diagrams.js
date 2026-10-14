// 繁體中文版的圖。結構與 ../diagrams.js 相同，只改中文文字。
drawDiagrams({
github:{height:260,narrow:{height:420,pos:{lap:[.25,.08],clu:[.75,.08],gh:[.5,.4],hist:[.2,.7],pages:[.8,.7],ppl:[.8,.93]}},nodes:[
 {id:'lap',label:'筆電上的 session',kind:'agent',x:.12,y:.2,info:'寫作、畫圖、複查。只透過 push / pull，不手動把檔案搬到叢集。'},
 {id:'clu',label:'叢集上的 session 和 job',kind:'agent',x:.12,y:.8,info:'重的運算。job 拉下它該跑的 commit；小的結果以 commit 回來。'},
 {id:'gh',label:'GitHub repo',kind:'you',x:.48,y:.5,info:'<b>紀錄</b><br>每個實際步驟 commit 一次。每個 session 在自己的 worktree 和 branch 上做事。'},
 {id:'hist',label:'歷史：log 和 diff',kind:'file',x:.82,y:.15,info:'結束時新的 session 讀這個，而不是前一個 session 的摘要。'},
 {id:'pages',label:'從 docs/ 發布的網站',kind:'file',x:.82,y:.55,info:'private repo 發布的公開網頁。docs/ 裡只放可以公開的東西。'},
 {id:'ppl',label:'指導教授、朋友、手機',kind:'ok',x:.82,y:.88,info:'給一個連結，而不是叫人 pull branch。'}],
 links:[{s:'lap',t:'gh',label:'push / pull'},{s:'clu',t:'gh',label:'push / pull'},{s:'gh',t:'hist'},{s:'gh',t:'pages'},{s:'pages',t:'ppl'}]},
modes:{height:120,narrow:{height:230,pos:{a:[.5,.1],p:[.5,.37],u:[.5,.63],n:[.5,.9]}},axis:['每步都看','只看結果'],nodes:[
 {id:'a',label:'逐步核准',kind:'you',x:.12,y:.3,info:'<b>每個 command 都要核准</b><br>適用於剛開始的第一週、會動到共用資料、刪檔，或一次送很多 job 的工作。<br>代價是你會變瓶頸，一離開，長 task 就停住。'},
 {id:'p',label:'核准計畫',kind:'file',x:.38,y:.3,info:'<b>先看計畫，再放它跑</b><br>它先寫 plan，你讀過、修正後，之後的修改不再逐一問。安全 command 事先列白名單，有風險的照樣要問。<br>我白天大部分工作都在這格。'},
 {id:'u',label:'無人看管',kind:'agent',x:.64,y:.3,info:'<b>完全不問</b><br>只能放在界線清楚的環境：自己的 repository 副本、唯讀 input、沒有 secret，而且 job 數、core 數、時間上限要由 scheduler 強制，不是只寫在 prompt 裡。'},
 {id:'n',label:'過夜跑',kind:'agent',x:.88,y:.3,info:'<b>過夜跑</b><br>目標能一句話說完、有它能跑的 check，而且運算已在 scheduler 串好時才適合。凌晨兩點還需要你判斷，就不適合。'}],
 links:[{s:'a',t:'p'},{s:'p',t:'u'},{s:'u',t:'n'}]},
night:{height:280,narrow:{height:470,pos:{b:[.5,.05],s1:[.3,.22],c1:[.3,.38],s2:[.3,.54],c2:[.3,.7],j:[.72,.3],x:[.75,.72],m:[.4,.95]}},axis:['傍晚','早上'],nodes:[
 {id:'b',label:'任務與檢查',kind:'you',x:.12,y:.2,info:'<b>離開前</b><br>一句話目標。哪些檔案必須存在、幾列、數值範圍。哪些 command 可以直接跑。'},
 {id:'s1',label:'階段 1',kind:'agent',x:.33,y:.2,info:'一小段工作，以一個檔案結束，做完就 commit。'},
 {id:'c1',label:'check',kind:'ok',x:.46,y:.2,info:'一個你看過它失敗的 check。失敗時代理要停下來寫原因，不是設法讓它通過。'},
 {id:'s2',label:'階段 2',kind:'agent',x:.6,y:.2,info:'只從通過檢查的階段 1 輸出開始。'},
 {id:'c2',label:'check',kind:'ok',x:.74,y:.2,info:'同樣規則。'},
 {id:'j',label:'job 串接',kind:'file',x:.3,y:.6,info:'長運算用 batch job 跑，前一個成功才啟動下一個。不要讓代理一直 polling queue。'},
 {id:'x',label:'停下說明',kind:'bad',x:.8,y:.88,info:'check 失敗時，代理停下來，在 status file 寫原因。它不會改 check 讓它通過。'},
 {id:'m',label:'早上複查',kind:'you',x:.9,y:.6,info:'<b>早上</b><br>新 session 讀 commit、STATUS.md 和輸出檔，回報完成了什麼、哪些沒有根據。你讀這份，不讀夜間 session 自己的摘要。'}],
 links:[{s:'b',t:'s1'},{s:'s1',t:'c1'},{s:'c1',t:'s2'},{s:'s2',t:'c2'},{s:'s1',t:'j',dash:1},{s:'j',t:'s2',dash:1},{s:'c2',t:'m'},{s:'c1',t:'x',label:'失敗'},{s:'c2',t:'x',label:'失敗'}]},
loop:{height:300,nodes:[
 {id:'you',label:'你',kind:'you',x:.1,y:.5,info:'<b>你</b><br>用白話說目標，例如「從原始計數重做表二」。'},
 {id:'model',label:'模型',kind:'agent',x:.27,y:.5,info:'<b>語言模型</b><br>決定下一步做什麼。在聊天裡它只能回文字。'},
 {id:'read',label:'讀檔',kind:'agent',x:.66,y:.13,info:'<b>讀</b><br>打開你的 script、資料表頭、log 和規則檔。'},
 {id:'run',label:'跑指令',kind:'agent',x:.88,y:.5,info:'<b>執行</b><br>跑 Python、R、shell，送叢集 job。每個 command 都能設成要你核准。'},
 {id:'err',label:'讀輸出',kind:'agent',x:.66,y:.87,info:'<b>讀輸出</b><br>error、traceback、空檔。它在這裡發現，或漏掉，出了什麼問題。'},
 {id:'edit',label:'修改',kind:'agent',x:.47,y:.5,info:'<b>修改</b><br>改 code 再跑一次。迴圈持續到它覺得完成為止。'},
 {id:'res',label:'結果',kind:'you',x:.27,y:.87,info:'<b>結果</b><br>檔案、數字、摘要。摘要只是它的說法，檔案才是證據。'}],
 links:[{s:'you',t:'model',label:'目標'},{s:'model',t:'read',bend:-.1},{s:'read',t:'run'},{s:'run',t:'err'},{s:'err',t:'edit'},{s:'edit',t:'read',dash:1},{s:'err',t:'res'},{s:'res',t:'you',bend:.2,label:'你檢查'}]},

roles:{height:210,narrow:{height:330,pos:{q:[.5,.07],code:[.28,.42],jobs:[.72,.42],lit:[.28,.6],fig:[.72,.6],j:[.5,.93]}},
 groups:[{id:'ag',label:'代理負責',members:['code','jobs','lit','fig']}],
 nodes:[
 {id:'q',label:'研究問題',kind:'you',x:.11,y:.55,info:'決定問題。代理不會告訴你這個問題沒意思。'},
 {id:'code',label:'寫程式',kind:'agent',x:.4,y:.42,info:'例行的分析又快，通常也對。'},
 {id:'jobs',label:'跑作業',kind:'agent',x:.62,y:.42,info:'撰寫並提交批次作業，查佇列。'},
 {id:'lit',label:'讀論文',kind:'agent',x:.4,y:.7,info:'摘要附原文引句。每段引句都要核對是否真在論文裡。'},
 {id:'fig',label:'畫圖',kind:'agent',x:.62,y:.7,info:'照寫好的圖規格通常畫得不錯，但要你要求才會檢查自己的成圖。'},
 {id:'j',label:'答案對嗎',kind:'you',x:.89,y:.55,info:'判斷結果。我大多數失敗，都是結果根本沒被真的檢查過。'}],
 links:[{s:'q',t:'ag'},{s:'ag',t:'j'}]},

rules:{height:270,narrow:{height:310,pos:{file:[.18,.17],a1:[.5,.17],bad:[.79,.17],a2:[.15,.62],chk:[.45,.62],ok:[.8,.52],stop:[.7,.85]}},
 groups:[{id:'g1',label:'規則在檔案',members:['file','a1','bad']},{id:'g2',label:'規則在程式',members:['a2','chk','ok','stop']}],
 nodes:[
 {id:'file',label:'CLAUDE.md',kind:'file',x:.12,y:.2,info:'<b>規則檔</b><br>session 開始時讀一次。幾小時後，沒有東西再指回它。'},
 {id:'a1',label:'分析',kind:'agent',x:.45,y:.2,info:'本來該遵守這條規則的分析。'},
 {id:'bad',label:'bug 仍交付',kind:'bad',x:.82,y:.2,info:'9 月 4 日：三個檔案早就禁止的 bug 還是交出去了。'},
 {id:'a2',label:'分析',kind:'agent',x:.12,y:.67,info:'同一份分析，但規則直接擋在路上。'},
 {id:'chk',label:'程式檢查',kind:'you',x:.45,y:.67,info:'<b>它會拒絕：</b><br>資料不足以偵測效應，卻說「沒有效應」<br>control 用不同 measure 配對<br>圖沒有 sample size<br>在共用 checkout 裡 commit'},
 {id:'ok',label:'結果',kind:'ok',x:.82,y:.56,info:'只有通過檢查的結果到得了這裡。'},
 {id:'stop',label:'停下說原因',kind:'bad',x:.82,y:.82,info:'run 失敗，訊息會說明是哪條規則擋下來。'}],
 links:[{s:'file',t:'a1',dash:1,label:'開始時讀一次'},{s:'a1',t:'bad',label:'幾小時後'},{s:'a2',t:'chk'},{s:'chk',t:'ok',label:'通過'},{s:'chk',t:'stop',label:'失敗'}]},

session:{type:'timeline',window:3,zh:1,steps:[
 {talk:'仔細談過目標與限制。',file:'brief',disk:'BRIEF.md：目標、input、完成定義、已知陷阱。'},
 {talk:'決定排除兩個 sample，也記下原因。',file:'task',disk:'task list：把排除 sample 記成一個步驟。'},
 {talk:'第一個 job 失敗，改了 module 版本。',file:'commit',disk:'修正過的 job script 已 commit。'},
 {talk:'主要比較的數字。',file:'status',disk:'STATUS.md：結果、檔案路徑、計算方式。'},
 {talk:'control 看起來有問題，重跑。',file:'commit',disk:'重跑的 control 和輸出已 commit。'},
 {talk:'寫完摘要。',file:'status',disk:'STATUS.md 已更新；新 session 從這裡開始複查。'}]},

clean:{height:300,narrow:{height:340,pos:{m:[.25,.07],raw:[.75,.07],rb:[.5,.32],cmp:[.5,.55],p:[.15,.88],f:[.48,.88],b:[.82,.88]}},nodes:[
 {id:'m',label:'Methods',kind:'file',x:.1,y:.25,info:'只能看寫下來的內容，不能看原 script 或中間檔。'},
 {id:'raw',label:'原始 input',kind:'file',x:.1,y:.75,info:'基因體、annotation、reads，最一開始的檔案。'},
 {id:'rb',label:'代理重做',kind:'agent',x:.42,y:.5,info:'在空資料夾裡重做。文字缺細節時必須停下來說，不能猜。'},
 {id:'cmp',label:'逐一比對',kind:'agent',x:.68,y:.5,info:'每個報告數字都和重做結果逐一比對。'},
 {id:'p',label:'PASS',kind:'ok',x:.9,y:.15,info:'和論文一致。'},
 {id:'f',label:'FAIL',kind:'bad',x:.9,y:.5,info:'對不上，是一個需要解釋的真正差異。'},
 {id:'b',label:'BLOCKED',kind:'you',x:.9,y:.85,info:'照寫下的內容算不出來。我的例子：沒寫明的搜尋設定影響 13,663 個基因中的 732 個，還有一個 filter step 完全沒寫。'}],
 links:[{s:'m',t:'rb'},{s:'raw',t:'rb'},{s:'rb',t:'cmp'},{s:'cmp',t:'p'},{s:'cmp',t:'f'},{s:'cmp',t:'b'}]}
});
