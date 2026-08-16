from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='refrigerator-freezer-temperature-control',
        defaults={
            'title_jp': '<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>・<ruby>冷凍庫<rt>れいとうこ</rt></ruby>の<ruby>温度管理<rt>おんどかんり</rt></ruby>',
            'title_furigana': '',
            'title_vi': 'Bài 5: Quản lý nhiệt độ tủ lạnh và tủ đông',
            'content_jp': '''<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>保管<rt>ほかん</rt></ruby>するためには、<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>と<ruby>冷凍庫<rt>れいとうこ</rt></ruby>の<ruby>温度<rt>おんど</rt></ruby>を<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>管理<rt>かんり</rt></ruby>することが<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>は10℃<ruby>以下<rt>いか</rt></ruby>、<ruby>冷凍庫<rt>れいとうこ</rt></ruby>は－15℃<ruby>以下<rt>いか</rt></ruby>を<ruby>目安<rt>めやす</rt></ruby>として<ruby>管理<rt>かんり</rt></ruby>します。\n\n<ruby>温度<rt>おんど</rt></ruby>は<ruby>定期的<rt>ていきてき</rt></ruby>に<ruby>確認<rt>かくにん</rt></ruby>し、<ruby>記録<rt>きろく</rt></ruby>します。<ruby>異常<rt>いじょう</rt></ruby>があったときは、<ruby>原因<rt>げんいん</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>して<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>対応<rt>たいおう</rt></ruby>をします。\n\n<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>詰<rt>つ</rt></ruby>め<ruby>込<rt>こ</rt></ruby>みすぎると<ruby>冷気<rt>れいき</rt></ruby>が<ruby>十分<rt>じゅうぶん</rt></ruby>に<ruby>循環<rt>じゅんかん</rt></ruby>しないことがあります。また、<ruby>扉<rt>とびら</rt></ruby>を<ruby>長時間<rt>ちょうじかん</rt></ruby><ruby>開<rt>あ</rt></ruby>けたままにしないようにします。\n\n<ruby>生肉<rt>なまにく</rt></ruby>や<ruby>生魚<rt>なまざかな</rt></ruby>などは、ほかの<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>汚染<rt>おせん</rt></ruby>しないように<ruby>保管方法<rt>ほかんほうほう</rt></ruby>にも<ruby>注意<rt>ちゅうい</rt></ruby>します。''',
            'content_furigana': '',
            'content_vi': '''## 1. Nhiệt độ phải nhớ\nTheo tài liệu học 外食業, mốc quản lý cơ bản cần nhớ là:\n\n- **Tủ lạnh 冷蔵庫: 10°C trở xuống**\n- **Tủ đông 冷凍庫: -15°C trở xuống**\n\nĐây là các con số rất quan trọng khi làm câu hỏi về quản lý vệ sinh.\n\n## 2. Không chỉ nhìn nhiệt độ một lần\nNhiệt độ cần được kiểm tra định kỳ và ghi chép. Nếu phát hiện bất thường, phải kiểm tra nguyên nhân và có biện pháp xử lý phù hợp.\n\n## 3. Không nhồi tủ quá đầy\nNếu cho quá nhiều thực phẩm vào tủ, khí lạnh có thể không lưu thông tốt. Việc mở cửa tủ quá lâu cũng làm nhiệt độ bên trong tăng lên.\n\n## 4. Cách sắp xếp thực phẩm cũng quan trọng\nThịt sống và cá sống phải được bảo quản sao cho dịch hoặc tác nhân gây hại không làm nhiễm thực phẩm khác, đặc biệt là thực phẩm đã chế biến hoặc ăn ngay.\n\n## Ví dụ thực tế\nĐầu ca, nhân viên kiểm tra nhiệt kế của tủ lạnh và thấy 14°C. Không nên chỉ đóng cửa tủ rồi bỏ qua. Cần kiểm tra nguyên nhân, tình trạng thực phẩm và báo cáo/xử lý theo quy định của cửa hàng.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ:\n• 冷蔵庫 = 10°C以下.\n• 冷凍庫 = -15°C以下.\n• Phải kiểm tra và ghi chép nhiệt độ định kỳ.\n• Không nhồi thực phẩm quá đầy và không mở cửa tủ quá lâu.\n• Khi nhiệt độ bất thường phải kiểm tra nguyên nhân và xử lý, không được bỏ qua.\n• Câu tình huống có thể kết hợp quản lý nhiệt độ với phòng ô nhiễm chéo.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 5,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>の<ruby>温度<rt>おんど</rt></ruby>の<ruby>目安<rt>めやす</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。','Mốc nhiệt độ phù hợp của tủ lạnh là gì?','10℃以下','20℃以下','30℃以下','A','Tủ lạnh cần nhớ mốc 10°C trở xuống.'),
        ('<ruby>冷凍庫<rt>れいとうこ</rt></ruby>の<ruby>温度<rt>おんど</rt></ruby>の<ruby>目安<rt>めやす</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。','Mốc nhiệt độ phù hợp của tủ đông là gì?','0℃以下','－15℃以下','10℃以下','B','Tủ đông cần nhớ mốc -15°C trở xuống.'),
        ('<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>の<ruby>温度<rt>おんど</rt></ruby>に<ruby>異常<rt>いじょう</rt></ruby>があったとき、どうしますか。','Khi nhiệt độ tủ lạnh bất thường nên làm gì?','そのままにする','原因を確認して必要な対応をする','扉を開けたままにする','B','Phải xác định nguyên nhân và xử lý phù hợp.'),
        ('<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>に<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>詰<rt>つ</rt></ruby>め<ruby>込<rt>こ</rt></ruby>みすぎると、どのような<ruby>問題<rt>もんだい</rt></ruby>がありますか。','Nhồi tủ lạnh quá đầy có thể gây vấn đề gì?','冷気が循環しにくくなる','必ず温度が下がる','食品が自動的に消毒される','A','Quá đầy có thể cản trở sự lưu thông của khí lạnh.'),
        ('<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>保管<rt>ほかん</rt></ruby>するときに<ruby>重要<rt>じゅうよう</rt></ruby>なことはどれですか。','Điều gì quan trọng khi bảo quản thịt sống?','他の食品を汚染しないようにする','加熱済み食品の上にそのまま置く','温度を確認しない','A','Phải sắp xếp và chứa đựng sao cho thịt sống không làm nhiễm thực phẩm khác.'),
    ]
    for i,q in enumerate(qs,1):
        QuickQuestion.objects.create(lesson=lesson,question_jp=q[0],question_vi=q[1],option_a=q[2],option_b=q[3],option_c=q[4],correct_answer=q[5],explanation_vi=q[6],order=i)


class Migration(migrations.Migration):
    dependencies = [('study', '0027_add_ginou1_hygiene_lesson4')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
