from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import PremiumRequestForm, RegistrationForm
from .models import (
    Exam, LearningCategory, Lesson, PremiumPlan, PremiumProfile, PremiumRequest,
    Question, ServiceSituation, VocabularyEntry,
)


def user_has_premium(user):
    if not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser:
        return True
    return PremiumProfile.objects.filter(user=user, is_premium=True).exists()


def home(request):
    return render(request, 'study/home.html', {'has_premium': user_has_premium(request.user)})


@login_required
def premium(request):
    profile, _ = PremiumProfile.objects.get_or_create(user=request.user)
    latest_request = PremiumRequest.objects.filter(user=request.user).first()
    plans = PremiumPlan.objects.filter(is_active=True)

    if request.method == 'POST' and not profile.is_premium:
        form = PremiumRequestForm(request.POST)
        if form.is_valid():
            premium_request = form.save(commit=False)
            premium_request.user = request.user
            premium_request.amount_vnd = premium_request.plan.sale_price_vnd
            premium_request.save()
            admin_url = request.build_absolute_uri(f'/admin/study/premiumrequest/{premium_request.id}/change/')
            send_mail(subject=f'[Tokutei Study] Yêu cầu Premium từ {request.user.username}', message=(f'Người dùng: {request.user.username}\n'f'Tên chuyển khoản: {premium_request.transfer_name}\n'f'Gói: {premium_request.plan.name}\n'f'Số tiền: {premium_request.amount_vnd:,}đ\n'f'Ngày chuyển: {premium_request.transfer_date}\n'f'Mã giao dịch: {premium_request.reference or "Không có"}\n\n'f'Mở yêu cầu để duyệt: {admin_url}'), from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.ADMIN_NOTIFICATION_EMAIL], fail_silently=True)
            return redirect('premium')
    else:
        form = PremiumRequestForm()
    return render(request, 'study/premium.html', {'form': form,'profile': profile,'latest_request': latest_request,'plans': plans,'bank_info': settings.PREMIUM_BANK_INFO})


def register(request):
    if request.user.is_authenticated: return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(); login(request, user); return redirect('home')
    else: form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def tokutei1(request): return render(request, 'study/tokutei1.html', {'has_premium': user_has_premium(request.user)})
def tokutei2(request): return render(request, 'study/tokutei2.html', {'has_premium': user_has_premium(request.user)})


def library(request):
    categories = LearningCategory.objects.prefetch_related('lessons').all(); completed_ids=set(request.session.get('completed_lesson_ids', [])); total_lessons=Lesson.objects.filter(is_published=True).count(); completed_count=Lesson.objects.filter(is_published=True,id__in=completed_ids).count(); progress_percent=round(completed_count/total_lessons*100) if total_lessons else 0; category_cards=[]
    for category in categories:
        lessons=[lesson for lesson in category.lessons.all() if lesson.is_published]; learned_count=sum(lesson.id in completed_ids for lesson in lessons); category_cards.append({'category':category,'lessons':lessons,'learned_count':learned_count,'total':len(lessons)})
    return render(request,'study/library.html',{'category_cards':category_cards,'completed_ids':completed_ids,'completed_count':completed_count,'total_lessons':total_lessons,'progress_percent':progress_percent})


def lesson_detail(request,category_slug,lesson_slug):
    lesson=get_object_or_404(Lesson.objects.select_related('category').prefetch_related('quick_questions'),category__slug=category_slug,slug=lesson_slug,is_published=True); completed_ids=request.session.get('completed_lesson_ids',[]); return render(request,'study/lesson_detail.html',{'lesson':lesson,'is_completed':lesson.id in completed_ids})

@require_POST
def toggle_lesson_progress(request,lesson_id):
    lesson=get_object_or_404(Lesson,id=lesson_id,is_published=True); completed_ids=set(request.session.get('completed_lesson_ids',[])); completed=lesson.id not in completed_ids
    if completed: completed_ids.add(lesson.id)
    else: completed_ids.remove(lesson.id)
    request.session['completed_lesson_ids']=sorted(completed_ids); request.session.modified=True
    if request.headers.get('x-requested-with')=='XMLHttpRequest': return JsonResponse({'completed':completed})
    return redirect('lesson_detail',category_slug=lesson.category.slug,lesson_slug=lesson.slug)


