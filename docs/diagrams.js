drawDiagrams({
modes:{height:120,narrow:{height:230,pos:{a:[.5,.1],p:[.5,.37],u:[.5,.63],n:[.5,.9]}},axis:['you watch every step','you check the result'],nodes:[
 {id:'a',label:'Approve each step',kind:'you',x:.12,y:.3,info:'<b>Approve each command</b><br>Use for: your first week, anything touching shared data, deleting files, or submitting many jobs.<br>Cost: you are the bottleneck; long tasks stall when you look away.'},
 {id:'p',label:'Approve the plan',kind:'file',x:.38,y:.3,info:'<b>Plan first, then let it run</b><br>It writes a plan; you read and correct it; then edits run without asking. Safe commands are pre-approved in a list; risky ones still ask.<br>This is where most of my daytime work sits.'},
 {id:'u',label:'Run unattended',kind:'agent',x:.64,y:.3,info:'<b>No questions asked</b><br>Only inside a bounded space: its own copy of the repository, no access to raw data it could overwrite, a limit on jobs it can submit.'},
 {id:'n',label:'Overnight',kind:'agent',x:.88,y:.3,info:'<b>Overnight</b><br>Works when the goal is one sentence, success is a check it can run, and the compute is chained in the scheduler. Fails when it needs your judgement at 2 a.m.'}],
 links:[{s:'a',t:'p'},{s:'p',t:'u'},{s:'u',t:'n'}]},
night:{height:250,narrow:{height:430,pos:{b:[.5,.05],s1:[.3,.25],c1:[.3,.43],s2:[.3,.61],c2:[.3,.79],j:[.72,.53],m:[.5,.95]}},axis:['evening','morning'],nodes:[
 {id:'b',label:'Brief + done-check',kind:'you',x:.11,y:.2,info:'<b>Before you leave</b><br>One-sentence goal. Which files must exist, how many rows, what range. Which commands it may run without asking.'},
 {id:'s1',label:'Stage 1',kind:'agent',x:.31,y:.2,info:'A small piece that ends in a file. Committed when done.'},
 {id:'c1',label:'Check',kind:'ok',x:.45,y:.2,info:'A check that has been seen to fail. If it fails, the agent stops and writes why, rather than trying to make it pass.'},
 {id:'s2',label:'Stage 2',kind:'agent',x:.6,y:.2,info:'Starts only from stage 1 output that passed.'},
 {id:'c2',label:'Check',kind:'ok',x:.74,y:.2,info:'Same rule.'},
 {id:'j',label:'Jobs chained in the scheduler',kind:'file',x:.46,y:.6,info:'Long compute runs as batch jobs that start each other when the previous one succeeds. No agent sits polling the queue.'},
 {id:'m',label:'Fresh review',kind:'you',x:.9,y:.6,info:'<b>Morning</b><br>A new session reads the commits, STATUS.md and the output files and reports what was done and what is unsupported. You read that, not the night session\'s own summary.'}],
 links:[{s:'b',t:'s1'},{s:'s1',t:'c1'},{s:'c1',t:'s2'},{s:'s2',t:'c2'},{s:'s1',t:'j',dash:1},{s:'j',t:'s2',dash:1},{s:'c2',t:'m'}]},
loop:{height:300,nodes:[
 {id:'you',label:'You',kind:'you',x:.1,y:.5,info:'<b>You</b><br>Type a goal in plain language: "rebuild Table 2 from the raw counts".'},
 {id:'model',label:'Model',kind:'agent',x:.27,y:.5,info:'<b>Language model</b><br>Decides the next action. In chat it can only reply with text.'},
 {id:'read',label:'Read files',kind:'agent',x:.66,y:.13,info:'<b>Read</b><br>Opens your scripts, data headers, logs and the rules file.'},
 {id:'run',label:'Run commands',kind:'agent',x:.88,y:.5,info:'<b>Run</b><br>Executes Python, R, shell, submits cluster jobs. Each command can need your approval.'},
 {id:'err',label:'Read output',kind:'agent',x:.66,y:.87,info:'<b>Read the output</b><br>Errors, tracebacks, empty files. This is where it notices (or misses) that something went wrong.'},
 {id:'edit',label:'Edit',kind:'agent',x:.47,y:.5,info:'<b>Edit</b><br>Changes code and runs again. The loop repeats until it decides it is done.'},
 {id:'res',label:'Result',kind:'you',x:.27,y:.87,info:'<b>Result</b><br>Files, numbers, a summary. The summary is its own account; the files are the evidence.'}],
 links:[{s:'you',t:'model',label:'goal'},{s:'model',t:'read',bend:-.1},{s:'read',t:'run'},{s:'run',t:'err'},{s:'err',t:'edit'},{s:'edit',t:'read',dash:1},{s:'err',t:'res'},{s:'res',t:'you',bend:.2,label:'you check'}]},

roles:{height:210,narrow:{height:330,pos:{q:[.5,.07],code:[.28,.42],jobs:[.72,.42],lit:[.28,.6],fig:[.72,.6],j:[.5,.93]}},
 groups:[{id:'ag',label:'the agent does',members:['code','jobs','lit','fig']}],
 nodes:[
 {id:'q',label:'What to ask',kind:'you',x:.11,y:.55,info:'Choosing the question. The agent will not tell you a question is uninteresting.'},
 {id:'code',label:'Write code',kind:'agent',x:.4,y:.42,info:'Fast and usually correct for routine analysis.'},
 {id:'jobs',label:'Run jobs',kind:'agent',x:.62,y:.42,info:'Writes and submits batch jobs, checks the queue.'},
 {id:'lit',label:'Read papers',kind:'agent',x:.4,y:.7,info:'Summaries with quotes. Check that each quote exists.'},
 {id:'fig',label:'Draw figures',kind:'agent',x:.62,y:.7,info:'Follows a written figure spec well; checks its own rendering only if told to.'},
 {id:'j',label:'Is it right?',kind:'you',x:.89,y:.55,info:'Judging the result. Most of my failures were results nobody had really checked.'}],
 links:[{s:'q',t:'ag'},{s:'ag',t:'j'}]},

rules:{height:270,narrow:{height:310,pos:{file:[.18,.17],a1:[.5,.17],bad:[.79,.17],a2:[.15,.62],chk:[.45,.62],ok:[.8,.52],stop:[.7,.85]}},
 groups:[{id:'g1',label:'rule in a file',members:['file','a1','bad']},{id:'g2',label:'rule in code',members:['a2','chk','ok','stop']}],
 nodes:[
 {id:'file',label:'CLAUDE.md',kind:'file',x:.12,y:.2,info:'<b>Rules file</b><br>Read once when the session starts. Hours later, nothing points back to it.'},
 {id:'a1',label:'Analysis',kind:'agent',x:.45,y:.2,info:'The analysis that was supposed to follow the rule.'},
 {id:'bad',label:'Defect ships',kind:'bad',x:.82,y:.2,info:'4 September: three defects the file already prohibited.'},
 {id:'a2',label:'Analysis',kind:'agent',x:.12,y:.67,info:'Same analysis, with the rule in its path.'},
 {id:'chk',label:'Check (code)',kind:'you',x:.45,y:.67,info:'<b>Refuses:</b><br>"no effect" without enough data to see one<br>a control matched on a different measure<br>a figure with no sample size<br>a commit in a shared checkout'},
 {id:'ok',label:'Result',kind:'ok',x:.82,y:.56,info:'Only results that passed the check get here.'},
 {id:'stop',label:'Stops with a reason',kind:'bad',x:.82,y:.82,info:'The run fails with a message saying which rule applied.'}],
 links:[{s:'file',t:'a1',dash:1,label:'read at start'},{s:'a1',t:'bad',label:'hours later'},{s:'a2',t:'chk'},{s:'chk',t:'ok',label:'passes'},{s:'chk',t:'stop',label:'fails'}]},

session:{type:'timeline',window:3,steps:[
 {talk:'Goal and constraints discussed in detail.',file:'brief',disk:'BRIEF.md: goal, inputs, what done means, known traps.'},
 {talk:'Decided to exclude two samples, and why.',file:'tasks',disk:'Task list with the exclusion recorded as a step.'},
 {talk:'First job failed; fixed the module version.',file:'commit',disk:'Commit with the fixed job script.'},
 {talk:'Numbers for the main comparison.',file:'status',disk:'STATUS.md: result, file path, how computed.'},
 {talk:'Control looked odd; reran it.',file:'commit',disk:'Commit with the rerun control and its output.'},
 {talk:'Wrote the summary.',file:'status',disk:'STATUS.md updated; a fresh session reviews from here.'}]},

clean:{height:300,narrow:{height:340,pos:{m:[.25,.07],raw:[.75,.07],rb:[.5,.32],cmp:[.5,.55],p:[.15,.88],f:[.48,.88],b:[.82,.88]}},nodes:[
 {id:'m',label:'Methods text',kind:'file',x:.1,y:.25,info:'Only what is written down. No access to the original scripts or intermediate files.'},
 {id:'raw',label:'Raw inputs',kind:'file',x:.1,y:.75,info:'Genome, annotation, reads: the starting files.'},
 {id:'rb',label:'Agent rebuilds',kind:'agent',x:.42,y:.5,info:'In an empty folder. When the text is missing a detail, it must stop and say so instead of guessing.'},
 {id:'cmp',label:'Compare',kind:'agent',x:.68,y:.5,info:'Each reported number against the rebuilt one.'},
 {id:'p',label:'PASS',kind:'ok',x:.9,y:.15,info:'Matches the paper.'},
 {id:'f',label:'FAIL',kind:'bad',x:.9,y:.5,info:'Does not match. A real discrepancy to explain.'},
 {id:'b',label:'BLOCKED',kind:'you',x:.9,y:.85,info:'Cannot be computed from the text. Mine: an unstated search setting changed 732 of 13,663 genes, and one filtering step was written nowhere.'}],
 links:[{s:'m',t:'rb'},{s:'raw',t:'rb'},{s:'rb',t:'cmp'},{s:'cmp',t:'p'},{s:'cmp',t:'f'},{s:'cmp',t:'b'}]}
});
