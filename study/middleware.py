class RemoveVocabularyFlagMiddleware:
    """Remove the Vietnam flag emoji from rendered JLPT vocabulary HTML."""

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

        if '🇻🇳' in html:
            html = html.replace('🇻🇳 ', '').replace('🇻🇳', '')
            response.content = html.encode(response.charset or 'utf-8')
            if response.has_header('Content-Length'):
                response['Content-Length'] = str(len(response.content))

        return response
