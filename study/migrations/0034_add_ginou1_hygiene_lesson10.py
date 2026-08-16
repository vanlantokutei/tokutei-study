from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='pest-control',
        defaults={
            'title_jp': '<ruby>害虫<rt>がいちゅう</rt></ruby>・<ruby>害獣<rt>がいじゅう</rt></ruby>の<ruby>防除<rt>ぼうじょ</rt></ruby>',
            'title_furigana': '',
            'title_vi': 'Bài 10: Phòng chống côn trùng và động vật gây hại',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>飲食店<rt>いんしょくてん</rt></ruby>では、ゴキブリ、ハエ、ネズミなどの<ruby>害虫<rt>がいちゅう</rt></ruby>・<ruby>害獣<rt>がいじゅう</rt></ruby>が<ruby>食品<rt>しょくひん</rt></ruby>や<ruby>調理場<rt>ちょうりば</rt></ruby>を<ruby>汚染<rt>おせん</rt></ruby>することがあります。\n\n<ruby>害虫<rt>がいちゅう</rt></ruby>・<ruby>害獣<rt>がいじゅう</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐためには、まず<ruby>侵入<rt>しんにゅう</rt></ruby>させないことが<ruby>重要<rt>じゅうよう</rt></ruby>です。<ruby>扉<rt>とびら</rt></ruby>や<ruby>窓<rt>まど</rt></ruby>、<ruby>排水口<rt>はいすいこう</rt></ruby>など、<ruby>侵入経路<rt>しんにゅうけいろ</rt></ruby>となる<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>します。\n\nまた、<ruby>食品<rt>しょくひん</rt></ruby>やごみを<ruby>放置<rt>ほうち</rt></ruby>せず、<ruby>清掃<rt>せいそう</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>い、<ruby>餌<rt>えさ</rt></ruby>や<ruby>隠<rt>かく</rt></ruby>れ<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>作<rt>つく</rt></ruby>らないようにします。ごみは<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>容器<rt>ようき</rt></ruby>に<ruby>入<rt>い</rt></ruby>れ、<ruby>決<rt>き</rt></ruby>められた<ruby>方法<rt>ほうほう</rt></ruby>で<ruby>管理<rt>かんり</rt></ruby>します。\n\n<ruby>害虫<rt>がいちゅう</rt></ruby>や<ruby>害獣<rt>がいじゅう</rt></ruby>の<ruby>痕跡<rt>こんせき</rt></ruby>や<ruby>異常<rt>いじょう</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけた<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>責任者<rt>せきにんしゃ</rt></ruby>に<ruby>報告<rt>ほうこく</rt></ruby>し、<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>対策<rt>たいさく</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>います。\n\n<ruby>薬剤<rt>やくざい</rt></ruby>などを<ruby>使用<rt>しよう</rt></ruby>するときは、<ruby>食品<rt>しょくひん</rt></ruby>や<ruby>器具<rt>きぐ</rt></ruby>を<ruby>汚染<rt>おせん</rt></ruby>しないように、<ruby>決<rt>き</rt></ruby>められた<ruby>方法<rt>ほうほう</rt></ruby>を<ruby>守<rt>まも</rt></ruby>ることが<ruby>必要<rt>ひつよう</rt></ruby>です。''',
            'content_furigana': '',
            'content_vi': '''## 1. Vì sao phải phòng chống côn trùng và động vật gây hại?\nGián, ruồi, chuột và các sinh vật gây hại có thể mang vi khuẩn, làm bẩn thực phẩm, dụng cụ và khu vực chế biến.\n\n## 2. Ưu tiên ngăn chúng xâm nhập\nKiểm tra những nơi có thể trở thành đường xâm nhập như cửa ra vào, cửa sổ, khe hở và khu vực thoát nước. Không để cửa mở không cần thiết và cần xử lý các vị trí có nguy cơ theo quy định của cửa hàng.\n\n## 3. Không tạo thức ăn và nơi trú ẩn cho chúng\n- Không để thức ăn thừa hoặc rác tồn đọng.\n- Vệ sinh khu vực làm việc thường xuyên.\n- Quản lý rác trong thùng chứa phù hợp.\n- Giữ khu vực kho và bếp gọn gàng, sạch sẽ.\n\n## 4. Khi phát hiện dấu hiệu bất thường\nNếu thấy gián, chuột, phân chuột, dấu cắn phá hoặc dấu hiệu khác, cần báo cho người phụ trách và thực hiện biện pháp xử lý phù hợp. Không nên bỏ qua.\n\n## 5. Chú ý khi dùng thuốc diệt côn trùng\nThuốc hoặc hóa chất sử dụng không đúng cách có thể làm nhiễm thực phẩm. Phải tuân thủ phương pháp đã quy định và tránh để thuốc tiếp xúc với thực phẩm hoặc dụng cụ chế biến.\n\n## Ví dụ thực tế\nNhân viên phát hiện dấu phân chuột gần kho nguyên liệu nhưng chỉ quét đi và không báo cáo. Đây là cách xử lý không phù hợp vì cần tìm nguyên nhân, đường xâm nhập và thực hiện biện pháp phòng chống.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ khi thi:\n• ゴキブリ・ハエ・ネズミ = các đối tượng gây hại thường gặp.\n• Phòng chống bắt đầu từ việc không cho xâm nhập và không tạo nguồn thức ăn/nơi trú ẩn.\n• 食品やごみを放置しない = không để thực phẩm/rác tồn đọng.\n• Phát hiện dấu hiệu bất thường → báo 責任者 và xử lý phù hợp.\n• Thuốc diệt côn trùng không được làm nhiễm thực phẩm hoặc dụng cụ.\n• Câu tình huống thường hỏi cách phòng ngừa, quản lý rác hoặc cách xử lý khi phát hiện dấu vết chuột/côn trùng.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 10,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>害虫<rt>がいちゅう</rt></ruby>・<ruby>害獣<rt>がいじゅう</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐために<ruby>重要<rt>じゅうよう</rt></ruby>なことはどれですか。','Điều nào quan trọng để phòng côn trùng và động vật gây hại?','侵入させない','食品を床に置く','ごみを放置する','A','Ngăn chúng xâm nhập là một biện pháp phòng ngừa cơ bản.'),
        ('ゴキブリやネズミの<ruby>餌<rt>えさ</rt></ruby>を<ruby>作<rt>つく</rt></ruby>らないために、どうしますか。','Làm gì để không tạo nguồn thức ăn cho gián và chuột?','食品やごみを放置しない','食べ残しを一晩置く','ごみ箱を開けたままにする','A','Không để thức ăn hoặc rác tồn đọng giúp giảm nguồn thức ăn của sinh vật gây hại.'),
        ('<ruby>倉庫<rt>そうこ</rt></ruby>でネズミの<ruby>痕跡<rt>こんせき</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけたとき、どうしますか。','Khi phát hiện dấu vết chuột trong kho nên làm gì?','責任者に報告して適切に対応する','何もせず放置する','食品の近くに隠す','A','Cần báo cáo và xử lý nguyên nhân cũng như nguy cơ xâm nhập.'),
        ('<ruby>薬剤<rt>やくざい</rt></ruby>を<ruby>使用<rt>しよう</rt></ruby>するときに<ruby>注意<rt>ちゅうい</rt></ruby>することはどれですか。','Khi sử dụng thuốc/hóa chất diệt côn trùng cần chú ý gì?','食品や器具を汚染しない','食品に直接かける','使用方法を守らない','A','Phải sử dụng đúng quy định và tránh làm nhiễm thực phẩm hoặc dụng cụ.'),
        ('<ruby>害虫<rt>がいちゅう</rt></ruby>・<ruby>害獣対策<rt>がいじゅうたいさく</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。','Hành động nào KHÔNG phù hợp để phòng sinh vật gây hại?','清掃してごみを適切に管理する','侵入経路を確認する','生ごみを長時間そのまま放置する','C','Để rác hữu cơ lâu tạo nguồn thức ăn và thu hút côn trùng, động vật gây hại.'),
    ]
    for i, q in enumerate(qs, 1):
        QuickQuestion.objects.create(
            lesson=lesson,
            question_jp=q[0], question_furigana=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0033_add_ginou1_hygiene_lesson9')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
