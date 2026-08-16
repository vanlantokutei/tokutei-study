from django.db import migrations


SOURCES = {
    'hygiene': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_hygiene_controls_text_ja_v1.2.pdf',
    'cooking': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/jf_preparation_of_food_and_drink_text_ja_v1.1.pdf',
    'service': 'https://www.jfnet.or.jp/wp/wp-content/uploads/2025/09/230808jf_customer_service_text_ja_v1.1.pdf',
}

# (môn thi, nhóm phụ, tiếng Nhật, furigana, nghĩa tiếng Việt)
NEW_WORDS = [
    ('hygiene', 'food_poisoning', '汚染', 'おせん', 'ô nhiễm; nhiễm bẩn'),
    ('hygiene', 'food_poisoning', '防止', 'ぼうし', 'ngăn ngừa'),
    ('hygiene', 'core', '確認', 'かくにん', 'xác nhận; kiểm tra'),
    ('hygiene', 'core', '実施', 'じっし', 'thực hiện'),
    ('hygiene', 'food_poisoning', '生息', 'せいそく', 'sinh sống; tồn tại'),
    ('hygiene', 'food_poisoning', '芽胞', 'がほう', 'bào tử'),
    ('hygiene', 'food_poisoning', '酸素', 'さんそ', 'ôxy'),
    ('hygiene', 'food_poisoning', '感染源', 'かんせんげん', 'nguồn lây nhiễm'),
    ('hygiene', 'food_poisoning', '発生要因', 'はっせいよういん', 'yếu tố phát sinh'),
    ('hygiene', 'food_poisoning', '原因物質', 'げんいんぶっしつ', 'chất gây bệnh; tác nhân'),
    ('hygiene', 'food_poisoning', '化学物質', 'かがくぶっしつ', 'hóa chất'),
    ('hygiene', 'food_poisoning', '殺虫剤', 'さっちゅうざい', 'thuốc diệt côn trùng'),
    ('hygiene', 'food_poisoning', '農薬', 'のうやく', 'thuốc bảo vệ thực vật'),
    ('hygiene', 'food_poisoning', 'ガラス片', 'がらすへん', 'mảnh kính'),
    ('hygiene', 'food_poisoning', '金属片', 'きんぞくへん', 'mảnh kim loại'),
    ('hygiene', 'food_poisoning', '雑菌', 'ざっきん', 'tạp khuẩn'),
    ('hygiene', 'workplace_safety', '区別', 'くべつ', 'phân biệt; dùng riêng'),
    ('hygiene', 'temperature_numbers', '期限', 'きげん', 'thời hạn'),
    ('hygiene', 'temperature_numbers', '冷蔵', 'れいぞう', 'bảo quản lạnh'),
    ('hygiene', 'temperature_numbers', '冷凍', 'れいとう', 'đông lạnh'),
    ('hygiene', 'temperature_numbers', '常温', 'じょうおん', 'nhiệt độ thường'),
    ('hygiene', 'temperature_numbers', '庫内温度', 'こないおんど', 'nhiệt độ bên trong tủ'),
    ('hygiene', 'store_operations', '先入れ先出し', 'さきいれさきだし', 'nhập trước xuất trước'),
    ('hygiene', 'store_operations', '検品', 'けんぴん', 'kiểm tra hàng hóa'),
    ('hygiene', 'store_operations', '外観', 'がいかん', 'hình thức bên ngoài'),
    ('hygiene', 'store_operations', 'におい', 'におい', 'mùi'),
    ('hygiene', 'store_operations', '包装', 'ほうそう', 'bao bì; đóng gói'),
    ('hygiene', 'store_operations', '破損', 'はそん', 'hư hỏng; vỡ'),
    ('hygiene', 'workplace_safety', '汚れ', 'よごれ', 'vết bẩn'),
    ('hygiene', 'food_poisoning', 'ふん便', 'ふんべん', 'phân'),
    ('hygiene', 'food_poisoning', '傷口', 'きずぐち', 'vết thương'),
    ('hygiene', 'workplace_safety', '手袋', 'てぶくろ', 'găng tay'),
    ('hygiene', 'workplace_safety', 'マスク', 'ますく', 'khẩu trang'),
    ('hygiene', 'workplace_safety', '帽子', 'ぼうし', 'mũ'),
    ('hygiene', 'workplace_safety', '爪', 'つめ', 'móng tay'),
    ('hygiene', 'workplace_safety', '毛髪', 'もうはつ', 'tóc'),
    ('hygiene', 'workplace_safety', '害虫', 'がいちゅう', 'côn trùng gây hại'),
    ('hygiene', 'workplace_safety', 'ねずみ', 'ねずみ', 'chuột'),
    ('hygiene', 'workplace_safety', '排水溝', 'はいすいこう', 'rãnh thoát nước'),
    ('hygiene', 'workplace_safety', 'ゴミ箱', 'ごみばこ', 'thùng rác'),
    ('hygiene', 'workplace_safety', '洗剤', 'せんざい', 'chất tẩy rửa'),
    ('hygiene', 'temperature_numbers', '濃度', 'のうど', 'nồng độ'),
    ('hygiene', 'workplace_safety', '清潔', 'せいけつ', 'sạch sẽ'),
    ('hygiene', 'workplace_safety', '不潔', 'ふけつ', 'mất vệ sinh'),

    ('cooking', 'core', '調理', 'ちょうり', 'nấu ăn; chế biến'),
    ('cooking', 'workplace_safety', '調理場', 'ちょうりば', 'khu vực bếp'),
    ('cooking', 'practical_planning', '調理工程', 'ちょうりこうてい', 'quy trình chế biến'),
    ('cooking', 'practical_planning', 'レシピ', 'れしぴ', 'công thức món ăn'),
    ('cooking', 'practical_planning', '分量', 'ぶんりょう', 'lượng; định lượng'),
    ('cooking', 'practical_planning', '献立', 'こんだて', 'thực đơn; kế hoạch món ăn'),
    ('cooking', 'practical_planning', '仕込み', 'しこみ', 'chuẩn bị nguyên liệu trước'),
    ('cooking', 'cooking_actions', '加工', 'かこう', 'gia công; chế biến'),
    ('cooking', 'cooking_actions', '冷ます', 'さます', 'làm nguội'),
    ('cooking', 'cooking_actions', '温める', 'あたためる', 'hâm nóng'),
    ('cooking', 'cooking_actions', '漬ける', 'つける', 'ngâm; ướp'),
    ('cooking', 'cooking_actions', '和える', 'あえる', 'trộn với sốt/gia vị'),
    ('cooking', 'cooking_actions', '裏ごし', 'うらごし', 'lọc, nghiền qua rây'),
    ('cooking', 'cooking_actions', '泡立てる', 'あわだてる', 'đánh tạo bọt'),
    ('cooking', 'cooking_actions', '伸ばす', 'のばす', 'cán; kéo dài'),
    ('cooking', 'cooking_actions', '成形', 'せいけい', 'tạo hình'),
    ('cooking', 'cooking_actions', '骨を取る', 'ほねをとる', 'lọc bỏ xương'),
    ('cooking', 'cooking_actions', '筋を切る', 'すじをきる', 'cắt gân thịt'),
    ('cooking', 'cooking_actions', '油を切る', 'あぶらをきる', 'để ráo dầu'),
    ('cooking', 'cooking_actions', '灰汁を取る', 'あくをとる', 'vớt bọt, loại bỏ vị chát'),
    ('cooking', 'cooking_actions', '味付け', 'あじつけ', 'nêm nếm'),
    ('cooking', 'cooking_actions', '味見', 'あじみ', 'nếm thử'),
    ('cooking', 'core', '食感', 'しょっかん', 'kết cấu, cảm giác khi ăn'),
    ('cooking', 'core', '硬い', 'かたい', 'cứng'),
    ('cooking', 'core', '柔らかい', 'やわらかい', 'mềm'),
    ('cooking', 'core', '粘り', 'ねばり', 'độ dính; độ dai'),
    ('cooking', 'core', 'とろみ', 'とろみ', 'độ sánh'),
    ('cooking', 'ingredients_tools', '水分', 'すいぶん', 'lượng nước; độ ẩm'),
    ('cooking', 'ingredients_tools', '油脂', 'ゆし', 'dầu và chất béo'),
    ('cooking', 'ingredients_tools', '肉類', 'にくるい', 'nhóm thịt'),
    ('cooking', 'ingredients_tools', '魚介類', 'ぎょかいるい', 'hải sản'),
    ('cooking', 'ingredients_tools', '野菜類', 'やさいるい', 'nhóm rau củ'),
    ('cooking', 'ingredients_tools', '穀類', 'こくるい', 'ngũ cốc'),
    ('cooking', 'ingredients_tools', '豆類', 'まめるい', 'các loại đậu'),
    ('cooking', 'ingredients_tools', '乳製品', 'にゅうせいひん', 'sản phẩm từ sữa'),
    ('cooking', 'ingredients_tools', '卵類', 'たまごるい', 'nhóm trứng'),
    ('cooking', 'ingredients_tools', '冷凍食品', 'れいとうしょくひん', 'thực phẩm đông lạnh'),
    ('cooking', 'ingredients_tools', '缶詰', 'かんづめ', 'đồ hộp'),
    ('cooking', 'ingredients_tools', 'ボウル', 'ぼうる', 'tô trộn'),
    ('cooking', 'ingredients_tools', 'ざる', 'ざる', 'rổ; rá'),
    ('cooking', 'ingredients_tools', 'おたま', 'おたま', 'muôi; vá'),
    ('cooking', 'ingredients_tools', '菜箸', 'さいばし', 'đũa nấu ăn'),
    ('cooking', 'ingredients_tools', 'トング', 'とんぐ', 'kẹp gắp'),
    ('cooking', 'ingredients_tools', 'へら', 'へら', 'xẻng; phới dẹt'),

    ('service', 'communication', '来店', 'らいてん', 'đến cửa hàng'),
    ('service', 'communication', '退店', 'たいてん', 'rời cửa hàng'),
    ('service', 'communication', '迎える', 'むかえる', 'đón tiếp'),
    ('service', 'communication', '見送る', 'みおくる', 'tiễn khách'),
    ('service', 'store_operations', '席', 'せき', 'chỗ ngồi'),
    ('service', 'store_operations', 'テーブル', 'てーぶる', 'bàn'),
    ('service', 'store_operations', 'カウンター', 'かうんたー', 'quầy; chỗ ngồi tại quầy'),
    ('service', 'communication', 'メニュー', 'めにゅー', 'thực đơn'),
    ('service', 'communication', 'おすすめ', 'おすすめ', 'món được đề xuất'),
    ('service', 'store_operations', '品切れ', 'しなぎれ', 'hết món; hết hàng'),
    ('service', 'communication', '追加注文', 'ついかちゅうもん', 'gọi thêm món'),
    ('service', 'ingredients_tools', '取り皿', 'とりざら', 'đĩa nhỏ chia thức ăn'),
    ('service', 'ingredients_tools', '箸', 'はし', 'đũa'),
    ('service', 'ingredients_tools', 'スプーン', 'すぷーん', 'thìa'),
    ('service', 'ingredients_tools', 'フォーク', 'ふぉーく', 'nĩa'),
    ('service', 'ingredients_tools', 'ナイフ', 'ないふ', 'dao ăn'),
    ('service', 'ingredients_tools', 'おしぼり', 'おしぼり', 'khăn ướt'),
    ('service', 'ingredients_tools', '飲み物', 'のみもの', 'đồ uống'),
    ('service', 'allergy_diversity', '酒類', 'しゅるい', 'đồ uống có cồn'),
    ('service', 'allergy_diversity', 'ビール', 'びーる', 'bia'),
    ('service', 'allergy_diversity', '日本酒', 'にほんしゅ', 'rượu sake Nhật'),
    ('service', 'allergy_diversity', 'ワイン', 'わいん', 'rượu vang'),
    ('service', 'workplace_safety', '酔客', 'すいきゃく', 'khách say rượu'),
    ('service', 'store_operations', '注文ミス', 'ちゅうもんみす', 'sai sót khi nhận món'),
    ('service', 'communication', '待ち時間', 'まちじかん', 'thời gian chờ'),
    ('service', 'communication', '呼び出し', 'よびだし', 'gọi; thông báo gọi'),
    ('service', 'communication', '電話対応', 'でんわたいおう', 'tiếp nhận và xử lý điện thoại'),
    ('service', 'store_operations', '取り消し', 'とりけし', 'hủy bỏ'),
    ('service', 'store_operations', '返品', 'へんぴん', 'trả lại hàng'),
    ('service', 'store_operations', '返金', 'へんきん', 'hoàn tiền'),
    ('service', 'store_operations', '割引', 'わりびき', 'giảm giá'),
    ('service', 'store_operations', '税込', 'ぜいこみ', 'đã gồm thuế'),
    ('service', 'store_operations', '税抜', 'ぜいぬき', 'chưa gồm thuế'),
    ('service', 'store_operations', 'クレジットカード', 'くれじっとかーど', 'thẻ tín dụng'),
    ('service', 'store_operations', '電子マネー', 'でんしまねー', 'tiền điện tử'),
    ('service', 'store_operations', 'レジ', 'れじ', 'quầy/máy tính tiền'),
    ('service', 'store_operations', 'レシート', 'れしーと', 'hóa đơn bán lẻ'),
    ('service', 'store_operations', '売上', 'うりあげ', 'doanh thu'),
    ('service', 'store_operations', '釣銭', 'つりせん', 'tiền lẻ trả lại'),
    ('service', 'ingredients_tools', '食器', 'しょっき', 'bát đĩa, dụng cụ ăn'),
    ('service', 'workplace_safety', '割れ物', 'われもの', 'đồ dễ vỡ'),
    ('service', 'workplace_safety', '火災', 'かさい', 'hỏa hoạn'),
]


def add_words(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    next_order = {
        category: (VocabularyEntry.objects.filter(category=category).order_by('-order').values_list('order', flat=True).first() or 0)
        for category in SOURCES
    }
    for category, topic, word_jp, furigana, meaning_vi in NEW_WORDS:
        next_order[category] += 1
        VocabularyEntry.objects.update_or_create(
            category=category,
            word_jp=word_jp,
            defaults={
                'topic': topic,
                'furigana': furigana,
                'meaning_vi': meaning_vi,
                'order': next_order[category],
                'is_published': True,
                'source_title': '外食業技能測定試験 学習用テキスト - 日本フードサービス協会',
                'source_url': SOURCES[category],
            },
        )


def remove_words(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    for category in SOURCES:
        words = [row[2] for row in NEW_WORDS if row[0] == category]
        VocabularyEntry.objects.filter(category=category, word_jp__in=words).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0016_classify_vocabulary_topics')]
    operations = [migrations.RunPython(add_words, remove_words)]
