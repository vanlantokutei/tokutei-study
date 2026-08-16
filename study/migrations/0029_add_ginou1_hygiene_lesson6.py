from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='cross-contamination-prevention',
        defaults={
            'title_jp': '<ruby>交差汚染<rt>こうさおせん</rt></ruby>・<ruby>二次汚染<rt>にじおせん</rt></ruby>の<ruby>防止<rt>ぼうし</rt></ruby>',
            'title_furigana': '',
            'title_vi': 'Bài 6: Phòng ngừa ô nhiễm chéo và ô nhiễm thứ cấp',
            'content_jp': '''<ruby>生肉<rt>なまにく</rt></ruby>や<ruby>生魚<rt>なまざかな</rt></ruby>などには、<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>となる<ruby>細菌<rt>さいきん</rt></ruby>などが<ruby>付着<rt>ふちゃく</rt></ruby>していることがあります。\n\nそれらが<ruby>手<rt>て</rt></ruby>、<ruby>包丁<rt>ほうちょう</rt></ruby>、まな<ruby>板<rt>いた</rt></ruby>、<ruby>容器<rt>ようき</rt></ruby>などを<ruby>通<rt>とお</rt></ruby>して、ほかの<ruby>食品<rt>しょくひん</rt></ruby>に<ruby>移<rt>うつ</rt></ruby>らないようにすることが<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n<ruby>生<rt>なま</rt></ruby>の<ruby>食品<rt>しょくひん</rt></ruby>と、<ruby>加熱済<rt>かねつず</rt></ruby>みの<ruby>食品<rt>しょくひん</rt></ruby>やそのまま<ruby>食<rt>た</rt></ruby>べる<ruby>食品<rt>しょくひん</rt></ruby>は、できるだけ<ruby>分<rt>わ</rt></ruby>けて<ruby>取<rt>と</rt></ruby>り<ruby>扱<rt>あつか</rt></ruby>います。\n\n<ruby>包丁<rt>ほうちょう</rt></ruby>やまな<ruby>板<rt>いた</rt></ruby>などは、<ruby>用途<rt>ようと</rt></ruby>ごとに<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けるか、<ruby>使用後<rt>しようご</rt></ruby>に<ruby>十分<rt>じゅうぶん</rt></ruby>な<ruby>洗浄<rt>せんじょう</rt></ruby>・<ruby>消毒<rt>しょうどく</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>います。\n\nまた、<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>では<ruby>生肉<rt>なまにく</rt></ruby>や<ruby>生魚<rt>なまざかな</rt></ruby>の<ruby>汁<rt>しる</rt></ruby>が、ほかの<ruby>食品<rt>しょくひん</rt></ruby>にかからないように<ruby>容器<rt>ようき</rt></ruby>などを<ruby>使<rt>つか</rt></ruby>って<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>保管<rt>ほかん</rt></ruby>します。\n\n<ruby>作業<rt>さぎょう</rt></ruby>が<ruby>変<rt>か</rt></ruby>わるときには、<ruby>必要<rt>ひつよう</rt></ruby>に<ruby>応<rt>おう</rt></ruby>じて<ruby>手洗<rt>てあら</rt></ruby>いを<ruby>行<rt>おこな</rt></ruby>い、<ruby>汚染<rt>おせん</rt></ruby>を<ruby>広<rt>ひろ</rt></ruby>げないようにします。''',
            'content_furigana': '',
            'content_vi': '''## 1. Ô nhiễm chéo là gì?\nThịt sống, cá sống hoặc các nguyên liệu chưa xử lý có thể mang vi khuẩn gây ngộ độc. Nếu vi khuẩn truyền qua **tay, dao, thớt, hộp đựng hoặc bề mặt làm việc** sang thực phẩm khác thì có nguy cơ gây ô nhiễm chéo/ô nhiễm thứ cấp.\n\n## 2. Thực phẩm sống và thực phẩm ăn ngay phải tách biệt\nĐặc biệt chú ý không để thực phẩm sống tiếp xúc với:\n- món đã nấu chín;\n- rau hoặc món ăn dùng trực tiếp;\n- dụng cụ sạch dùng cho thực phẩm sau gia nhiệt.\n\n## 3. Dao và thớt\nCách tốt là **phân dụng cụ theo mục đích sử dụng**. Nếu phải dùng lại, cần rửa và khử trùng thích hợp trước khi chuyển sang loại thực phẩm khác.\n\n## 4. Trong tủ lạnh\nKhông để nước/dịch từ thịt hoặc cá sống chảy xuống thực phẩm khác. Nên sử dụng hộp, khay hoặc cách chứa phù hợp để ngăn rò rỉ.\n\n## 5. Tay cũng là đường truyền ô nhiễm\nSau khi chạm vào nguyên liệu sống, rác hoặc vật bẩn, phải rửa tay đúng lúc trước khi tiếp tục xử lý thực phẩm sạch.\n\n## Ví dụ thực tế\nNhân viên cắt thịt gà sống rồi dùng cùng dao để cắt rau ăn ngay mà không rửa/khử trùng. Đây là ví dụ điển hình của nguy cơ **交差汚染・二次汚染**.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ:\n• 生肉・生魚 → đặc biệt chú ý nguồn ô nhiễm.\n• Dao/thớt dùng cho thực phẩm sống không được chuyển thẳng sang thực phẩm đã chín hoặc ăn ngay.\n• Tách dụng cụ hoặc 洗浄・消毒 trước khi dùng lại.\n• Trong tủ lạnh phải ngăn dịch thịt/cá sống làm nhiễm thực phẩm khác.\n• Đổi công việc từ bẩn → sạch phải chú ý rửa tay.\n• Khi gặp câu tình huống, hãy tìm “đường truyền” của vi khuẩn: tay, dao, thớt, hộp, bề mặt hoặc nước dịch thực phẩm.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 6,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>切<rt>き</rt></ruby>ったまな<ruby>板<rt>いた</rt></ruby>を、そのままサラダに<ruby>使<rt>つか</rt></ruby>うと、どのような<ruby>危険<rt>きけん</rt></ruby>がありますか。','Dùng ngay thớt vừa cắt thịt sống để làm salad có nguy cơ gì?','交差汚染','売上増加','予約取消','A','Vi khuẩn từ thịt sống có thể truyền qua thớt sang salad.'),
        ('<ruby>包丁<rt>ほうちょう</rt></ruby>やまな<ruby>板<rt>いた</rt></ruby>の<ruby>管理<rt>かんり</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。','Cách quản lý dao và thớt nào phù hợp?','用途ごとに使い分ける','いつも同じものを洗わず使う','床に置く','A','Phân dụng cụ theo mục đích giúp giảm nguy cơ ô nhiễm chéo.'),
        ('<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>で<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>保管<rt>ほかん</rt></ruby>するとき、<ruby>重要<rt>じゅうよう</rt></ruby>なことはどれですか。','Khi bảo quản thịt sống trong tủ lạnh, điều nào quan trọng?','汁が他の食品にかからないようにする','加熱済み食品に直接のせる','容器を使わない','A','Phải ngăn dịch từ thịt sống làm nhiễm thực phẩm khác.'),
        ('<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>触<rt>さわ</rt></ruby>った<ruby>後<rt>あと</rt></ruby>、<ruby>別<rt>べつ</rt></ruby>の<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>扱<rt>あつか</rt></ruby>う<ruby>前<rt>まえ</rt></ruby>に<ruby>必要<rt>ひつよう</rt></ruby>なことはどれですか。','Sau khi chạm thịt sống, trước khi xử lý thực phẩm khác cần làm gì?','適切に手を洗う','何もしない','手を服で拭くだけ','A','Rửa tay đúng cách giúp ngăn tác nhân truyền từ thực phẩm sống sang thực phẩm khác.'),
        ('<ruby>二次汚染<rt>にじおせん</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐ<ruby>行動<rt>こうどう</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。','Hành động nào KHÔNG phù hợp để phòng ô nhiễm thứ cấp?','器具を洗浄・消毒する','生と加熱済み食品を分ける','生肉用の包丁を洗わずそのまま使う','C','Dùng dao của thịt sống mà không rửa rồi chuyển sang thực phẩm khác làm tăng nguy cơ ô nhiễm.'),
    ]
    for i,q in enumerate(qs,1):
        QuickQuestion.objects.create(lesson=lesson,question_jp=q[0],question_vi=q[1],option_a=q[2],option_b=q[3],option_c=q[4],correct_answer=q[5],explanation_vi=q[6],order=i)


class Migration(migrations.Migration):
    dependencies = [('study', '0028_add_ginou1_hygiene_lesson5')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
