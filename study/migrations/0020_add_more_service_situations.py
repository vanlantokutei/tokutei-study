from django.db import migrations


# category, slug, title JP, furigana, title VI, customer JP, furigana, customer VI,
# response JP, furigana, response VI, handling steps VI
MORE = [
    ('welcome_order','change-seat','席を変えたい','せきを かえたい','Khách muốn đổi chỗ','席を変えてもいいですか。','せきを かえても いいですか。','Tôi có thể đổi chỗ không?','空席を確認いたします。少々お待ちください。','くうせきを かくにんいたします。しょうしょう おまちください。','Tôi sẽ kiểm tra chỗ trống, xin quý khách đợi một chút.','Kiểm tra chỗ trống; xác nhận bàn mới đã sẵn sàng; hỗ trợ chuyển đồ; cập nhật số bàn.'),
    ('welcome_order','child-chair','子ども用の椅子が必要','こどもようの いすが ひつよう','Khách cần ghế trẻ em','子ども用の椅子はありますか。','こどもようの いすは ありますか。','Có ghế dành cho trẻ em không?','はい、ございます。すぐにお持ちします。','はい、ございます。すぐに おもちします。','Vâng, nhà hàng có. Tôi sẽ mang tới ngay.','Xác nhận loại ghế; đặt chắc chắn; tránh lối đi; nhắc người đi cùng chú ý an toàn.'),
    ('welcome_order','large-group','大人数のお客様が来店','おおにんずうの おきゃくさまが らいてん','Một nhóm đông khách đến','八人ですが、入れますか。','はちにんですが、はいれますか。','Chúng tôi có tám người, có vào được không?','お席を確認いたしますので、少々お待ちください。','おせきを かくにんいたしますので、しょうしょう おまちください。','Tôi sẽ kiểm tra chỗ ngồi, xin quý khách chờ một chút.','Xác nhận số người; tìm bàn phù hợp; báo thời gian chờ; không tự ý ghép bàn cản trở lối đi.'),
    ('welcome_order','takeout-request','持ち帰りを希望する','もちかえりを きぼうする','Khách muốn mang món về','この料理は持ち帰りできますか。','この りょうりは もちかえり できますか。','Món này có thể mang về không?','持ち帰りできるか確認いたします。','もちかえり できるか かくにんいたします。','Tôi sẽ kiểm tra xem món này có thể mang về không.','Kiểm tra quy định và độ an toàn của món; thông báo thời hạn sử dụng; đóng gói đúng cách.'),
    ('welcome_order','language-support','日本語が分からないお客様','にほんごが わからない おきゃくさま','Khách không hiểu tiếng Nhật','英語のメニューはありますか。','えいごの めにゅーは ありますか。','Có thực đơn tiếng Anh không?','はい、ございます。こちらをご覧ください。','はい、ございます。こちらを ごらんください。','Vâng, có. Xin quý khách xem thực đơn này.','Dùng thực đơn hình ảnh/ngôn ngữ phù hợp; nói chậm; chỉ món để xác nhận; tránh giả vờ đã hiểu.'),

    ('complaint','food-cold','料理が冷めている','りょうりが さめている','Món ăn bị nguội','料理が冷たいです。','りょうりが つめたいです。','Món ăn bị lạnh.','申し訳ございません。すぐに確認いたします。','もうしわけございません。すぐに かくにんいたします。','Thành thật xin lỗi. Tôi sẽ kiểm tra ngay.','Xin lỗi; không tranh luận; thu món theo quy định; báo bếp/người phụ trách; phục vụ lại món phù hợp.'),
    ('complaint','taste-too-salty','料理の味が濃い','りょうりの あじが こい','Khách nói món quá mặn','この料理は塩辛すぎます。','この りょうりは しおからすぎます。','Món này quá mặn.','申し訳ございません。責任者に確認いたします。','もうしわけございません。せきにんしゃに かくにんいたします。','Xin lỗi quý khách. Tôi sẽ kiểm tra với người phụ trách.','Lắng nghe; xin lỗi; xác nhận món; báo người phụ trách; đưa phương án thay thế theo quy định.'),
    ('complaint','broken-dish','食器を割ってしまった','しょっきを わってしまった','Làm vỡ bát đĩa gần khách','','','','危険ですので、そのままお待ちください。すぐに片付けます。','きけんですので、そのまま おまちください。すぐに かたづけます。','Có nguy hiểm, xin quý khách giữ nguyên vị trí. Tôi sẽ dọn ngay.','Ngăn khách chạm mảnh vỡ; khoanh vùng; nhặt bằng dụng cụ; kiểm tra mảnh nhỏ; thay món nếu có nguy cơ lẫn dị vật.'),
    ('complaint','spilled-drink','飲み物をこぼした','のみものを こぼした','Làm đổ đồ uống lên khách','服がぬれてしまいました。','ふくが ぬれてしまいました。','Quần áo của tôi bị ướt.','大変申し訳ございません。すぐにタオルをお持ちします。','たいへん もうしわけございません。すぐに たおるを おもちします。','Thành thật xin lỗi. Tôi sẽ mang khăn tới ngay.','Xin lỗi; mang khăn sạch; bảo đảm sàn không trơn; báo người phụ trách; xử lý bồi thường theo quy định.'),
    ('complaint','noisy-customer','ほかのお客様がうるさい','ほかの おきゃくさまが うるさい','Khách phàn nàn bàn khác quá ồn','隣の席がうるさいです。','となりの せきが うるさいです。','Bàn bên cạnh quá ồn.','ご迷惑をおかけして申し訳ございません。確認いたします。','ごめいわくを おかけして もうしわけございません。かくにんいたします。','Xin lỗi vì đã làm phiền. Tôi sẽ kiểm tra.','Xin lỗi người phản ánh; báo người phụ trách; lịch sự nhắc bàn ồn; cân nhắc đổi chỗ; tránh gây xung đột.'),

    ('allergy','unknown-ingredient','原材料が分からない','げんざいりょうが わからない','Không chắc về thành phần món','このソースに乳製品は入っていますか。','この そーすに にゅうせいひんは はいっていますか。','Nước sốt này có sản phẩm sữa không?','分からないため、調理担当者に確認いたします。','わからないため、ちょうりたんとうしゃに かくにんいたします。','Tôi chưa chắc nên sẽ xác nhận với người chế biến.','Tuyệt đối không đoán; kiểm tra công thức/nhãn; xác nhận nguy cơ nhiễm chéo; trả lời chính xác.'),
    ('allergy','allergic-reaction','アレルギー症状が出た','あれるぎーしょうじょうが でた','Khách xuất hiện triệu chứng dị ứng','息が苦しいです。','いきが くるしいです。','Tôi khó thở.','すぐに救急車を呼びます。動かずにお待ちください。','すぐに きゅうきゅうしゃを よびます。うごかずに おまちください。','Tôi sẽ gọi cấp cứu ngay. Xin quý khách đừng di chuyển.','Gọi cấp cứu và người phụ trách ngay; không tự cho thuốc/thức ăn; lưu thông tin món; làm theo hướng dẫn y tế.'),
    ('allergy','vegetarian-request','ベジタリアン料理を希望','べじたりあんりょうりを きぼう','Khách yêu cầu món chay','肉と魚を使わない料理はありますか。','にくと さかなを つかわない りょうりは ありますか。','Có món nào không dùng thịt và cá không?','使用している食材を確認してご案内します。','しようしている しょくざいを かくにんして ごあんないします。','Tôi sẽ kiểm tra nguyên liệu rồi hướng dẫn quý khách.','Hỏi rõ mức độ ăn chay; kiểm tra nước dùng/gia vị; giải thích trung thực về dụng cụ dùng chung.'),
    ('allergy','halal-request','ハラール料理について聞かれた','はらーるりょうりについて きかれた','Khách hỏi về món Halal','この料理はハラールですか。','この りょうりは はらーるですか。','Món này có phải Halal không?','確認できないため、食材と調理方法をご説明します。','かくにんできないため、しょくざいと ちょうりほうほうを ごせつめいします。','Chúng tôi không thể xác nhận nên sẽ giải thích nguyên liệu và cách chế biến.','Không tự tuyên bố Halal nếu cửa hàng không được xác nhận; cung cấp thông tin nguyên liệu và nguy cơ dùng chung.'),
    ('allergy','elderly-support','高齢のお客様への対応','こうれいの おきゃくさまへの たいおう','Hỗ trợ khách cao tuổi','入口に段差はありますか。','いりぐちに だんさは ありますか。','Lối vào có bậc không?','安全な入口をご案内いたします。','あんぜんな いりぐちを ごあんないいたします。','Tôi sẽ hướng dẫn quý khách tới lối vào an toàn.','Hỏi khách cần hỗ trợ gì; không tự kéo/đẩy; dọn lối đi; chọn chỗ an toàn; nói rõ và chậm.'),

    ('payment','card-declined','カード決済ができない','かーどけっさいが できない','Không thanh toán được bằng thẻ','カードが使えませんか。','かーどが つかえませんか。','Thẻ không sử dụng được sao?','もう一度確認します。別のお支払い方法はございますか。','もういちど かくにんします。べつの おしはらいほうほうは ございますか。','Tôi sẽ kiểm tra lại. Quý khách có phương thức thanh toán khác không?','Thử lại đúng quy trình; không nói lý do ngân hàng khi không biết; đề nghị phương thức khác; bảo vệ thông tin thẻ.'),
    ('payment','not-enough-cash','現金が足りない','げんきんが たりない','Khách không đủ tiền mặt','現金が足りません。','げんきんが たりません。','Tôi không đủ tiền mặt.','ほかのお支払い方法を確認いたします。','ほかの おしはらいほうほうを かくにんいたします。','Tôi sẽ kiểm tra phương thức thanh toán khác.','Giữ thái độ kín đáo; nêu phương thức được chấp nhận; báo người phụ trách nếu không thể thanh toán.'),
    ('payment','split-bill','別々に会計したい','べつべつに かいけいしたい','Khách muốn thanh toán riêng','別々に払えますか。','べつべつに はらえますか。','Chúng tôi có thể trả riêng không?','伝票を確認いたします。少々お待ちください。','でんぴょうを かくにんいたします。しょうしょう おまちください。','Tôi sẽ kiểm tra hóa đơn, xin quý khách đợi một chút.','Kiểm tra chính sách; xác nhận cách chia; đọc lại từng khoản; tránh thu thiếu hoặc thu hai lần.'),
    ('payment','lost-property','忘れ物を見つけた','わすれものを みつけた','Phát hiện đồ khách bỏ quên','','','','忘れ物として責任者に届けます。','わすれものとして せきにんしゃに とどけます。','Tôi sẽ giao đồ bỏ quên cho người phụ trách.','Không tự mở/sử dụng; ghi nơi và thời gian phát hiện; giao người phụ trách; xác minh đặc điểm trước khi trả.'),
    ('payment','reservation-change','予約を変更したい','よやくを へんこうしたい','Khách muốn thay đổi đặt bàn','予約時間を八時に変えたいです。','よやくじかんを はちじに かえたいです。','Tôi muốn đổi giờ đặt bàn sang 8 giờ.','空席を確認して変更いたします。','くうせきを かくにんして へんこういたします。','Tôi sẽ kiểm tra chỗ và thay đổi đặt bàn.','Xác nhận tên/số điện thoại/ngày giờ/số người; kiểm tra chỗ; đọc lại thông tin sau khi sửa.'),

    ('emergency','earthquake','地震が発生した','じしんが はっせいした','Xảy ra động đất','','','','頭を守って、揺れがおさまるまでお待ちください。','あたまを まもって、ゆれが おさまるまで おまちください。','Xin bảo vệ đầu và chờ đến khi rung lắc dừng lại.','Bảo vệ khách khỏi vật rơi; không chạy ra ngoài khi đang rung; sau đó kiểm tra lối thoát và hướng dẫn sơ tán.'),
    ('emergency','power-outage','停電した','ていでんした','Nhà hàng mất điện','','','','その場でお待ちください。安全を確認いたします。','そのばで おまちください。あんぜんを かくにんいたします。','Xin quý khách đứng yên tại chỗ. Chúng tôi sẽ kiểm tra an toàn.','Bật đèn khẩn cấp; ngăn khách di chuyển trong tối; dừng thiết bị; kiểm tra bếp và hướng dẫn theo người phụ trách.'),
    ('emergency','customer-choking','お客様が喉を詰まらせた','おきゃくさまが のどを つまらせた','Khách bị nghẹn','','','','救急車を呼んでください。すぐに対応します。','きゅうきゅうしゃを よんでください。すぐに たいおうします。','Hãy gọi cấp cứu. Chúng tôi sẽ xử lý ngay.','Gọi trợ giúp/cấp cứu; đánh giá khách có ho/nói được không; sơ cứu chỉ khi đã được huấn luyện; không cho uống nước tùy tiện.'),
    ('emergency','knife-injury','従業員が包丁でけがをした','じゅうぎょういんが ほうちょうで けがをした','Nhân viên bị dao cắt','','','','作業を止めて、すぐに責任者へ報告します。','さぎょうを とめて、すぐに せきにんしゃへ ほうこくします。','Dừng công việc và báo người phụ trách ngay.','Dừng chế biến; tránh máu tiếp xúc thực phẩm; sơ cứu; loại bỏ thực phẩm/dụng cụ có nguy cơ; vệ sinh khử trùng theo quy định.'),
    ('emergency','gas-smell','ガスのにおいがする','がすの においが する','Phát hiện mùi gas','','','','火を使わず、責任者に報告して避難します。','ひを つかわず、せきにんしゃに ほうこくして ひなんします。','Không sử dụng lửa, báo người phụ trách và sơ tán.','Không bật/tắt công tắc điện; tránh lửa; báo động; khóa gas nếu an toàn; thông gió và sơ tán theo quy định.'),
]


