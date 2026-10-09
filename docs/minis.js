// Small illustrations for the failure patterns. Each draws into a 260x150 box.
(function(){
var INK='#333',RED='#8a2c2c',BLUE='#2f4a5c',OLIVE='#5c5a2f',GREEN='#2e6b45',GREY='#bbb';
function svg(el){return d3.select(el).append('svg').attr('viewBox','0 0 260 150').attr('width','100%')}
function t(s,x,y,txt,o){o=o||{};return s.append('text').attr('x',x).attr('y',y).attr('class','glabel').attr('text-anchor',o.a||'start').style('fill',o.c||'#555').style('font-size',(o.size||13)+'px').text(txt)}
var D={
 empty:function(s){ // treatment bar vs empty control, verdict "pass"
  s.append('line').attr('x1',30).attr('x2',170).attr('y1',120).attr('y2',120).attr('stroke',GREY);
  s.append('rect').attr('x',50).attr('y',45).attr('width',40).attr('height',75).attr('fill',BLUE);
  s.append('rect').attr('x',110).attr('y',45).attr('width',40).attr('height',75).attr('fill','none').attr('stroke',GREY).attr('stroke-dasharray','4 3');
  t(s,70,138,'treated',{a:'middle'});t(s,130,138,'control',{a:'middle'});t(s,130,88,'0 rows',{a:'middle',c:RED});
  s.append('rect').attr('x',185).attr('y',60).attr('width',62).attr('height',26).attr('rx',5).attr('fill',GREEN);
  t(s,216,78,'"passed"',{a:'middle',c:'#fff'});s.append('line').attr('x1',188).attr('x2',244).attr('y1',73).attr('y2',73).attr('stroke',RED).attr('stroke-width',2);
 },
 exit0:function(s){
  s.append('rect').attr('x',20).attr('y',30).attr('width',140).attr('height',14).attr('rx',3).attr('fill',BLUE);
  t(s,20,22,'job finished · exit 0');
  s.append('path').attr('d','M60 70h70l20 20v50h-90z').attr('fill','none').attr('stroke',INK);
  s.append('line').attr('x1',70).attr('x2',130).attr('y1',85).attr('y2',85).attr('stroke',INK);
  t(s,105,118,'header only',{a:'middle',c:RED});t(s,175,100,'0 data rows',{c:RED});
 },
 unit:function(s){ // pooled trend up, within-group flat/down
  var g=[[30,95],[105,65],[180,35]],r=d3.randomLcg(3);
  g.forEach(function(c,i){for(var k=0;k<8;k++){var x=c[0]+r()*40,y=c[1]+(x-c[0])*0.45+r()*6;
    s.append('circle').attr('cx',x).attr('cy',y).attr('r',3).attr('fill',[BLUE,OLIVE,RED][i]).attr('opacity',.85)}
    s.append('line').attr('x1',c[0]).attr('x2',c[0]+40).attr('y1',c[1]+3).attr('y2',c[1]+21).attr('stroke',[BLUE,OLIVE,RED][i])});
  s.append('line').attr('x1',30).attr('x2',225).attr('y1',112).attr('y2',38).attr('stroke',GREY).attr('stroke-dasharray','5 4');
  t(s,230,30,'pooled: up',{a:'end'});t(s,30,147,'within each group: down',{c:RED});
 },
 crash:function(s){
  s.append('line').attr('x1',20).attr('x2',240).attr('y1',75).attr('y2',75).attr('stroke',GREY);
  s.append('rect').attr('x',20).attr('y',62).attr('width',160).attr('height',26).attr('rx',4).attr('fill',BLUE);
  t(s,100,79,'25 min of computing',{a:'middle',c:'#fff'});
  t(s,195,58,'print',{a:'middle'});s.append('text').attr('x',195).attr('y',82).attr('text-anchor','middle').attr('fill',RED).style('font-size','20px').text('×');
  s.append('rect').attr('x',215).attr('y',62).attr('width',30).attr('height',26).attr('rx',4).attr('fill','none').attr('stroke',GREY).attr('stroke-dasharray','3 3');
  t(s,230,104,'save',{a:'middle',c:'#666'});t(s,20,130,'save first, print second',{c:RED});
 },
 stale:function(s){
  s.append('rect').attr('x',15).attr('y',40).attr('width',90).attr('height',60).attr('rx',5).attr('fill','none').attr('stroke',INK);
  t(s,60,32,'source',{a:'middle'});t(s,60,75,'corrected',{a:'middle',c:RED});
  s.append('rect').attr('x',155).attr('y',40).attr('width',90).attr('height',60).attr('rx',5).attr('fill','none').attr('stroke',INK);
  t(s,200,32,'your site',{a:'middle'});t(s,200,68,'old version',{a:'middle'});t(s,200,88,'checks ✓ ✓ ✓',{a:'middle',c:GREEN});
  s.append('line').attr('x1',110).attr('x2',150).attr('y1',70).attr('y2',70).attr('stroke',GREY).attr('stroke-dasharray','4 3');
  t(s,130,130,'the checks compare the site with itself',{a:'middle',c:RED});
 },
 gap:function(s){
  s.append('rect').attr('x',30).attr('y',20).attr('width',110).attr('height',115).attr('rx',4).attr('fill','none').attr('stroke',INK);
  t(s,40,38,'Methods');[55,70,100,115].forEach(function(y){s.append('line').attr('x1',40).attr('x2',128).attr('y1',y).attr('y2',y).attr('stroke',GREY)});
  s.append('rect').attr('x',40).attr('y',80).attr('width',88).attr('height',11).attr('fill','none').attr('stroke',RED).attr('stroke-dasharray','3 2');
  t(s,155,78,'setting never',{c:RED});t(s,155,93,'written down',{c:RED});t(s,155,122,'5% of genes',{});t(s,155,137,'change with it',{});
 },
 shared:function(s){
  s.append('rect').attr('x',90).attr('y',50).attr('width',80).attr('height',55).attr('rx',5).attr('fill','none').attr('stroke',INK);
  t(s,130,82,'one folder',{a:'middle'});
  [[20,30,'session A'],[200,30,'session B']].forEach(function(a){s.append('rect').attr('x',a[0]).attr('y',a[1]).attr('width',60).attr('height',22).attr('rx',4).attr('fill',BLUE);t(s,a[0]+30,a[1]+15,a[2],{a:'middle',c:'#fff'})});
  s.append('line').attr('x1',80).attr('x2',95).attr('y1',45).attr('y2',60).attr('stroke',INK);s.append('line').attr('x1',200).attr('x2',165).attr('y1',45).attr('y2',60).attr('stroke',INK);
  t(s,130,130,'B commits A\'s half-finished edit',{a:'middle',c:RED});
 }};
window.drawMinis=function(){document.querySelectorAll('[data-mini]').forEach(function(el){D[el.dataset.mini](svg(el))})};
})();
