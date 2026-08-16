from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0021_premiumprofile_premiumrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Tiêu đề')),
                ('message', models.TextField(verbose_name='Nội dung')),
                ('action_url', models.CharField(blank=True, default='', help_text='Có thể nhập /tokutei1/exams/ hoặc một đường dẫn https://...', max_length=500, verbose_name='Đường dẫn xem thêm')),
                ('audience', models.CharField(choices=[('all', 'Tất cả thành viên'), ('premium', 'Chỉ thành viên Premium'), ('free', 'Chỉ thành viên Free')], default='all', max_length=20, verbose_name='Gửi đến')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Đã gửi lúc')),
                ('sent_count', models.PositiveIntegerField(default=0, verbose_name='Đã gửi')),
                ('failed_count', models.PositiveIntegerField(default=0, verbose_name='Gửi lỗi')),
            ],
            options={
                'verbose_name': 'Thông báo',
                'verbose_name_plural': 'Thông báo',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserNotificationPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_email', models.BooleanField(default=True, verbose_name='Nhận thông báo qua email')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notification_preference', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cài đặt email người dùng',
                'verbose_name_plural': 'Cài đặt email người dùng',
            },
        ),
    ]
