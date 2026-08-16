from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tiêu đề')),
                ('message', models.TextField(verbose_name='Nội dung')),
                ('link', models.URLField(blank=True, verbose_name='Đường dẫn')),
                ('audience', models.CharField(choices=[('all', 'Tất cả thành viên'), ('premium', 'Chỉ Premium'), ('free', 'Chỉ Free')], default='all', max_length=20, verbose_name='Người nhận')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Ngày gửi')),
                ('sent_count', models.PositiveIntegerField(default=0, verbose_name='Đã gửi')),
                ('failed_count', models.PositiveIntegerField(default=0, verbose_name='Gửi lỗi')),
            ],
            options={'verbose_name': 'Thông báo', 'verbose_name_plural': 'Thông báo', 'ordering': ['-created_at']},
        ),
    ]
