import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tokutei_site.settings")

import django
django.setup()

from study.models import Question, Exam, ExamQuestion
from pykakasi import kakasi

kks = kakasi()

def ruby(text):
    out = []
    for x in kks.convert(text):
        orig = x["orig"]
        hira = x["hira"]
        if re.search(r"[\u4e00-\u9fff]", orig):
            out.append(f"<ruby>{orig}<rt>{hira}</rt></ruby>")
        else:
            out.append(orig)
    return "".join(out)


data = [
# =========================
# 学科試験・衛生管理 10
# =========================
("theory","hygiene","",
"調理前に爪を確認する理由として最も適切なものはどれですか。",
"Tại sao cần kiểm tra móng tay trước khi chế biến?",
"汚れや異物混入を防ぐため","Để phòng bụi bẩn và dị vật lẫn vào thực phẩm",
"料理の味を濃くするため","Để làm món ăn đậm vị hơn",
"手を温めるため","Để làm ấm tay",
"A","爪は短く清潔に保ち、汚れや異物混入を防ぎます。"),

("theory","hygiene","",
"食品を保管するときに容器へふたをする主な目的は何ですか。",
"Mục đích chính của việc đậy nắp hộp khi bảo quản thực phẩm là gì?",
"汚染や乾燥を防ぐため","Để phòng nhiễm bẩn và khô thực phẩm",
"食品を必ず熱くするため","Để chắc chắn làm thực phẩm nóng",
"容器を重くするため","Để làm hộp nặng hơn",
"A","適切にふたをすることで、異物や他の食品からの汚染を防ぎやすくなります。"),

("theory","hygiene","",
"ごみ箱を衛生的に管理する方法として適切なのはどれですか。",
"Cách quản lý thùng rác hợp vệ sinh là gì?",
"ふたをして定期的にごみを処理する","Đậy nắp và xử lý rác định kỳ",
"いっぱいになるまで何日も放置する","Để nhiều ngày đến khi đầy",
"食品のすぐ上に置く","Đặt ngay phía trên thực phẩm",
"A","ごみは害虫や悪臭、汚染の原因になるため適切に管理します。"),

("theory","hygiene","",
"調理中に髪の毛が食品に入るのを防ぐために適切なのはどれですか。",
"Cách phù hợp để tránh tóc rơi vào thực phẩm là gì?",
"帽子などを正しく着用する","Đội mũ đúng cách",
"髪を何度も触る","Thường xuyên chạm tóc",
"髪を料理の上で整える","Chỉnh tóc phía trên món ăn",
"A","毛髪混入を防ぐため、帽子などを正しく着用します。"),

("theory","hygiene","",
"冷蔵食品を受け取るときに確認することとして適切なのはどれですか。",
"Khi nhận thực phẩm lạnh, điều nào cần kiểm tra?",
"温度や包装、品質の状態","Nhiệt độ, bao bì và tình trạng chất lượng",
"配達員の趣味","Sở thích của người giao hàng",
"箱の色だけ","Chỉ màu hộp",
"A","納品時には温度、期限、包装、品質などを確認します。"),

("theory","hygiene","",
"洗剤を使用するときに重要なことはどれですか。",
"Điều quan trọng khi sử dụng chất tẩy rửa là gì?",
"決められた使用方法を守る","Tuân thủ cách sử dụng quy định",
"量を確認せず大量に使う","Dùng thật nhiều mà không kiểm tra lượng",
"食品へ直接かける","Đổ trực tiếp lên thực phẩm",
"A","薬剤は表示や店舗の手順に従って安全に使用します。"),

("theory","hygiene","",
"生卵を扱った後の対応として適切なのはどれですか。",
"Sau khi xử lý trứng sống, hành động nào phù hợp?",
"必要な手洗いと器具の衛生管理を行う","Rửa tay cần thiết và vệ sinh dụng cụ",
"そのまま他の食品を触る","Chạm ngay thực phẩm khác",
"手を服で拭くだけ","Chỉ lau tay vào quần áo",
"A","生の食品を扱った後は交差汚染防止のため適切な衛生管理を行います。"),

("theory","hygiene","",
"床を清掃するとき、食品への汚染を防ぐために重要なことはどれですか。",
"Khi vệ sinh sàn, điều quan trọng để tránh nhiễm bẩn thực phẩm là gì?",
"食品や器具へ汚水がかからないようにする","Không để nước bẩn bắn vào thực phẩm và dụng cụ",
"食品を床に置く","Đặt thực phẩm xuống sàn",
"調理中の鍋に清掃水を入れる","Cho nước lau sàn vào nồi đang nấu",
"A","清掃時には汚れを周囲へ広げないよう注意します。"),

("theory","hygiene","",
"解凍中の食品を長時間室温に置くことを避ける理由は何ですか。",
"Tại sao tránh để thực phẩm đang rã đông ở nhiệt độ phòng quá lâu?",
"微生物が増殖する可能性があるため","Vì vi sinh vật có thể phát triển",
"必ず味が甘くなるため","Vì chắc chắn món sẽ ngọt hơn",
"食品が軽くなるため","Vì thực phẩm sẽ nhẹ hơn",
"A","解凍は衛生的な方法で行い、温度管理に注意します。"),

("theory","hygiene","",
"食品衛生の記録を残す目的として適切なのはどれですか。",
"Mục đích phù hợp của việc lưu hồ sơ vệ sinh thực phẩm là gì?",
"管理状況を確認できるようにするため","Để có thể kiểm tra tình trạng quản lý",
"紙を増やすため","Để tăng số lượng giấy",
"料理名を忘れるため","Để quên tên món",
"A","記録は衛生管理の実施状況を確認するために重要です。"),

# =========================
# 学科試験・飲食物調理 10
# =========================
("theory","cooking","",
"食材を使用する前に必要量を確認する理由として適切なのはどれですか。",
"Tại sao cần kiểm tra lượng nguyên liệu cần thiết trước khi sử dụng?",
"過不足や食品ロスを減らすため","Để giảm thiếu/thừa và lãng phí thực phẩm",
"必ず料理を冷たくするため","Để chắc chắn làm món lạnh",
"食器を増やすため","Để tăng số lượng bát đĩa",
"A","必要量を把握することで効率的な仕込みと食品ロス削減につながります。"),

("theory","cooking","",
"鍋の取っ手が熱くなっている場合、適切な対応はどれですか。",
"Nếu tay cầm nồi đang nóng, xử lý nào phù hợp?",
"安全な方法で扱い、やけどを防ぐ","Xử lý an toàn để tránh bỏng",
"素手で急いで持つ","Cầm vội bằng tay trần",
"他の人へ投げ渡す","Ném sang cho người khác",
"A","熱い器具を扱うときはやけど防止のため安全な方法を取ります。"),

("theory","cooking","",
"複数の料理を同時に作るときに大切なことはどれですか。",
"Điều quan trọng khi nấu nhiều món cùng lúc là gì?",
"作業順序と提供時間を考える","Cân nhắc thứ tự thao tác và thời gian phục vụ",
"すべての料理を同じ時間だけ加熱する","Nấu tất cả cùng một thời gian",
"注文内容を確認しない","Không kiểm tra order",
"A","作業の優先順位を考え、品質と提供時間を管理します。"),

("theory","cooking","",
"計量スプーンを使う利点として適切なのはどれですか。",
"Lợi ích của việc dùng thìa đong là gì?",
"分量を一定にしやすい","Dễ giữ định lượng ổn định",
"料理を必ず大きくできる","Chắc chắn làm món to hơn",
"食材を冷凍できる","Có thể đông lạnh nguyên liệu",
"A","正しい計量によって味や品質を一定にしやすくなります。"),

("theory","cooking","",
"加熱後の料理を盛り付ける際に重要なことはどれですか。",
"Điều quan trọng khi trình bày món sau khi nấu là gì?",
"清潔な器具や食器を使用する","Dùng dụng cụ và bát đĩa sạch",
"生肉を置いた皿をそのまま使う","Dùng ngay đĩa đã đặt thịt sống",
"床に置いて盛り付ける","Đặt xuống sàn để trình bày",
"A","加熱後の食品へ二次汚染が起こらないようにします。"),

("theory","cooking","",
"食材の下処理を効率よく行うために適切なのはどれですか。",
"Cách phù hợp để sơ chế nguyên liệu hiệu quả là gì?",
"作業内容と必要な器具を事前に確認する","Kiểm tra trước công việc và dụng cụ cần thiết",
"途中で何度も器具を探す","Liên tục tìm dụng cụ giữa chừng",
"レシピを見ない","Không xem công thức",
"A","事前準備によって安全かつ効率的に作業できます。"),

("theory","cooking","",
"味見をするときの衛生的な方法として適切なのはどれですか。",
"Cách nếm thức ăn hợp vệ sinh là gì?",
"清潔な専用の器具を使う","Dùng dụng cụ sạch dành riêng",
"同じスプーンを何度も口に入れて鍋へ戻す","Dùng lại thìa đã đưa vào miệng",
"指で直接味見する","Nếm trực tiếp bằng ngón tay",
"A","味見には清潔な器具を使用し、食品を汚染しないようにします。"),

("theory","cooking","",
"料理の見た目をそろえるために重要なことはどれですか。",
"Điều quan trọng để món ăn có hình thức đồng đều là gì?",
"盛り付け基準を守る","Tuân thủ tiêu chuẩn trình bày",
"毎回自由に盛る","Mỗi lần trình bày tùy ý",
"皿を変え続ける","Liên tục đổi đĩa",
"A","盛り付け基準を守ることで品質を安定させます。"),

("theory","cooking","",
"調理中に食材が不足した場合の適切な対応はどれですか。",
"Nếu thiếu nguyên liệu trong lúc chế biến, xử lý nào phù hợp?",
"責任者に報告し対応を確認する","Báo người phụ trách và xác nhận cách xử lý",
"勝手に別の食材へ変更する","Tự ý đổi sang nguyên liệu khác",
"何も言わず料理を出す","Không nói gì và phục vụ",
"A","食材変更はアレルギーや品質にも関わるため自己判断で行いません。"),

("theory","cooking","",
"使用済みの油を管理するときに重要なことはどれですか。",
"Điều quan trọng khi quản lý dầu đã sử dụng là gì?",
"状態を確認し店舗の基準に従う","Kiểm tra tình trạng và tuân thủ tiêu chuẩn cửa hàng",
"永久に使い続ける","Dùng mãi mãi",
"水と混ぜて保存する","Trộn với nước để bảo quản",
"A","油の劣化状態を確認し、店舗のルールに従って交換・処理します。"),

# =========================
# 学科試験・接客全般 10
# =========================
("theory","service","",
"お客様にメニューを説明するときに重要なことはどれですか。",
"Điều quan trọng khi giải thích menu cho khách là gì?",
"正確で分かりやすく説明する","Giải thích chính xác, dễ hiểu",
"分からなくても適当に説明する","Không biết vẫn giải thích đại",
"価格を勝手に変更する","Tự ý thay đổi giá",
"A","メニュー内容は正確に案内します。"),

("theory","service","",
"料理を提供するときの声かけとして適切なのはどれですか。",
"Cách nói phù hợp khi phục vụ món là gì?",
"料理名などを確認しながら丁寧に提供する","Lịch sự xác nhận tên món khi phục vụ",
"無言で置く","Đặt xuống không nói gì",
"遠くから投げる","Ném từ xa",
"A","丁寧な声かけと確認によって誤提供を防ぎます。"),

("theory","service","",
"店内が満席の場合、お客様への対応として適切なのはどれですか。",
"Nếu cửa hàng kín chỗ, xử lý khách thế nào là phù hợp?",
"状況を説明し待ち時間などを案内する","Giải thích tình hình và thời gian chờ",
"何も説明しない","Không giải thích gì",
"必ず帰ってもらう","Luôn yêu cầu khách về",
"A","混雑状況を丁寧に説明し、必要な案内を行います。"),

("theory","service","",
"お客様から追加注文を受けたときに大切なことはどれですか。",
"Điều quan trọng khi nhận order bổ sung là gì?",
"内容を正確に確認する","Xác nhận chính xác nội dung",
"最初の注文を消す","Xóa order đầu tiên",
"聞かなかったことにする","Coi như không nghe",
"A","追加注文も復唱などで正確に確認します。"),

("theory","service","",
"電話対応で重要なことはどれですか。",
"Điều quan trọng khi nghe điện thoại là gì?",
"店名や内容を分かりやすく伝える","Nói rõ tên cửa hàng và nội dung",
"何も名乗らない","Không giới thiệu gì",
"途中で電話を切る","Cúp máy giữa chừng",
"A","電話でも丁寧で正確な対応を行います。"),

("theory","service","",
"お客様が会計を別々にしたいと申し出た場合、どうしますか。",
"Nếu khách muốn thanh toán riêng, nên làm gì?",
"店舗の対応方法を確認して案内する","Xác nhận quy định cửa hàng rồi hướng dẫn",
"必ず断る","Luôn từ chối",
"金額を適当に分ける","Chia tiền tùy ý",
"A","店舗のルールに従って正確に会計対応します。"),

("theory","service","",
"小さな子ども連れのお客様への対応で重要なことはどれですか。",
"Điều quan trọng khi phục vụ khách có trẻ nhỏ là gì?",
"安全に配慮して案内する","Hướng dẫn có chú ý đến an toàn",
"子どもを無視する","Phớt lờ trẻ em",
"危険な席へ必ず案内する","Luôn dẫn đến chỗ nguy hiểm",
"A","お客様の状況に応じて安全に配慮します。"),

("theory","service","",
"お客様が料理の写真を見せて注文した場合、重要なことはどれですか。",
"Nếu khách cho xem ảnh món để gọi, điều nào quan trọng?",
"希望する料理を正確に確認する","Xác nhận chính xác món khách muốn",
"別の料理を勝手に出す","Tự ý mang món khác",
"写真を捨てる","Vứt ảnh đi",
"A","注文内容を正しく確認して誤注文を防ぎます。"),

("theory","service","",
"会計後にレシートを渡すときの対応として適切なのはどれですか。",
"Cách phù hợp khi đưa hóa đơn sau thanh toán là gì?",
"金額を確認して丁寧に渡す","Kiểm tra số tiền và đưa lịch sự",
"床に置く","Đặt xuống sàn",
"別のお客様へ渡す","Đưa cho khách khác",
"A","会計内容を確認し、正しいレシートを渡します。"),

("theory","service","",
"外国人のお客様と意思疎通が難しい場合、適切な対応はどれですか。",
"Nếu khó giao tiếp với khách nước ngoài, nên xử lý thế nào?",
"分かりやすい方法で丁寧に確認する","Dùng cách dễ hiểu để xác nhận lịch sự",
"怒って大声で話す","Nổi giận và nói thật to",
"注文を無視する","Phớt lờ order",
"A","言葉が通じにくい場合も、表示や簡単な表現などを活用して丁寧に確認します。"),

# =========================
# 実技・判断試験 9
# =========================
("practical","hygiene","judgment",
"冷蔵庫内で生魚の汁が他の食品に付着しているのを発見しました。適切な対応はどれですか。",
"Phát hiện nước cá sống dính vào thực phẩm khác trong tủ lạnh. Xử lý phù hợp là gì?",
"汚染の可能性を確認し、責任者へ報告して適切に処理する","Kiểm tra nguy cơ nhiễm bẩn, báo người phụ trách và xử lý phù hợp",
"そのまま販売する","Bán luôn",
"汁だけ拭いて必ず使用する","Chỉ lau nước rồi chắc chắn sử dụng",
"A","交差汚染の可能性があるため、自己判断で提供せず適切に対応します。"),

("practical","hygiene","judgment",
"手洗い場に石けんがありません。調理前にどうしますか。",
"Không có xà phòng tại bồn rửa tay. Trước khi chế biến nên làm gì?",
"補充など必要な対応をして正しく手を洗う","Bổ sung và rửa tay đúng cách",
"水だけで必ず十分と考える","Cho rằng chỉ nước luôn đủ",
"手洗いをしない","Không rửa tay",
"A","必要な手洗い環境を整えてから作業します。"),

("practical","hygiene","judgment",
"食品庫で期限表示のない容器を見つけました。どうしますか。",
"Phát hiện hộp thực phẩm không có nhãn hạn trong kho. Nên làm gì?",
"使用せず内容や管理状況を確認する","Không sử dụng, kiểm tra nội dung và tình trạng quản lý",
"すぐ料理に使う","Dùng ngay vào món",
"新しい期限を適当に書く","Tự viết hạn mới",
"A","不明な食品は自己判断で使用せず確認します。"),

("practical","cooking","judgment",
"スープを加熱中に焦げたにおいがしました。適切な対応はどれですか。",
"Trong lúc hâm súp có mùi khét. Xử lý phù hợp là gì?",
"加熱状態を確認し、必要に応じて火を止める","Kiểm tra tình trạng và tắt nhiệt khi cần",
"さらに強火にする","Tăng lửa lớn hơn",
"何も確認せず提供する","Không kiểm tra và phục vụ",
"A","異常を感じた場合は状態を確認して品質や安全を確保します。"),

("practical","cooking","judgment",
"料理を盛り付けた後、皿にひびがあることに気づきました。どうしますか。",
"Sau khi trình bày món, phát hiện đĩa bị nứt. Nên làm gì?",
"安全な食器に交換して盛り付け直す","Đổi sang bát đĩa an toàn và trình bày lại",
"そのまま提供する","Phục vụ luôn",
"ひびをテープで隠す","Che vết nứt bằng băng dính",
"A","破損した食器は事故や異物混入につながるため使用しません。"),

("practical","cooking","judgment",
"注文より多く料理を作ってしまいました。適切な対応はどれですか。",
"Đã làm nhiều món hơn số order. Xử lý nào phù hợp?",
"責任者に報告し店舗のルールに従う","Báo người phụ trách và làm theo quy định",
"別のお客様へ勝手に出す","Tự ý đưa cho khách khác",
"床に置く","Đặt xuống sàn",
"A","余剰食品は自己判断せず、店舗のルールに従います。"),

("practical","service","judgment",
"お客様が熱い料理でやけどをしたと申し出ました。適切な対応はどれですか。",
"Khách báo bị bỏng do món nóng. Xử lý phù hợp là gì?",
"状態を確認し責任者に報告して必要な対応を行う","Kiểm tra tình trạng, báo người phụ trách và hỗ trợ cần thiết",
"無視する","Phớt lờ",
"お客様の責任だと言う","Nói đó là lỗi của khách",
"A","安全確認と必要な救護、報告を速やかに行います。"),

("practical","service","judgment",
"お客様が注文していない料理が会計に入っています。どうしますか。",
"Hóa đơn có món khách không gọi. Nên làm gì?",
"注文と会計内容を確認して訂正する","Kiểm tra order và sửa hóa đơn",
"そのまま請求する","Cứ thu tiền",
"別の料金を追加する","Thêm phí khác",
"A","会計内容を正確に確認してミスを訂正します。"),

("practical","service","judgment",
"入口付近の床が雨で濡れています。適切な対応はどれですか。",
"Sàn gần cửa vào bị ướt do mưa. Xử lý phù hợp là gì?",
"転倒防止のため速やかに安全対策を行う","Nhanh chóng xử lý để phòng trượt ngã",
"乾くまで放置する","Để nguyên đến khi khô",
"お客様に掃除してもらう","Nhờ khách lau",
"A","濡れた床は転倒事故につながるため速やかに対応します。"),

# =========================
# 実技・計画立案 6
# =========================
("practical","hygiene","planning",
"清掃用の希釈液を2L作るのに原液40mlが必要です。6L作る場合、原液は何ml必要ですか。",
"Pha 2L dung dịch cần 40ml dung dịch gốc. Pha 6L cần bao nhiêu ml?",
"120ml","120ml","80ml","80ml","240ml","240ml",
"A","40ml × 3 = 120mlです。"),

("practical","hygiene","planning",
"冷蔵庫の温度を2時間ごとに確認します。10時間で何回確認しますか。",
"Kiểm tra nhiệt độ tủ lạnh mỗi 2 giờ. Trong 10 giờ kiểm tra bao nhiêu lần?",
"5回","5 lần","10回","10 lần","20回","20 lần",
"A","10 ÷ 2 = 5回です。"),

("practical","cooking","planning",
"1人分に120gの野菜を使います。15人分では何g必要ですか。",
"Mỗi phần dùng 120g rau. 15 phần cần bao nhiêu gram?",
"1,800g","1.800g","1,200g","1.200g","2,400g","2.400g",
"A","120 × 15 = 1,800gです。"),

("practical","cooking","planning",
"1杯に25mlのソースを使います。24杯では何ml必要ですか。",
"Mỗi phần dùng 25ml sốt. 24 phần cần bao nhiêu ml?",
"600ml","600ml","500ml","500ml","750ml","750ml",
"A","25 × 24 = 600mlです。"),

("practical","service","planning",
"会計は4,280円です。10,000円を受け取りました。お釣りはいくらですか。",
"Hóa đơn 4.280 yên, khách đưa 10.000 yên. Tiền thừa là bao nhiêu?",
"5,720円","5.720 yên","4,720円","4.720 yên","6,720円","6.720 yên",
"A","10,000 - 4,280 = 5,720円です。"),

("practical","service","planning",
"3組のお客様の会計が1,850円、2,300円、1,450円でした。合計はいくらですか。",
"Ba nhóm khách có hóa đơn 1.850, 2.300 và 1.450 yên. Tổng là bao nhiêu?",
"5,600円","5.600 yên","5,500円","5.500 yên","5,700円","5.700 yên",
"A","1,850 + 2,300 + 1,450 = 5,600円です。"),
]

