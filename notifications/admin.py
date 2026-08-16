from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'created_at', 'sent_at', 'sent_count', 'failed_count')
    list_filter = ('audience', 'sent_at')
    search_fields = ('title', 'message')
    actions = ['send_selected_notifications']

    @admin.action(description='Gửi email thông báo đã chọn')
    def send_selected_notifications(self, request, queryset):
        User = get_user_model()
        for notification in queryset:
            users = User.objects.filter(is_active=True).exclude(email='')
            if notification.audience == 'premium':
                users = users.filter(profile__premium_until__gt=timezone.now())
            elif notification.audience == 'free':
                users = users.exclude(profile__premium_until__gt=timezone.now())

            sent = 0
            failed = 0
            for user in users.iterator():
                try:
                    body = notification.message
                    if notification.link:
                        body += f'\n\nXem chi tiết: {notification.link}'
                    send_mail(
                        notification.title,
                        body,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
                    sent += 1
                except Exception:
                    failed += 1

            notification.sent_at = timezone.now()
            notification.sent_count = sent
            notification.failed_count = failed
            notification.save(update_fields=['sent_at', 'sent_count', 'failed_count'])

        self.message_user(request, 'Đã xử lý gửi thông báo.', level=messages.SUCCESS)
