// Small static diagrams with hover (and keyboard focus) for detail. Needs d3 v7.
(function(){
var tip=document.createElement('div');tip.className='gtip';document.body.appendChild(tip);
function showTip(ev,html){if(!html)return;tip.innerHTML=html;tip.style.opacity=1;moveTip(ev)}
function moveTip(ev){var x=ev.clientX+14,y=ev.clientY+14,w=tip.offsetWidth;if(x+w>innerWidth-8)x=ev.clientX-w-14;if(x<8)x=8;tip.style.left=x+'px';tip.style.top=y+'px'}
function hideTip(){tip.style.opacity=0}
var C={you:'#8a2c2c',agent:'#2f4a5c',file:'#5c5a2f',bad:'#b03a2e',ok:'#2e6b45',muted:'#8a8a8a'};

function graph(el,spec){
  var W=el.clientWidth||640,narrow=W<520,alt=narrow&&spec.narrow,H=alt?spec.narrow.height:(spec.height||320)*(narrow?1.35:1);
  var svg=d3.select(el).append('svg').attr('viewBox',[0,0,W,H]).attr('width','100%').attr('height',H);
  var id='a'+Math.random().toString(36).slice(2,7);
  svg.append('defs').append('marker').attr('id',id).attr('viewBox','0 -4 8 8').attr('refX',8).attr('markerWidth',7).attr('markerHeight',7).attr('orient','auto')
    .append('path').attr('d','M0,-4L8,0L0,4').attr('fill','#999');
  var nodes=spec.nodes.map(function(n){var q=alt&&spec.narrow.pos[n.id]?spec.narrow.pos[n.id]:[n.x,n.y];return Object.assign({},n,{tx:q[0]*W,ty:q[1]*H,x:q[0]*W,y:q[1]*H})});
  var byId={};nodes.forEach(function(n){byId[n.id]=n});
  var links=(spec.links||[]).map(function(l){return Object.assign({},l,{source:byId[l.s],target:byId[l.t]})});
  if(spec.axis&&!alt){var ay=H-14;svg.append('line').attr('x1',4).attr('x2',W-4).attr('y1',ay).attr('y2',ay).attr('stroke','#bbb').attr('marker-end','url(#'+id+')');
    svg.append('text').attr('class','glabel').attr('x',4).attr('y',ay-6).text(spec.axis[0]);
    svg.append('text').attr('class','glabel').attr('x',W-6).attr('y',ay-6).attr('text-anchor','end').text(spec.axis[1]);}
  var link=svg.append('g').selectAll('g').data(links).join('g');
  var lp=link.append('path').attr('fill','none').attr('stroke',function(l){return l.color?C[l.color]:'#aaa'}).attr('stroke-width',1.4)
    .attr('stroke-dasharray',function(l){return l.dash?'4 4':null}).attr('marker-end','url(#'+id+')');
  var lt=link.append('text').attr('class','glabel').text(function(l){return narrow?'':(l.label||'')});
  var node=svg.append('g').selectAll('g').data(nodes).join('g').attr('class','gnode');
  node.append('rect').attr('rx',7);
  node.append('text').attr('text-anchor','middle').attr('dy','0.35em').attr('fill','#fff').attr('class','gname')
    .text(function(n){return n.label});
  node.each(function(n){var t=d3.select(this).select('text').node().getBBox();n.w=t.width+22;n.h=t.height+12;
    d3.select(this).select('rect').attr('x',-n.w/2).attr('y',-n.h/2).attr('width',n.w).attr('height',n.h)
      .attr('fill',C[n.kind]||C.agent).attr('fill-opacity',n.faint?0.35:1)});
  node.attr('tabindex',0).attr('role','img').attr('aria-label',function(n){return n.label+(n.info?': '+n.info.replace(/<[^>]+>/g,' '):'')})
    .on('focus',function(ev,n){var r=this.getBoundingClientRect();showTip({clientX:r.right,clientY:r.bottom},n.info)}).on('blur',hideTip);
  node.on('mouseover',function(ev,n){showTip(ev,n.info);
      lp.attr('stroke-opacity',function(l){return l.source===n||l.target===n?1:0.25})})
    .on('mousemove',moveTip).on('mouseout',function(){hideTip();lp.attr('stroke-opacity',1)})
    .on('click',function(ev,n){if(n.url)window.open(n.url,'_blank')});
  // settle overlaps once, off-screen, then draw a static layout
  var sim=d3.forceSimulation(nodes).stop()
    .force('x',d3.forceX(function(n){return n.tx}).strength(0.4))
    .force('y',d3.forceY(function(n){return n.ty}).strength(0.4))
    ;
  if(spec.collide)sim.force('c',d3.forceCollide(function(n){return n.w/2+6}).strength(0.8));
  for(var i=0;i<200;i++){sim.tick();nodes.forEach(function(n){n.x=Math.max(n.w/2+2,Math.min(W-n.w/2-2,n.x));n.y=Math.max(n.h/2+2,Math.min(H-n.h/2-2,n.y))})}
  node.attr('transform',function(n){return 'translate('+n.x+','+n.y+')'}).style('cursor',function(n){return n.url?'pointer':'default'});
  lp.attr('d',function(l){var a=l.source,b=l.target,dx=b.x-a.x,dy=b.y-a.y;
    var p=edge(a,dx,dy),q=edge(b,-dx,-dy),bend=l.bend||0;
    var mx=(p[0]+q[0])/2-dy*bend,my=(p[1]+q[1])/2+dx*bend;l.mx=mx;l.my=my;
    return 'M'+p[0]+','+p[1]+'Q'+mx+','+my+' '+q[0]+','+q[1]});
  lt.attr('x',function(l){return l.mx}).attr('y',function(l){return l.my-5}).attr('text-anchor','middle');
  node.on('mouseover.hl',function(){d3.select(this).select('rect').attr('stroke','#111').attr('stroke-width',1.5)})
      .on('mouseout.hl',function(){d3.select(this).select('rect').attr('stroke',null)});
  function edge(n,dx,dy){var hw=n.w/2+3,hh=n.h/2+3,s=Math.min(Math.abs(dx)>1e-6?hw/Math.abs(dx):1e9,Math.abs(dy)>1e-6?hh/Math.abs(dy):1e9);return [n.x+dx*s,n.y+dy*s]}
  if(spec.legend){el.insertAdjacentHTML('beforeend','<div class="gnote">'+spec.legend.map(function(l){return '<span style="display:inline-block;width:.8em;height:.8em;border-radius:3px;background:'+C[l[0]]+';margin:0 .35em 0 .9em;vertical-align:-1px"></span>'+l[1]}).join('')+'</div>')}
  if(spec.note){el.insertAdjacentHTML('beforeend','<div class="gnote">'+spec.note+'</div>')}
  var withInfo=spec.nodes.filter(function(n){return n.info});
  if(withInfo.length&&!spec.nokey){el.insertAdjacentHTML('beforeend','<details class="gkey"><summary>What each box means</summary><dl>'+withInfo.map(function(n){return '<dt>'+n.label+'</dt><dd>'+n.info.replace(/^<b>[^<]*<\/b><br>/,'')+'</dd>'}).join('')+'</dl></details>')}
}

function timeline(el,spec){
  var W=el.clientWidth||640,H=190,n=spec.steps.length,pad=10,bw=(W-90-pad*n)/n;
  var svg=d3.select(el).append('svg').attr('viewBox',[0,0,W,H]).attr('width','100%').attr('height',H);
  svg.append('text').attr('class','glabel').attr('x',0).attr('y',42).text('conversation');
  svg.append('text').attr('class','glabel').attr('x',0).attr('y',122).text('files');
  var conv=svg.selectAll('.cv').data(spec.steps).join('rect').attr('x',function(d,i){return 90+i*(bw+pad)}).attr('y',25).attr('width',bw).attr('height',30).attr('rx',6).attr('fill',C.agent);
  var file=svg.selectAll('.fl').data(spec.steps).join('rect').attr('x',function(d,i){return 90+i*(bw+pad)}).attr('y',105).attr('width',bw).attr('height',30).attr('rx',6).attr('fill',C.file);
  svg.selectAll('.ft').data(spec.steps).join('text').attr('class','gname').attr('fill','#fff').attr('text-anchor','middle')
    .attr('x',function(d,i){return 90+i*(bw+pad)+bw/2}).attr('y',125).text(function(d){return W<520?'':d.file});
  var label=svg.append('text').attr('class','glabel').attr('x',W/2).attr('y',175).attr('text-anchor','middle');
  var row=document.createElement('div');row.className='gnote';
  row.innerHTML='<label>hours into the session <input type="range" min="0" max="'+(n-1)+'" value="0" style="vertical-align:middle;width:12em"></label>';
  el.appendChild(row);var inp=row.querySelector('input');
  function upd(){var t=+inp.value,keep=spec.window;
    conv.transition().duration(250).attr('fill-opacity',function(d,i){return i>t?0.08:(t-i<keep?1:0.18)}).attr('fill',function(d,i){return t-i<keep?C.agent:C.muted});
    file.transition().duration(250).attr('fill-opacity',function(d,i){return i>t?0.08:1});
    var lost=Math.max(0,t+1-keep);label.text(lost?lost+' of '+(t+1)+' steps now only exist as a summary in the conversation; all '+(t+1)+' are on disk':'everything is still in the conversation');}
  inp.oninput=upd;upd();
  conv.on('mouseover',function(ev,d){showTip(ev,'<b>Conversation, step '+(spec.steps.indexOf(d)+1)+'</b><br>'+d.talk)}).on('mousemove',moveTip).on('mouseout',hideTip);
  file.on('mouseover',function(ev,d){showTip(ev,'<b>On disk: '+d.file+'</b><br>'+d.disk)}).on('mousemove',moveTip).on('mouseout',hideTip);
}
window.drawDiagrams=function(specs){document.querySelectorAll('[data-g]').forEach(function(el){var s=specs[el.dataset.g];if(!s)return;(s.type==='timeline'?timeline:graph)(el,s)})};
})();
