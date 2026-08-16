from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from study.models import PremiumProfile
from .models import SiteNotification, UserNotificationPreference


@admin.register(UserNotificationPreference)
class UserNotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'receive_email', 'updated_at')
    list_filter = ('receive_email',)
    search_fields = ('user__username', 'user__email')
    list_editable = ('receive_email',)


@admin.action(description='Gửi email thông báo đã chọn')
def send_notification_email(modeladmin, request, queryset):
    User = get_user_model()

    for notification in queryset:
        if notification.sent_at:
            modeladmin.message_user(
                request,
                f'“{notification.title}” đã được gửi trước đó. Hãy tạo thông báo mới nếu muốn gửi lại.',
                level=messages.WARNING,
            )
            continue

        users = User.objects.filter(is_active=True).exclude(email='')

        if notification.audience == 'premium':
            premium_user_ids = PremiumProfile.objects.filter(
                is_premium=True
            ).values_list('user_id', flat=True)
            users = users.filter(id__in=premium_user_ids)
        elif notification.audience == 'free':
            premium_user_ids = PremiumProfile.objects.filter(
                is_premium=True
            ).values_list('user_id', flat=True)
            users = users.exclude(id__in=premium_user_ids)

        opted_out_ids = UserNotificationPreference.objects.filter(
            receive_email=False
        ).values_list('user_id', flat=True)
        users = users.exclude(id__in=opted_out_ids)

        sent = 0
        failed = 0
        for user in users.iterator():
            action_text = ''
            if notification.action_url:
                url = notification.action_url.strip()
                if url.startswith('/'):
                    url = f'https://onthitokutei.com{url}'
                action_text = f'\n\nXem chi tiết: {url}'

            body = (
                f'Xin chào {user.username},\n\n'
                f'{notification.message}'
                f'{action_text}\n\n'
                '— Tokutei Study\n'
                'Bạn nhận email này vì tài khoản đang bật nhận thông báo.'
            )

            try:
                result = send_mail(
                    subject=f'[Tokutei Study] {notification.title}',
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                if result:
                    sent += 1
                else:
                    failed += 1
            except Exception:
                failed += 1

        notification.sent_at = timezone.now()
        notification.sent_count = sent
        notification.failed_count = failed
        notification.save(update_fields=['sent_at', 'sent_count', 'failed_count'])

        level = messages.SUCCESS if failed == 0 else messages.WARNING
        modeladmin.message_user(
            request,
            f'“{notification.title}”: đã gửi {sent} email, lỗi {failed}.',
            level=level,
        )


@admin.register(SiteNotification)
class SiteNotificationAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'audience', 'created_at', 'sent_at', 'sent_count', 'failed_count'
    )
    list_filter = ('audience', 'sent_at', 'created_at')
    search_fields = ('title', 'message')
    readonly_fields = ('created_at', 'sent_at', 'sent_count', 'failed_count')
    actions = (send_notification_email,)
    fieldsets = (
        ('Nội dung thông báo', {
            'fields': ('title', 'message', 'action_url', 'audience')
        }),
        ('Trạng thái gửi', {
            'fields': ('created_at', 'sent_at', 'sent_count', 'failed_count')
        }),
    )
