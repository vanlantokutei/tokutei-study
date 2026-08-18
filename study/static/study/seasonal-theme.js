(function(){
  function hardNavigation(){
    document.addEventListener('click',function(e){
      if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
      var a=e.target.closest&&e.target.closest('a[href]');
      if(!a||a.target==='_blank'||a.hasAttribute('download')) return;
      var u;
      try{u=new URL(a.href,location.href);}catch(err){return;}
      if(u.origin!==location.origin) return;
    },false);
  }

  function brandTextFor(path,section){
    if(path.indexOf('/jlpt/')===0 || section==='jlpt') return '🇯🇵 JLPT';
    if(path.indexOf('/tokutei')===0 || path.indexOf('/exams')===0 || section==='tokutei') return '🎓 TOKUTEI GINOU';
    if(path.indexOf('/service')===0 || section==='topics') return '💬 HỌC THEO CHỦ ĐỀ';
    if(path.indexOf('/vocabulary')===0) return '📚 KHO TỪ VỰNG';
    if(section==='dictionary') return '🔍 TRA CỨU NHẬT ↔ VIỆT';
    return '🇯🇵 ÔN THI TOKUTEI';
  }

  function setBrand(section){
    var brand=document.querySelector('.brand');
    if(!brand) return;
    brand.textContent=brandTextFor(location.pathname,section||'');
  }

  function bindHomeSections(){
    var navMap={tokutei:'tokutei',jlpt:'jlpt',topics:'topics',dictionary:'dictionary'};
    Object.keys(navMap).forEach(function(id){
      var links=document.querySelectorAll('a[href="#'+id+'"]');
      links.forEach(function(a){a.addEventListener('click',function(){setBrand(navMap[id]);});});
    });
    var cards=[['.main-card.tokutei','tokutei'],['.main-card.jlpt','jlpt'],['.main-card.topic','topics'],['.main-card.dictionary','dictionary']];
    cards.forEach(function(item){
      var el=document.querySelector(item[0]);
      if(el) el.addEventListener('click',function(){setBrand(item[1]);});
    });
  }

  function init(){
    document.documentElement.setAttribute('data-ui','business');
    hardNavigation();
    setBrand((location.hash||'').replace('#',''));
    bindHomeSections();
    window.addEventListener('hashchange',function(){setBrand((location.hash||'').replace('#',''));});
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init);
  else init();
})();
