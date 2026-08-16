import logging
import os
from html import escape

import resend
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Notification

logger = logging.getLogger(__name__)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'created_at', 'sent_at', 'sent_count', 'failed_count')
    list_filter = ('audience', 'sent_at')
    search_fields = ('title', 'message')
    actions = ['send_selected_notifications']

    @admin.action(description='Gửi email thông báo đã chọn')
    def send_selected_notifications(self, request, queryset):
        api_key = os.getenv('RESEND_API_KEY', '').strip()
        from_email = os.getenv('RESEND_FROM_EMAIL', 'Tokutei Study <onboarding@resend.dev>').strip()

        if not api_key:
            self.message_user(
                request,
                'Thiếu RESEND_API_KEY trong Render Environment.',
                level=messages.ERROR,
            )
            return

        resend.api_key = api_key
        User = get_user_model()

        total_sent = 0
        total_failed = 0

        for notification in queryset:
            users = User.objects.filter(is_active=True).exclude(email='')

            # Chỉ gửi cho người dùng chưa tắt nhận email.
            users = users.exclude(notification_preference__receive_email=False)

            if notification.audience == 'premium':
                users = users.filter(premium_profile__is_premium=True)
            elif notification.audience == 'free':
                users = users.exclude(premium_profile__is_premium=True)

            sent = 0
            failed = 0

            for user in users.iterator():
                try:
                    message_html = '<p>' + escape(notification.message).replace('\n', '<br>') + '</p>'
                    if notification.link:
                        safe_link = escape(notification.link, quote=True)
                        message_html += f'<p><a href="{safe_link}">Xem chi tiết</a></p>'

                    resend.Emails.send({
                        'from': from_email,
                        'to': [user.email],
                        'subject': notification.title,
                        'html': message_html,
                    })
                    sent += 1
                    total_sent += 1
                    logger.info(
                        'Resend notification sent: notification_id=%s user_id=%s email=%s',
                        notification.id,
                        user.id,
                        user.email,
                    )
                except Exception as exc:
                    failed += 1
                    total_failed += 1
                    logger.exception(
                        'Resend notification failed: notification_id=%s user_id=%s email=%s error=%s',
                        notification.id,
                        user.id,
                        user.email,
                        exc,
                    )

            notification.sent_at = timezone.now()
            notification.sent_count = sent
            notification.failed_count = failed
            notification.save(update_fields=['sent_at', 'sent_count', 'failed_count'])

        level = messages.SUCCESS if total_failed == 0 else messages.WARNING
        self.message_user(
            request,
            f'Đã xử lý gửi qua Resend. Thành công: {total_sent} | Lỗi: {total_failed}',
            level=level,
        )
