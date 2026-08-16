from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Exam, LearningCategory, Lesson, Question, ServiceSituation, VocabularyEntry


def home(request):
    return render(request, 'study/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def tokutei1(request):
    return render(request, 'study/tokutei1.html')


def library(request):
    categories = LearningCategory.objects.prefetch_related('lessons').all()
    completed_ids = set(request.session.get('completed_lesson_ids', []))
    total_lessons = Lesson.objects.filter(is_published=True).count()
    completed_count = Lesson.objects.filter(
        is_published=True,
        id__in=completed_ids,
    ).count()
    progress_percent = round(completed_count / total_lessons * 100) if total_lessons else 0

    category_cards = []
    for category in categories:
        lessons = [lesson for lesson in category.lessons.all() if lesson.is_published]
        learned_count = sum(lesson.id in completed_ids for lesson in lessons)
        category_cards.append({
            'category': category,
            'lessons': lessons,
            'learned_count': learned_count,
            'total': len(lessons),
        })

    return render(request, 'study/library.html', {
        'category_cards': category_cards,
        'completed_ids': completed_ids,
        'completed_count': completed_count,
        'total_lessons': total_lessons,
        'progress_percent': progress_percent,
    })


def lesson_detail(request, category_slug, lesson_slug):
    lesson = get_object_or_404(
        Lesson.objects.select_related('category').prefetch_related('quick_questions'),
        category__slug=category_slug,
        slug=lesson_slug,
        is_published=True,
    )
    completed_ids = request.session.get('completed_lesson_ids', [])
    return render(request, 'study/lesson_detail.html', {
        'lesson': lesson,
        'is_completed': lesson.id in completed_ids,
    })


@require_POST
def toggle_lesson_progress(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, is_published=True)
    completed_ids = set(request.session.get('completed_lesson_ids', []))
    if lesson.id in completed_ids:
        completed_ids.remove(lesson.id)
        completed = False
    else:
        completed_ids.add(lesson.id)
        completed = True
    request.session['completed_lesson_ids'] = sorted(completed_ids)
    request.session.modified = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'completed': completed})
    return redirect('lesson_detail', category_slug=lesson.category.slug, lesson_slug=lesson.slug)


def vocabulary(request):
    selected_category = request.GET.get('category', '')
    selected_topic = request.GET.get('topic', '')
    search_text = request.GET.get('q', '').strip()
    entries = VocabularyEntry.objects.filter(is_published=True)

    valid_categories = dict(VocabularyEntry.CATEGORY_CHOICES)
    if selected_category in valid_categories:
        entries = entries.filter(category=selected_category)
    else:
        selected_category = ''

    valid_topics = dict(VocabularyEntry.TOPIC_CHOICES)
    if selected_topic in valid_topics:
        entries = entries.filter(topic=selected_topic)
    else:
        selected_topic = ''

    if search_text:
        entries = entries.filter(
            Q(word_jp__icontains=search_text)
            | Q(furigana__icontains=search_text)
            | Q(meaning_vi__icontains=search_text)
        )

    learned_ids = set(request.session.get('learned_vocabulary_ids', []))
    total_words = VocabularyEntry.objects.filter(is_published=True).count()
    learned_count = VocabularyEntry.objects.filter(
        is_published=True, id__in=learned_ids
    ).count()
    progress_percent = round(learned_count / total_words * 100) if total_words else 0

    return render(request, 'study/vocabulary.html', {
        'entries': entries,
        'categories': VocabularyEntry.CATEGORY_CHOICES,
        'topics': VocabularyEntry.TOPIC_CHOICES,
        'selected_category': selected_category,
        'selected_topic': selected_topic,
        'search_text': search_text,
        'learned_ids': learned_ids,
        'learned_count': learned_count,
        'total_words': total_words,
        'progress_percent': progress_percent,
    })


@require_POST
def toggle_vocabulary_progress(request, entry_id):
    entry = get_object_or_404(VocabularyEntry, id=entry_id, is_published=True)
    learned_ids = set(request.session.get('learned_vocabulary_ids', []))
    if entry.id in learned_ids:
        learned_ids.remove(entry.id)
    else:
        learned_ids.add(entry.id)
    request.session['learned_vocabulary_ids'] = sorted(learned_ids)
    request.session.modified = True

    next_url = request.POST.get('next', '')
    if next_url.startswith('/'):
        return redirect(next_url)
    return redirect('vocabulary')


def service_situations(request):
    selected_category = request.GET.get('category', '')
    search_text = request.GET.get('q', '').strip()
    situations = ServiceSituation.objects.filter(is_published=True)
    valid_categories = dict(ServiceSituation.CATEGORY_CHOICES)

    if selected_category in valid_categories:
        situations = situations.filter(category=selected_category)
    else:
        selected_category = ''
    if search_text:
        situations = situations.filter(
            Q(title_jp__icontains=search_text)
            | Q(title_vi__icontains=search_text)
            | Q(situation_vi__icontains=search_text)
            | Q(customer_phrase_jp__icontains=search_text)
        )

    completed_ids = set(request.session.get('completed_situation_ids', []))
    total = ServiceSituation.objects.filter(is_published=True).count()
    completed_count = ServiceSituation.objects.filter(
        is_published=True, id__in=completed_ids
    ).count()
    progress_percent = round(completed_count / total * 100) if total else 0

    return render(request, 'study/service_situations.html', {
        'situations': situations,
        'categories': ServiceSituation.CATEGORY_CHOICES,
        'selected_category': selected_category,
        'search_text': search_text,
        'completed_ids': completed_ids,
        'completed_count': completed_count,
        'total': total,
        'progress_percent': progress_percent,
    })