if len(data) != 45:
    raise SystemExit(f"❌ Dữ liệu phải có 45 câu, hiện có {len(data)}")

existing = set(
    Question.objects.values_list("question_jp", flat=True)
)

duplicates = [
    row[3]
    for row in data
    if row[3] in existing
]

if duplicates:
    print("❌ PHÁT HIỆN CÂU TRÙNG:")
    for q in duplicates:
        print("-", q)
    raise SystemExit("Dừng để bảo vệ database.")

exam = Exam.objects.get(level="1", order=3)

if ExamQuestion.objects.filter(exam=exam).exists():
    raise SystemExit("❌ Đề 03 đã có câu. Không import chồng.")

for number, row in enumerate(data, start=1):
    section, category, ptype, qjp, qvi, a, avi, b, bvi, c, cvi, correct, explanation = row

    q = Question.objects.create(
        level="1",
        section=section,
        practical_type=ptype,
        category=category,
        question_jp=qjp,
        question_vi=qvi,
        question_ruby=ruby(qjp),
        option_a=a,
        option_a_vi=avi,
        option_a_ruby=ruby(a),
        option_b=b,
        option_b_vi=bvi,
        option_b_ruby=ruby(b),
        option_c=c,
        option_c_vi=cvi,
        option_c_ruby=ruby(c),
        correct_answer=correct,
        explanation=explanation,
    )

    ExamQuestion.objects.create(
        exam=exam,
        question=q,
        order=number
    )

print("✅ Không trùng câu nào trong database")
print("🎉 ĐỀ 03 ĐÃ TẠO THÀNH CÔNG: 45/45")
