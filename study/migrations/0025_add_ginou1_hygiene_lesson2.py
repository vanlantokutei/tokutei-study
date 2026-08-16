from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')

    category = LearningCategory.objects.get(slug='hygiene-controls')
    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='three-principles-food-poisoning-prevention',
        defaults={
            'title_jp': '食中毒予防の3原則',
            'title_furigana': 'しょくちゅうどく よぼう の さんげんそく',
            'title_vi': 'Bài 2: 3 nguyên tắc phòng ngộ độc thực phẩm',
            'content_jp': '''【学習ポイント】\n食中毒を予防するための基本は「つけない」「増やさない」「やっつける」の3つです。\n\n① つけない\n手や調理器具などを通して、食品に食中毒の原因となる細菌などをつけないようにします。手洗いを正しく行い、肉や魚などに使った器具と、加熱後の食品に使う器具を適切に管理します。\n\n② 増やさない\n細菌は条件がそろうと増えるため、食品を適切な温度で保管し、必要以上に長く室温に置かないことが重要です。\n\n③ やっつける\n加熱が必要な食品は中心部まで適切に加熱します。また、器具などは必要に応じて洗浄・消毒します。\n\nこの3原則は、飲食店で安全な食品を提供するための基本的な考え方です。''',
            'content_furigana': '''【がくしゅうポイント】\nしょくちゅうどく を よぼうする ための きほん は「つけない」「ふやさない」「やっつける」の 3つ です。\n\n① つけない：て や ちょうりきぐ などから、しょくひん に さいきん などを つけない。\n② ふやさない：しょくひん を てきせつな おんど で ほかんし、しつおん に ながく おかない。\n③ やっつける：ひつような しょくひん は ちゅうしんぶ まで てきせつに かねつする。きぐ は せんじょう・しょうどくする。''',
            'content_vi': '''## 1. Ba nguyên tắc phải thuộc\nBa nguyên tắc cơ bản để phòng ngộ độc thực phẩm là:\n\n**つけない – Không để nhiễm/bám vào**\nKhông để vi khuẩn và các tác nhân gây ngộ độc truyền từ tay, dụng cụ hoặc thực phẩm sống sang thực phẩm khác. Rửa tay đúng cách và quản lý riêng dụng cụ là biện pháp rất quan trọng.\n\n**増やさない（ふやさない）– Không để sinh sôi**\nVi khuẩn có thể tăng số lượng khi gặp điều kiện thích hợp. Vì vậy cần bảo quản thực phẩm ở nhiệt độ phù hợp và tránh để thực phẩm ở nhiệt độ phòng lâu hơn cần thiết.\n\n**やっつける – Tiêu diệt/xử lý**\nNhững thực phẩm cần gia nhiệt phải được làm nóng đúng cách đến phần trung tâm. Dụng cụ cũng phải được rửa và khử trùng theo yêu cầu.\n\n## 2. Cách nhớ nhanh khi thi\n- Tay/dụng cụ sạch, tránh lây sang món khác → **つけない**\n- Bảo quản lạnh, không để ngoài lâu → **増やさない**\n- Gia nhiệt, khử trùng → **やっつける**\n\n## 3. Ví dụ thực tế\nBạn cắt thịt gà sống rồi dùng ngay cùng chiếc thớt để cắt rau ăn liền. Đây là nguy cơ làm tác nhân gây hại **bám/truyền sang** thực phẩm khác → liên quan đến nguyên tắc **つけない**.\n\nMột món cần giữ lạnh nhưng bị để ở ngoài quá lâu tạo điều kiện cho vi khuẩn tăng lên → liên quan đến **増やさない**.\n\nGia nhiệt món ăn đúng cách đến bên trong → liên quan đến **やっつける**.''',
            'exam_notes_vi': '''Điểm cần nhớ khi thi:\n• Thuộc đúng thứ tự ý nghĩa: つけない = tránh nhiễm; 増やさない = không cho tăng sinh; やっつける = xử lý/tiêu diệt.\n• Rửa tay và tránh dùng chung dụng cụ bẩn thường liên quan đến つけない.\n• Kiểm soát thời gian và nhiệt độ bảo quản thường liên quan đến 増やさない.\n• Gia nhiệt và khử trùng thường liên quan đến やっつける.\n• Khi gặp câu tình huống, hãy xác định vấn đề thuộc nguyên tắc nào trước rồi mới chọn đáp án.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 2,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    questions = [
        ('食中毒予防の3原則として正しい組み合わせはどれですか。', 'Đâu là bộ 3 nguyên tắc phòng ngộ độc đúng?', 'つけない・増やさない・やっつける', '洗わない・冷やさない・放置する', '見る・聞く・待つ', 'A', 'Ba nguyên tắc cần thuộc là つけない・増やさない・やっつける.'),
        ('生肉を切ったまな板を、そのまま加熱後の食品に使わないことは主にどの原則ですか。', 'Không dùng ngay thớt vừa cắt thịt sống cho thực phẩm đã nấu chín chủ yếu thuộc nguyên tắc nào?', '増やさない', 'つけない', 'やっつける', 'B', 'Mục tiêu là tránh tác nhân từ thịt sống truyền/bám sang thực phẩm khác, nên thuộc つけない.'),
        ('食品を適切な温度で保管することは主にどの原則ですか。', 'Bảo quản thực phẩm ở nhiệt độ phù hợp chủ yếu thuộc nguyên tắc nào?', '増やさない', 'つけない', 'やっつける', 'A', 'Kiểm soát nhiệt độ giúp hạn chế vi khuẩn tăng sinh, nên thuộc 増やさない.'),
        ('食品を中心部まで適切に加熱することは主にどの原則ですか。', 'Gia nhiệt thực phẩm đúng cách tới phần trung tâm chủ yếu thuộc nguyên tắc nào?', 'つけない', '増やさない', 'やっつける', 'C', 'Gia nhiệt thích hợp là biện pháp xử lý tác nhân gây hại, thuộc やっつける.'),
        ('調理前に正しく手を洗う目的として最も適切なものはどれですか。', 'Mục đích phù hợp nhất của việc rửa tay đúng cách trước khi chế biến là gì?', '食品に原因物質をつけないため', '細菌を増やすため', '食品を室温にするため', 'A', 'Rửa tay giúp tránh đưa tác nhân gây hại từ tay sang thực phẩm, tương ứng với つけない.'),
    ]
    for i, q in enumerate(questions, 1):
        QuickQuestion.objects.create(
            lesson=lesson, question_jp=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0024_add_ginou1_hygiene_lesson1')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