@require_POST
def toggle_situation_progress(request, situation_id):
    situation = get_object_or_404(ServiceSituation, id=situation_id, is_published=True)
    completed_ids = set(request.session.get('completed_situation_ids', []))
    if situation.id in completed_ids:
        completed_ids.remove(situation.id)
    else:
        completed_ids.add(situation.id)
    request.session['completed_situation_ids'] = sorted(completed_ids)
    request.session.modified = True
    next_url = request.POST.get('next', '')
    return redirect(next_url if next_url.startswith('/') else 'service_situations')


def practice1(request):
    question_id = request.GET.get('id')

    questions = Question.objects.filter(level='1').order_by('id')

    if question_id:
        question = questions.filter(id=question_id).first()
    else:
        question = questions.first()

    next_question = None

    if question:
        next_question = questions.filter(id__gt=question.id).first()

        if not next_question:
            next_question = questions.first()

    return render(
        request,
        'study/practice1.html',
        {
            'question': question,
            'next_question': next_question,
        }
    )


def exam_list(request):
    exams = Exam.objects.filter(
        level='1'
    ).order_by('order')

    return render(
        request,
        'study/exam_list.html',
        {'exams': exams}
    )


def _create_exam_attempt(request, exam):
    import random
    import time
    from .models import ExamQuestion

    items = list(
        ExamQuestion.objects
        .filter(exam=exam)
        .select_related("question")
        .order_by("order")
    )

    random.shuffle(items)

    order_ids = [x.id for x in items]

    option_maps = {}

    for item in items:
        letters = ["A", "B", "C"]
        random.shuffle(letters)
        option_maps[str(item.id)] = letters

    request.session[f"exam_{exam.id}_order"] = order_ids
    request.session[f"exam_{exam.id}_option_maps"] = option_maps
    request.session[f"exam_{exam.id}_answers"] = {}
    request.session[f"exam_{exam.id}_start"] = int(time.time())
    request.session.modified = True


def take_exam(request, exam_id, question_number=1):
    import time

    from django.shortcuts import get_object_or_404, redirect
    from .models import ExamQuestion

    exam = get_object_or_404(Exam, id=exam_id)

    order_key = f"exam_{exam.id}_order"
    option_key = f"exam_{exam.id}_option_maps"
    answer_key = f"exam_{exam.id}_answers"
    start_key = f"exam_{exam.id}_start"

    # Nếu vào trực tiếp mà chưa có lượt thi thì tự tạo
    if order_key not in request.session:
        _create_exam_attempt(request, exam)

    order_ids = request.session.get(order_key, [])
    option_maps = request.session.get(option_key, {})
    answers = request.session.get(answer_key, {})

    total = len(order_ids)

    if question_number < 1 or question_number > total:
        return redirect("exam_result", exam_id=exam.id)

    current_id = order_ids[question_number - 1]

    current = get_object_or_404(
        ExamQuestion,
        id=current_id,
        exam=exam
    )

    # Lưu đáp án
    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer in ["A", "B", "C"]:
            answers[str(current.id)] = answer
            request.session[answer_key] = answers
            request.session.modified = True

        if question_number < total:
            return redirect(
                "take_exam_question",
                exam_id=exam.id,
                question_number=question_number + 1
            )

        return redirect(
            "exam_result",
            exam_id=exam.id
        )

    # Timer
    if start_key not in request.session:
        request.session[start_key] = int(time.time())

    elapsed = int(time.time()) - request.session[start_key]
    limit = exam.time_limit * 60
    remaining_seconds = max(0, limit - elapsed)

    if remaining_seconds <= 0:
        return redirect(
            "exam_result",
            exam_id=exam.id
        )

    q = current.question

    option_data = {
        "A": {
            "ruby": q.option_a_ruby,
            "vi": q.option_a_vi,
        },
        "B": {
            "ruby": q.option_b_ruby,
            "vi": q.option_b_vi,
        },
        "C": {
            "ruby": q.option_c_ruby,
            "vi": q.option_c_vi,
        },
    }

    shuffled = option_maps.get(
        str(current.id),
        ["A", "B", "C"]
    )

    display_options = []

    for index, original_letter in enumerate(shuffled):
        display_options.append({
            # Chữ người thi nhìn thấy
            "label": ["A", "B", "C"][index],

            # Giá trị thật dùng để chấm điểm
            "value": original_letter,

            "ruby": option_data[original_letter]["ruby"],
            "vi": option_data[original_letter]["vi"],
        })

    question_nav = []

    for position, item_id in enumerate(order_ids, start=1):
        question_nav.append({
            "number": position,
            "answered": str(item_id) in answers,
            "current": position == question_number,
        })

    return render(
        request,
        "study/take_exam.html",
        {
            "exam": exam,
            "question": q,
            "question_number": question_number,
            "total": total,
            "remaining_seconds": remaining_seconds,
            "display_options": display_options,
            "question_nav": question_nav,
        }
    )


