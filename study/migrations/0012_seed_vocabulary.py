from django.db import migrations


WORDS = [
    ('hygiene', '衛生', 'えいせい', 'vệ sinh', '衛生管理を徹底します。', 'えいせいかんりを てっていします。', 'Thực hiện triệt để việc quản lý vệ sinh.'),
    ('hygiene', '食中毒', 'しょくちゅうどく', 'ngộ độc thực phẩm', '食中毒を予防します。', 'しょくちゅうどくを よぼうします。', 'Phòng ngừa ngộ độc thực phẩm.'),
    ('hygiene', '交差汚染', 'こうさおせん', 'nhiễm chéo', '交差汚染を防ぎます。', 'こうさおせんを ふせぎます。', 'Ngăn ngừa nhiễm chéo.'),
    ('hygiene', '消毒', 'しょうどく', 'khử trùng', '調理器具を消毒します。', 'ちょうりきぐを しょうどくします。', 'Khử trùng dụng cụ nấu ăn.'),
    ('hygiene', '手洗い', 'てあらい', 'rửa tay', '作業前に手洗いをします。', 'さぎょうまえに てあらいを します。', 'Rửa tay trước khi làm việc.'),
    ('hygiene', '賞味期限', 'しょうみきげん', 'hạn sử dụng ngon nhất', '賞味期限を確認します。', 'しょうみきげんを かくにんします。', 'Kiểm tra hạn dùng ngon nhất.'),
    ('cooking', '加熱', 'かねつ', 'gia nhiệt', '中心部まで加熱します。', 'ちゅうしんぶまで かねつします。', 'Gia nhiệt tới phần trung tâm.'),
    ('cooking', '冷却', 'れいきゃく', 'làm nguội', '食品をすばやく冷却します。', 'しょくひんを すばやく れいきゃくします。', 'Làm nguội thực phẩm nhanh chóng.'),
    ('cooking', '解凍', 'かいとう', 'rã đông', '冷蔵庫で解凍します。', 'れいぞうこで かいとうします。', 'Rã đông trong tủ lạnh.'),
    ('cooking', '下処理', 'したしょり', 'sơ chế', '野菜の下処理をします。', 'やさいの したしょりを します。', 'Sơ chế rau củ.'),
    ('cooking', '中心温度', 'ちゅうしんおんど', 'nhiệt độ trung tâm', '中心温度を測ります。', 'ちゅうしんおんどを はかります。', 'Đo nhiệt độ trung tâm.'),
    ('cooking', '盛り付け', 'もりつけ', 'trình bày món ăn', '料理をきれいに盛り付けます。', 'りょうりを きれいに もりつけます。', 'Trình bày món ăn đẹp mắt.'),
    ('service', '接客', 'せっきゃく', 'phục vụ khách hàng', '丁寧に接客します。', 'ていねいに せっきゃくします。', 'Phục vụ khách hàng lịch sự.'),
    ('service', '注文', 'ちゅうもん', 'gọi món; đơn gọi món', '注文を確認します。', 'ちゅうもんを かくにんします。', 'Xác nhận đơn gọi món.'),
    ('service', '配膳', 'はいぜん', 'bày và phục vụ món', '料理を正しく配膳します。', 'りょうりを ただしく はいぜんします。', 'Phục vụ món ăn đúng cách.'),
    ('service', '会計', 'かいけい', 'thanh toán', 'レジで会計をします。', 'レジで かいけいを します。', 'Thanh toán tại quầy thu ngân.'),
    ('service', '苦情', 'くじょう', 'phàn nàn; khiếu nại', '苦情を責任者に報告します。', 'くじょうを せきにんしゃに ほうこくします。', 'Báo cáo khiếu nại cho người phụ trách.'),
    ('service', '予約', 'よやく', 'đặt chỗ', '電話で予約を受けます。', 'でんわで よやくを うけます。', 'Nhận đặt chỗ qua điện thoại.'),
]


def seed_words(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    category_order = {'hygiene': 0, 'cooking': 0, 'service': 0}
    for category, word, furigana, meaning, example, example_furigana, example_vi in WORDS:
        category_order[category] += 1
        VocabularyEntry.objects.update_or_create(
            category=category, word_jp=word,
            defaults={
                'furigana': furigana, 'meaning_vi': meaning,
                'example_jp': example, 'example_furigana': example_furigana,
                'example_vi': example_vi, 'order': category_order[category],
                'is_published': True,
            },
        )


def remove_words(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    VocabularyEntry.objects.filter(word_jp__in=[word[1] for word in WORDS]).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0011_vocabularyentry')]
    operations = [migrations.RunPython(seed_words, remove_words)]
