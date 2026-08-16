from django.db import models


class Question(models.Model):

    LEVEL_CHOICES = [
        ('1', '特定技能1号'),
        ('2', '特定技能2号'),
    ]

    SECTION_CHOICES = [
        ('theory', '学科試験'),
        ('practical', '実技試験'),
    ]

    PRACTICAL_TYPE_CHOICES = [
        ('', '---'),
        ('judgment', '判断試験'),
        ('planning', '計画立案'),
    ]

    CATEGORY_CHOICES = [
        ('hygiene', '衛生管理'),
        ('cooking', '飲食物調理'),
        ('service', '接客全般'),
    ]

    level = models.CharField(
        max_length=1,
        choices=LEVEL_CHOICES,
        default='1'
    )

    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        default='theory',
        verbose_name='Phần thi'
    )

    practical_type = models.CharField(
        max_length=20,
        choices=PRACTICAL_TYPE_CHOICES,
        blank=True,
        default='',
        verbose_name='Loại câu thực hành'
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='hygiene',
        verbose_name='Chủ đề'
    )

    question_jp = models.TextField(
        verbose_name='Câu hỏi tiếng Nhật'
    )

    question_ruby = models.TextField(
        blank=True,
        default='',
        verbose_name='Câu hỏi tiếng Nhật + Furigana'
    )

    question_vi = models.TextField(
        blank=True,
        default='',
        verbose_name='Câu hỏi tiếng Việt'
    )

    option_a = models.CharField(
        max_length=500,
        verbose_name='Đáp án A'
    )

    option_a_vi = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='Đáp án A tiếng Việt'
    )

    option_a_ruby = models.TextField(
        blank=True,
        default='',
        verbose_name='Đáp án A Furigana'
    )

    option_b = models.CharField(
        max_length=500,
        verbose_name='Đáp án B'
    )

    option_b_vi = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='Đáp án B tiếng Việt'
    )

    option_b_ruby = models.TextField(
        blank=True,
        default='',
        verbose_name='Đáp án B Furigana'
    )

    option_c = models.CharField(
        max_length=500,
        verbose_name='Đáp án C'
    )

    option_c_vi = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='Đáp án C tiếng Việt'
    )

    option_c_ruby = models.TextField(
        blank=True,
        default='',
        verbose_name='Đáp án C Furigana'
    )

    points = models.PositiveIntegerField(
        default=0,
        verbose_name='Điểm'
    )

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
        ],
        verbose_name='Đáp án đúng'
    )

    explanation = models.TextField(
        blank=True,
        default='',
        verbose_name='Giải thích tiếng Nhật'
    )

    explanation_vi = models.TextField(
        blank=True,
        default='',
        verbose_name='Giải thích tiếng Việt'
    )

    def __str__(self):
        return f"{self.get_section_display()} - {self.question_jp}"


class Exam(models.Model):

    level = models.CharField(
        max_length=1,
        choices=Question.LEVEL_CHOICES,
        default='1'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Tên đề'
    )

    description = models.TextField(
        blank=True,
        default=''
    )

    is_free = models.BooleanField(
        default=True,
        verbose_name='Miễn phí'
    )

    order = models.PositiveIntegerField(
        default=1
    )

    time_limit = models.PositiveIntegerField(
        default=70,
        verbose_name='Thời gian thi (phút)'
    )

    questions = models.ManyToManyField(
        Question,
        through='ExamQuestion',
        related_name='exams'
    )

    def __str__(self):
        return self.title


