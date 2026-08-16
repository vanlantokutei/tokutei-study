from django.db import migrations


def seed_library(apps, schema_editor):
    Category = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')

    starter = [
        {
            'category': ('hygiene-management', '衛生管理', 'Quản lý vệ sinh', '🧼', 1,
                         'Vệ sinh cá nhân, ngộ độc thực phẩm và quản lý theo HACCP.'),
            'lesson': ('hand-washing', '正しい手洗い', 'ただしい てあらい', 'Rửa tay đúng cách',
                       '調理の前、トイレの後、生の肉や魚に触れた後は、正しい方法で手を洗います。手のひら、手の甲、指の間、指先、手首まで洗います。',
                       'ちょうりの まえ、トイレの あと、なまの にくや さかなに ふれた あとは、ただしい ほうほうで てを あらいます。',
                       'Phải rửa tay đúng cách trước khi chế biến, sau khi đi vệ sinh và sau khi chạm vào thịt/cá sống. Rửa đủ lòng bàn tay, mu bàn tay, kẽ và đầu ngón tay, đến cổ tay.',
                       'Đề thi thường hỏi thời điểm phải rửa tay và các vị trí dễ bị bỏ sót. Găng tay không thay thế việc rửa tay.'),
            'question': ('手を洗う必要があるのはいつですか。', 'てを あらう ひつようが あるのは いつですか。', 'Khi nào cần rửa tay?',
                         '生の肉に触れた後', '休憩する前だけ', '店を閉めた後だけ', 'A',
                         'Sau khi chạm vào thịt sống phải rửa tay để tránh nhiễm chéo.'),
        },
        {
            'category': ('food-preparation', '飲食物調理', 'Chế biến đồ ăn, thức uống', '🍳', 2,
                         'Kiến thức sơ chế, gia nhiệt, bảo quản và dụng cụ chế biến.'),
            'lesson': ('heating', '加熱調理', 'かねつ ちょうり', 'Gia nhiệt thực phẩm',
                       '食品は中心部まで十分に加熱します。見た目だけで判断せず、必要な場合は中心温度を測ります。',
                       'しょくひんは ちゅうしんぶまで じゅうぶんに かねつします。みためだけで はんだんせず、ひつような ばあいは ちゅうしんおんどを はかります。',
                       'Thực phẩm phải được gia nhiệt đầy đủ tới phần trung tâm. Không chỉ đánh giá bằng vẻ ngoài; khi cần phải đo nhiệt độ trung tâm.',
                       'Phân biệt nhiệt độ bề mặt với nhiệt độ trung tâm. Câu hỏi thường tập trung vào cách xác nhận thực phẩm đã được gia nhiệt an toàn.'),
            'question': ('加熱が十分か確認する方法として適切なのはどれですか。', 'かねつが じゅうぶんか かくにんする ほうほうとして てきせつなのは どれですか。', 'Cách nào phù hợp để xác nhận gia nhiệt đã đủ?',
                         '色だけを見る', '中心温度を測る', 'においだけを確認する', 'B',
                         'Đo nhiệt độ trung tâm là phương pháp khách quan để xác nhận gia nhiệt.'),
        },
        {
            'category': ('customer-service', '接客全般', 'Phục vụ khách hàng', '🤝', 3,
                         'Tiếp đón, phục vụ, xử lý phàn nàn và an toàn trong cửa hàng.'),
            'lesson': ('greeting', '基本的な接客', 'きほんてきな せっきゃく', 'Phục vụ khách hàng cơ bản',
                       'お客様には明るく挨拶し、注文を正確に確認します。料理を提供するときは、料理名と注意事項を分かりやすく伝えます。',
                       'おきゃくさまには あかるく あいさつし、ちゅうもんを せいかくに かくにんします。りょうりを ていきょうするときは、りょうりめいと ちゅういじこうを わかりやすく つたえます。',
                       'Chào khách niềm nở và xác nhận đơn gọi món chính xác. Khi phục vụ, cần nói rõ tên món và những lưu ý cần thiết.',
                       'Ưu tiên sự chính xác khi nhận món; nếu chưa nghe rõ phải hỏi lại. Không tự đoán yêu cầu của khách.'),
            'question': ('注文が聞き取れなかったとき、どうしますか。', 'ちゅうもんが ききとれなかったとき、どうしますか。', 'Khi không nghe rõ món khách gọi, nên làm gì?',
                         '自分で決める', '聞き返して確認する', '注文を無視する', 'B',
                         'Cần lịch sự hỏi lại và xác nhận để tránh phục vụ sai món.'),
        },
        {
            'category': ('vocabulary', '重要語彙', 'Từ vựng quan trọng', '🗂️', 4,
                         'Từ vựng thường gặp trong giáo trình, nơi làm việc và câu hỏi thi.'),
            'lesson': ('basic-hygiene-words', '衛生管理の基本語彙', 'えいせい かんりの きほん ごい', 'Từ vựng vệ sinh cơ bản',
                       '衛生（えいせい）：sự vệ sinh\n食中毒（しょくちゅうどく）：ngộ độc thực phẩm\n加熱（かねつ）：gia nhiệt\n冷却（れいきゃく）：làm nguội\n交差汚染（こうさおせん）：nhiễm chéo',
                       'えいせい／しょくちゅうどく／かねつ／れいきゃく／こうさおせん',
                       'Hãy học từ theo cặp hành động và nguy cơ: gia nhiệt–làm nguội; thực phẩm sống–thực phẩm chín; vệ sinh–nhiễm chéo.',
                       'Nhìn kỹ chữ Hán trong đề. 「加熱」 là gia nhiệt, còn 「冷却」 là làm nguội; đây là hai thao tác khác nhau.'),
            'question': ('「交差汚染」の意味はどれですか。', '「こうさおせん」の いみは どれですか。', '「交差汚染」 có nghĩa là gì?',
                         'Nhiễm chéo', 'Gia nhiệt', 'Chào khách', 'A',
                         '交差汚染（こうさおせん） nghĩa là nhiễm chéo.'),
        },
    ]

    for item in starter:
        slug, title_jp, title_vi, icon, order, description = item['category']
        category, _ = Category.objects.update_or_create(slug=slug, defaults={
            'title_jp': title_jp, 'title_vi': title_vi, 'icon': icon,
            'order': order, 'description_vi': description,
        })
        lesson_data = item['lesson']
        lesson, _ = Lesson.objects.update_or_create(category=category, slug=lesson_data[0], defaults={
            'title_jp': lesson_data[1], 'title_furigana': lesson_data[2], 'title_vi': lesson_data[3],
            'content_jp': lesson_data[4], 'content_furigana': lesson_data[5], 'content_vi': lesson_data[6],
            'exam_notes_vi': lesson_data[7], 'order': 1, 'is_published': True,
        })
        question = item['question']
        QuickQuestion.objects.update_or_create(lesson=lesson, order=1, defaults={
            'question_jp': question[0], 'question_furigana': question[1], 'question_vi': question[2],
            'option_a': question[3], 'option_b': question[4], 'option_c': question[5],
            'correct_answer': question[6], 'explanation_vi': question[7],
        })


def remove_starter(apps, schema_editor):
    Category = apps.get_model('study', 'LearningCategory')
    Category.objects.filter(slug__in=[
        'hygiene-management', 'food-preparation', 'customer-service', 'vocabulary'
    ]).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0009_learningcategory_lesson_quickquestion')]
    operations = [migrations.RunPython(seed_library, remove_starter)]
