from datetime import timedelta

from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from .models import (
    Exam, LearningCategory, Lesson, PremiumPlan, PremiumProfile, PremiumRequest,
    QuickQuestion, Question, ServiceSituation, VocabularyEntry,
)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'is_free', 'order', 'time_limit')
    list_filter = ('level', 'is_free')
    list_editable = ('is_free', 'order')


@admin.register(PremiumProfile)
class PremiumProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium', 'activated_at', 'expires_at')
    list_filter = ('is_premium',)
    search_fields = ('user__username', 'user__email')


@admin.register(PremiumPlan)
class PremiumPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price_vnd', 'sale_price_vnd', 'discount_percent', 'is_featured', 'is_active', 'order')
    list_editable = ('sale_price_vnd', 'is_featured', 'is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.action(description='Duyệt Premium cho yêu cầu đã chọn')
def approve_premium(modeladmin, request, queryset):
    approved = 0
    for item in queryset.select_related('user'):
        profile, _ = PremiumProfile.objects.get_or_create(user=item.user)
        profile.is_premium = True
        profile.activated_at = timezone.now()
        profile.expires_at = (
            timezone.now() + timedelta(days=item.plan.duration_days)
            if item.plan.duration_days else None
        )
        profile.save(update_fields=['is_premium', 'activated_at', 'expires_at'])
        item.status = 'approved'
        item.reviewed_by = request.user
        item.reviewed_at = timezone.now()
        item.save(update_fields=['status', 'reviewed_by', 'reviewed_at', 'updated_at'])
        if item.user.email:
            send_mail(
                '[Tokutei Study] Premium đã được duyệt',
                'Tài khoản của bạn đã được nâng cấp Premium. Bạn có thể mở các bộ đề Premium ngay bây giờ.',
                settings.DEFAULT_FROM_EMAIL,
                [item.user.email],
                fail_silently=True,
            )
        approved += 1
    modeladmin.message_user(request, f'Đã duyệt {approved} tài khoản Premium.')


@admin.action(description='Từ chối yêu cầu đã chọn')
def reject_premium(modeladmin, request, queryset):
    updated = queryset.update(
        status='rejected',
        reviewed_by=request.user,
        reviewed_at=timezone.now(),
    )
    modeladmin.message_user(request, f'Đã từ chối {updated} yêu cầu.')


@admin.register(PremiumRequest)
class PremiumRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'transfer_name', 'amount_vnd', 'transfer_date', 'status', 'created_at')
    list_filter = ('status', 'plan', 'transfer_date', 'created_at')
    search_fields = ('user__username', 'user__email', 'transfer_name', 'reference')
    readonly_fields = ('created_at', 'updated_at', 'reviewed_at', 'reviewed_by')
    actions = (approve_premium, reject_premium)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'category', 'question_jp', 'correct_answer')
    list_filter = ('level', 'category')
    search_fields = ('question_jp', 'question_vi')


@admin.register(LearningCategory)
class LearningCategoryAdmin(admin.ModelAdmin):
    list_display = ('title_jp', 'title_vi', 'order', 'slug')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title_vi',)}


class QuickQuestionInline(admin.StackedInline):
    model = QuickQuestion
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title_vi', 'category', 'order', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title_jp', 'title_vi', 'content_jp', 'content_vi')
    prepopulated_fields = {'slug': ('title_vi',)}
    inlines = (QuickQuestionInline,)


@admin.register(VocabularyEntry)
class VocabularyEntryAdmin(admin.ModelAdmin):
    list_display = ('word_jp', 'furigana', 'meaning_vi', 'category', 'topic', 'is_published')
    list_filter = ('category', 'topic', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('word_jp', 'furigana', 'meaning_vi', 'example_jp', 'example_vi')


@admin.register(ServiceSituation)
class ServiceSituationAdmin(admin.ModelAdmin):
    list_display = ('title_vi', 'title_jp', 'category', 'order', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title_jp', 'title_vi', 'situation_jp', 'situation_vi', 'response_jp')
    prepopulated_fields = {'slug': ('title_vi',)}
