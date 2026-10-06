"""Draws the site's line figures as SVG. Run: python3 tools/draw.py"""
import random, math
INK="#1a1a1a"; RED="#a33"; GREY="#999"
FONT='font-family="Georgia,Times New Roman,serif"'

class Fig:
    def __init__(s,w,h,seed=1): s.w,s.h=w,h; s.o=[]; s.r=random.Random(seed)
    def j(s,a=1.2): return s.r.uniform(-a,a)
    def line(s,x1,y1,x2,y2,c=INK,w=1.6,dash=None):
        mx,my=(x1+x2)/2+s.j(2),(y1+y2)/2+s.j(2)
        d=f'stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<path d="M{x1+s.j():.1f},{y1+s.j():.1f} Q{mx:.1f},{my:.1f} {x2+s.j():.1f},{y2+s.j():.1f}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" {d}/>')
    def box(s,x,y,w,h,c=INK,dash=None,fill=None):
        if fill: s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="none"/>')
        for a,b,cc,dd in [((x,y),(x+w,y),0,0),((x+w,y),(x+w,y+h),0,0),((x+w,y+h),(x,y+h),0,0),((x,y+h),(x,y),0,0)]:
            s.line(*a,*b,c=c,dash=dash)
    def arrow(s,x1,y1,x2,y2,c=INK,dash=None):
        s.line(x1,y1,x2,y2,c=c,dash=dash); a=math.atan2(y2-y1,x2-x1)
        for d in (2.6,-2.6):
            s.line(x2,y2,x2-11*math.cos(a+d/6),y2-11*math.sin(a+d/6),c=c)
    def text(s,x,y,t,size=15,c=INK,anchor="middle",style=""):
        lines=t.split("\n")
        for i,l in enumerate(lines):
            s.o.append(f'<text x="{x}" y="{y+i*size*1.6}" {FONT} font-size="{size*1.3:.0f}" fill="{c}" text-anchor="{anchor}" {style}>{l}</text>')
    def label_box(s,x,y,w,h,t,size=15,c=INK,dash=None,fill=None,tc=None):
        s.box(x,y,w,h,c=c,dash=dash,fill=fill); n=t.count("\n")+1
        s.text(x+w/2,y+h/2-(n-1)*size*0.8+size*0.45,t,size,tc or c)
    def person(s,x,y,c=INK):
        s.o.append(f'<circle cx="{x+s.j(.5):.1f}" cy="{y}" r="11" fill="none" stroke="{c}" stroke-width="1.6"/>')
        s.line(x,y+11,x,y+42,c=c); s.line(x,y+20,x-14,y+32,c=c); s.line(x,y+20,x+14,y+32,c=c)
        s.line(x,y+42,x-11,y+62,c=c); s.line(x,y+42,x+11,y+62,c=c)
    def save(s,name):
        open(f"docs/fig/{name}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" width="{s.w}" height="{s.h}">\n'+"\n".join(s.o)+"\n</svg>\n")

# a. chat vs agent
f=Fig(640,330,2)
f.text(160,28,"Chat",17,style='font-style="italic"'); f.text(480,28,"Agent",17,style='font-style="italic"')
f.person(60,70); f.label_box(150,85,130,44,"model"); f.arrow(85,100,145,102); f.arrow(215,135,215,185)
f.label_box(160,190,110,40,"text"); f.text(215,262,"you copy it, run it,\npaste the error back",13,GREY)
f.line(320,40,320,280,c="#ccc")
f.person(380,70); f.label_box(450,85,140,44,"model"); f.arrow(405,100,445,102)
for (x,y),l in [((520,165),"read files"),((600,222),"run it"),((520,282),"read error"),((440,222),"edit")]: f.text(x,y,l,13)
f.arrow(520,132,520,148)
f.arrow(552,170,580,200); f.arrow(580,236,552,264); f.arrow(488,264,460,236); f.arrow(460,200,488,170)
f.text(520,318,"it runs the loop itself",13,GREY); f.save("chat-vs-agent")

# b. you and the agent
f=Fig(640,225,3)
f.person(90,60); f.text(90,155,"you",15)
f.text(90,185,"what to ask\nwhether it is right",13,RED)
f.label_box(370,70,180,64,"agent\ncode · jobs · reading",14)
f.arrow(130,80,360,90); f.text(245,72,"a question",13)
f.arrow(360,120,130,120); f.text(245,140,"results",13)
f.text(460,175,"fast, tireless,\nsometimes confidently wrong",13,GREY)
f.save("you-and-agent")

# c. rules in a file vs in code
f=Fig(640,300,4)
f.text(160,28,"Rule in a file",16,style='font-style="italic"'); f.text(480,28,"Rule in code",16,style='font-style="italic"')
f.label_box(40,60,120,50,"CLAUDE.md",13,GREY)
f.arrow(30,190,290,190); f.text(100,175,"analysis",13)
f.text(160,230,"the file was read at the start;\nnothing points to it now",13,GREY)
f.text(300,165,"defect ships",13,RED,anchor="end")
f.line(320,40,320,280,c="#ccc")
f.arrow(350,190,470,190); f.text(400,175,"analysis",13)
f.box(475,150,22,80,c=RED,fill="#f6e6e6"); f.text(486,250,"check",13,RED)
f.text(560,180,"stops:\nno power check,\nno result",13,RED)
f.save("rules-file-vs-code")

# d. long session
f=Fig(640,260,5)
f.text(30,40,"conversation",14,anchor="start")
for i in range(6):
    op=["#ccc","#bbb","#999","#777","#444",INK][i]
    f.box(150+i*78,22,66,32,c=op,dash="4 3" if i<3 else None)
f.text(150+0*78+33,74,"summarized",12,GREY); f.text(150+5*78+33,74,"now",12)
f.text(30,150,"files on disk",14,anchor="start")
for i,l in enumerate(["brief","task list","status","commit","commit","status"]):
    f.label_box(150+i*78,130,66,32,l,12)
f.arrow(150,200,600,200); f.text(375,225,"hours",13,GREY)
f.text(375,250,"the files are still complete at the end; the conversation is not",13,GREY)
f.save("long-session")

# e. clean room
f=Fig(640,250,6)
f.label_box(20,40,130,60,"Methods text\n+ raw inputs",13)
f.arrow(155,70,215,70)
f.label_box(220,30,150,80,"empty folder\nagent rebuilds\nno old files",13,dash="5 3")
f.arrow(375,70,430,70)
f.label_box(435,40,180,60,"compare with the\nreported numbers",13)
f.arrow(525,105,525,140)
f.text(445,165,"PASS",14,anchor="start"); f.text(445,190,"FAIL",14,anchor="start"); f.text(445,215,"BLOCKED: text missing",14,RED,anchor="start")
f.text(200,180,"the BLOCKED list is the result:\neverything you knew\nbut never wrote down",13,GREY)
f.save("clean-room")
print("ok")

# f. landscape: how much the human stays in the loop
f=Fig(640,250,7)
f.arrow(40,120,600,120)
f.text(40,150,"you drive",14,anchor="start"); f.text(600,150,"it drives",14,anchor="end")
for x,y,l in [(80,80,"Claude Code\nCodex · Aider"),(230,80,"PaperQA2\nBiomni"),(380,80,"Virtual Lab\nRobin"),(530,80,"AI Scientist\nKosmos")]:
    f.text(x,y-34,l,16); f.line(x,y+12,x,114,c=GREY)
f.text(320,200,"benchmarks: weakest at choosing methods\nand interpreting results, not running code",15,RED)
f.save("landscape")
