import re


class RemoveVocabularyFlagMiddleware:
    """Normalize Vietnamese labels in rendered JLPT N5 vocabulary HTML."""

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

        response.content = html.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))

        return response