class ExamQuestion(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('exam', 'question')

    def __str__(self):
        return f"{self.exam.title} - Câu {self.order}"


class LearningCategory(models.Model):
    """Nhóm kiến thức của Kho tài liệu, tách biệt với ngân hàng đề thi."""

    slug = models.SlugField(unique=True)
    title_jp = models.CharField(max_length=120)
    title_vi = models.CharField(max_length=120)
    description_vi = models.TextField(blank=True, default='')
    icon = models.CharField(max_length=10, blank=True, default='📘')
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Nhóm tài liệu'
        verbose_name_plural = 'Nhóm tài liệu'

    def __str__(self):
        return f"{self.title_jp} - {self.title_vi}"


class Lesson(models.Model):
    """Bài học song ngữ; có thể nhập dần từ giáo trình chính thức."""

    category = models.ForeignKey(
        LearningCategory,
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    slug = models.SlugField()
    title_jp = models.CharField(max_length=200)
    title_furigana = models.CharField(max_length=250, blank=True, default='')
    title_vi = models.CharField(max_length=200)
    content_jp = models.TextField()
    content_furigana = models.TextField(blank=True, default='')
    content_vi = models.TextField()
    exam_notes_vi = models.TextField(blank=True, default='')
    source_title = models.CharField(max_length=250, blank=True, default='')
    source_url = models.URLField(blank=True, default='')
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['category__order', 'order', 'id']
        unique_together = ('category', 'slug')
        verbose_name = 'Bài học'
        verbose_name_plural = 'Bài học'

    def __str__(self):
        return f"{self.category.title_vi}: {self.title_vi}"


class QuickQuestion(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='quick_questions',
    )
    question_jp = models.TextField()
    question_furigana = models.TextField(blank=True, default='')
    question_vi = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    correct_answer = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C')],
    )
    explanation_vi = models.TextField(blank=True, default='')
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Câu luyện nhanh'
        verbose_name_plural = 'Câu luyện nhanh'

    def __str__(self):
        return self.question_vi[:80]


class VocabularyEntry(models.Model):
    CATEGORY_CHOICES = [
        ('hygiene', '衛生管理 - Quản lý vệ sinh'),
        ('cooking', '飲食物調理 - Chế biến'),
        ('service', '接客全般 - Phục vụ khách hàng'),
    ]
    TOPIC_CHOICES = [
        ('core', 'Kiến thức cốt lõi'),
        ('ingredients_tools', 'Thực phẩm, nguyên liệu và dụng cụ'),
        ('cooking_actions', 'Thao tác chế biến'),
        ('food_poisoning', 'Ngộ độc và triệu chứng'),
        ('temperature_numbers', 'Nhiệt độ, thời gian và tính toán'),
        ('communication', 'Giao tiếp với khách hàng'),
        ('store_operations', 'Thanh toán, đặt bàn và xử lý phàn nàn'),
        ('allergy_diversity', 'Dị ứng và chế độ ăn đặc biệt'),
        ('workplace_safety', 'An toàn, cháy nổ và sơ tán'),
        ('practical_planning', 'Thực hành và lập kế hoạch'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    topic = models.CharField(
        max_length=30,
        choices=TOPIC_CHOICES,
        default='core',
        verbose_name='Nhóm nội dung',
    )
    word_jp = models.CharField(max_length=120, verbose_name='Từ tiếng Nhật')
    furigana = models.CharField(max_length=150, verbose_name='Furigana')
    meaning_vi = models.CharField(max_length=250, verbose_name='Nghĩa tiếng Việt')
    example_jp = models.TextField(blank=True, default='', verbose_name='Ví dụ tiếng Nhật')
    example_furigana = models.TextField(blank=True, default='', verbose_name='Furigana của ví dụ')
    example_vi = models.TextField(blank=True, default='', verbose_name='Nghĩa của ví dụ')
    exam_note_vi = models.TextField(blank=True, default='', verbose_name='Ghi chú khi thi')
    source_title = models.CharField(max_length=250, blank=True, default='', verbose_name='Tên nguồn')
    source_url = models.URLField(blank=True, default='', verbose_name='Đường dẫn nguồn')
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'order', 'id']
        verbose_name = 'Từ vựng'
        verbose_name_plural = 'Kho từ vựng'
        indexes = [
            models.Index(fields=['category', 'is_published']),
            models.Index(fields=['topic', 'is_published']),
        ]

    def __str__(self):
        return f"{self.word_jp} ({self.furigana}) - {self.meaning_vi}"


class ServiceSituation(models.Model):
    CATEGORY_CHOICES = [
        ('welcome_order', 'Đón khách và gọi món'),
        ('complaint', 'Phàn nàn và sai sót'),
        ('allergy', 'Dị ứng và yêu cầu đặc biệt'),
        ('payment', 'Thanh toán và đặt bàn'),
        ('emergency', 'Sự cố và tình huống khẩn cấp'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    slug = models.SlugField(unique=True)
    title_jp = models.CharField(max_length=200)
    title_furigana = models.CharField(max_length=250, blank=True, default='')
    title_vi = models.CharField(max_length=200)
    situation_jp = models.TextField(verbose_name='Bối cảnh tiếng Nhật')
    situation_furigana = models.TextField(blank=True, default='')
    situation_vi = models.TextField(verbose_name='Bối cảnh tiếng Việt')
    customer_phrase_jp = models.TextField(blank=True, default='', verbose_name='Lời khách nói')
    customer_phrase_furigana = models.TextField(blank=True, default='')
    customer_phrase_vi = models.TextField(blank=True, default='')
    response_jp = models.TextField(verbose_name='Câu trả lời mẫu tiếng Nhật')
    response_furigana = models.TextField(blank=True, default='')
    response_vi = models.TextField(verbose_name='Câu trả lời mẫu tiếng Việt')
    handling_steps_vi = models.TextField(verbose_name='Các bước xử lý')
    exam_note_vi = models.TextField(blank=True, default='')
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'order', 'id']
        verbose_name = 'Tình huống dịch vụ'
        verbose_name_plural = 'Tình huống ngành dịch vụ'

    def __str__(self):
        return self.title_vi
