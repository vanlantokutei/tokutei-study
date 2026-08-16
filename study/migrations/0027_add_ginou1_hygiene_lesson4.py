from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='receiving-ingredients-check',
        defaults={
            'title_jp': '原材料の受入れ確認',
            'title_furigana': 'げんざいりょう の うけいれ かくにん',
            'title_vi': 'Bài 4: Kiểm tra khi tiếp nhận nguyên liệu',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】
<ruby>原材料<rt>げんざいりょう</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れるときは、<ruby>安全<rt>あんぜん</rt></ruby>な<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>使用<rt>しよう</rt></ruby>するために、<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>します。

① <ruby>納品<rt>のうひん</rt></ruby>された<ruby>食品<rt>しょくひん</rt></ruby>の<ruby>品名<rt>ひんめい</rt></ruby>、<ruby>数量<rt>すうりょう</rt></ruby>、<ruby>期限表示<rt>きげんひょうじ</rt></ruby>などを<ruby>確認<rt>かくにん</rt></ruby>します。

② <ruby>包装<rt>ほうそう</rt></ruby>の<ruby>破損<rt>はそん</rt></ruby>、<ruby>汚<rt>よご</rt></ruby>れ、<ruby>異常<rt>いじょう</rt></ruby>なにおいなどがないかを<ruby>確認<rt>かくにん</rt></ruby>します。

③ <ruby>冷蔵品<rt>れいぞうひん</rt></ruby>や<ruby>冷凍品<rt>れいとうひん</rt></ruby>は、<ruby>必要<rt>ひつよう</rt></ruby>に<ruby>応<rt>おう</rt></ruby>じて<ruby>温度<rt>おんど</rt></ruby>や<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>し、<ruby>受入<rt>うけい</rt></ruby>れ<ruby>後<rt>ご</rt></ruby>は<ruby>速<rt>すみ</rt></ruby>やかに<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>場所<rt>ばしょ</rt></ruby>へ<ruby>保管<rt>ほかん</rt></ruby>します。

<ruby>問題<rt>もんだい</rt></ruby>がある<ruby>原材料<rt>げんざいりょう</rt></ruby>をそのまま<ruby>使用<rt>しよう</rt></ruby>せず、<ruby>店舗<rt>てんぽ</rt></ruby>のルールに<ruby>従<rt>したが</rt></ruby>って<ruby>報告<rt>ほうこく</rt></ruby>・<ruby>対応<rt>たいおう</rt></ruby>します。''',
            'content_furigana': '',
            'content_vi': '''## 1. Vì sao phải kiểm tra ngay khi nhận hàng?
Nếu nguyên liệu có vấn đề nhưng vẫn đưa vào kho và sử dụng, nguy cơ mất an toàn thực phẩm sẽ tăng lên. Vì vậy bước **受入れ確認 – kiểm tra khi tiếp nhận** là điểm kiểm soát đầu tiên của cửa hàng.

## 2. Những nội dung cần kiểm tra
- Tên hàng và số lượng có đúng đơn giao không.
- Hạn sử dụng/hạn chất lượng và nhãn có bình thường không.
- Bao bì có rách, bẩn, phồng hoặc có dấu hiệu bất thường không.
- Thực phẩm có mùi hoặc trạng thái bất thường không.
- Hàng lạnh/hàng đông lạnh có được duy trì trong tình trạng phù hợp không.

## 3. Sau khi nhận hàng
Không nên để hàng lạnh hoặc hàng đông lạnh nằm ngoài khu vực bảo quản quá lâu. Sau khi kiểm tra xong, phải nhanh chóng đưa nguyên liệu vào nơi bảo quản phù hợp.

## 4. Nếu phát hiện bất thường
Không tự ý sử dụng nguyên liệu có vấn đề. Hãy tách riêng, báo cáo người phụ trách và xử lý theo quy định của cửa hàng.

## Ví dụ thực tế
Một thùng thịt đông lạnh được giao tới nhưng bên ngoài đã mềm và có dấu hiệu rã đông. Không nên chỉ nhìn hạn sử dụng rồi nhận hàng ngay. Cần kiểm tra tình trạng và xử lý theo quy định.''',
            'exam_notes_vi': '''Điểm cần nhớ khi thi:
• Kiểm tra ngay tại thời điểm nhận nguyên liệu, không chờ đến lúc chế biến.
• Nhớ các nhóm kiểm tra: hàng hóa/số lượng → hạn → bao bì/trạng thái → nhiệt độ/tình trạng bảo quản.
• Hàng lạnh và đông lạnh cần được đưa vào nơi bảo quản phù hợp sớm sau khi tiếp nhận.
• Khi có bất thường: không sử dụng tùy tiện → báo cáo và xử lý theo quy định.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 4,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    questions = [
        ('<ruby>原材料<rt>げんざいりょう</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れるとき、まず<ruby>確認<rt>かくにん</rt></ruby>することとして<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。', 'Khi tiếp nhận nguyên liệu, việc kiểm tra nào là phù hợp?', '品名・数量・期限表示など', '店の音楽', '客席の色', 'A', 'Khi nhận nguyên liệu cần kiểm tra tên hàng, số lượng, hạn và tình trạng của hàng.'),
        ('<ruby>包装<rt>ほうそう</rt></ruby>が<ruby>破損<rt>はそん</rt></ruby>している<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけたとき、どうしますか。', 'Nếu phát hiện bao bì thực phẩm bị hỏng, nên làm gì?', 'そのまま使う', '状態を確認し、ルールに従って対応する', 'すぐ客に出す', 'B', 'Không nên tự ý sử dụng nguyên liệu có dấu hiệu bất thường.'),
        ('<ruby>冷蔵品<rt>れいぞうひん</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れた<ruby>後<rt>あと</rt></ruby>の<ruby>対応<rt>たいおう</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。', 'Sau khi nhận hàng lạnh, xử lý nào phù hợp?', '長時間室温に置く', '速やかに適切な場所へ保管する', '入口に置く', 'B', 'Hàng cần làm lạnh nên được đưa vào nơi bảo quản phù hợp càng sớm càng tốt.'),
        ('<ruby>受入<rt>うけい</rt></ruby>れ<ruby>時<rt>じ</rt></ruby>に<ruby>確認<rt>かくにん</rt></ruby>する<ruby>内容<rt>ないよう</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。', 'Nội dung nào KHÔNG liên quan đến kiểm tra khi nhận hàng?', '期限表示', '包装の状態', '従業員の靴の色', 'C', 'Màu giày nhân viên không phải nội dung kiểm tra nguyên liệu khi nhận hàng.'),
        ('<ruby>異常<rt>いじょう</rt></ruby>がある<ruby>原材料<rt>げんざいりょう</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけたときの<ruby>基本<rt>きほん</rt></ruby>はどれですか。', 'Khi phát hiện nguyên liệu bất thường, nguyên tắc cơ bản là gì?', 'そのまま調理する', '報告せず捨てる', '使用せず、報告してルールに従う', 'C', 'Không tự ý sử dụng; cần báo cáo và xử lý theo quy định.'),
    ]
    for i, q in enumerate(questions, 1):
        QuickQuestion.objects.create(
            lesson=lesson,
            question_jp=q[0],
            question_furigana=q[0],
            question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0026_add_ginou1_hygiene_lesson3')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
