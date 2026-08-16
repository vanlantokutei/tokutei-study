from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')

    category, _ = LearningCategory.objects.get_or_create(
        slug='hygiene-controls',
        defaults={
            'title_jp': '衛生管理',
            'title_vi': 'Quản lý vệ sinh',
            'description_vi': 'Giáo án biên soạn theo tài liệu học 外食業 特定技能1号 của Japan Foodservice Association.',
            'icon': '🧼',
            'order': 1,
        },
    )

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='food-poisoning-basics',
        defaults={
            'title_jp': '食中毒に関する基礎知識',
            'title_furigana': 'しょくちゅうどく に かんする きそちしき',
            'title_vi': 'Bài 1: Kiến thức cơ bản về ngộ độc thực phẩm',
            'content_jp': '''【学習ポイント】\n食中毒は、細菌やウイルスなどが付いた食品を食べることなどによって、下痢、腹痛、発熱、嘔吐などの症状が出ることです。\n\n飲食店では、見た目やにおいだけで食品が安全かどうかを判断できない場合があります。そのため、原材料の受入れ、保管、調理、提供まで衛生管理を続けることが重要です。\n\n食中毒を防ぐためには、原因となるものを食品に「つけない」、食品中で「増やさない」、加熱などで「やっつける」という考え方を理解します。次の授業でこの3原則を詳しく学びます。''',
            'content_furigana': '''【がくしゅうポイント】\nしょくちゅうどく は、さいきん や ウイルス などが ついた しょくひん を たべること などによって、げり、ふくつう、はつねつ、おうと などの しょうじょう が でることです。\n\nいんしょくてん では、みため や におい だけで しょくひん が あんぜん かどうかを はんだん できない ばあい が あります。そのため、げんざいりょう の うけいれ、ほかん、ちょうり、ていきょう まで えいせいかんり を つづけることが じゅうよう です。''',
            'content_vi': '''## 1. Ngộ độc thực phẩm là gì?\nNgộ độc thực phẩm là tình trạng cơ thể xuất hiện các triệu chứng như tiêu chảy, đau bụng, sốt hoặc nôn ói sau khi ăn thực phẩm bị nhiễm tác nhân gây hại như vi khuẩn hoặc virus.\n\n## 2. Vì sao người làm nhà hàng phải học phần này?\nThực phẩm nguy hiểm không phải lúc nào cũng có mùi lạ hoặc nhìn thấy bằng mắt. Vì vậy không được chỉ dựa vào màu sắc, mùi hay cảm giác để kết luận thực phẩm an toàn. Việc quản lý vệ sinh phải được thực hiện xuyên suốt từ lúc nhận nguyên liệu → bảo quản → chế biến → phục vụ khách.\n\n## 3. Các triệu chứng cần nhớ\n- 下痢（げり）: tiêu chảy\n- 腹痛（ふくつう）: đau bụng\n- 発熱（はつねつ）: sốt\n- 嘔吐（おうと）: nôn ói\n\n## 4. Tư duy phòng ngừa quan trọng\nKhi ôn thi, hãy nhớ ba hướng phòng ngộ độc: không để tác nhân gây hại bám vào thực phẩm, không để chúng sinh sôi và xử lý/tiêu diệt chúng bằng phương pháp phù hợp như gia nhiệt. Bài tiếp theo sẽ học kỹ 3 nguyên tắc này.\n\n## Ví dụ tại nhà hàng\nNhân viên vừa xử lý thịt sống rồi dùng cùng tay hoặc dụng cụ để chạm vào món đã chế biến có thể làm tác nhân gây hại truyền sang món ăn. Vì vậy phải tuân thủ quy trình vệ sinh, rửa tay và quản lý dụng cụ đúng cách.''',
            'exam_notes_vi': '''Điểm cần nhớ khi thi:\n• Không kết luận thực phẩm an toàn chỉ vì nhìn hoặc ngửi thấy bình thường.\n• Nhớ các triệu chứng: tiêu chảy, đau bụng, sốt, nôn ói.\n• Nhớ chuỗi quản lý: tiếp nhận nguyên liệu → bảo quản → chế biến → phục vụ.\n• Chuẩn bị cho bài tiếp theo: 3 nguyên tắc phòng ngộ độc = つけない・増やさない・やっつける.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 1,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    questions = [
        ('食中毒の症状として適切なものはどれですか。', 'Triệu chứng nào phù hợp với ngộ độc thực phẩm?', '下痢や腹痛', '髪が長くなる', '視力がよくなる', 'A', '下痢 và 腹痛 là những triệu chứng cần nhớ của ngộ độc thực phẩm.'),
        ('食品は、見た目やにおいが普通なら必ず安全ですか。', 'Nếu thực phẩm nhìn và ngửi bình thường thì có chắc chắn an toàn không?', 'はい、必ず安全です', 'いいえ、安全とは限りません', '温度に関係なく安全です', 'B', 'Không thể chỉ dùng mắt hoặc mùi để xác định thực phẩm có an toàn hay không.'),
        ('飲食店の衛生管理はいつ行いますか。', 'Quản lý vệ sinh trong nhà hàng cần thực hiện khi nào?', '調理するときだけ', '閉店するときだけ', '原材料の受入れから提供まで', 'C', 'Vệ sinh phải được quản lý xuyên suốt từ tiếp nhận nguyên liệu đến khi phục vụ.'),
        ('食中毒予防の考え方に含まれるものはどれですか。', 'Nội dung nào thuộc tư duy phòng ngộ độc?', 'つけない', '放置する', '確認しない', 'A', 'つけない là một trong ba nguyên tắc quan trọng; hai nguyên tắc còn lại là 増やさない và やっつける.'),
        ('嘔吐の意味はどれですか。', '嘔吐 có nghĩa là gì?', 'Sốt', 'Nôn ói', 'Đau đầu', 'B', '嘔吐（おうと） nghĩa là nôn ói.'),
    ]
    for i, q in enumerate(questions, 1):
        QuickQuestion.objects.create(
            lesson=lesson, question_jp=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0023_add_vocabulary_batch_1')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
