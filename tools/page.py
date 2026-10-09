"""Shared page shell. Usage: from page import page; page('x.html','Title','<body html>')"""
PAGES=[("index.html","Essay"),("examples.html","Examples"),("reading.html","Reading"),("session.html","Session")]
def page(fn,title,body,desc="",script=""):
    nav='<nav>'+''.join(f'<a href="{h}"'+(' class="here"' if h==fn else '')+f'>{t}</a>' for h,t in PAGES)+'</nav>'
    open('docs/'+fn,'w').write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://chenhsieh.github.io/agentic-research-toolkit/img/card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://chenhsieh.github.io/agentic-research-toolkit/img/card.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3E%3Crect width=%2716%27 height=%2716%27 rx=%273%27 fill=%27%238a2c2c%27/%3E%3C/svg%3E">
<link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
{body}
<p class="small" style="margin-top:4em">Chen Hsieh · <a href="https://github.com/ChenHsieh/agentic-research-toolkit">source</a> · text CC BY 4.0</p>
<script src="toc.js"></script>
{script}
</body>
</html>
''')
COPY='''<script>
document.querySelectorAll('pre').forEach(function(p){var b=document.createElement('button');b.className='copy';b.textContent='copy';
b.onclick=function(){navigator.clipboard.writeText(p.querySelector('code').innerText).then(function(){b.textContent='copied';setTimeout(function(){b.textContent='copy'},1200)})};p.appendChild(b)});
</script>'''
COPY2='''<script>
document.querySelectorAll('pre,.prompt').forEach(function(el){var b=document.createElement('button');b.className='copy';b.type='button';b.textContent='Copy';
b.onclick=function(){var t=el.matches('pre')?el.querySelector('code').innerText:el.querySelector('p').innerText;navigator.clipboard.writeText(t).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1400)})};el.appendChild(b)});
</script>'''