def vocabulary(request):
    selected_category=request.GET.get('category',''); selected_topic=request.GET.get('topic',''); search_text=request.GET.get('q','').strip(); entries=VocabularyEntry.objects.filter(is_published=True); valid_categories=dict(VocabularyEntry.CATEGORY_CHOICES)
    if selected_category in valid_categories: entries=entries.filter(category=selected_category)
    else: selected_category=''
    valid_topics=dict(VocabularyEntry.TOPIC_CHOICES)
    if selected_topic in valid_topics: entries=entries.filter(topic=selected_topic)
    else: selected_topic=''
    if search_text: entries=entries.filter(Q(word_jp__icontains=search_text)|Q(furigana__icontains=search_text)|Q(meaning_vi__icontains=search_text))
    learned_ids=set(request.session.get('learned_vocabulary_ids',[])); total_words=VocabularyEntry.objects.filter(is_published=True).count(); learned_count=VocabularyEntry.objects.filter(is_published=True,id__in=learned_ids).count(); progress_percent=round(learned_count/total_words*100) if total_words else 0
    return render(request,'study/vocabulary.html',{'entries':entries,'categories':VocabularyEntry.CATEGORY_CHOICES,'topics':VocabularyEntry.TOPIC_CHOICES,'selected_category':selected_category,'selected_topic':selected_topic,'search_text':search_text,'learned_ids':learned_ids,'learned_count':learned_count,'total_words':total_words,'progress_percent':progress_percent})

@require_POST
def toggle_vocabulary_progress(request,entry_id):
    entry=get_object_or_404(VocabularyEntry,id=entry_id,is_published=True); learned_ids=set(request.session.get('learned_vocabulary_ids',[]))
    if entry.id in learned_ids: learned_ids.remove(entry.id)
    else: learned_ids.add(entry.id)
    request.session['learned_vocabulary_ids']=sorted(learned_ids); request.session.modified=True; next_url=request.POST.get('next',''); return redirect(next_url if next_url.startswith('/') else 'vocabulary')


def service_situations(request):
    selected_category=request.GET.get('category',''); search_text=request.GET.get('q','').strip(); situations=ServiceSituation.objects.filter(is_published=True); valid_categories=dict(ServiceSituation.CATEGORY_CHOICES)
    if selected_category in valid_categories: situations=situations.filter(category=selected_category)
    else: selected_category=''
    if search_text: situations=situations.filter(Q(title_jp__icontains=search_text)|Q(title_vi__icontains=search_text)|Q(situation_vi__icontains=search_text)|Q(customer_phrase_jp__icontains=search_text))
    completed_ids=set(request.session.get('completed_situation_ids',[])); total=ServiceSituation.objects.filter(is_published=True).count(); completed_count=ServiceSituation.objects.filter(is_published=True,id__in=completed_ids).count(); progress_percent=round(completed_count/total*100) if total else 0
    return render(request,'study/service_situations.html',{'situations':situations,'categories':ServiceSituation.CATEGORY_CHOICES,'selected_category':selected_category,'search_text':search_text,'completed_ids':completed_ids,'completed_count':completed_count,'total':total,'progress_percent':progress_percent})

@require_POST
def toggle_situation_progress(request,situation_id):
    situation=get_object_or_404(ServiceSituation,id=situation_id,is_published=True); completed_ids=set(request.session.get('completed_situation_ids',[]))
    if situation.id in completed_ids: completed_ids.remove(situation.id)
    else: completed_ids.add(situation.id)
    request.session['completed_situation_ids']=sorted(completed_ids); request.session.modified=True; next_url=request.POST.get('next',''); return redirect(next_url if next_url.startswith('/') else 'service_situations')


def practice1(request):
    question_id=request.GET.get('id'); questions=Question.objects.filter(level='1').order_by('id'); question=questions.filter(id=question_id).first() if question_id else questions.first(); next_question=None
    if question: next_question=questions.filter(id__gt=question.id).first() or questions.first()
    return render(request,'study/practice1.html',{'question':question,'next_question':next_question})


def exam_list(request):
    exams=Exam.objects.filter(level='1').order_by('order'); return render(request,'study/exam_list.html',{'exams':exams,'has_premium':user_has_premium(request.user)})


def _create_exam_attempt(request,exam):
    import random,time
    from .models import ExamQuestion
    items=list(ExamQuestion.objects.filter(exam=exam).select_related('question').order_by('order')); random.shuffle(items); order_ids=[x.id for x in items]; option_maps={}
    for item in items:
        letters=['A','B','C']; random.shuffle(letters); option_maps[str(item.id)]=letters
    request.session[f'exam_{exam.id}_order']=order_ids; request.session[f'exam_{exam.id}_option_maps']=option_maps; request.session[f'exam_{exam.id}_answers']={}; request.session[f'exam_{exam.id}_start']=int(time.time()); request.session.modified=True


