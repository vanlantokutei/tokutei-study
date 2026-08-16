import os
import time

from django.core.management.base import BaseCommand
from openai import OpenAI

from study.models import Question


class Command(BaseCommand):
    help = "Tự động tạo giải thích tiếng Việt cho các câu còn thiếu"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Giới hạn số câu xử lý. 0 = tất cả"
        )

    def handle(self, *args, **options):
        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            self.stdout.write(
                self.style.ERROR(
                    "❌ Chưa có OPENAI_API_KEY"
                )
            )
            return

        client = OpenAI(api_key=api_key)

        qs = Question.objects.filter(
            explanation_vi=""
        ).order_by("id")

        if options["limit"] > 0:
            qs = qs[:options["limit"]]

        total = len(qs)

        self.stdout.write(
            f"🔎 Tìm thấy {total} câu chưa có giải thích tiếng Việt"
        )

        success = 0
        failed = 0

        for index, q in enumerate(qs, start=1):

            prompt = f"""
Bạn đang viết nội dung ôn thi 特定技能 外食業 cho người Việt.

Hãy viết GIẢI THÍCH TIẾNG VIỆT ngắn gọn, chính xác, dễ học
cho câu hỏi dưới đây.

Yêu cầu:
- Giải thích vì sao đáp án đúng là đúng.
- Nếu cần, giải thích ngắn vì sao các lựa chọn còn lại sai.
- Không dịch máy cứng nhắc.
- Không thêm thông tin không chắc chắn.
- Viết 2 đến 4 câu.
- Chỉ trả về phần giải thích tiếng Việt.

Câu hỏi tiếng Nhật:
{q.question_jp}

Bản dịch tiếng Việt:
{q.question_vi}

A: {q.option_a}
B: {q.option_b}
C: {q.option_c}

Đáp án đúng:
{q.correct_answer}

Giải thích tiếng Nhật hiện có:
{q.explanation}
"""

            try:
                response = client.responses.create(
                    model="gpt-5.1-mini",
                    input=prompt
                )

                text = response.output_text.strip()

                if not text:
                    raise ValueError("AI trả về nội dung trống")

                q.explanation_vi = text
                q.save(
                    update_fields=["explanation_vi"]
                )

                success += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"✅ {index}/{total} - Question ID {q.id}"
                    )
                )

            except Exception as e:
                failed += 1

                self.stdout.write(
                    self.style.ERROR(
                        f"❌ ID {q.id}: {e}"
                    )
                )

                time.sleep(2)

        self.stdout.write("")
        self.stdout.write("================================")
        self.stdout.write(
            f"✅ Thành công: {success}"
        )
        self.stdout.write(
            f"❌ Lỗi: {failed}"
        )
        self.stdout.write("================================")
