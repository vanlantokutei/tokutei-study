from django.db import migrations


SITUATIONS = [
    ('welcome_order','fully-booked','満席のとき','まんせきの とき','Khi nhà hàng hết chỗ','店内は満席で、お客様が来店しました。','てんないは まんせきで、おきゃくさまが らいてんしました。','Nhà hàng đã kín chỗ và có khách mới đến.','今、入れますか。','いま、はいれますか。','Bây giờ tôi vào được không?','申し訳ございません。ただいま満席です。お待ちいただけますでしょうか。','もうしわけございません。ただいま まんせきです。おまち いただけますでしょうか。','Thành thật xin lỗi, hiện tại nhà hàng đã kín chỗ. Quý khách có thể vui lòng chờ không?','1. Xin lỗi khách.\n2. Thông báo rõ đang kín chỗ.\n3. Cho biết thời gian chờ dự kiến.\n4. Xác nhận khách có muốn chờ hay không.','Không được nói trống không 「満席です」 rồi bỏ mặc khách.'),
    ('welcome_order','unclear-order','注文が聞き取れない','ちゅうもんが ききとれない','Không nghe rõ món khách gọi','お客様の注文を聞き取ることができませんでした。','おきゃくさまの ちゅうもんを ききとることが できませんでした。','Nhân viên không nghe rõ món khách gọi.','これを二つください。','これを ふたつ ください。','Cho tôi hai phần món này.','恐れ入ります。もう一度ご注文をお願いいたします。','おそれいります。もういちど ごちゅうもんを おねがいいたします。','Xin lỗi đã làm phiền. Quý khách vui lòng gọi lại món một lần nữa.','1. Lịch sự xin khách nhắc lại.\n2. Chỉ vào thực đơn để xác nhận món.\n3. Nhắc lại tên món và số lượng.','Không tự đoán món; phải 復唱 — nhắc lại để xác nhận.'),
    ('welcome_order','sold-out','注文した料理が品切れ','ちゅうもんした りょうりが しなぎれ','Món khách gọi đã hết','注文を受けた料理が品切れになっています。','ちゅうもんを うけた りょうりが しなぎれに なっています。','Món vừa được khách gọi hiện đã hết.','この料理をお願いします。','この りょうりを おねがいします。','Cho tôi món này.','申し訳ございません。こちらは品切れです。よろしければ、こちらはいかがでしょうか。','もうしわけございません。こちらは しなぎれです。よろしければ、こちらは いかがでしょうか。','Thành thật xin lỗi, món này đã hết. Nếu quý khách đồng ý, món này thì sao ạ?','1. Xin lỗi.\n2. Thông báo món đã hết.\n3. Đề xuất món thay thế phù hợp.\n4. Xác nhận lại lựa chọn của khách.','Nên đề xuất món thay thế, không chỉ thông báo hết món.'),
    ('complaint','wrong-dish','料理を間違えて提供した','りょうりを まちがえて ていきょうした','Phục vụ sai món','別のお客様の料理を提供してしまいました。','べつの おきゃくさまの りょうりを ていきょうして しまいました。','Nhân viên đã mang nhầm món của khách khác.','これは注文していません。','これは ちゅうもんして いません。','Tôi không gọi món này.','大変申し訳ございません。すぐに確認して、正しい料理をお持ちします。','たいへん もうしわけございません。すぐに かくにんして、ただしい りょうりを おもちします。','Thành thật xin lỗi. Tôi sẽ kiểm tra ngay và mang đúng món tới.','1. Xin lỗi ngay.\n2. Thu hồi món sai theo quy định.\n3. Kiểm tra phiếu gọi món.\n4. Báo bếp và người phụ trách.\n5. Mang đúng món cho khách.','Không tranh luận hoặc đổ lỗi cho khách hay nhà bếp.'),
    ('complaint','long-wait','料理の提供が遅い','りょうりの ていきょうが おそい','Khách chờ món quá lâu','料理の提供に通常より時間がかかっています。','りょうりの ていきょうに つうじょうより じかんが かかっています。','Món ăn mất nhiều thời gian hơn bình thường.','まだ料理が来ません。','まだ りょうりが きません。','Món của tôi vẫn chưa tới.','お待たせして申し訳ございません。すぐに厨房に確認いたします。','おまたせして もうしわけございません。すぐに ちゅうぼうに かくにんいたします。','Xin lỗi vì đã để quý khách chờ. Tôi sẽ kiểm tra với nhà bếp ngay.','1. Xin lỗi vì để khách chờ.\n2. Kiểm tra trạng thái món.\n3. Báo thời gian dự kiến chính xác.\n4. Theo dõi đến khi món được phục vụ.','Không đưa ra thời gian tùy ý trước khi hỏi nhà bếp.'),
    ('complaint','foreign-object','料理に異物が入っている','りょうりに いぶつが はいっている','Có dị vật trong món ăn','お客様が料理の中に異物を見つけました。','おきゃくさまが りょうりの なかに いぶつを みつけました。','Khách phát hiện dị vật trong món ăn.','料理に何か入っています。','りょうりに なにか はいっています。','Có thứ gì đó trong món ăn.','大変申し訳ございません。料理には触れず、すぐに責任者をお呼びいたします。','たいへん もうしわけございません。りょうりには ふれず、すぐに せきにんしゃを およびいたします。','Thành thật xin lỗi. Xin đừng chạm vào món ăn; tôi sẽ gọi người phụ trách ngay.','1. Xin lỗi và giữ nguyên hiện trạng món.\n2. Không tự ý vứt dị vật.\n3. Báo người phụ trách ngay.\n4. Ghi nhận bàn, món và thời điểm.\n5. Xử lý theo quy định cửa hàng.','Đây là vấn đề an toàn thực phẩm; phải báo cáo, không tự xử lý một mình.'),
    ('allergy','allergy-check','食物アレルギーを確認する','しょくもつ あれるぎーを かくにんする','Xác nhận dị ứng thực phẩm','お客様が料理にアレルゲンが含まれるか質問しました。','おきゃくさまが りょうりに あれるげんが ふくまれるか しつもんしました。','Khách hỏi món ăn có chứa chất gây dị ứng hay không.','卵は入っていますか。','たまごは はいっていますか。','Món này có trứng không?','確認いたしますので、少々お待ちください。','かくにんいたしますので、しょうしょう おまちください。','Tôi sẽ kiểm tra, xin quý khách vui lòng đợi một chút.','1. Không trả lời theo trí nhớ hoặc suy đoán.\n2. Xác nhận nguyên liệu và thông tin dị ứng.\n3. Hỏi người phụ trách hoặc nhà bếp.\n4. Truyền đạt kết quả chính xác cho khách.','Nếu không chắc chắn, luôn phải 確認 — kiểm tra.'),
    ('allergy','special-diet','宗教上食べられないもの','しゅうきょうじょう たべられない もの','Khách có yêu cầu ăn uống theo tôn giáo','お客様には宗教上食べられない食材があります。','おきゃくさまには しゅうきょうじょう たべられない しょくざいが あります。','Khách có nguyên liệu không thể ăn vì lý do tôn giáo.','豚肉を使っていない料理はありますか。','ぶたにくを つかっていない りょうりは ありますか。','Có món nào không sử dụng thịt lợn không?','食材と調理方法を確認してご案内いたします。','しょくざいと ちょうりほうほうを かくにんして ごあんないいたします。','Tôi sẽ kiểm tra nguyên liệu và phương pháp chế biến rồi hướng dẫn quý khách.','1. Hỏi rõ nguyên liệu cần tránh.\n2. Kiểm tra cả gia vị và cách chế biến.\n3. Chú ý nguy cơ dùng chung dụng cụ.\n4. Không cam kết khi chưa xác nhận.','Không chỉ kiểm tra nguyên liệu chính; gia vị và dụng cụ dùng chung cũng quan trọng.'),
    ('payment','payment-error','会計の金額が違う','かいけいの きんがくが ちがう','Số tiền thanh toán không đúng','お客様が会計金額に間違いがあると言っています。','おきゃくさまが かいけいきんがくに まちがいが あると いっています。','Khách cho rằng số tiền thanh toán bị sai.','この料理は注文していません。','この りょうりは ちゅうもんして いません。','Tôi không gọi món này.','申し訳ございません。伝票を確認いたします。','もうしわけございません。でんぴょうを かくにんいたします。','Xin lỗi quý khách. Tôi sẽ kiểm tra lại phiếu gọi món.','1. Xin lỗi và kiểm tra hóa đơn.\n2. Đối chiếu đơn gọi món.\n3. Sửa sai theo quyền hạn hoặc gọi người phụ trách.\n4. Xác nhận lại số tiền trước khi thu.','Không khẳng định khách sai trước khi kiểm tra.'),
    ('payment','reservation-missing','予約が見つからない','よやくが みつからない','Không tìm thấy thông tin đặt bàn','来店したお客様の予約が予約表にありません。','らいてんした おきゃくさまの よやくが よやくひょうに ありません。','Không thấy tên khách trong danh sách đặt bàn.','七時に予約した田中です。','しちじに よやくした たなかです。','Tôi là Tanaka, đã đặt bàn lúc 7 giờ.','申し訳ございません。お名前と電話番号をもう一度確認させていただけますか。','もうしわけございません。おなまえと でんわばんごうを もういちど かくにんさせて いただけますか。','Xin lỗi, tôi có thể xác nhận lại tên và số điện thoại của quý khách không?','1. Xin lỗi và giữ thái độ bình tĩnh.\n2. Xác nhận tên, giờ, số người và số điện thoại.\n3. Kiểm tra lại hệ thống.\n4. Báo người phụ trách nếu vẫn không tìm thấy.','Không nói ngay 「予約はありません」 khi chưa kiểm tra đủ thông tin.'),
    ('emergency','customer-fall','お客様が転倒した','おきゃくさまが てんとうした','Khách bị ngã','店内でお客様が転びました。','てんないで おきゃくさまが ころびました。','Một khách hàng bị ngã trong nhà hàng.','足が痛いです。','あしが いたいです。','Chân tôi đau.','大丈夫ですか。動かずにお待ちください。すぐに責任者を呼びます。','だいじょうぶですか。うごかずに おまちください。すぐに せきにんしゃを よびます。','Quý khách có ổn không? Xin đừng di chuyển; tôi sẽ gọi người phụ trách ngay.','1. Kiểm tra ý thức và tình trạng khách.\n2. Không tự ý di chuyển người bị thương.\n3. Báo người phụ trách.\n4. Gọi cấp cứu khi cần.\n5. Cô lập nguyên nhân gây trượt ngã.','Ưu tiên an toàn con người; không tiếp tục phục vụ như bình thường.'),
    ('emergency','fire','店内で火災が発生した','てんないで かさいが はっせいした','Xảy ra hỏa hoạn trong nhà hàng','調理場から煙と火が出ています。','ちょうりばから けむりと ひが でています。','Có khói và lửa phát ra từ khu bếp.','','','','火事です。落ち着いて、非常口から避難してください。','かじです。おちついて、ひじょうぐちから ひなんしてください。','Có hỏa hoạn. Xin hãy bình tĩnh và sơ tán qua lối thoát hiểm.','1. Báo động và gọi cứu hỏa theo quy định.\n2. Hướng dẫn khách tới lối thoát hiểm.\n3. Không dùng thang máy.\n4. Chỉ chữa cháy ban đầu khi bảo đảm an toàn.\n5. Tập trung tại điểm quy định.','Khi khẩn cấp, hướng dẫn phải ngắn, rõ và ưu tiên sơ tán.'),
]


def seed_situations(apps, schema_editor):
    Situation = apps.get_model('study', 'ServiceSituation')
    counters = {}
    for row in SITUATIONS:
        category, slug = row[0], row[1]
        counters[category] = counters.get(category, 0) + 1
        Situation.objects.update_or_create(slug=slug, defaults={
            'category': category, 'title_jp': row[2], 'title_furigana': row[3], 'title_vi': row[4],
            'situation_jp': row[5], 'situation_furigana': row[6], 'situation_vi': row[7],
            'customer_phrase_jp': row[8], 'customer_phrase_furigana': row[9], 'customer_phrase_vi': row[10],
            'response_jp': row[11], 'response_furigana': row[12], 'response_vi': row[13],
            'handling_steps_vi': row[14], 'exam_note_vi': row[15],
            'order': counters[category], 'is_published': True,
        })


def remove_situations(apps, schema_editor):
    Situation = apps.get_model('study', 'ServiceSituation')
    Situation.objects.filter(slug__in=[row[1] for row in SITUATIONS]).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0018_servicesituation')]
    operations = [migrations.RunPython(seed_situations, remove_situations)]
