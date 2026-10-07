// Side contents with current-section marker, and a thin reading-progress line.
(function(){
  var hs=[].slice.call(document.querySelectorAll('h2'));
  var bar=document.createElement('div');bar.className='progress';document.body.appendChild(bar);
  function prog(){var h=document.documentElement,max=h.scrollHeight-innerHeight;bar.style.width=(max>0?100*scrollY/max:0)+'%'}
  addEventListener('scroll',prog,{passive:true});prog();
  if(hs.length<3)return;
  var nav=document.createElement('aside');nav.className='toc';
  var title=document.querySelector('h1');
  nav.innerHTML='<div class="toc-h">'+(title?title.textContent:'Contents')+'</div>';
  var ol=document.createElement('ol');
  hs.forEach(function(h,i){
    if(!h.id)h.id=h.textContent.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
    var li=document.createElement('li');li.innerHTML='<a href="#'+h.id+'"><span>'+(i+1)+'</span>'+h.textContent+'</a>';ol.appendChild(li)});
  nav.appendChild(ol);document.body.appendChild(nav);
  var links=[].slice.call(ol.querySelectorAll('a'));
  function spy(){var cur=0;hs.forEach(function(h,i){if(h.getBoundingClientRect().top<innerHeight*0.3)cur=i});
    links.forEach(function(a,i){a.classList.toggle('on',i===cur)})}
  addEventListener('scroll',spy,{passive:true});spy();
})();