def take_exam(request,exam_id,question_number=1):
    import time
    from .models import ExamQuestion
    exam=get_object_or_404(Exam,id=exam_id)
    if not exam.is_free and not user_has_premium(request.user): return redirect('premium')
    order_key=f'exam_{exam.id}_order'; option_key=f'exam_{exam.id}_option_maps'; answer_key=f'exam_{exam.id}_answers'; start_key=f'exam_{exam.id}_start'
    if order_key not in request.session: _create_exam_attempt(request,exam)
    order_ids=request.session.get(order_key,[]); option_maps=request.session.get(option_key,{}); answers=request.session.get(answer_key,{}); total=len(order_ids)
    if question_number<1 or question_number>total: return redirect('exam_result',exam_id=exam.id)
    current_id=order_ids[question_number-1]; current=get_object_or_404(ExamQuestion,id=current_id,exam=exam)
    if request.method=='POST':
        answer=request.POST.get('answer')
        if answer in ['A','B','C']: answers[str(current.id)]=answer; request.session[answer_key]=answers; request.session.modified=True
        if question_number<total: return redirect('take_exam_question',exam_id=exam.id,question_number=question_number+1)
        return redirect('exam_result',exam_id=exam.id)
    if start_key not in request.session: request.session[start_key]=int(time.time())
    remaining_seconds=max(0,exam.time_limit*60-(int(time.time())-request.session[start_key]))
    if remaining_seconds<=0:return redirect('exam_result',exam_id=exam.id)
    q=current.question; option_data={'A':{'ruby':q.option_a_ruby,'vi':q.option_a_vi},'B':{'ruby':q.option_b_ruby,'vi':q.option_b_vi},'C':{'ruby':q.option_c_ruby,'vi':q.option_c_vi}}; shuffled=option_maps.get(str(current.id),['A','B','C']); display_options=[]
    for index,original_letter in enumerate(shuffled): display_options.append({'label':['A','B','C'][index],'value':original_letter,'ruby':option_data[original_letter]['ruby'],'vi':option_data[original_letter]['vi']})
    question_nav=[{'number':position,'answered':str(item_id) in answers,'current':position==question_number} for position,item_id in enumerate(order_ids,start=1)]
    return render(request,'study/take_exam.html',{'exam':exam,'question':q,'question_number':question_number,'total':total,'remaining_seconds':remaining_seconds,'display_options':display_options,'question_nav':question_nav})


def start_exam(request,exam_id):
    exam=get_object_or_404(Exam,id=exam_id)
    if not exam.is_free and not user_has_premium(request.user):return redirect('premium')
    _create_exam_attempt(request,exam); return redirect('take_exam',exam_id=exam.id)


def exam_intro(request,exam_id):
    from .models import ExamQuestion
    exam=get_object_or_404(Exam,id=exam_id)
    if not exam.is_free and not user_has_premium(request.user):return redirect('premium')
    total=ExamQuestion.objects.filter(exam=exam).count(); return render(request,'study/exam_intro.html',{'exam':exam,'total':total})


def exam_result(request,exam_id):
    from .models import ExamQuestion
    exam=get_object_or_404(Exam,id=exam_id); order_ids=request.session.get(f'exam_{exam.id}_order',[]); answers=request.session.get(f'exam_{exam.id}_answers',{}); option_maps=request.session.get(f'exam_{exam.id}_option_maps',{}); correct=0; wrong=[]
    for item_id in order_ids:
        item=ExamQuestion.objects.select_related('question').get(id=item_id); selected=answers.get(str(item_id)); q=item.question
        if selected==q.correct_answer: correct+=1
        else: wrong.append({'item':item,'selected':selected,'option_map':option_maps.get(str(item_id),['A','B','C'])})
    total=len(order_ids); score=round(correct/total*100) if total else 0; request.session[f'exam_{exam.id}_wrong_ids']=[x['item'].id for x in wrong]
    return render(request,'study/exam_result.html',{'exam':exam,'correct':correct,'total':total,'score':score,'wrong_count':len(wrong)})


def wrong_answers(request,exam_id):
    from .models import ExamQuestion
    exam=get_object_or_404(Exam,id=exam_id); ids=request.session.get(f'exam_{exam.id}_wrong_ids',[]); items=list(ExamQuestion.objects.filter(id__in=ids).select_related('question')); return render(request,'study/wrong_answers.html',{'exam':exam,'items':items})


def retry_wrong(request,exam_id,index):
    from .models import ExamQuestion
    exam=get_object_or_404(Exam,id=exam_id); ids=request.session.get(f'exam_{exam.id}_wrong_ids',[])
    if not ids:return redirect('exam_list')
    index=max(0,min(index,len(ids)-1)); item=get_object_or_404(ExamQuestion,id=ids[index]); q=item.question; feedback=None
    if request.method=='POST': feedback=request.POST.get('answer')==q.correct_answer
    return render(request,'study/retry_wrong.html',{'exam':exam,'question':q,'index':index,'total':len(ids),'feedback':feedback})
