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

        # Convert old flag-based labels to explicit Vietnamese labels.
        html = html.replace('<div class="meaning">🇻🇳 ', '<div class="meaning"><span class="vn-label">Nghĩa tiếng Việt:</span> ')
        html = html.replace('<div class="vi">🇻🇳 ', '<div class="vi"><span class="vn-label">Dịch tiếng Việt:</span> ')
        html = html.replace('🇻🇳 ', '').replace('🇻🇳', '')

        # Capitalize only the first character of each Vietnamese vocabulary meaning.
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

        # Allow learners to jump directly to any vocabulary lesson that already exists.
        # Lesson 1 uses the base vocabulary URL; lessons 2-9 have their own routes.
        lesson_jump_script = r'''
<script id="jlpt-vocab-direct-jump">
(function () {
  var grid = document.getElementById('lessonGrid');
  if (!grid) return;

  var match = location.pathname.match(/\/lesson-(\d+)\/?$/);
  var currentLesson = match ? parseInt(match[1], 10) : 1;
  var maxAvailableLesson = 9;

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

        if 'id="jlpt-vocab-direct-jump"' not in html:
            if '</body>' in html:
                html = html.replace('</body>', lesson_jump_script + '</body>')
            else:
                html += lesson_jump_script

        response.content = html.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))

        return response
