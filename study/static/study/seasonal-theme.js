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

  function addNavModalStyles(){
    if(document.getElementById('navModalStyles')) return;
    var style=document.createElement('style');
    style.id='navModalStyles';
    style.textContent='\
      .nav-modal-overlay{position:fixed;inset:0;z-index:5000;display:flex;align-items:center;justify-content:center;padding:24px;background:rgba(15,23,42,.48);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);opacity:0;visibility:hidden;transition:opacity .2s ease,visibility .2s ease}\
      .nav-modal-overlay.open{opacity:1;visibility:visible}\
      .nav-modal-card{width:min(92vw,520px);background:#fff;border:1px solid rgba(255,255,255,.75);border-radius:24px;padding:28px;box-shadow:0 30px 80px rgba(15,23,42,.30);transform:translateY(12px) scale(.985);transition:transform .2s ease}\
      .nav-modal-overlay.open .nav-modal-card{transform:none}\
      .nav-modal-top{display:flex;align-items:flex-start;justify-content:space-between;gap:18px}\
      .nav-modal-title{margin:0;font-size:28px;line-height:1.2;color:#0f172a}\
      .nav-modal-text{margin:10px 0 0;color:#64748b;line-height:1.6}\
      .nav-modal-close{border:0;background:#f1f5f9;color:#475569;width:40px;height:40px;border-radius:12px;font-size:25px;cursor:pointer;flex:0 0 auto}\
      .nav-modal-actions{display:flex;gap:10px;margin-top:24px}\
      .nav-modal-open,.nav-modal-cancel{flex:1;border:0;border-radius:12px;padding:13px 16px;font:inherit;font-weight:850;cursor:pointer;text-align:center}\
      .nav-modal-open{background:#0f766e;color:#fff}.nav-modal-cancel{background:#eef2f7;color:#334155}\
      body.nav-modal-open{overflow:hidden}\
      @media(max-width:560px){.nav-modal-overlay{align-items:flex-end;padding:0}.nav-modal-card{width:100%;border-radius:24px 24px 0 0;padding:24px 18px 26px}.nav-modal-title{font-size:24px}.nav-modal-actions{flex-direction:column}.nav-modal-open,.nav-modal-cancel{width:100%}}';
    document.head.appendChild(style);
  }

  function navMeta(href,text){
    if(href==='#tokutei') return {title:'🎓 Tokutei Ginou',text:'Mở khu học Tokutei và chọn ngành, Ginou 1 hoặc Ginou 2.',section:'tokutei'};
    if(href==='#jlpt') return {title:'🇯🇵 JLPT N5–N1',text:'Mở khu học JLPT và chọn cấp độ bạn muốn học.',section:'jlpt'};
    if(href==='#topics') return {title:'💬 Học theo chủ đề',text:'Mở khu học tiếng Nhật theo tình huống và chủ đề thực tế.',section:'topics'};
    if(href==='#dictionary') return {title:'🔍 Tra cứu Nhật ↔ Việt',text:'Mở khu tra cứu từ tiếng Nhật và tiếng Việt.',section:'dictionary'};
    if(href==='/premium/' || href.indexOf('/premium/')!==-1) return {title:'👑 Premium',text:'Xem các gói Premium và nội dung được mở khóa.',section:''};
    return {title:text||'Mở nội dung',text:'Bạn muốn mở mục này?',section:''};
  }

  function ensureNavModal(){
    var overlay=document.getElementById('navModalOverlay');
    if(overlay) return overlay;
    addNavModalStyles();
    overlay=document.createElement('div');
    overlay.id='navModalOverlay';
    overlay.className='nav-modal-overlay';
    overlay.setAttribute('aria-hidden','true');
    overlay.innerHTML='<div class="nav-modal-card" role="dialog" aria-modal="true" aria-labelledby="navModalTitle"><div class="nav-modal-top"><div><h2 class="nav-modal-title" id="navModalTitle"></h2><p class="nav-modal-text" id="navModalText"></p></div><button class="nav-modal-close" type="button" aria-label="Đóng">×</button></div><div class="nav-modal-actions"><button class="nav-modal-cancel" type="button">Đóng</button><button class="nav-modal-open" type="button">Mở nội dung →</button></div></div>';
    document.body.appendChild(overlay);
    function close(){overlay.classList.remove('open');overlay.setAttribute('aria-hidden','true');document.body.classList.remove('nav-modal-open');}
    overlay.querySelector('.nav-modal-close').addEventListener('click',close);
    overlay.querySelector('.nav-modal-cancel').addEventListener('click',close);
    overlay.addEventListener('click',function(e){if(e.target===overlay) close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&overlay.classList.contains('open')) close();});
    overlay._closeModal=close;
    return overlay;
  }

  function openNavModal(link){
    var overlay=ensureNavModal();
    var href=link.getAttribute('href')||'';
    var meta=navMeta(href,link.textContent.trim());
    overlay.querySelector('#navModalTitle').textContent=meta.title;
    overlay.querySelector('#navModalText').textContent=meta.text;
    var openBtn=overlay.querySelector('.nav-modal-open');
    openBtn.onclick=function(){
      overlay._closeModal();
      if(meta.section) setBrand(meta.section);
      if(href.charAt(0)==='#'){
        var target=document.querySelector(href);
        if(target){history.replaceState(null,'',href);target.scrollIntoView({behavior:'smooth',block:'start'});return;}
      }
      location.href=href;
    };
    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden','false');
    document.body.classList.add('nav-modal-open');
  }

  function bindTopNavModal(){
    if(location.pathname!=='/') return;
    var nav=document.querySelector('.nav');
    if(!nav) return;
    nav.querySelectorAll('a[href]').forEach(function(link){
      link.addEventListener('click',function(e){
        if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
        e.preventDefault();
        openNavModal(link);
      });
    });
  }

  function init(){
    document.documentElement.setAttribute('data-ui','business');
    hardNavigation();
    setBrand((location.hash||'').replace('#',''));
    bindHomeSections();
    bindTopNavModal();
    window.addEventListener('hashchange',function(){setBrand((location.hash||'').replace('#',''));});
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init);
  else init();
})();
