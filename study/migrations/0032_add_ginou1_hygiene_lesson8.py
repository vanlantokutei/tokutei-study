from django.db import migrations


def add_lesson(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    lesson, _ = Lesson.objects.update_or_create(
        category=category,
        slug='employee-health-management',
        defaults={
            'title_jp': '<ruby>従業員<rt>じゅうぎょういん</rt></ruby>の<ruby>健康管理<rt>けんこうかんり</rt></ruby>',
            'title_furigana': '',
            'title_vi': 'Bài 8: Quản lý sức khỏe nhân viên',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>扱<rt>あつか</rt></ruby>う<ruby>従業員<rt>じゅうぎょういん</rt></ruby>の<ruby>健康状態<rt>けんこうじょうたい</rt></ruby>は、<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐために<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n<ruby>下痢<rt>げり</rt></ruby>、<ruby>嘔吐<rt>おうと</rt></ruby>、<ruby>発熱<rt>はつねつ</rt></ruby>などの<ruby>症状<rt>しょうじょう</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>責任者<rt>せきにんしゃ</rt></ruby>に<ruby>報告<rt>ほうこく</rt></ruby>し、<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>扱<rt>あつか</rt></ruby>う<ruby>作業<rt>さぎょう</rt></ruby>を<ruby>避<rt>さ</rt></ruby>けるなど、<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>対応<rt>たいおう</rt></ruby>することが<ruby>必要<rt>ひつよう</rt></ruby>です。\n\nまた、<ruby>手<rt>て</rt></ruby>や<ruby>指<rt>ゆび</rt></ruby>に<ruby>傷<rt>きず</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>も<ruby>注意<rt>ちゅうい</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。<ruby>傷口<rt>きずぐち</rt></ruby>を<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>保護<rt>ほご</rt></ruby>し、<ruby>必要<rt>ひつよう</rt></ruby>に<ruby>応<rt>おう</rt></ruby>じて<ruby>手袋<rt>てぶくろ</rt></ruby>などを<ruby>使用<rt>しよう</rt></ruby>します。\n\n<ruby>作業前<rt>さぎょうまえ</rt></ruby>には<ruby>自分<rt>じぶん</rt></ruby>の<ruby>体調<rt>たいちょう</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>し、<ruby>異常<rt>いじょう</rt></ruby>があるときは<ruby>自己判断<rt>じこはんだん</rt></ruby>で<ruby>隠<rt>かく</rt></ruby>さず、<ruby>責任者<rt>せきにんしゃ</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えることが<ruby>大切<rt>たいせつ</rt></ruby>です。''',
            'content_furigana': '',
            'content_vi': '''## 1. Vì sao phải quản lý sức khỏe nhân viên?\nNgười trực tiếp xử lý thực phẩm có thể trở thành nguồn làm lây vi khuẩn hoặc virus sang món ăn. Vì vậy, kiểm tra tình trạng sức khỏe trước khi làm việc là một phần quan trọng của quản lý vệ sinh.\n\n## 2. Những triệu chứng phải đặc biệt chú ý\n- Tiêu chảy.\n- Nôn ói.\n- Sốt hoặc tình trạng sức khỏe bất thường có nguy cơ ảnh hưởng đến an toàn thực phẩm.\n\nKhi có các triệu chứng này, nhân viên cần báo cho người phụ trách và không được tự ý tiếp tục công việc trực tiếp xử lý thực phẩm nếu chưa có cách xử lý phù hợp.\n\n## 3. Khi tay hoặc ngón tay có vết thương\nVết thương ở tay có thể trở thành nguy cơ làm nhiễm thực phẩm. Cần bảo vệ vết thương đúng cách và sử dụng biện pháp phù hợp như găng tay khi cần thiết.\n\n## 4. Không che giấu tình trạng sức khỏe\nTrước khi bắt đầu ca làm, cần tự kiểm tra sức khỏe. Nếu có bất thường phải báo ngay cho người phụ trách để quyết định công việc phù hợp.\n\n## Ví dụ thực tế\nMột nhân viên bị tiêu chảy nhưng không báo và vẫn tiếp tục chia món ăn trực tiếp. Đây là hành động không phù hợp trong quản lý vệ sinh.''',
            'exam_notes_vi': '''⭐ Điểm cần nhớ khi thi:\n• 下痢・嘔吐・発熱 → nghĩ ngay đến báo cáo tình trạng sức khỏe.\n• Có triệu chứng bất thường không nên tự ý tiếp tục xử lý thực phẩm.\n• 手や指の傷 → phải bảo vệ vết thương đúng cách.\n• Nhân viên phải kiểm tra sức khỏe trước khi làm việc.\n• Không che giấu triệu chứng; cần báo cho 責任者.\n• Câu tình huống thường hỏi hành động nào phù hợp khi nhân viên có triệu chứng hoặc có vết thương ở tay.''',
            'source_title': '日本フードサービス協会 外食業 特定技能1号 学習用テキスト「衛生管理」',
            'source_url': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
            'order': 8,
            'is_published': True,
        },
    )

    QuickQuestion.objects.filter(lesson=lesson).delete()
    qs = [
        ('<ruby>従業員<rt>じゅうぎょういん</rt></ruby>に<ruby>下痢<rt>げり</rt></ruby>や<ruby>嘔吐<rt>おうと</rt></ruby>の<ruby>症状<rt>しょうじょう</rt></ruby>があるとき、まずどうしますか。','Khi nhân viên bị tiêu chảy hoặc nôn ói, trước tiên nên làm gì?','責任者に報告する','何も言わず調理を続ける','お客様に直接聞く','A','Khi có triệu chứng bất thường cần báo cho người phụ trách để có cách xử lý phù hợp.'),
        ('<ruby>体調不良<rt>たいちょうふりょう</rt></ruby>の<ruby>従業員<rt>じゅうぎょういん</rt></ruby>が<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>扱<rt>あつか</rt></ruby>うことについて、<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>考<rt>かんが</rt></ruby>えはどれですか。','Nhân viên đang có triệu chứng sức khỏe bất thường có nên trực tiếp xử lý thực phẩm không?','責任者に報告し適切に対応する','必ずそのまま作業する','症状を隠す','A','Không được che giấu triệu chứng; phải báo cáo và bố trí công việc phù hợp.'),
        ('<ruby>手<rt>て</rt></ruby>や<ruby>指<rt>ゆび</rt></ruby>に<ruby>傷<rt>きず</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>、どうしますか。','Khi tay hoặc ngón tay có vết thương nên làm gì?','傷口を適切に保護する','何もしない','食品に直接触れさせる','A','Vết thương phải được bảo vệ đúng cách để giảm nguy cơ làm nhiễm thực phẩm.'),
        ('<ruby>作業前<rt>さぎょうまえ</rt></ruby>に<ruby>従業員<rt>じゅうぎょういん</rt></ruby>が<ruby>確認<rt>かくにん</rt></ruby>するものはどれですか。','Trước khi bắt đầu công việc, nhân viên nên kiểm tra điều gì?','自分の健康状態','店の音楽だけ','客席の色だけ','A','Kiểm tra tình trạng sức khỏe trước ca làm là một phần của quản lý vệ sinh.'),
        ('<ruby>健康管理<rt>けんこうかんり</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。','Hành động nào KHÔNG phù hợp trong quản lý sức khỏe?','異常があれば責任者に報告する','傷を適切に保護する','嘔吐しても隠して食品を扱い続ける','C','Che giấu triệu chứng và tiếp tục xử lý thực phẩm làm tăng nguy cơ mất an toàn vệ sinh.'),
    ]
    for i, q in enumerate(qs, 1):
        QuickQuestion.objects.create(
            lesson=lesson,
            question_jp=q[0], question_furigana=q[0], question_vi=q[1],
            option_a=q[2], option_b=q[3], option_c=q[4],
            correct_answer=q[5], explanation_vi=q[6], order=i,
        )


class Migration(migrations.Migration):
    dependencies = [('study', '0031_add_ginou1_hygiene_lesson7')]
    operations = [migrations.RunPython(add_lesson, migrations.RunPython.noop)]
