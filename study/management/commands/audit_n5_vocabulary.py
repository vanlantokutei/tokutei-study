import ast
import re
from collections import defaultdict
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Audit JLPT N5 vocabulary lessons for duplicate main vocabulary entries."

    def handle(self, *args, **options):
        template_dir = Path(settings.BASE_DIR) / "study" / "templates" / "study"
        files = [template_dir / "jlpt_n5_vocabulary.html"]
        files += [template_dir / f"jlpt_n5_vocabulary_lesson{i}.html" for i in range(2, 26)]

        by_word = defaultdict(list)
        by_kana = defaultdict(list)
        counts = {}

        for lesson, path in enumerate(files, start=1):
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            match = re.search(r"const\s+words\s*=\s*(\[.*?\]);\s*const\s+", text, re.S)
            if not match:
                self.stdout.write(self.style.WARNING(f"Bài {lesson}: không đọc được mảng words"))
                continue
            try:
                words = ast.literal_eval(match.group(1))
            except Exception as exc:
                self.stdout.write(self.style.ERROR(f"Bài {lesson}: lỗi parse: {exc}"))
                continue

            counts[lesson] = len(words)
            for row in words:
                if len(row) < 2:
                    continue
                word = str(row[0]).strip()
                kana = str(row[1]).strip()
                by_word[word].append(lesson)
                # Kana-only duplicate is useful to review, but identical written forms are the hard error.
                by_kana[kana].append((lesson, word))

        duplicate_words = {w: ls for w, ls in by_word.items() if len(set(ls)) > 1}
        self.stdout.write("\n=== JLPT N5 VOCABULARY AUDIT ===")
        for lesson in sorted(counts):
            self.stdout.write(f"Bài {lesson:02}: {counts[lesson]} từ")

        self.stdout.write("\n=== TỪ CHÍNH BỊ TRÙNG ===")
        if not duplicate_words:
            self.stdout.write(self.style.SUCCESS("Không có từ chính bị trùng."))
        else:
            for word, lessons in sorted(duplicate_words.items()):
                unique_lessons = sorted(set(lessons))
                self.stdout.write(self.style.ERROR(f"{word}: bài {', '.join(map(str, unique_lessons))}"))

        self.stdout.write("\n=== KANA GIỐNG NHAU (CẦN KIỂM TRA NGHĨA) ===")
        for kana, entries in sorted(by_kana.items()):
            lessons = {lesson for lesson, _ in entries}
            forms = {word for _, word in entries}
            if len(lessons) > 1 and len(forms) > 1:
                detail = ", ".join(f"B{lesson}:{word}" for lesson, word in entries)
                self.stdout.write(f"{kana}: {detail}")

        if duplicate_words:
            raise SystemExit(1)