def start_exam(request, exam_id):
    from django.shortcuts import get_object_or_404, redirect

    exam = get_object_or_404(Exam, id=exam_id)

    # Mỗi lần bấm bắt đầu/làm lại:
    # xáo câu và xáo A/B/C hoàn toàn mới
    _create_exam_attempt(request, exam)

    return redirect(
        "take_exam",
        exam_id=exam.id
    )


def exam_intro(request, exam_id):
    from django.shortcuts import get_object_or_404
    from .models import ExamQuestion

    exam = get_object_or_404(Exam, id=exam_id)

    total = ExamQuestion.objects.filter(exam=exam).count()

    theory_count = ExamQuestion.objects.filter(
        exam=exam,
        question__section='theory'
    ).count()

    practical_count = ExamQuestion.objects.filter(
        exam=exam,
        question__section='practical'
    ).count()

    return render(
        request,
        'study/exam_intro.html',
        {
            'exam': exam,
            'total': total,
            'theory_count': theory_count,
            'practical_count': practical_count,
        }
    )


def retry_wrong(request, exam_id, index=0):
    from django.shortcuts import get_object_or_404, redirect
    from .models import ExamQuestion

    exam = get_object_or_404(Exam, id=exam_id)

    wrong_key = f"exam_{exam.id}_wrong_orders"
    wrong_orders = request.session.get(wrong_key, [])

    if not wrong_orders:
        return redirect('exam_result', exam_id=exam.id)

    if index >= len(wrong_orders):
        return redirect('exam_result', exam_id=exam.id)

    order = wrong_orders[index]

    item = (
        ExamQuestion.objects
        .filter(exam=exam, order=order)
        .select_related('question')
        .first()
    )

    if not item:
        return redirect('exam_result', exam_id=exam.id)

    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer == item.question.correct_answer:
            return redirect(
                'retry_wrong',
                exam_id=exam.id,
                index=index + 1
            )

    return render(
        request,
        'study/retry_wrong.html',
        {
            'exam': exam,
            'question': item.question,
            'order': order,
            'index': index,
            'total_wrong': len(wrong_orders),
            'next_index': index + 1,
        }
    )



def exam_result(request, exam_id):
    from django.shortcuts import get_object_or_404
    from .models import ExamQuestion

    exam = get_object_or_404(Exam, id=exam_id)

    items = (
        ExamQuestion.objects
        .filter(exam=exam)
        .select_related("question")
    )

    answers = request.session.get(
        f"exam_{exam.id}_answers",
        {}
    )

    total = items.count()
    correct_count = 0
    wrong_count = 0
    unanswered_count = 0

    for item in items:

        # Sau khi xáo câu, đáp án được lưu theo ExamQuestion ID
        selected = answers.get(str(item.id), "")

        if not selected:
            unanswered_count += 1

        elif selected == item.question.correct_answer:
            correct_count += 1

        else:
            wrong_count += 1

    score_percent = (
        round(correct_count / total * 100, 1)
        if total else 0
    )

    passed = score_percent >= 65

    return render(
        request,
        "study/exam_result.html",
        {
            "exam": exam,
            "total": total,
            "correct_count": correct_count,
            "wrong_count": wrong_count,
            "unanswered_count": unanswered_count,
            "score_percent": score_percent,
            "passed": passed,
        }
    )


def wrong_answers(request, exam_id):
    from django.shortcuts import get_object_or_404
    from .models import ExamQuestion

    exam = get_object_or_404(Exam, id=exam_id)

    answers = request.session.get(
        f"exam_{exam.id}_answers",
        {}
    )

    # Lấy thứ tự câu đúng theo lượt thi đã xáo
    order_ids = request.session.get(
        f"exam_{exam.id}_order",
        []
    )

    db_items = {
        x.id: x
        for x in (
            ExamQuestion.objects
            .filter(exam=exam)
            .select_related("question")
        )
    }

    wrong_items = []

    # Nếu có thứ tự đã xáo thì hiển thị theo đúng thứ tự lúc thi
    if order_ids:
        ordered_items = [
            db_items[x]
            for x in order_ids
            if x in db_items
        ]
    else:
        ordered_items = list(db_items.values())

    for position, item in enumerate(ordered_items, start=1):

        selected = answers.get(str(item.id), "")
        correct = item.question.correct_answer

        # Chỉ hiện câu đã trả lời nhưng trả lời sai
        if selected and selected != correct:
            wrong_items.append({
                "order": position,
                "question": item.question,
                "selected": selected,
                "correct": correct,
            })

    return render(
        request,
        "study/wrong_answers.html",
        {
            "exam": exam,
            "wrong_items": wrong_items,
            "wrong_count": len(wrong_items),
        }
    )
