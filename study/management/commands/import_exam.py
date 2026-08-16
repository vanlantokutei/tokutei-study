import json
import re

from django.core.management.base import BaseCommand, CommandError
from pykakasi import kakasi

from study.models import Exam, Question, ExamQuestion


class Command(BaseCommand):
    help = "Import 45 câu cho một đề Tokutei 外食業"

    def add_arguments(self, parser):
        parser.add_argument("exam_order", type=int)
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        exam_order = options["exam_order"]
        json_file = options["json_file"]

        try:
            exam = Exam.objects.get(
                level="1",
                order=exam_order
            )
        except Exam.DoesNotExist:
            raise CommandError(
                f"Không tìm thấy Đề {exam_order:02d}"
            )

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if len(data) != 45:
            raise CommandError(
                f"File phải có đúng 45 câu. Hiện có {len(data)}."
            )

        theory = [
            x for x in data
            if x["section"] == "theory"
        ]

        practical = [
            x for x in data
            if x["section"] == "practical"
        ]

        if len(theory) != 30:
            raise CommandError(
                f"学科 phải có 30 câu. Hiện có {len(theory)}."
            )

        if len(practical) != 15:
            raise CommandError(
                f"実技 phải có 15 câu. Hiện có {len(practical)}."
            )

        valid_categories = {
            "hygiene",
            "cooking",
            "service"
        }

        for category in valid_categories:
            theory_count = sum(
                1 for x in theory
                if x["category"] == category
            )

            if theory_count != 10:
                raise CommandError(
                    f"学科 {category} phải có 10 câu, "
                    f"hiện có {theory_count}."
                )

            practical_items = [
                x for x in practical
                if x["category"] == category
            ]

            if len(practical_items) != 5:
                raise CommandError(
                    f"実技 {category} phải có 5 câu."
                )

            judgment = sum(
                1 for x in practical_items
                if x.get("practical_type") == "judgment"
            )

            planning = sum(
                1 for x in practical_items
                if x.get("practical_type") == "planning"
            )

            if judgment != 3 or planning != 2:
                raise CommandError(
                    f"{category}: 実技 phải có "
                    f"3 判断 + 2 計画立案."
                )

        kks = kakasi()

        def make_ruby(text):
            result = []

            for item in kks.convert(text):
                original = item["orig"]
                hira = item["hira"]

                if re.search(
                    r"[\u4e00-\u9fff]",
                    original
                ):
                    result.append(
                        f"<ruby>{original}"
                        f"<rt>{hira}</rt>"
                        f"</ruby>"
                    )
                else:
                    result.append(original)

            return "".join(result)

        # Xóa liên kết cũ của đề nếu có
        ExamQuestion.objects.filter(
            exam=exam
        ).delete()

        for order, x in enumerate(data, start=1):

            correct = x["correct_answer"]

            if correct not in ["A", "B", "C"]:
                raise CommandError(
                    f"Câu {order}: đáp án phải là A/B/C."
                )

            q = Question.objects.create(
                level="1",
                section=x["section"],
                practical_type=x.get(
                    "practical_type",
                    ""
                ),
                category=x["category"],

                question_jp=x["question_jp"],
                question_ruby=make_ruby(
                    x["question_jp"]
                ),
                question_vi=x["question_vi"],

                option_a=x["option_a"],
                option_a_ruby=make_ruby(
                    x["option_a"]
                ),
                option_a_vi=x["option_a_vi"],

                option_b=x["option_b"],
                option_b_ruby=make_ruby(
                    x["option_b"]
                ),
                option_b_vi=x["option_b_vi"],

                option_c=x["option_c"],
                option_c_ruby=make_ruby(
                    x["option_c"]
                ),
                option_c_vi=x["option_c_vi"],

                correct_answer=correct,
                explanation=x["explanation"],
            )

            ExamQuestion.objects.create(
                exam=exam,
                question=q,
                order=order
            )

            self.stdout.write(
                f"✅ Câu {order:02d}/45"
            )

        exam.time_limit = 70
        exam.is_free = True
        exam.save(
            update_fields=[
                "time_limit",
                "is_free"
            ]
        )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Đề {exam_order:02d}: "
                f"45/45 câu hoàn thành"
            )
        )
