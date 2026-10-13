// 繁體中文版的圖。結構與 ../diagrams.js 相同，只翻譯文字。
drawDiagrams({
modes:{height:120,narrow:{height:230,pos:{a:[.5,.1],p:[.5,.37],u:[.5,.63],n:[.5,.9]}},axis:['你盯著每一步','你只檢查結果'],nodes:[
 {id:'a',label:'每一步都同意',kind:'you',x:.12,y:.3,info:'<b>每個指令都要你同意</b><br>適用：剛開始的第一週、任何會動到共用資料、刪檔、或一次送很多工作的事。<br>代價：你變成瓶頸；你一不看，長任務就停住。'},
 {id:'p',label:'同意計畫',kind:'file',x:.38,y:.3,info:'<b>先擬計畫，再放它跑</b><br>它寫計畫，你讀過並修正，之後的修改不再詢問。安全的指令事先列入清單；有風險的還是會問。<br>我白天的工作大多在這一格。'},
 {id:'u',label:'無人看管',kind:'agent',x:.64,y:.3,info:'<b>完全不問</b><br>只能在有邊界的空間裡：它自己的一份儲存庫、唯讀的輸入、沒有任何密碼金鑰，而且工作數、核心數、時間的上限是排程器強制的，不是寫在提示裡拜託它的。'},
 {id:'n',label:'過夜',kind:'agent',x:.88,y:.3,info:'<b>過夜</b><br>行得通的條件：目標一句話、成功與否是一個它跑得了的檢查、運算在排程器裡串好。如果凌晨兩點需要你的判斷，就行不通。'}],
 links:[{s:'a',t:'p'},{s:'p',t:'u'},{s:'u',t:'n'}]},
night:{height:280,narrow:{height:470,pos:{b:[.5,.05],s1:[.3,.22],c1:[.3,.38],s2:[.3,.54],c2:[.3,.7],j:[.72,.3],x:[.75,.72],m:[.4,.95]}},axis:['傍晚','早上'],nodes:[
 {id:'b',label:'任務說明＋完成檢查',kind:'you',x:.12,y:.2,info:'<b>離開之前</b><br>一句話的目標。哪些檔案要存在、幾列、數值範圍。哪些指令可以不問就跑。'},
 {id:'s1',label:'階段 1',kind:'agent',x:.33,y:.2,info:'一小段工作，以一個檔案結束，做完就 commit。'},
 {id:'c1',label:'檢查',kind:'ok',x:.46,y:.2,info:'一個你看過它失敗的檢查。失敗時代理停下來寫原因，而不是想辦法讓它通過。'},
 {id:'s2',label:'階段 2',kind:'agent',x:.6,y:.2,info:'只從通過檢查的階段 1 輸出開始。'},
 {id:'c2',label:'檢查',kind:'ok',x:.74,y:.2,info:'同樣的規則。'},
 {id:'j',label:'工作在排程器裡串好',kind:'file',x:.3,y:.6,info:'長時間的運算以批次工作執行，前一個成功才啟動下一個。沒有代理坐在那裡一直問佇列。'},
 {id:'x',label:'停下來，寫原因',kind:'bad',x:.8,y:.88,info:'檢查失敗時，代理停下來並在狀態檔裡寫原因。它不會去改檢查讓它通過。'},
 {id:'m',label:'新的工作階段複查',kind:'you',x:.9,y:.6,info:'<b>早上</b><br>一個新的工作階段讀 commit、狀態檔和輸出檔，回報做了什麼、哪些沒有根據。你讀的是這份，不是夜裡那個工作階段自己寫的摘要。'}],
 links:[{s:'b',t:'s1'},{s:'s1',t:'c1'},{s:'c1',t:'s2'},{s:'s2',t:'c2'},{s:'s1',t:'j',dash:1},{s:'j',t:'s2',dash:1},{s:'c2',t:'m'},{s:'c1',t:'x',label:'失敗'},{s:'c2',t:'x',label:'失敗'}]},
loop:{height:300,nodes:[
 {id:'you',label:'你',kind:'you',x:.1,y:.5,info:'<b>你</b><br>用白話打出目標，例如「從原始計數重做表二」。'},
 {id:'model',label:'模型',kind:'agent',x:.27,y:.5,info:'<b>語言模型</b><br>決定下一步做什麼。在聊天裡它只能回文字。'},
 {id:'read',label:'讀檔案',kind:'agent',x:.66,y:.13,info:'<b>讀</b><br>打開你的程式、資料表頭、log 和規則檔。'},
 {id:'run',label:'執行指令',kind:'agent',x:.88,y:.5,info:'<b>執行</b><br>跑 Python、R、shell，送出叢集工作。每個指令都可以設定成要你同意。'},
 {id:'err',label:'讀輸出',kind:'agent',x:.66,y:.87,info:'<b>讀輸出</b><br>錯誤訊息、traceback、空檔案。它就是在這裡注意到（或沒注意到）出了問題。'},
 {id:'edit',label:'修改',kind:'agent',x:.47,y:.5,info:'<b>修改</b><br>改程式再跑一次。這個迴圈一直重複，直到它認為做完了。'},
 {id:'res',label:'結果',kind:'you',x:.27,y:.87,info:'<b>結果</b><br>檔案、數字、一段摘要。摘要是它自己的說法；檔案才是證據。'}],
 links:[{s:'you',t:'model',label:'目標'},{s:'model',t:'read',bend:-.1},{s:'read',t:'run'},{s:'run',t:'err'},{s:'err',t:'edit'},{s:'edit',t:'read',dash:1},{s:'err',t:'res'},{s:'res',t:'you',bend:.2,label:'你檢查'}]},

roles:{height:210,narrow:{height:330,pos:{q:[.5,.07],code:[.28,.42],jobs:[.72,.42],lit:[.28,.6],fig:[.72,.6],j:[.5,.93]}},
 groups:[{id:'ag',label:'代理做的事',members:['code','jobs','lit','fig']}],
 nodes:[
 {id:'q',label:'要問什麼',kind:'you',x:.11,y:.55,info:'選問題。代理不會告訴你這個問題沒意思。'},
 {id:'code',label:'寫程式',kind:'agent',x:.4,y:.42,info:'例行的分析又快，通常也對。'},
 {id:'jobs',label:'跑工作',kind:'agent',x:.62,y:.42,info:'寫並送出批次工作，查佇列。'},
 {id:'lit',label:'讀論文',kind:'agent',x:.4,y:.7,info:'附引文的摘要。每一句引文都要確認真的存在。'},
 {id:'fig',label:'畫圖',kind:'agent',x:.62,y:.7,info:'照寫好的規格畫得不錯；要你叫它，它才會檢查自己畫出來的圖。'},
 {id:'j',label:'答案對嗎？',kind:'you',x:.89,y:.55,info:'判斷結果。我大部分的失敗，都是沒有人真的檢查過的結果。'}],
 links:[{s:'q',t:'ag'},{s:'ag',t:'j'}]},

rules:{height:270,narrow:{height:310,pos:{file:[.18,.17],a1:[.5,.17],bad:[.79,.17],a2:[.15,.62],chk:[.45,.62],ok:[.8,.52],stop:[.7,.85]}},
 groups:[{id:'g1',label:'規則在檔案裡',members:['file','a1','bad']},{id:'g2',label:'規則在程式裡',members:['a2','chk','ok','stop']}],
 nodes:[
 {id:'file',label:'CLAUDE.md',kind:'file',x:.12,y:.2,info:'<b>規則檔</b><br>工作階段開始時讀一次。幾個小時後，沒有東西會再指回它。'},
 {id:'a1',label:'分析',kind:'agent',x:.45,y:.2,info:'本來應該遵守那條規則的分析。'},
 {id:'bad',label:'錯誤流出去',kind:'bad',x:.82,y:.2,info:'9 月 4 日：三個檔案裡早就禁止的錯。'},
 {id:'a2',label:'分析',kind:'agent',x:.12,y:.67,info:'同樣的分析，但規則擋在它的路上。'},
 {id:'chk',label:'檢查（程式）',kind:'you',x:.45,y:.67,info:'<b>它會拒絕：</b><br>資料不夠看出效應就說「沒有效應」<br>對照組用不同的量來配對<br>沒有樣本數的圖<br>在共用工作目錄裡 commit'},
 {id:'ok',label:'結果',kind:'ok',x:.82,y:.56,info:'只有通過檢查的結果到得了這裡。'},
 {id:'stop',label:'停下來並說明原因',kind:'bad',x:.82,y:.82,info:'執行失敗，並附上是哪一條規則擋下來的訊息。'}],
 links:[{s:'file',t:'a1',dash:1,label:'開始時讀一次'},{s:'a1',t:'bad',label:'幾小時後'},{s:'a2',t:'chk'},{s:'chk',t:'ok',label:'通過'},{s:'chk',t:'stop',label:'失敗'}]},

session:{type:'timeline',window:3,zh:1,steps:[
 {talk:'詳細討論了目標和限制。',file:'任務說明',disk:'BRIEF.md：目標、輸入、完成的定義、已知的坑。'},
 {talk:'決定排除兩個樣本，以及原因。',file:'待辦',disk:'待辦清單，排除樣本記成其中一步。'},
 {talk:'第一個工作失敗；修了模組版本。',file:'commit',disk:'含修正後工作腳本的 commit。'},
 {talk:'主要比較的數字。',file:'狀態',disk:'STATUS.md：結果、檔案路徑、怎麼算的。'},
 {talk:'對照組看起來怪怪的；重跑了。',file:'commit',disk:'含重跑的對照組及其輸出的 commit。'},
 {talk:'寫了摘要。',file:'狀態',disk:'STATUS.md 已更新；新的工作階段從這裡開始複查。'}]},

clean:{height:300,narrow:{height:340,pos:{m:[.25,.07],raw:[.75,.07],rb:[.5,.32],cmp:[.5,.55],p:[.15,.88],f:[.48,.88],b:[.82,.88]}},nodes:[
 {id:'m',label:'Methods 的文字',kind:'file',x:.1,y:.25,info:'只有寫下來的東西。不能看原本的程式或中間檔。'},
 {id:'raw',label:'原始輸入',kind:'file',x:.1,y:.75,info:'基因體、註解、reads：最開始的檔案。'},
 {id:'rb',label:'代理重做',kind:'agent',x:.42,y:.5,info:'在空資料夾裡。文字缺了細節時，它必須停下來說，而不是用猜的。'},
 {id:'cmp',label:'比對',kind:'agent',x:.68,y:.5,info:'每個發表的數字對上重做出來的數字。'},
 {id:'p',label:'PASS',kind:'ok',x:.9,y:.15,info:'和論文一致。'},
 {id:'f',label:'FAIL',kind:'bad',x:.9,y:.5,info:'不一致。一個真的需要解釋的差異。'},
 {id:'b',label:'BLOCKED',kind:'you',x:.9,y:.85,info:'照寫的內容算不出來。代理在這裡停下來並說明。'}],
 links:[{s:'m',t:'rb'},{s:'raw',t:'rb'},{s:'rb',t:'cmp'},{s:'cmp',t:'p'},{s:'cmp',t:'f'},{s:'cmp',t:'b'}]}
});
