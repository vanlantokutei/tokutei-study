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
    if(path.indexOf('/tinh-huong')===0 || section==='topics') return '💬 HỌC THEO CHỦ ĐỀ';
    if(path.indexOf('/vocabulary')===0 || path.indexOf('/tokutei1/vocabulary')===0) return '📚 KHO TỪ VỰNG';
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
      document.querySelectorAll('a[href="#'+id+'"]').forEach(function(a){
        a.addEventListener('click',function(){setBrand(navMap[id]);});
      });
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
      .nav-modal-overlay{position:fixed;inset:0;z-index:5000;display:flex;align-items:center;justify-content:center;padding:24px;background:rgba(15,23,42,.50);backdrop-filter:blur(11px);-webkit-backdrop-filter:blur(11px);opacity:0;visibility:hidden;transition:.2s}\
      .nav-modal-overlay.open{opacity:1;visibility:visible}\
      .nav-modal-card{width:min(94vw,760px);max-height:86vh;overflow:auto;background:#fff;border-radius:26px;padding:26px;box-shadow:0 30px 90px rgba(15,23,42,.32);transform:translateY(12px) scale(.985);transition:.2s}\
      .nav-modal-overlay.open .nav-modal-card{transform:none}\
      .nav-modal-top{display:flex;align-items:flex-start;justify-content:space-between;gap:18px;margin-bottom:18px}\
      .nav-modal-title{margin:0;font-size:27px;color:#0f172a}.nav-modal-text{margin:7px 0 0;color:#64748b;line-height:1.55}\
      .nav-modal-close{border:0;background:#f1f5f9;color:#475569;width:40px;height:40px;border-radius:12px;font-size:25px;cursor:pointer}\
      .nav-choice-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}\
      .nav-choice{display:block;border:1px solid #dce7e5;border-radius:17px;padding:17px;background:#fff;cursor:pointer;transition:.16s}\
      .nav-choice:hover{border-color:#0f766e;background:#f0fdfa;transform:translateY(-1px);box-shadow:0 9px 22px rgba(15,118,110,.08)}\
      .nav-choice-icon{font-size:25px;display:block;margin-bottom:7px}.nav-choice-title{display:block;font-weight:900;color:#0f172a;font-size:16px}.nav-choice-desc{display:block;color:#64748b;font-size:12px;line-height:1.45;margin-top:5px}\
      .nav-choice.disabled{opacity:.5;cursor:not-allowed;background:#f8fafc}.nav-choice.disabled:hover{transform:none;box-shadow:none;border-color:#dce7e5;background:#f8fafc}\
      .nav-modal-foot{margin-top:17px;color:#94a3b8;font-size:12px;text-align:center}\
      body.nav-modal-open{overflow:hidden}\
      @media(max-width:600px){.nav-modal-overlay{align-items:flex-end;padding:0}.nav-modal-card{width:100%;max-height:88vh;border-radius:25px 25px 0 0;padding:22px 16px 25px}.nav-choice-grid{grid-template-columns:1fr}.nav-modal-title{font-size:23px}}';
    document.head.appendChild(style);
  }

  var menus={
    tokutei:{
      title:'🎓 Chọn nội dung Tokutei',
      text:'Chọn ngay phần bạn muốn vào.',
      choices:[
        ['1️⃣','Tokutei Ginou 1','Ôn thi, bài học và luyện đề.','/tokutei1/'],
        ['2️⃣','Tokutei Ginou 2','Nội dung dành cho Tokutei Ginou 2.','/tokutei2/'],
        ['📝','Đề thi thử','Làm đề và xem kết quả.','/tokutei1/exams/'],
        ['📚','Tài liệu học','Bài học và tài liệu theo nhóm.','/tokutei1/library/'],
        ['🈶','Từ vựng','Kho từ vựng Tokutei.','/tokutei1/vocabulary/'],
        ['💬','Tình huống thực tế','Tiếng Nhật dùng trong công việc.','/tinh-huong/']
      ]
    },
    jlpt:{
      title:'🇯🇵 Chọn cấp độ JLPT',
      text:'Chọn cấp độ bạn muốn học ngay.',
      choices:[
        ['N5','JLPT N5','Nhập môn, từ vựng, ngữ pháp, Kana.','/jlpt/n5/'],
        ['N4','JLPT N4','Nền tảng trung cấp sơ cấp.','/jlpt/n4/'],
        ['N3','JLPT N3','Cấp độ trung cấp.','/jlpt/n3/'],
        ['N2','JLPT N2','Luyện kỹ năng nâng cao.','/jlpt/n2/'],
        ['N1','JLPT N1','Cấp độ cao nhất.','/jlpt/n1/']
      ]
    },
    topics:{
      title:'💬 Chọn chủ đề học',
      text:'Chọn dạng nội dung bạn muốn luyện.',
      choices:[
        ['🍽️','Nhà hàng & phục vụ','Các tình huống giao tiếp thực tế.','/tinh-huong/'],
        ['🈶','Từ vựng theo chủ đề','Từ vựng dùng trong công việc.','/tokutei1/vocabulary/'],
        ['📚','Bài học theo nhóm','Học theo từng nhóm nội dung.','/tokutei1/library/']
      ]
    },
    dictionary:{
      title:'🔍 Chọn cách tra cứu',
      text:'Chọn nơi bạn muốn tìm nhanh.',
      choices:[
        ['🔎','Tra nhanh tại trang chủ','Tìm từ Nhật hoặc Việt ngay trên trang.','#dictionary'],
        ['🈶','Mở kho từ vựng','Xem danh sách từ và nghĩa tiếng Việt.','/tokutei1/vocabulary/'],
        ['💬','Tra theo tình huống','Tìm câu dùng trong tình huống thực tế.','/tinh-huong/']
      ]
    },
    premium:{
      title:'👑 Premium',
      text:'Chọn phần Premium bạn muốn xem.',
      choices:[
        ['💎','Xem các gói Premium','Xem giá, ưu đãi và quyền lợi.','/premium/'],
        ['📝','Đăng ký / yêu cầu Premium','Gửi yêu cầu sau khi chuyển khoản.','/premium/']
      ]
    }
  };

  function ensureNavModal(){
    var overlay=document.getElementById('navModalOverlay');
    if(overlay) return overlay;
    addNavModalStyles();
    overlay=document.createElement('div');
    overlay.id='navModalOverlay';
    overlay.className='nav-modal-overlay';
    overlay.setAttribute('aria-hidden','true');
    overlay.innerHTML='<div class="nav-modal-card" role="dialog" aria-modal="true"><div class="nav-modal-top"><div><h2 class="nav-modal-title" id="navModalTitle"></h2><p class="nav-modal-text" id="navModalText"></p></div><button class="nav-modal-close" type="button" aria-label="Đóng">×</button></div><div class="nav-choice-grid" id="navChoiceGrid"></div><div class="nav-modal-foot">Bấm ra ngoài vùng mờ hoặc nhấn Esc để đóng</div></div>';
    document.body.appendChild(overlay);
    function close(){overlay.classList.remove('open');overlay.setAttribute('aria-hidden','true');document.body.classList.remove('nav-modal-open');}
    overlay.querySelector('.nav-modal-close').addEventListener('click',close);
    overlay.addEventListener('click',function(e){if(e.target===overlay) close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&overlay.classList.contains('open')) close();});
    overlay._closeModal=close;
    return overlay;
  }

  function openMenu(type){
    var data=menus[type];
    if(!data) return;
    var overlay=ensureNavModal();
    overlay.querySelector('#navModalTitle').textContent=data.title;
    overlay.querySelector('#navModalText').textContent=data.text;
    var grid=overlay.querySelector('#navChoiceGrid');
    grid.innerHTML='';
    data.choices.forEach(function(c){
      var a=document.createElement('a');
      a.className='nav-choice';
      a.href=c[3];
      a.innerHTML='<span class="nav-choice-icon">'+c[0]+'</span><span class="nav-choice-title">'+c[1]+'</span><span class="nav-choice-desc">'+c[2]+'</span>';
      a.addEventListener('click',function(e){
        if(c[3].charAt(0)==='#'){
          e.preventDefault();overlay._closeModal();setBrand(type==='dictionary'?'dictionary':type);
          var target=document.querySelector(c[3]);
          if(target){history.replaceState(null,'',c[3]);target.scrollIntoView({behavior:'smooth',block:'start'});}
        }
      });
      grid.appendChild(a);
    });
    overlay.classList.add('open');overlay.setAttribute('aria-hidden','false');document.body.classList.add('nav-modal-open');
  }

  function bindTopNavModal(){
    if(location.pathname!=='/') return;
    var nav=document.querySelector('.nav');
    if(!nav) return;
    nav.querySelectorAll('a[href]').forEach(function(link){
      var href=link.getAttribute('href')||'';
      var type='';
      if(href==='#tokutei') type='tokutei';
      else if(href==='#jlpt') type='jlpt';
      else if(href==='#topics') type='topics';
      else if(href==='#dictionary') type='dictionary';
      else if(href.indexOf('/premium/')!==-1) type='premium';
      if(!type) return;
      link.addEventListener('click',function(e){
        if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
        e.preventDefault();setBrand(type);openMenu(type);
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
