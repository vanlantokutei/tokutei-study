from django.conf import settings
from django.db import models


class UserNotificationPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notification_preference',
    )
    receive_email = models.BooleanField(
        default=True,
        verbose_name='Nhận thông báo qua email',
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cài đặt email người dùng'
        verbose_name_plural = 'Cài đặt email người dùng'

    def __str__(self):
        return f'{self.user.username} - {"Nhận email" if self.receive_email else "Tắt email"}'


class SiteNotification(models.Model):
    AUDIENCE_CHOICES = [
        ('all', 'Tất cả thành viên'),
        ('premium', 'Chỉ thành viên Premium'),
        ('free', 'Chỉ thành viên Free'),
    ]

    title = models.CharField(max_length=180, verbose_name='Tiêu đề')
    message = models.TextField(verbose_name='Nội dung')
    action_url = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='Đường dẫn xem thêm',
        help_text='Có thể nhập /tokutei1/exams/ hoặc một đường dẫn https://...',
    )
    audience = models.CharField(
        max_length=20,
        choices=AUDIENCE_CHOICES,
        default='all',
        verbose_name='Gửi đến',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name='Đã gửi lúc')
    sent_count = models.PositiveIntegerField(default=0, verbose_name='Đã gửi')
    failed_count = models.PositiveIntegerField(default=0, verbose_name='Gửi lỗi')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Thông báo'
        verbose_name_plural = 'Thông báo'

    def __str__(self):
        return self.title
