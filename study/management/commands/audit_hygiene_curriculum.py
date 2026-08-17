from django.core.management.base import BaseCommand
from django.db.models import Q

from study.models import LearningCategory, Lesson


class Command(BaseCommand):
    help = (
        'Kiểm tra mức độ bao phủ phần 衛生管理 của Tokutei Ginou 1. '
        'Lệnh chỉ audit, không tự sửa dữ liệu.'
    )

    # Checklist bám theo cấu trúc kiến thức 衛生管理 trong giáo trình học thi
    # 外食業 特定技能1号 của 日本フードサービス協会/OTAFF.
    TOPICS = [
        {
            'code': 'food_poisoning_basic',
            'jp': '食中毒の基礎',
            'vi': 'Khái niệm và nguyên nhân ngộ độc thực phẩm',
            'keywords': ['食中毒', '原因', '細菌', 'ウイルス'],
        },
        {
            'code': 'three_principles',
            'jp': '食中毒予防の3原則',
            'vi': '3 nguyên tắc phòng ngộ độc: không để nhiễm, không cho tăng, tiêu diệt',
            'keywords': ['つけない', '増やさない', 'やっつける'],
        },
        {
            'code': 'receiving',
            'jp': '原材料の受入れ確認',
            'vi': 'Kiểm tra nguyên liệu khi nhận hàng',
            'keywords': ['原材料', '受入', '納品', '確認'],
        },
        {
            'code': 'storage_temperature',
            'jp': '冷蔵・冷凍庫の温度確認',
            'vi': 'Quản lý nhiệt độ tủ lạnh và tủ đông',
            'keywords': ['冷蔵', '冷凍', '温度'],
        },
        {
            'code': 'cross_contamination',
            'jp': '交差汚染・二次汚染の防止',
            'vi': 'Phòng nhiễm chéo và nhiễm bẩn thứ cấp',
            'keywords': ['交差汚染', '二次汚染', '汚染'],
        },
        {
            'code': 'utensil_sanitation',
            'jp': '器具等の洗浄・消毒・殺菌',
            'vi': 'Rửa, khử trùng và vệ sinh dụng cụ',
            'keywords': ['器具', '洗浄', '消毒', '殺菌'],
        },
        {
            'code': 'toilet_cleaning',
            'jp': 'トイレの洗浄・消毒',
            'vi': 'Vệ sinh và khử trùng nhà vệ sinh',
            'keywords': ['トイレ', '洗浄', '消毒'],
        },
        {
            'code': 'employee_health',
            'jp': '従業員の健康管理',
            'vi': 'Quản lý sức khỏe nhân viên',
            'keywords': ['従業員', '健康', '体調', '下痢', '嘔吐'],
        },
        {
            'code': 'hand_washing',
            'jp': '手洗い',
            'vi': 'Thời điểm và phương pháp rửa tay đúng',
            'keywords': ['手洗', '手を洗'],
        },
        {
            'code': 'haccp_basic',
            'jp': 'HACCPの考え方を取り入れた衛生管理',
            'vi': 'Quản lý vệ sinh theo tư duy HACCP',
            'keywords': ['HACCP', 'ハサップ', '衛生管理計画'],
        },
        {
            'code': 'cooking_groups',
            'jp': '非加熱・加熱・加熱後冷却する食品の管理',
            'vi': 'Phân loại và quản lý món không gia nhiệt/gia nhiệt/làm nguội sau gia nhiệt',
            'keywords': ['非加熱', '加熱', '冷却'],
        },
        {
            'code': 'core_temperature',
            'jp': '中心温度と加熱管理',
            'vi': 'Nhiệt độ tâm và kiểm soát gia nhiệt',
            'keywords': ['中心温度', '75℃', '1分', '加熱'],
        },
        {
            'code': 'danger_zone',
            'jp': '危険温度帯・時間管理',
            'vi': 'Vùng nhiệt độ nguy hiểm và quản lý thời gian',
            'keywords': ['危険温度', '温度帯', '時間'],
        },
        {
            'code': 'records',
            'jp': '衛生管理の記録と振り返り',
            'vi': 'Ghi chép, lưu hồ sơ và xem lại việc quản lý vệ sinh',
            'keywords': ['記録', '衛生管理', '振り返'],
        },
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--details',
            action='store_true',
            help='Hiện bài nào đang khớp với từng chủ đề.',
        )

    def handle(self, *args, **options):
        category = (
            LearningCategory.objects.filter(
                Q(slug__icontains='hygiene')
                | Q(title_jp__icontains='衛生')
                | Q(title_vi__icontains='vệ sinh')
            )
            .order_by('order', 'id')
            .first()
        )

        if not category:
            self.stderr.write(self.style.ERROR(
                'Không tìm thấy LearningCategory của 衛生管理.'
            ))
            return

        lessons = list(
            Lesson.objects.filter(category=category, is_published=True)
            .prefetch_related('quick_questions')
            .order_by('order', 'id')
        )

        if not lessons:
            self.stderr.write(self.style.ERROR(
                f'Nhóm {category.title_jp} chưa có bài học đã publish.'
            ))
            return

        self.stdout.write(self.style.MIGRATE_HEADING(
            f'AUDIT 衛生管理 — {len(lessons)} bài hiện có'
        ))
        self.stdout.write(
            'Nguồn chuẩn: OTAFF → 日本フードサービス協会 / '
            '外食業 特定技能1号 学習用テキスト（衛生管理）\n'
        )

        covered = 0
        missing = []

        for topic in self.TOPICS:
            matched = []
            for lesson in lessons:
                text = ' '.join([
                    lesson.title_jp or '',
                    lesson.title_furigana or '',
                    lesson.title_vi or '',
                    lesson.content_jp or '',
                    lesson.content_furigana or '',
                    lesson.content_vi or '',
                    lesson.exam_notes_vi or '',
                ]).lower()

                hit_count = sum(1 for kw in topic['keywords'] if kw.lower() in text)
                # Với checklist có >=3 keyword, cần ít nhất 2 để tránh false positive.
                threshold = 2 if len(topic['keywords']) >= 3 else 1
                if hit_count >= threshold:
                    matched.append(lesson)

            if matched:
                covered += 1
                status = self.style.SUCCESS('OK')
            else:
                status = self.style.ERROR('THIẾU')
                missing.append(topic)

            self.stdout.write(
                f"[{status}] {topic['jp']} — {topic['vi']}"
            )
            if options['details'] and matched:
                for lesson in matched:
                    self.stdout.write(
                        f'      ↳ Bài {lesson.order}: {lesson.title_vi}'
                    )

        total = len(self.TOPICS)
        percent = round(covered * 100 / total)
        self.stdout.write('')
        if percent == 100:
            self.stdout.write(self.style.SUCCESS(
                f'Bao phủ checklist: {covered}/{total} = {percent}%'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Bao phủ checklist: {covered}/{total} = {percent}%'
            ))

        # Quality checks cho từng bài: nguồn, furigana, nội dung Việt, ghi chú thi, câu luyện nhanh.
        self.stdout.write('\nKIỂM TRA CHẤT LƯỢNG TỪNG BÀI')
        quality_issues = 0
        for lesson in lessons:
            problems = []
            if not lesson.source_title or not lesson.source_url:
                problems.append('thiếu nguồn tham khảo')
            if '<ruby>' not in (lesson.title_jp or '') and not lesson.title_furigana:
                problems.append('thiếu furigana tiêu đề')
            if '<ruby>' not in (lesson.content_jp or '') and not lesson.content_furigana:
                problems.append('thiếu furigana nội dung')
            if not (lesson.content_vi or '').strip():
                problems.append('thiếu giải thích tiếng Việt')
            if not (lesson.exam_notes_vi or '').strip():
                problems.append('thiếu điểm cần nhớ khi thi')
            if lesson.quick_questions.count() < 3:
                problems.append('nên có ít nhất 3 câu luyện nhanh')

            if problems:
                quality_issues += 1
                self.stdout.write(self.style.WARNING(
                    f'Bài {lesson.order} — {lesson.title_vi}: ' + '; '.join(problems)
                ))
            elif options['details']:
                self.stdout.write(self.style.SUCCESS(
                    f'Bài {lesson.order} — {lesson.title_vi}: đạt checklist chất lượng'
                ))

        if missing:
            self.stdout.write('\nCÁC CHỦ ĐỀ CẦN BỔ SUNG/TRIỂN KHAI RÕ HƠN')
            for i, topic in enumerate(missing, 1):
                self.stdout.write(
                    f"{i}. {topic['jp']} — {topic['vi']}"
                )

        self.stdout.write('\nLưu ý: đây là công cụ audit nội bộ. ' 
                          'Kết quả keyword không thay thế việc đối chiếu thủ công từng mục với PDF chính thức.')
        self.stdout.write('\nChạy chi tiết bằng:')
        self.stdout.write(self.style.SUCCESS(
            'python manage.py audit_hygiene_curriculum --details'
        ))
