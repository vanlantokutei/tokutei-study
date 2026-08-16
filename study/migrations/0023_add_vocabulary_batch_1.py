from django.db import migrations


WORDS = [
    ('hygiene','food_poisoning','細菌','さいきん','vi khuẩn'),
    ('hygiene','food_poisoning','ウイルス','ういるす','vi-rút'),
    ('hygiene','food_poisoning','寄生虫','きせいちゅう','ký sinh trùng'),
    ('hygiene','food_poisoning','ノロウイルス','のろういるす','Norovirus'),
    ('hygiene','food_poisoning','カンピロバクター','かんぴろばくたー','Campylobacter'),
    ('hygiene','food_poisoning','サルモネラ属菌','さるもねらぞくきん','vi khuẩn Salmonella'),
    ('hygiene','food_poisoning','黄色ブドウ球菌','おうしょくぶどうきゅうきん','tụ cầu vàng'),
    ('hygiene','food_poisoning','腸管出血性大腸菌','ちょうかんしゅっけつせいだいちょうきん','E. coli gây xuất huyết đường ruột'),
    ('hygiene','food_poisoning','潜伏期間','せんぷくきかん','thời gian ủ bệnh'),
    ('hygiene','food_poisoning','嘔吐','おうと','nôn ói'),
    ('hygiene','food_poisoning','下痢','げり','tiêu chảy'),
    ('hygiene','food_poisoning','腹痛','ふくつう','đau bụng'),
    ('hygiene','food_poisoning','発熱','はつねつ','sốt'),
    ('hygiene','food_poisoning','二次汚染','にじおせん','ô nhiễm thứ cấp'),
    ('hygiene','workplace_safety','衛生手袋','えいせいてぶくろ','găng tay vệ sinh'),
    ('hygiene','workplace_safety','作業着','さぎょうぎ','quần áo làm việc'),
    ('hygiene','workplace_safety','健康管理','けんこうかんり','quản lý sức khỏe'),
    ('hygiene','workplace_safety','体調不良','たいちょうふりょう','tình trạng sức khỏe không tốt'),
    ('hygiene','workplace_safety','清掃','せいそう','vệ sinh, lau dọn'),
    ('hygiene','workplace_safety','洗浄','せんじょう','rửa, làm sạch'),
    ('hygiene','workplace_safety','殺菌','さっきん','diệt khuẩn'),
    ('hygiene','workplace_safety','漂白剤','ひょうはくざい','chất tẩy trắng'),
    ('hygiene','store_operations','納品','のうひん','giao hàng, nhập hàng'),
    ('hygiene','store_operations','保管','ほかん','bảo quản'),
    ('hygiene','store_operations','保存','ほぞん','lưu trữ, bảo quản'),
    ('hygiene','temperature_numbers','消費期限','しょうひきげん','hạn sử dụng an toàn'),
    ('hygiene','temperature_numbers','温度管理','おんどかんり','quản lý nhiệt độ'),
    ('hygiene','temperature_numbers','室温','しつおん','nhiệt độ phòng'),
    ('hygiene','temperature_numbers','中心部','ちゅうしんぶ','phần trung tâm'),
    ('hygiene','core','衛生管理計画','えいせいかんりけいかく','kế hoạch quản lý vệ sinh'),

    ('cooking','ingredients_tools','包丁','ほうちょう','dao bếp'),
    ('cooking','ingredients_tools','まな板','まないた','thớt'),
    ('cooking','ingredients_tools','鍋','なべ','nồi'),
    ('cooking','ingredients_tools','フライパン','ふらいぱん','chảo'),
    ('cooking','ingredients_tools','計量器','けいりょうき','dụng cụ cân đo'),
    ('cooking','ingredients_tools','計量カップ','けいりょうかっぷ','cốc đong'),
    ('cooking','ingredients_tools','計量スプーン','けいりょうすぷーん','thìa đong'),
    ('cooking','ingredients_tools','温度計','おんどけい','nhiệt kế'),
    ('cooking','ingredients_tools','冷蔵庫','れいぞうこ','tủ lạnh'),
    ('cooking','ingredients_tools','冷凍庫','れいとうこ','tủ đông'),
    ('cooking','ingredients_tools','調味料','ちょうみりょう','gia vị'),
    ('cooking','ingredients_tools','食材','しょくざい','nguyên liệu thực phẩm'),
    ('cooking','ingredients_tools','生鮮食品','せいせんしょくひん','thực phẩm tươi sống'),
    ('cooking','cooking_actions','切る','きる','cắt'),
    ('cooking','cooking_actions','刻む','きざむ','băm, thái nhỏ'),
    ('cooking','cooking_actions','むく','むく','gọt, bóc vỏ'),
    ('cooking','cooking_actions','洗う','あらう','rửa'),
    ('cooking','cooking_actions','ゆでる','ゆでる','luộc'),
    ('cooking','cooking_actions','煮る','にる','ninh, nấu'),
    ('cooking','cooking_actions','焼く','やく','nướng, áp chảo'),
    ('cooking','cooking_actions','炒める','いためる','xào'),
    ('cooking','cooking_actions','揚げる','あげる','chiên ngập dầu'),
    ('cooking','cooking_actions','蒸す','むす','hấp'),
    ('cooking','cooking_actions','混ぜる','まぜる','trộn'),
    ('cooking','cooking_actions','計量する','けいりょうする','cân, đong'),
    ('cooking','cooking_actions','水切り','みずきり','để ráo nước'),
    ('cooking','cooking_actions','予熱','よねつ','làm nóng trước'),
    ('cooking','cooking_actions','再加熱','さいかねつ','hâm nóng lại'),
    ('cooking','practical_planning','調理時間','ちょうりじかん','thời gian chế biến'),
    ('cooking','practical_planning','作業手順','さぎょうてじゅん','trình tự thao tác'),

    ('service','communication','いらっしゃいませ','いらっしゃいませ','kính chào quý khách'),
    ('service','communication','かしこまりました','かしこまりました','vâng, tôi đã hiểu ạ'),
    ('service','communication','少々お待ちください','しょうしょうおまちください','xin quý khách vui lòng chờ một chút'),
    ('service','communication','お待たせしました','おまたせしました','xin lỗi đã để quý khách chờ'),
    ('service','communication','申し訳ございません','もうしわけございません','thành thật xin lỗi'),
    ('service','communication','ありがとうございました','ありがとうございました','xin cảm ơn quý khách'),
    ('service','communication','ご注文','ごちゅうもん','gọi món, đơn gọi món (lịch sự)'),
    ('service','communication','ご予約','ごよやく','đặt chỗ (lịch sự)'),
    ('service','communication','ご案内','ごあんない','hướng dẫn, đưa khách vào chỗ'),
    ('service','communication','確認いたします','かくにんいたします','tôi xin xác nhận/kiểm tra'),
    ('service','store_operations','レジ','れじ','quầy thu ngân, máy tính tiền'),
    ('service','store_operations','現金','げんきん','tiền mặt'),
    ('service','store_operations','釣り銭','つりせん','tiền thối lại'),
    ('service','store_operations','領収書','りょうしゅうしょ','hóa đơn, biên lai'),
    ('service','store_operations','伝票','でんぴょう','phiếu gọi món, phiếu thanh toán'),
    ('service','store_operations','クレジットカード','くれじっとかーど','thẻ tín dụng'),
    ('service','store_operations','電子マネー','でんしまねー','tiền điện tử'),
    ('service','store_operations','予約席','よやくせき','chỗ đã đặt trước'),
    ('service','store_operations','満席','まんせき','hết chỗ'),
    ('service','store_operations','空席','くうせき','chỗ trống'),
    ('service','communication','人数','にんずう','số người'),
    ('service','communication','お客様','おきゃくさま','quý khách'),
    ('service','communication','責任者','せきにんしゃ','người phụ trách'),
    ('service','communication','謝罪','しゃざい','xin lỗi, tạ lỗi'),
    ('service','communication','説明','せつめい','giải thích'),
    ('service','communication','報告','ほうこく','báo cáo'),
    ('service','communication','連絡','れんらく','liên lạc, thông báo'),
    ('service','allergy_diversity','食物アレルギー','しょくもつあれるぎー','dị ứng thực phẩm'),
    ('service','allergy_diversity','アレルゲン','あれるげん','chất gây dị ứng'),
    ('service','allergy_diversity','特定原材料','とくていげんざいりょう','nguyên liệu gây dị ứng bắt buộc ghi nhãn'),
    ('service','allergy_diversity','宗教','しゅうきょう','tôn giáo'),
    ('service','allergy_diversity','ベジタリアン','べじたりあん','người ăn chay'),
    ('service','allergy_diversity','ハラール','はらーる','Halal'),
    ('service','workplace_safety','火災','かさい','hỏa hoạn'),
    ('service','workplace_safety','地震','じしん','động đất'),
    ('service','workplace_safety','避難','ひなん','sơ tán'),
    ('service','workplace_safety','非常口','ひじょうぐち','lối thoát hiểm'),
    ('service','workplace_safety','消火器','しょうかき','bình chữa cháy'),
    ('service','workplace_safety','救急車','きゅうきゅうしゃ','xe cấp cứu'),
    ('service','workplace_safety','けが','けが','chấn thương'),
    ('service','workplace_safety','転倒','てんとう','té ngã'),
]


def add_unique_words(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    existing = set(VocabularyEntry.objects.values_list('word_jp', flat=True))
    order = VocabularyEntry.objects.count() + 1
    for category, topic, word, furigana, meaning in WORDS:
        if word in existing:
            continue
        VocabularyEntry.objects.create(
            category=category, topic=topic, word_jp=word, furigana=furigana,
            meaning_vi=meaning, order=order, is_published=True,
        )
        existing.add(word)
        order += 1


class Migration(migrations.Migration):
    dependencies = [('study', '0022_remove_duplicate_vocabulary')]
    operations = [migrations.RunPython(add_unique_words, migrations.RunPython.noop)]
