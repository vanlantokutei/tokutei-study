from django.db import models


class Notification(models.Model):
    AUDIENCE_CHOICES = [
        ('all', 'Tất cả thành viên'),
        ('premium', 'Chỉ Premium'),
        ('free', 'Chỉ Free'),
    ]

    title = models.CharField('Tiêu đề', max_length=200)
    message = models.TextField('Nội dung')
    link = models.URLField('Đường dẫn', blank=True)
    audience = models.CharField('Người nhận', max_length=20, choices=AUDIENCE_CHOICES, default='all')
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    sent_at = models.DateTimeField('Ngày gửi', blank=True, null=True)
    sent_count = models.PositiveIntegerField('Đã gửi', default=0)
    failed_count = models.PositiveIntegerField('Gửi lỗi', default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Thông báo'
        verbose_name_plural = 'Thông báo'

    def __str__(self):
        return self.title
