from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('premium/', views.premium, name='premium'),
    path('jlpt/n5/alphabet/', TemplateView.as_view(template_name='study/jlpt_n5_alphabet.html'), name='jlpt_n5_alphabet'),
    path('jlpt/n5/vocabulary/', TemplateView.as_view(template_name='study/jlpt_n5_vocabulary.html'), name='jlpt_n5_vocabulary'),
    path('jlpt/n5/vocabulary/lesson-2/', TemplateView.as_view(template_name='study/jlpt_n5_vocabulary_lesson2.html'), name='jlpt_n5_vocabulary_lesson2'),
    path('jlpt/n5/grammar/', TemplateView.as_view(template_name='study/jlpt_n5_grammar.html'), name='jlpt_n5_grammar'),
    path('jlpt/n5/grammar/lesson-1/', TemplateView.as_view(template_name='study/jlpt_n5_grammar_lesson1.html'), name='jlpt_n5_grammar_lesson1'),
    path('jlpt/<str:level>/', TemplateView.as_view(template_name='study/jlpt_level.html'), name='jlpt_level'),
    path('tokutei1/exam/<int:exam_id>/retry-wrong/<int:index>/', views.retry_wrong, name='retry_wrong'),
    path('tokutei1/exam/<int:exam_id>/intro/', views.exam_intro, name='exam_intro'),
    path('', views.home, name='home'),
    path('tinh-huong/', views.service_situations, name='service_situations_short'),
    path('tokutei1/situations/', views.service_situations, name='service_situations'),
    path('tokutei1/situations/progress/<int:situation_id>/', views.toggle_situation_progress, name='toggle_situation_progress'),
    path('tokutei1/vocabulary/', views.vocabulary, name='vocabulary'),
    path('tokutei1/vocabulary/progress/<int:entry_id>/', views.toggle_vocabulary_progress, name='toggle_vocabulary_progress'),
    path('tokutei1/library/', views.library, name='library'),
    path('tokutei1/library/progress/<int:lesson_id>/', views.toggle_lesson_progress, name='toggle_lesson_progress'),
    path('tokutei1/library/<slug:category_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
    path('tokutei1/', views.tokutei1, name='tokutei1'),
    path('tokutei2/', views.tokutei2, name='tokutei2'),
    path('tokutei1/practice/', views.practice1, name='practice1'),
    path('tokutei1/exams/', views.exam_list, name='exam_list'),
    path('tokutei1/exam/<int:exam_id>/', views.take_exam, name='take_exam'),
    path('tokutei1/exam/<int:exam_id>/<int:question_number>/', views.take_exam, name='take_exam_question'),
    path('tokutei1/exam/<int:exam_id>/result/', views.exam_result, name='exam_result'),
    path('tokutei1/exam/<int:exam_id>/start/', views.start_exam, name='start_exam'),
    path('tokutei1/exam/<int:exam_id>/wrong/', views.wrong_answers, name='wrong_answers'),
]
