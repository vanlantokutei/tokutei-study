import re


class RemoveVocabularyFlagMiddleware:
    """Normalize JLPT N5 vocabulary pages and shared navigation."""

    def __init__(self, get_response): self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.path.startswith('/jlpt/n5/vocabulary/'): return response
        content_type = response.get('Content-Type', '')
        if 'text/html' not in content_type or getattr(response, 'streaming', False): return response
        try: html = response.content.decode(response.charset or 'utf-8')
        except (UnicodeDecodeError, AttributeError): return response
        html = html.replace('<div class="meaning">🇻🇳 ', '<div class="meaning"><span class="vn-label">Nghĩa tiếng Việt:</span> ')
        html = html.replace('<div class="vi">🇻🇳 ', '<div class="vi"><span class="vn-label">Dịch tiếng Việt:</span> ')
        html = html.replace('🇻🇳 ', '').replace('🇻🇳', '')
        def cap(m):
            prefix,value,suffix=m.groups(); stripped=(value or '').lstrip()
            if not stripped:return m.group(0)
            lead=value[:len(value)-len(stripped)]; return f'{prefix}{lead}{stripped[0].upper()}{stripped[1:]}{suffix}'
        html=re.sub(r'(<div class="meaning"><span class="vn-label">Nghĩa tiếng Việt:</span>\s*)([^<]*?)(</div>)',cap,html)
        capitalization_script=r'''<script id="jlpt-vocab-capitalize-meaning">(function(){function c(n){var t=n.nodeValue||'',m=t.match(/^(\s*)([a-zà-ỹ])/i);if(!m)return false;var i=m[1].length,ch=t.charAt(i),u=ch.toLocaleUpperCase('vi-VN');if(ch===u)return false;n.nodeValue=t.slice(0,i)+u+t.slice(i+1);return true}function f(e){if(!e||!e.classList||!e.classList.contains('meaning'))return;var ns=[].slice.call(e.childNodes);for(var i=0;i<ns.length;i++){var n=ns[i];if(n.nodeType===Node.TEXT_NODE&&c(n))return;if(n.nodeType===Node.ELEMENT_NODE&&!n.classList.contains('vn-label')&&n.tagName!=='B'&&n.tagName!=='STRONG'){var w=document.createTreeWalker(n,NodeFilter.SHOW_TEXT),x;while((x=w.nextNode()))if(c(x))return}}}function a(r){if(r&&r.classList&&r.classList.contains('meaning'))f(r);(r||document).querySelectorAll&&(r||document).querySelectorAll('.meaning').forEach(f)}a(document);new MutationObserver(function(ms){ms.forEach(function(m){m.addedNodes.forEach(function(n){if(n.nodeType===Node.ELEMENT_NODE)a(n)})})}).observe(document.body,{childList:true,subtree:true})})();</script>'''
        lesson_jump_script=r'''<script id="jlpt-vocab-direct-jump">(function(){var g=document.getElementById('lessonGrid');if(!g)return;var m=location.pathname.match(/\/lesson-(\d+)\/?$/),cur=m?parseInt(m[1],10):1,max=13;g.querySelectorAll('.lesson-chip').forEach(function(c){var n=parseInt((c.textContent||'').trim(),10);if(!n||n>max)return;c.classList.remove('live','ready');c.classList.add(n===cur?'live':'ready');c.style.cursor='pointer';c.setAttribute('role','link');c.setAttribute('tabindex','0');var u=n===1?'/jlpt/n5/vocabulary/':'/jlpt/n5/vocabulary/lesson-'+n+'/';function o(){if(location.pathname!==u)location.href=u}c.addEventListener('click',o);c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();o()}})})})();</script>'''
        section_menu_script=r'''<style id="jlpt-n5-section-menu-style">.jlpt-section-row{display:flex;align-items:center;gap:10px;position:relative;width:max-content;max-width:100%}.jlpt-section-menu-btn{width:38px;height:38px;border:1px solid rgba(255,255,255,.28);border-radius:11px;background:rgba(255,255,255,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;cursor:pointer;padding:0;box-shadow:none!important;transform:none!important}.jlpt-section-menu-btn span{display:block;width:18px;height:2px;border-radius:99px;background:#fff}.jlpt-section-menu{position:absolute;top:46px;left:0;z-index:1000;width:min(330px,86vw);background:#fff;border:1px solid #dbe5e8;border-radius:17px;padding:9px;box-shadow:0 20px 45px rgba(15,23,42,.22);display:none}.jlpt-section-menu.open{display:block}.jlpt-section-menu a{display:flex;align-items:center;gap:11px;padding:12px 13px;border-radius:12px;color:#1e293b!important;text-decoration:none!important;font-weight:800;font-size:14px}.jlpt-section-menu a:hover{background:#f0fdfa;color:#0f766e!important}.jlpt-section-menu a.current{background:#0f766e;color:#fff!important}.jlpt-section-menu .mi{width:28px;text-align:center;font-size:19px}@media(max-width:560px){.jlpt-section-menu{position:fixed;left:16px;right:16px;top:auto;bottom:18px;width:auto;max-height:70vh;overflow:auto}.jlpt-section-menu-btn{width:36px;height:36px}}</style><script id="jlpt-n5-section-menu">(function(){var b=document.querySelector('.badge');if(!b||document.getElementById('jlptN5SectionMenuBtn'))return;var r=document.createElement('div');r.className='jlpt-section-row';b.parentNode.insertBefore(r,b);r.appendChild(b);var x=document.createElement('button');x.type='button';x.id='jlptN5SectionMenuBtn';x.className='jlpt-section-menu-btn';x.setAttribute('aria-label','Mở menu JLPT N5');x.innerHTML='<span></span><span></span><span></span>';r.appendChild(x);var n=document.createElement('nav');n.className='jlpt-section-menu';n.innerHTML='<a href="/jlpt/n5/alphabet/"><span class="mi">🔤</span>Bảng chữ cái</a><a class="current" href="/jlpt/n5/vocabulary/"><span class="mi">🈶</span>Từ vựng</a><a href="/jlpt/n5/?section=kanji"><span class="mi">漢</span>Kanji</a><a href="/jlpt/n5/grammar/"><span class="mi">文</span>Ngữ pháp</a><a href="/jlpt/n5/?section=reading"><span class="mi">📖</span>Đọc hiểu</a><a href="/jlpt/n5/?section=listening"><span class="mi">🎧</span>Nghe hiểu</a><a href="/jlpt/n5/?section=mock"><span class="mi">🎯</span>Thi thử</a><a href="/jlpt/n5/"><span class="mi">↩️</span>Trang JLPT N5</a>';r.appendChild(n);function q(){n.classList.remove('open')}x.addEventListener('click',function(e){e.stopPropagation();n.classList.toggle('open')});document.addEventListener('click',function(e){if(!r.contains(e.target))q()});document.addEventListener('keydown',function(e){if(e.key==='Escape')q()})})();</script>'''
        additions=''
        if 'id="jlpt-vocab-capitalize-meaning"' not in html:additions+=capitalization_script
        if 'id="jlpt-vocab-direct-jump"' not in html:additions+=lesson_jump_script
        if 'id="jlpt-n5-section-menu"' not in html:additions+=section_menu_script
        if additions:html=html.replace('</body>',additions+'</body>') if '</body>' in html else html+additions
        response.content=html.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):response['Content-Length']=str(len(response.content))
        return response
