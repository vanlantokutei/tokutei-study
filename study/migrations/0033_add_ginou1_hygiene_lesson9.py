from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='cleaning-disinfection-equipment',
        defaults={
            'title_jp': '<ruby>器具<rt>きぐ</rt></ruby>・<ruby>設備<rt>せつび</rt></ruby>の<ruby>洗浄<rt>せんじょう</rt></ruby>と<ruby>消毒<rt>しょうどく</rt></ruby>',
            'title_furigana': '',
            'title_vi': 'Bài 9: Vệ sinh và khử trùng dụng cụ, thiết bị',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>包丁<rt>ほうちょう</rt></ruby>、まな<ruby>板<rt>いた</rt></ruby>、<ruby>調理器具<rt>ちょうりきぐ</rt></ruby>、<ruby>作業台<rt>さぎょうだい</rt></ruby>などを<ruby>清潔<rt>せいけつ</rt></ruby>に<ruby>保<rt>たも</rt></ruby>つことは、<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>や<ruby>二次汚染<rt>にじおせん</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐために<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n<ruby>洗浄<rt>せんじょう</rt></ruby>では、<ruby>食品<rt>しょくひん</rt></ruby>の<ruby>残<rt>のこ</rt></ruby>りや<ruby>油<rt>あぶら</rt></ruby>、<ruby>汚<rt>よご</rt></ruby>れなどを<ruby>取<rt>と</rt></ruby>り<ruby>除<rt>のぞ</rt></ruby>きます。<ruby>必要<rt>ひつよう</rt></ruby>に<ruby>応<rt>おう</rt></ruby>じて<ruby>洗剤<rt>せんざい</rt></ruby>を<ruby>使<rt>つか</rt></ruby>い、<ruby>十分<rt>じゅうぶん</rt></ruby>にすすぎます。\n\n<ruby>消毒<rt>しょうどく</rt></ruby>は、<ruby>洗浄<rt>せんじょう</rt></ruby>した<ruby>器具<rt>きぐ</rt></ruby>などに<ruby>残<rt>のこ</rt></ruby>る<ruby>微生物<rt>びせいぶつ</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らすために<ruby>行<rt>おこな</rt></ruby>います。<ruby>汚<rt>よご</rt></ruby>れが<ruby>残<rt>のこ</rt></ruby>ったままでは<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>消毒<rt>しょうどく</rt></ruby>ができないことがあるため、<ruby>先<rt>さき</rt></ruby>に<ruby>洗浄<rt>せんじょう</rt></ruby>することが<ruby>大切<rt>たいせつ</rt></ruby>です。\n\n<ruby>洗浄<rt>せんじょう</rt></ruby>・<ruby>消毒後<rt>しょうどくご</rt></ruby>の<ruby>器具<rt>きぐ</rt></ruby>は、<ruby>再<rt>ふたた</rt></ruby>び<ruby>汚染<rt>おせん</rt></ruby>されないように<ruby>清潔<rt>せいけつ</rt></ruby>な<ruby>場所<rt>ばしょ</rt></ruby>で<ruby>保管<rt>ほかん</rt></ruby>します。\n\n<ruby>設備<rt>せつび</rt></ruby>や<ruby>作業場所<rt>さぎょうばしょ</rt></ruby>も<ruby>決<rt>き</rt></ruby>められた<ruby>方法<rt>ほうほう</rt></ruby>と<ruby>頻度<rt>ひんど</rt></ruby>で<ruby>清掃<rt>せいそう</rt></ruby>し、<ruby>清潔<rt>せいけつ</rt></ruby>な<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>維持<rt>いじ</rt></ruby>します。''',
            'content_furigana': '',
            'content_vi': '''## 1. Phân biệt 洗浄 và 消毒\n**洗浄 (せんじょう)** là làm sạch: loại bỏ thức ăn thừa, dầu mỡ và chất bẩn khỏi dao, thớt, dụng cụ hoặc thiết bị.\n\n**消毒 (しょうどく)** là khử trùng: giảm vi sinh vật còn lại sau khi đã làm sạch.\n\nĐiểm quan trọng: không nên nghĩ rằng chỉ xịt chất khử trùng lên một dụng cụ còn đầy dầu mỡ là đủ. Trước tiên phải làm sạch đúng cách.\n\n## 2. Trình tự cơ bản\nLoại bỏ chất bẩn → rửa bằng phương pháp phù hợp → tráng sạch → khử trùng khi cần → làm khô/bảo quản sạch.\n\n## 3. Sau khi vệ sinh xong vẫn phải chú ý\nDụng cụ sạch nếu đặt lại vào nơi bẩn thì có thể bị nhiễm lại. Vì vậy cần bảo quản tại vị trí sạch và tránh tiếp xúc với nguồn ô nhiễm.\n\n## 4. Không chỉ dao và thớt\nBàn thao tác, máy móc, thiết bị và khu vực chế biến cũng phải được vệ sinh theo phương pháp và tần suất đã quy định.\n\n## Ví dụ thực tế\nMột chiếc thớt vừa dùng cho thịt sống còn dính chất bẩn. Nhân viên chỉ xịt chất khử trùng rồi dùng ngay cho thực phẩm ăn sẵn. Cách làm này không phù hợp vì bước làm sạch chưa được thực hiện đầy đủ.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ khi thi:\n• 洗浄 = loại bỏ chất bẩn.\n• 消毒 = giảm vi sinh vật bằng phương pháp phù hợp.\n• Cơ bản phải làm sạch trước rồi mới khử trùng khi cần.\n• Dao, thớt, dụng cụ và bàn thao tác đều phải được quản lý vệ sinh.\n• Sau khi làm sạch phải bảo quản sao cho không bị tái nhiễm.\n• Câu tình huống thường hỏi thứ tự 洗浄 → 消毒 hoặc hành động nào gây 二次汚染.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 9,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>洗浄<rt>せんじょう</rt></ruby>の<ruby>主<rt>おも</rt></ruby>な<ruby>目的<rt>もくてき</rt></ruby>はどれですか。','Mục đích chính của 洗浄 là gì?','食品の残りや油、汚れを取り除く','売上を計算する','予約を確認する','A','洗浄 là quá trình loại bỏ chất bẩn, thức ăn thừa và dầu mỡ.'),
        ('<ruby>器具<rt>きぐ</rt></ruby>に<ruby>汚<rt>よご</rt></ruby>れが<ruby>残<rt>のこ</rt></ruby>っているとき、<ruby>消毒<rt>しょうどく</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしますか。','Khi dụng cụ còn bẩn, trước khi khử trùng cần làm gì?','適切に洗浄する','そのまま保管する','何もしない','A','Cần loại bỏ chất bẩn bằng cách làm sạch phù hợp trước khi khử trùng.'),
        ('<ruby>洗浄<rt>せんじょう</rt></ruby>・<ruby>消毒後<rt>しょうどくご</rt></ruby>の<ruby>器具<rt>きぐ</rt></ruby>はどこに<ruby>保管<rt>ほかん</rt></ruby>しますか。','Sau khi làm sạch và khử trùng, dụng cụ nên được bảo quản ở đâu?','清潔な場所','床の上','生肉の汁がかかる場所','A','Dụng cụ sạch phải được bảo quản ở nơi sạch để tránh tái nhiễm.'),
        ('<ruby>作業台<rt>さぎょうだい</rt></ruby>や<ruby>設備<rt>せつび</rt></ruby>の<ruby>管理<rt>かんり</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。','Cách quản lý bàn thao tác và thiết bị nào phù hợp?','決められた方法と頻度で清掃する','汚れていても放置する','一度も清掃しない','A','Khu vực và thiết bị phải được vệ sinh theo phương pháp và tần suất phù hợp.'),
        ('<ruby>衛生管理<rt>えいせいかんり</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。','Hành động nào KHÔNG phù hợp trong quản lý vệ sinh dụng cụ?','汚れを落としてから必要な消毒をする','清潔な場所に器具を保管する','生肉を切った汚れたまな板をそのままサラダに使う','C','Dùng thớt bẩn từ thịt sống trực tiếp cho salad có nguy cơ gây ô nhiễm chéo.'),
    ]
    for i, q in enumerate(qs, 1):
        QuickQuestion.objects.create(
            lesson=lesson,
            question_jp=q[0], question_furigana=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0032_add_ginou1_hygiene_lesson8')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
