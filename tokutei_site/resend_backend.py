import logging

import resend
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

logger = logging.getLogger(__name__)


class ResendEmailBackend(BaseEmailBackend):
    """Django email backend that sends messages through the Resend HTTPS API."""

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        api_key = getattr(settings, 'RESEND_API_KEY', '')
        if not api_key:
            logger.error('RESEND_API_KEY is not configured')
            return 0

        resend.api_key = api_key
        sent_count = 0

        for message in email_messages:
            try:
                from_email = getattr(
                    settings,
                    'RESEND_FROM_EMAIL',
                    'Ôn Thi Tokutei <noreply@onthitokutei.com>',
                )
                params = {
                    'from': from_email,
                    'to': list(message.to),
                    'subject': message.subject,
                    'text': message.body,
                }

                html_body = None
                for alternative in getattr(message, 'alternatives', []):
                    content = getattr(alternative, 'content', None)
                    mimetype = getattr(alternative, 'mimetype', None)
                    if content is None and isinstance(alternative, (tuple, list)) and len(alternative) >= 2:
                        content, mimetype = alternative[0], alternative[1]
                    if mimetype == 'text/html':
                        html_body = content
                        break
                if html_body:
                    params['html'] = html_body

                if message.cc:
                    params['cc'] = list(message.cc)
                if message.bcc:
                    params['bcc'] = list(message.bcc)
                if message.reply_to:
                    params['reply_to'] = list(message.reply_to)

                resend.Emails.send(params)
                sent_count += 1
            except Exception as exc:
                logger.exception('Resend email failed: %s', exc)
                if not self.fail_silently:
                    raise

        return sent_count
