"""Shared page shell. Usage: from page import page; page('x.html','Title','<body html>')"""
PAGES=[("index.html","Essay"),("examples.html","Examples"),("practice.html","Practice"),("reading.html","Reading"),("session.html","Session")]
def page(fn,title,body,desc="",script=""):
    nav='<nav>'+''.join(f'<a href="{h}"'+(' class="here"' if h==fn else '')+f'>{t}</a>' for h,t in PAGES)+'</nav>'
    open('docs/'+fn,'w').write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
{body}
<p class="small" style="margin-top:4em">Chen Hsieh · <a href="https://github.com/ChenHsieh/agentic-research-toolkit">source</a> · text CC BY 4.0</p>
{script}
</body>
</html>
''')
COPY='''<script>
document.querySelectorAll('pre').forEach(function(p){var b=document.createElement('button');b.className='copy';b.textContent='copy';
b.onclick=function(){navigator.clipboard.writeText(p.querySelector('code').innerText).then(function(){b.textContent='copied';setTimeout(function(){b.textContent='copy'},1200)})};p.appendChild(b)});
</script>'''
