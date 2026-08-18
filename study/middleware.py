import re


class RemoveVocabularyFlagMiddleware:
    """Normalize Vietnamese labels and improve JLPT N5 vocabulary navigation."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.path.startswith('/jlpt/n5/vocabulary/'):
            return response

        content_type = response.get('Content-Type', '')
        if 'text/html' not in content_type or getattr(response, 'streaming', False):
            return response

        try:
            html = response.content.decode(response.charset or 'utf-8')
        except (UnicodeDecodeError, AttributeError):
            return response

        html = html.replace('<div class="meaning">🇻🇳 ', '<div class="meaning"><span class="vn-label">Nghĩa tiếng Việt:</span> ')
        html = html.replace('<div class="vi">🇻🇳 ', '<div class="vi"><span class="vn-label">Dịch tiếng Việt:</span> ')
        html = html.replace('🇻🇳 ', '').replace('🇻🇳', '')

        def capitalize_meaning(match):
            prefix, value, suffix = match.groups()
            if not value:
                return match.group(0)
            return f'{prefix}{value[0].upper()}{value[1:]}{suffix}'

        html = re.sub(
            r'(<div class="meaning"><span class="vn-label">Nghĩa tiếng Việt:</span>\s*)([^<]*?)(</div>)',
            capitalize_meaning,
            html,
        )

        lesson_jump_script = r'''
<script id="jlpt-vocab-direct-jump">
(function () {
  var grid = document.getElementById('lessonGrid');
  if (!grid) return;

  var match = location.pathname.match(/\/lesson-(\d+)\/?$/);
  var currentLesson = match ? parseInt(match[1], 10) : 1;
  var maxAvailableLesson = 10;

  grid.querySelectorAll('.lesson-chip').forEach(function (chip) {
    var lesson = parseInt((chip.textContent || '').trim(), 10);
    if (!lesson || lesson > maxAvailableLesson) return;

    chip.classList.remove('live', 'ready');
    chip.classList.add(lesson === currentLesson ? 'live' : 'ready');
    chip.style.cursor = 'pointer';
    chip.setAttribute('role', 'link');
    chip.setAttribute('tabindex', '0');
    chip.setAttribute('aria-label', 'Mở bài từ vựng ' + lesson);

    var url = lesson === 1
      ? '/jlpt/n5/vocabulary/'
      : '/jlpt/n5/vocabulary/lesson-' + lesson + '/';

    function openLesson() {
      if (location.pathname !== url) location.href = url;
    }

    chip.addEventListener('click', openLesson);
    chip.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        openLesson();
      }
    });
  });
})();
</script>
'''

        section_menu_script = r'''
<style id="jlpt-n5-section-menu-style">
.jlpt-section-row{display:flex;align-items:center;gap:10px;position:relative;width:max-content;max-width:100%}
.jlpt-section-menu-btn{width:38px;height:38px;border:1px solid rgba(255,255,255,.28);border-radius:11px;background:rgba(255,255,255,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;cursor:pointer;padding:0;box-shadow:none!important;transform:none!important}
.jlpt-section-menu-btn span{display:block;width:18px;height:2px;border-radius:99px;background:#fff}
.jlpt-section-menu{position:absolute;top:46px;left:0;z-index:1000;width:min(330px,86vw);background:#fff;border:1px solid #dbe5e8;border-radius:17px;padding:9px;box-shadow:0 20px 45px rgba(15,23,42,.22);display:none}
.jlpt-section-menu.open{display:block}
.jlpt-section-menu a{display:flex;align-items:center;gap:11px;padding:12px 13px;border-radius:12px;color:#1e293b!important;text-decoration:none!important;font-weight:800;font-size:14px}
.jlpt-section-menu a:hover{background:#f0fdfa;color:#0f766e!important}
.jlpt-section-menu a.current{background:#0f766e;color:#fff!important}
.jlpt-section-menu .mi{width:28px;text-align:center;font-size:19px}
@media(max-width:560px){.jlpt-section-menu{position:fixed;left:16px;right:16px;top:auto;bottom:18px;width:auto;max-height:70vh;overflow:auto}.jlpt-section-menu-btn{width:36px;height:36px}}
</style>
<script id="jlpt-n5-section-menu">
(function(){
  var badge=document.querySelector('.badge');
  if(!badge || document.getElementById('jlptN5SectionMenuBtn')) return;
  var row=document.createElement('div');row.className='jlpt-section-row';badge.parentNode.insertBefore(row,badge);row.appendChild(badge);
  var btn=document.createElement('button');btn.type='button';btn.id='jlptN5SectionMenuBtn';btn.className='jlpt-section-menu-btn';btn.setAttribute('aria-label','Mở menu JLPT N5');btn.setAttribute('aria-expanded','false');btn.innerHTML='<span></span><span></span><span></span>';row.appendChild(btn);
  var menu=document.createElement('nav');menu.className='jlpt-section-menu';menu.id='jlptN5SectionMenu';menu.innerHTML='\
    <a href="/jlpt/n5/alphabet/"><span class="mi">🔤</span>Bảng chữ cái</a>\
    <a class="current" href="/jlpt/n5/vocabulary/"><span class="mi">🈶</span>Từ vựng</a>\
    <a href="/jlpt/n5/?section=kanji"><span class="mi">漢</span>Kanji</a>\
    <a href="/jlpt/n5/grammar/"><span class="mi">文</span>Ngữ pháp</a>\
    <a href="/jlpt/n5/?section=reading"><span class="mi">📖</span>Đọc hiểu</a>\
    <a href="/jlpt/n5/?section=listening"><span class="mi">🎧</span>Nghe hiểu</a>\
    <a href="/jlpt/n5/?section=mock"><span class="mi">🎯</span>Thi thử</a>\
    <a href="/jlpt/n5/"><span class="mi">↩️</span>Trang JLPT N5</a>';row.appendChild(menu);
  function closeMenu(){menu.classList.remove('open');btn.setAttribute('aria-expanded','false');}
  btn.addEventListener('click',function(e){e.stopPropagation();var open=menu.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');});
  document.addEventListener('click',function(e){if(!row.contains(e.target)) closeMenu();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape') closeMenu();});
})();
</script>
'''

        additions = ''
        if 'id="jlpt-vocab-direct-jump"' not in html:
            additions += lesson_jump_script
        if 'id="jlpt-n5-section-menu"' not in html:
            additions += section_menu_script

        if additions:
            if '</body>' in html:
                html = html.replace('</body>', additions + '</body>')
            else:
                html += additions

        response.content = html.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))

        return response
