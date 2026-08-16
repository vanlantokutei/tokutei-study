from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='food-poisoning-bacteria-viruses',
        defaults={
            'title_jp': '食中毒の原因となる細菌・ウイルス',
            'title_furigana': 'しょくちゅうどく の げんいん と なる さいきん・ういるす',
            'title_vi': 'Bài 3: Vi khuẩn và virus gây ngộ độc thực phẩm',
            'content_jp': '''【学習ポイント】\n食中毒の原因には、細菌やウイルスなどがあります。原因ごとに特徴が違うため、食品の取扱い、手洗い、加熱、器具の洗浄・消毒などを正しく行うことが重要です。\n\n代表的なものとして、カンピロバクター、サルモネラ属菌、腸管出血性大腸菌、黄色ブドウ球菌、ノロウイルスなどがあります。\n\nカンピロバクターは鶏肉などの取扱いで注意が必要です。生や加熱不十分な肉を避け、器具を通した二次汚染にも注意します。\n\nサルモネラ属菌は卵や食肉などの取扱いで注意し、適切な保管と加熱を行います。\n\n腸管出血性大腸菌は少ない菌量でも問題になることがあるため、衛生的な取扱いと十分な加熱が重要です。\n\n黄色ブドウ球菌は人の手などを介して食品に付着することがあります。手洗い、傷の管理、食品に直接触れない工夫が重要です。\n\nノロウイルスでは、感染した人から食品や環境を介して広がることがあります。体調管理、正しい手洗い、適切な消毒などが重要です。''',
            'content_furigana': '''【がくしゅうポイント】\nしょくちゅうどく の げんいん には、さいきん や ウイルス などが あります。\nだいひょうてきな ものは、カンピロバクター、サルモネラぞくきん、ちょうかんしゅっけつせいだいちょうきん、おうしょくブドウきゅうきん、ノロウイルス などです。\n\nにく や たまご などは てきせつに ほかんし、ひつような しょくひん は じゅうぶんに かねつします。てあらい、きぐ の せんじょう・しょうどく、にじおせん の ぼうし も たいせつです。''',
            'content_vi': '''## 1. Không phải mọi ngộ độc đều có cùng nguyên nhân\nTrong nhà hàng, cần phân biệt **vi khuẩn (細菌)** và **virus (ウイルス)** vì đặc điểm và biện pháp phòng ngừa có thể khác nhau.\n\n## 2. Những tác nhân quan trọng cần nhận biết\n**カンピロバクター – Campylobacter**\nThường cần đặc biệt chú ý khi xử lý thịt gia cầm. Tránh ăn/phục vụ thịt sống hoặc chưa được gia nhiệt đầy đủ và phải phòng ô nhiễm chéo từ dao, thớt, tay.\n\n**サルモネラ属菌 – Salmonella**\nCần chú ý khi xử lý trứng và thịt. Bảo quản phù hợp và gia nhiệt đúng cách là những biện pháp quan trọng.\n\n**腸管出血性大腸菌（ちょうかんしゅっけつせいだいちょうきん）**\nLà nhóm E. coli có thể gây bệnh nghiêm trọng. Cần xử lý thực phẩm vệ sinh và gia nhiệt thích hợp.\n\n**黄色ブドウ球菌（おうしょくブドウきゅうきん）– Tụ cầu vàng**\nCó thể truyền từ con người sang thực phẩm qua tay. Vì vậy rửa tay, quản lý vết thương ở tay và hạn chế tiếp xúc trực tiếp với thực phẩm là rất quan trọng.\n\n**ノロウイルス – Norovirus**\nCó thể lây lan từ người nhiễm bệnh qua thực phẩm hoặc môi trường. Nhân viên cần quản lý sức khỏe, rửa tay đúng cách và thực hiện vệ sinh/khử trùng phù hợp.\n\n## 3. Cách học để làm câu tình huống\nĐừng chỉ học tên. Hãy nối **tác nhân → thực phẩm/nguồn cần chú ý → cách phòng ngừa**.\n\nVí dụ: nhân viên vừa cắt thịt gà sống rồi dùng cùng dụng cụ cho món ăn sẵn. Hãy nghĩ đến nguy cơ từ thịt gia cầm và **二次汚染 – ô nhiễm thứ cấp/chéo**.''',
            'exam_notes_vi': '''Điểm cần nhớ khi thi:\n• カンピロバクター: đặc biệt chú ý thịt gia cầm và gia nhiệt không đầy đủ.\n• サルモネラ属菌: chú ý trứng, thịt và quản lý bảo quản/gia nhiệt.\n• 腸管出血性大腸菌: xử lý vệ sinh và gia nhiệt thích hợp rất quan trọng.\n• 黄色ブドウ球菌: liên hệ với tay/người chế biến và quản lý vết thương.\n• ノロウイルス: nhớ quản lý sức khỏe nhân viên + rửa tay + vệ sinh/khử trùng.\n• Câu thi tình huống thường yêu cầu chọn biện pháp phòng ngừa phù hợp chứ không chỉ hỏi tên tác nhân.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 3,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    questions = [
        ('鶏肉の取扱いで特に注意する食中毒の原因として適切なものはどれですか。', 'Khi xử lý thịt gia cầm, tác nhân nào cần đặc biệt chú ý?', 'カンピロバクター', '花粉', '砂糖', 'A', 'Campylobacter là một tác nhân quan trọng cần chú ý khi xử lý thịt gia cầm.'),
        ('人の手などを介して食品に付着することがあるものはどれですか。', 'Tác nhân nào có thể bám vào thực phẩm thông qua tay người?', '黄色ブドウ球菌', '水', '塩', 'A', '黄色ブドウ球菌 có thể liên quan đến tay/người chế biến, nên vệ sinh tay và quản lý vết thương rất quan trọng.'),
        ('ノロウイルス対策として重要なものはどれですか。', 'Biện pháp nào quan trọng để phòng Norovirus?', '体調管理と正しい手洗い', '食品を長く室温に置く', '手を洗わない', 'A', 'Quản lý sức khỏe và rửa tay đúng cách là các biện pháp quan trọng.'),
        ('生肉に使った器具から他の食品に原因物質が移ることを何と考えますか。', 'Tác nhân từ dụng cụ dùng cho thịt sống truyền sang thực phẩm khác được xem là gì?', '二次汚染', '予約', '会計', 'A', 'Đây là nguy cơ 二次汚染, cần quản lý dao, thớt và các dụng cụ đúng cách.'),
        ('食中毒対策として不適切なものはどれですか。', 'Biện pháp nào KHÔNG phù hợp để phòng ngộ độc?', '必要な食品を適切に加熱する', '手洗いを正しく行う', '生肉用の器具を洗わずそのまま使う', 'C', 'Dùng lại dụng cụ tiếp xúc thịt sống mà không rửa có thể gây ô nhiễm chéo.'),
    ]
    for i, q in enumerate(questions, 1):
        QuickQuestion.objects.create(
            lesson=lesson, question_jp=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0025_add_ginou1_hygiene_lesson2')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
