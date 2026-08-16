from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='proper-hand-washing',
        defaults={
            'title_jp': '<ruby>正<rt>ただ</rt></ruby>しい<ruby>手洗<rt>てあら</rt></ruby>い',
            'title_furigana': '',
            'title_vi': 'Bài 7: Rửa tay đúng cách',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>手<rt>て</rt></ruby>には、<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>となる<ruby>細菌<rt>さいきん</rt></ruby>やウイルスが<ruby>付着<rt>ふちゃく</rt></ruby>することがあります。<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>取<rt>と</rt></ruby>り<ruby>扱<rt>あつか</rt></ruby>うため、<ruby>必要<rt>ひつよう</rt></ruby>なタイミングで<ruby>正<rt>ただ</rt></ruby>しく<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>うことが<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n【<ruby>手洗<rt>てあら</rt></ruby>いが<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>主<rt>おも</rt></ruby>なタイミング】\n・<ruby>作業<rt>さぎょう</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>める<ruby>前<rt>まえ</rt></ruby>\n・トイレの<ruby>後<rt>あと</rt></ruby>\n・<ruby>生肉<rt>なまにく</rt></ruby>や<ruby>生魚<rt>なまざかな</rt></ruby>などを<ruby>触<rt>さわ</rt></ruby>った<ruby>後<rt>あと</rt></ruby>\n・ごみや<ruby>汚<rt>よご</rt></ruby>れたものを<ruby>触<rt>さわ</rt></ruby>った<ruby>後<rt>あと</rt></ruby>\n・<ruby>盛<rt>も</rt></ruby>り<ruby>付<rt>つ</rt></ruby>けなど、<ruby>清潔<rt>せいけつ</rt></ruby>な<ruby>作業<rt>さぎょう</rt></ruby>に<ruby>移<rt>うつ</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>\n\n【<ruby>洗<rt>あら</rt></ruby>い<ruby>方<rt>かた</rt></ruby>】\n<ruby>流水<rt>りゅうすい</rt></ruby>で<ruby>手<rt>て</rt></ruby>をぬらし、<ruby>石<rt>せっ</rt></ruby>けんなどを<ruby>使<rt>つか</rt></ruby>って、<ruby>手<rt>て</rt></ruby>のひら、<ruby>手<rt>て</rt></ruby>の<ruby>甲<rt>こう</rt></ruby>、<ruby>指<rt>ゆび</rt></ruby>の<ruby>間<rt>あいだ</rt></ruby>、<ruby>指先<rt>ゆびさき</rt></ruby>、<ruby>爪<rt>つめ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>り、<ruby>親指<rt>おやゆび</rt></ruby>、<ruby>手首<rt>てくび</rt></ruby>まで<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>洗<rt>あら</rt></ruby>います。その<ruby>後<rt>あと</rt></ruby>、<ruby>流水<rt>りゅうすい</rt></ruby>でよくすすぎ、<ruby>清潔<rt>せいけつ</rt></ruby>な<ruby>方法<rt>ほうほう</rt></ruby>で<ruby>乾燥<rt>かんそう</rt></ruby>させます。\n\n<ruby>手袋<rt>てぶくろ</rt></ruby>を<ruby>使用<rt>しよう</rt></ruby>する<ruby>場合<rt>ばあい</rt></ruby>でも、<ruby>手洗<rt>てあら</rt></ruby>いが<ruby>不要<rt>ふよう</rt></ruby>になるわけではありません。<ruby>汚<rt>よご</rt></ruby>れた<ruby>手袋<rt>てぶくろ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>い<ruby>続<rt>つづ</rt></ruby>けると、<ruby>汚染<rt>おせん</rt></ruby>を<ruby>広<rt>ひろ</rt></ruby>げる<ruby>原因<rt>げんいん</rt></ruby>になります。''',
            'content_furigana': '',
            'content_vi': '''## 1. Vì sao phải rửa tay?\nTay là một trong những con đường dễ làm vi khuẩn và virus truyền sang thực phẩm. Vì vậy, rửa tay đúng lúc và đúng cách là biện pháp cơ bản để phòng ngộ độc thực phẩm.\n\n## 2. Những lúc đặc biệt cần rửa tay\n- Trước khi bắt đầu công việc.\n- Sau khi đi vệ sinh.\n- Sau khi chạm vào thịt sống, cá sống hoặc nguyên liệu có nguy cơ nhiễm bẩn.\n- Sau khi chạm vào rác hoặc đồ bẩn.\n- Trước khi chuyển từ công việc bẩn sang công việc sạch như chia món, trang trí hoặc xử lý thực phẩm ăn ngay.\n\n## 3. Những vị trí dễ rửa sót\nKhông chỉ chà lòng bàn tay. Cần chú ý mu bàn tay, kẽ ngón tay, đầu ngón và quanh móng, ngón cái và cổ tay.\n\n## 4. Quy trình cơ bản\nLàm ướt tay bằng nước chảy → dùng xà phòng → chà kỹ toàn bộ bàn tay → xả sạch dưới nước chảy → làm khô bằng phương pháp sạch.\n\n## 5. Đeo găng tay không thay thế việc rửa tay\nGăng tay bẩn vẫn có thể làm lây nhiễm sang thực phẩm khác. Phải rửa tay và thay găng đúng thời điểm theo công việc.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ khi thi:\n• “Đeo găng = không cần rửa tay” là SAI.\n• Sau toilet, sau khi chạm thịt/cá sống, rác hoặc vật bẩn → phải nghĩ ngay đến 手洗い.\n• Khi chuyển từ thao tác bẩn sang thao tác sạch → rửa tay.\n• Dễ bỏ sót: kẽ ngón, đầu ngón, quanh móng, ngón cái, mu bàn tay và cổ tay.\n• Câu tình huống thường hỏi “khi nào phải rửa tay” và “cách nào không phù hợp”.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 7,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>手洗<rt>てあら</rt></ruby>いが<ruby>必要<rt>ひつよう</rt></ruby>なタイミングはどれですか。','Khi nào cần rửa tay?','トイレの後','一日の仕事が全部終わった後だけ','必要ない','A','Sau khi đi vệ sinh là thời điểm bắt buộc phải chú ý rửa tay.'),
        ('<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>触<rt>さわ</rt></ruby>った<ruby>後<rt>あと</rt></ruby>、サラダを<ruby>盛<rt>も</rt></ruby>り<ruby>付<rt>つ</rt></ruby>ける<ruby>前<rt>まえ</rt></ruby>にどうしますか。','Sau khi chạm thịt sống, trước khi làm salad nên làm gì?','適切に手を洗う','そのまま作業する','服で手を拭くだけ','A','Cần rửa tay đúng cách trước khi chuyển từ thao tác bẩn sang thực phẩm ăn ngay.'),
        ('<ruby>手洗<rt>てあら</rt></ruby>いで<ruby>洗<rt>あら</rt></ruby>い<ruby>残<rt>のこ</rt></ruby>しやすい<ruby>場所<rt>ばしょ</rt></ruby>として<ruby>注意<rt>ちゅうい</rt></ruby>するものはどれですか。','Vị trí nào cần đặc biệt chú ý vì dễ rửa sót?','指の間や指先、爪の周り','服の袖だけ','靴の裏だけ','A','Kẽ ngón, đầu ngón và quanh móng là những vị trí cần chà kỹ.'),
        ('<ruby>手袋<rt>てぶくろ</rt></ruby>をすれば、<ruby>手洗<rt>てあら</rt></ruby>いは<ruby>必要<rt>ひつよう</rt></ruby>ありませんか。','Nếu đeo găng tay thì không cần rửa tay đúng không?','必要である','絶対に必要ない','一週間に一回でよい','A','Đeo găng không thay thế việc rửa tay; găng bẩn cũng có thể làm lây nhiễm.'),
        ('<ruby>正<rt>ただ</rt></ruby>しい<ruby>手洗<rt>てあら</rt></ruby>いとして<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。','Cách nào KHÔNG phù hợp khi rửa tay?','指の間まで洗う','流水ですすぐ','手のひらだけを短時間ぬらして終わる','C','Chỉ làm ướt nhanh lòng bàn tay không thể làm sạch đầy đủ các vị trí cần thiết.'),
    ]
    for i, q in enumerate(qs, 1):
        QuickQuestion.objects.create(
            lesson=lesson,
            question_jp=q[0], question_furigana=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0030_standardize_hygiene_lessons_1_4_ruby')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
