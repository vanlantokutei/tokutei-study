from django.contrib import admin
from .models import (
    LearningCategory, Lesson, QuickQuestion, Question,
    ServiceSituation, VocabularyEntry,
)

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