def add_more(apps, schema_editor):
    Situation = apps.get_model('study', 'ServiceSituation')
    counters = {
        key: (Situation.objects.filter(category=key).order_by('-order').values_list('order', flat=True).first() or 0)
        for key in ['welcome_order','complaint','allergy','payment','emergency']
    }
    for row in MORE:
        category, slug, title_jp, title_furigana, title_vi = row[:5]
        counters[category] += 1
        Situation.objects.update_or_create(slug=slug, defaults={
            'category': category, 'title_jp': title_jp, 'title_furigana': title_furigana,
            'title_vi': title_vi, 'situation_jp': f'{title_jp}という状況です。',
            'situation_furigana': f'{title_furigana}という じょうきょうです。',
            'situation_vi': f'Tình huống: {title_vi}.',
            'customer_phrase_jp': row[5], 'customer_phrase_furigana': row[6],
            'customer_phrase_vi': row[7], 'response_jp': row[8],
            'response_furigana': row[9], 'response_vi': row[10],
            'handling_steps_vi': row[11],
            'exam_note_vi': 'Giữ bình tĩnh, xác nhận thông tin và báo người phụ trách khi vượt quá quyền hạn.',
            'order': counters[category], 'is_published': True,
        })


def remove_more(apps, schema_editor):
    Situation = apps.get_model('study', 'ServiceSituation')
    Situation.objects.filter(slug__in=[row[1] for row in MORE]).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0019_seed_service_situations')]
    operations = [migrations.RunPython(add_more, remove_more)]
