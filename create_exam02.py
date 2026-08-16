import os
import json
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
# ===== 学科試験：衛生管理 10 =====
["theory","hygiene","",
"調理場に入る前に確認することとして、最も適切なものはどれですか。",
"Trước khi vào khu vực bếp, điều nào cần kiểm tra phù hợp nhất?",
"手指や服装が清潔であること","Tay và trang phục sạch sẽ",
"今日の売上だけ","Chỉ doanh thu hôm nay",
"お客様の人数だけ","Chỉ số lượng khách",
"A",
"調理場へ入る前には、手指や服装など衛生状態を確認します。"],

["theory","hygiene","",
"冷蔵庫に食品を入れすぎることによる問題はどれですか。",
"Vấn đề khi nhét quá nhiều thực phẩm vào tủ lạnh là gì?",
"冷気が十分に循環しにくくなる","Khí lạnh khó lưu thông đầy đủ",
"食品が必ず長持ちする","Thực phẩm chắc chắn để được lâu hơn",
"電気を使わなくなる","Không cần dùng điện",
"A",
"食品を詰め込みすぎると冷気の循環が悪くなり、適切な温度管理が難しくなります。"],

["theory","hygiene","",
"手洗いが必要なタイミングとして適切なものはどれですか。",
"Thời điểm nào thích hợp để rửa tay?",
"トイレの後","Sau khi đi vệ sinh",
"勤務終了後だけ","Chỉ sau khi kết thúc ca",
"一日に一回だけ","Chỉ một lần mỗi ngày",
"A",
"トイレの後など、汚染の可能性がある場合には必ず手洗いを行います。"],

["theory","hygiene","",
"食品を床に直接置いてはいけない主な理由は何ですか。",
"Lý do chính không được đặt thực phẩm trực tiếp xuống sàn là gì?",
"汚染される危険があるため","Vì có nguy cơ bị nhiễm bẩn",
"食品が軽くなるため","Vì thực phẩm sẽ nhẹ đi",
"値段が変わるため","Vì giá sẽ thay đổi",
"A",
"床は汚染されている可能性が高いため、食品を直接置いてはいけません。"],

["theory","hygiene","",
"清掃用の薬剤を食品の近くに保管しない理由として適切なのはどれですか。",
"Tại sao không nên bảo quản hóa chất vệ sinh gần thực phẩm?",
"食品への混入を防ぐため","Để tránh hóa chất lẫn vào thực phẩm",
"薬剤の色を守るため","Để giữ màu hóa chất",
"食品を冷やすため","Để làm lạnh thực phẩm",
"A",
"洗剤や薬剤は誤使用や食品への混入を防ぐため、決められた場所で管理します。"],

["theory","hygiene","",
"冷凍庫から取り出した食品を解凍した後、再び冷凍する場合に注意する理由は何ですか。",
"Tại sao cần cẩn thận khi đông lạnh lại thực phẩm đã rã đông?",
"品質や衛生上の問題が生じる可能性があるため","Vì có thể phát sinh vấn đề chất lượng và vệ sinh",
"食品の色が必ず青くなるため","Vì thực phẩm chắc chắn chuyển màu xanh",
"容器が重くなるため","Vì hộp sẽ nặng hơn",
"A",
"解凍・再冷凍の繰り返しは品質低下や衛生上のリスクにつながるため、店舗のルールに従います。"],

["theory","hygiene","",
"調理従事者が発熱している場合の対応として適切なのはどれですか。",
"Nhân viên chế biến bị sốt thì xử lý nào phù hợp?",
"責任者に報告する","Báo cho người phụ trách",
"何も言わずに働く","Không nói gì và tiếp tục làm",
"マスクだけすれば必ず調理できる","Chỉ cần đeo khẩu trang là chắc chắn được nấu",
"A",
"健康状態に異常がある場合は自己判断せず責任者へ報告します。"],

["theory","hygiene","",
"使用後のふきんを衛生的に管理する方法として適切なのはどれですか。",
"Cách quản lý khăn lau sau khi sử dụng sao cho vệ sinh là gì?",
"決められた方法で洗浄・消毒する","Rửa và khử trùng theo phương pháp quy định",
"濡れたまま放置する","Để nguyên khi còn ướt",
"床に置いて乾かす","Đặt dưới sàn để phơi",
"A",
"ふきんは汚染源にならないよう、洗浄・消毒・乾燥など適切に管理します。"],

["theory","hygiene","",
"食品の保管で先入れ先出しを行う目的として適切なのはどれですか。",
"Mục đích của nguyên tắc nhập trước xuất trước trong bảo quản thực phẩm là gì?",
"古いものから使用し期限管理をしやすくする","Dùng hàng cũ trước để dễ quản lý hạn",
"新しい食品だけ捨てる","Chỉ bỏ thực phẩm mới",
"食品の温度を上げる","Tăng nhiệt độ thực phẩm",
"A",
"先入れ先出しによって在庫や期限を適切に管理できます。"],

["theory","hygiene","",
"調理場で害虫を見つけた場合、適切な対応はどれですか。",
"Nếu phát hiện côn trùng gây hại trong bếp, nên xử lý thế nào?",
"責任者に報告し適切な対策を行う","Báo người phụ trách và thực hiện biện pháp phù hợp",
"そのままにする","Để nguyên",
"食品の中に隠す","Giấu vào trong thực phẩm",
"A",
"害虫は食品汚染につながるため、発見した場合は報告し適切に対応します。"],

# ===== 学科試験：飲食物調理 10 =====
["theory","cooking","",
"同じ料理を毎回同じ品質で提供するために重要なことはどれですか。",
"Điều quan trọng để luôn phục vụ cùng một món với chất lượng ổn định là gì?",
"レシピや分量を守る","Tuân thủ công thức và định lượng",
"毎回自由に量を変える","Mỗi lần tự thay đổi lượng",
"計量しない","Không cân đo",
"A",
"レシピと標準量を守ることで品質を安定させます。"],

["theory","cooking","",
"包丁を使用するときの安全な方法として適切なのはどれですか。",
"Cách sử dụng dao an toàn là gì?",
"正しい持ち方と作業方法を守る","Tuân thủ cách cầm và thao tác đúng",
"刃を人に向ける","Hướng lưỡi dao về phía người khác",
"濡れた床に置く","Đặt trên sàn ướt",
"A",
"包丁は正しい取り扱い方法を守り、事故を防ぎます。"],

["theory","cooking","",
"揚げ物を調理するときに注意することはどれですか。",
"Khi chiên thực phẩm cần chú ý điều gì?",
"油の温度や状態を確認する","Kiểm tra nhiệt độ và tình trạng dầu",
"水を大量に油へ入れる","Cho nhiều nước vào dầu",
"油を床にこぼす","Đổ dầu xuống sàn",
"A",
"揚げ物では油温と油の状態を適切に管理することが重要です。"],

["theory","cooking","",
"野菜を洗浄する目的として最も適切なものはどれですか。",
"Mục đích phù hợp nhất của việc rửa rau là gì?",
"汚れや異物を除くため","Để loại bỏ bụi bẩn và dị vật",
"必ず色を変えるため","Để chắc chắn đổi màu",
"重さを増やすため","Để tăng trọng lượng",
"A",
"野菜は必要に応じて洗浄し、汚れや異物を除去します。"],

["theory","cooking","",
"注文数に合わせて食材を準備することで期待できることはどれですか。",
"Chuẩn bị nguyên liệu phù hợp số lượng order giúp điều gì?",
"食品ロスの削減","Giảm lãng phí thực phẩm",
"必ず調理時間が倍になる","Thời gian nấu chắc chắn tăng gấp đôi",
"衛生管理が不要になる","Không cần quản lý vệ sinh",
"A",
"必要量を把握して準備することで食品ロスや過剰仕込みを減らせます。"],

["theory","cooking","",
"盛り付ける前に皿を確認する理由として適切なのはどれですか。",
"Tại sao cần kiểm tra đĩa trước khi trình bày món?",
"汚れや破損がないか確認するため","Để kiểm tra có bẩn hoặc hư hỏng không",
"皿の値段を決めるため","Để quyết định giá chiếc đĩa",
"お客様の年齢を確認するため","Để kiểm tra tuổi khách",
"A",
"清潔で破損のない食器を使用することが安全な提供につながります。"],

["theory","cooking","",
"食材の切り方をそろえる利点として適切なのはどれですか。",
"Lợi ích của việc cắt nguyên liệu đồng đều là gì?",
"加熱や仕上がりを均一にしやすい","Dễ làm chín và hoàn thiện đồng đều",
"必ず価格が下がる","Giá chắc chắn giảm",
"保存期限がなくなる","Không còn hạn bảo quản",
"A",
"大きさをそろえることで加熱のばらつきを減らし、品質を安定させやすくなります。"],

["theory","cooking","",
"大量調理をするときに重要なことはどれですか。",
"Khi nấu số lượng lớn, điều nào quan trọng?",
"必要量と作業手順を事前に確認する","Kiểm tra trước lượng cần thiết và quy trình",
"注文を確認しない","Không kiểm tra order",
"すべて目分量で作る","Làm tất cả bằng ước lượng",
"A",
"大量調理では量、時間、作業手順などを計画的に確認します。"],

["theory","cooking","",
"調理機器に異常な音がした場合の適切な対応はどれですか。",
"Nếu thiết bị bếp phát ra tiếng bất thường, xử lý nào phù hợp?",
"使用を止め責任者に報告する","Ngừng sử dụng và báo người phụ trách",
"強くたたいて使う","Đập mạnh rồi tiếp tục dùng",
"そのまま長時間使う","Tiếp tục dùng lâu",
"A",
"異常がある機器を無理に使用すると事故につながるため、使用を止めて報告します。"],

["theory","cooking","",
"料理を提供する直前の確認として適切なのはどれですか。",
"Kiểm tra nào phù hợp ngay trước khi phục vụ món?",
"注文内容と料理が合っているか確認する","Kiểm tra món có đúng order không",
"厨房の家賃を確認する","Kiểm tra tiền thuê bếp",
"従業員の住所を確認する","Kiểm tra địa chỉ nhân viên",
"A",
"誤提供を防ぐため、注文と料理を確認してから提供します。"],

# ===== 学科試験：接客全般 10 =====
["theory","service","",
"お客様を席へ案内するときに大切なことはどれですか。",
"Điều quan trọng khi hướng dẫn khách vào chỗ ngồi là gì?",
"安全で丁寧に案内する","Hướng dẫn an toàn và lịch sự",
"何も言わず指だけさす","Không nói gì chỉ tay",
"走らせる","Bắt khách chạy",
"A",
"店内の状況を確認しながら丁寧に案内します。"],

["theory","service","",
"注文を復唱する主な目的は何ですか。",
"Mục đích chính của việc nhắc lại order là gì?",
"注文間違いを防ぐため","Để tránh sai order",
"会話を長くするため","Để kéo dài cuộc nói chuyện",
"価格を変えるため","Để thay đổi giá",
"A",
"注文内容を復唱して確認することで誤りを防ぎます。"],

["theory","service","",
"お客様から質問されて分からない場合、適切な対応はどれですか。",
"Nếu khách hỏi nhưng bạn không biết, xử lý nào phù hợp?",
"確認してから正確に答える","Xác nhận rồi trả lời chính xác",
"適当に答える","Trả lời đại",
"無視する","Phớt lờ",
"A",
"分からない場合は推測せず、確認して正確に案内します。"],

["theory","service","",
"車いすのお客様への対応として適切なのはどれですか。",
"Cách phục vụ phù hợp đối với khách dùng xe lăn là gì?",
"必要に応じて安全な移動を支援する","Hỗ trợ di chuyển an toàn khi cần",
"必ず自分で移動させる","Luôn tự ý di chuyển họ",
"対応しない","Không phục vụ",
"A",
"お客様の意思を確認し、必要に応じて安全に配慮した支援を行います。"],

["theory","service","",
"店内で大きな音がしてお客様が驚いている場合、どうしますか。",
"Nếu có tiếng động lớn trong cửa hàng làm khách giật mình, nên làm gì?",
"状況を確認し必要に応じて説明する","Kiểm tra tình hình và giải thích khi cần",
"笑うだけ","Chỉ cười",
"無視する","Phớt lờ",
"A",
"安全を確認し、お客様が不安にならないよう必要な案内を行います。"],

["theory","service","",
"会計時に金額を間違えたことに気づいた場合、適切な対応はどれですか。",
"Nếu phát hiện tính sai tiền, xử lý nào phù hợp?",
"確認して正しい金額に訂正する","Kiểm tra và sửa về số tiền đúng",
"そのままにする","Để nguyên",
"お客様のせいにする","Đổ lỗi cho khách",
"A",
"会計ミスは確認し、速やかに訂正して適切に対応します。"],

["theory","service","",
"お客様の忘れ物を見つけた場合の対応として適切なのはどれですか。",
"Nếu phát hiện đồ khách bỏ quên, nên xử lý thế nào?",
"店のルールに従って責任者へ報告する","Báo người phụ trách theo quy định cửa hàng",
"自分で持ち帰る","Tự mang về",
"捨てる","Vứt đi",
"A",
"忘れ物は店舗の規定に従って適切に管理します。"],

["theory","service","",
"混雑時の接客で重要なことはどれですか。",
"Điều quan trọng khi phục vụ lúc đông khách là gì?",
"落ち着いて正確に対応する","Bình tĩnh và xử lý chính xác",
"確認をすべて省略する","Bỏ tất cả bước xác nhận",
"お客様を無視する","Phớt lờ khách",
"A",
"混雑時も安全と正確さを優先し、落ち着いて対応します。"],

["theory","service","",
"お客様が店内で気分が悪くなった場合、適切な対応はどれですか。",
"Nếu khách cảm thấy không khỏe trong cửa hàng, xử lý nào phù hợp?",
"安全を確認し責任者に報告して必要な対応を行う","Kiểm tra an toàn, báo người phụ trách và hỗ trợ cần thiết",
"すぐに店外へ出す","Lập tức đuổi ra ngoài",
"何もしない","Không làm gì",
"A",
"お客様の状態を確認し、必要に応じて責任者への報告や救護対応を行います。"],

["theory","service","",
"閉店時に客席で確認すべきこととして適切なのはどれですか。",
"Khi đóng cửa, điều nào cần kiểm tra tại khu vực khách?",
"忘れ物や危険箇所がないか","Có đồ bỏ quên hoặc vị trí nguy hiểm không",
"料理の値段だけ","Chỉ giá món ăn",
"従業員の趣味","Sở thích nhân viên",
"A",
"閉店時には安全、忘れ物、清掃状態などを確認します。"],

# ===== 実技 判断試験 9 =====
["practical","hygiene","judgment",
"冷蔵庫の扉が長時間開いたままになっています。最初に行うべき対応はどれですか。",
"Cửa tủ lạnh đã mở trong thời gian dài. Trước tiên nên làm gì?",
"扉を閉め、温度や食品の状態を確認する","Đóng cửa và kiểm tra nhiệt độ, tình trạng thực phẩm",
"さらに扉を開ける","Mở cửa rộng thêm",
"電源を切る","Tắt nguồn",
"A",
"温度上昇の可能性があるため、まず扉を閉め、温度や食品の状態を確認します。"],

["practical","hygiene","judgment",
"調理台に生肉の汁がこぼれました。次の対応として適切なのはどれですか。",
"Nước thịt sống đổ lên bàn chế biến. Xử lý nào phù hợp tiếp theo?",
"決められた方法で洗浄・消毒する","Rửa và khử trùng theo quy định",
"乾くまで待つ","Chờ khô",
"布で隠す","Che bằng khăn",
"A",
"生肉由来の汚染を広げないよう、適切に洗浄・消毒します。"],

["practical","hygiene","judgment",
"従業員が手に傷を負っています。食品を扱う場合の対応として適切なのはどれですか。",
"Nhân viên bị thương ở tay. Nếu xử lý thực phẩm thì nên làm gì?",
"傷を適切に保護し店舗のルールに従う","Bảo vệ vết thương đúng cách và tuân thủ quy định",
"そのまま素手で作業する","Làm tay trần như bình thường",
"傷を食品で隠す","Che vết thương bằng thực phẩm",
"A",
"傷口からの汚染を防ぐため、適切な保護と店舗ルールに従った対応が必要です。"],

["practical","cooking","judgment",
"焼いた肉の中心がまだ生のように見えます。どうしますか。",
"Thịt đã nướng nhưng phần giữa vẫn có vẻ sống. Nên làm gì?",
"必要な加熱を追加し安全を確認する","Gia nhiệt thêm và xác nhận an toàn",
"そのまま提供する","Phục vụ luôn",
"冷たい水をかけて提供する","Dội nước lạnh rồi phục vụ",
"A",
"中心まで必要な加熱ができていることを確認してから提供します。"],

["practical","cooking","judgment",
"注文票と完成した料理が違うことに気づきました。どうしますか。",
"Phát hiện món hoàn thành không khớp phiếu order. Nên làm gì?",
"提供を止め注文内容を確認する","Ngừng phục vụ và kiểm tra order",
"そのまま出す","Phục vụ luôn",
"注文票を捨てる","Vứt phiếu order",
"A",
"誤提供防止のため、注文と料理を確認してから提供します。"],

["practical","cooking","judgment",
"調理機器から煙が出ています。最も適切な対応はどれですか。",
"Thiết bị bếp đang bốc khói. Xử lý nào phù hợp nhất?",
"安全を確保し使用を止め責任者に報告する","Đảm bảo an toàn, ngừng sử dụng và báo người phụ trách",
"そのまま使い続ける","Tiếp tục dùng",
"水を必ず大量にかける","Luôn đổ thật nhiều nước",
"A",
"機器の異常時は安全を最優先し、使用停止と報告を行います。"],

["practical","service","judgment",
"お客様が注文した飲み物をこぼしてしまいました。対応として適切なのはどれですか。",
"Khách làm đổ đồ uống. Xử lý nào phù hợp?",
"安全を確保し速やかに清掃する","Đảm bảo an toàn và nhanh chóng vệ sinh",
"閉店まで放置する","Để đến khi đóng cửa",
"お客様を責める","Trách khách",
"A",
"転倒事故などを防ぐため、こぼれた液体は速やかに安全に処理します。"],

["practical","service","judgment",
"お客様が料理に異物があると申し出ました。最初の対応はどれですか。",
"Khách báo có dị vật trong món ăn. Xử lý đầu tiên là gì?",
"話を聞き、提供を止めて責任者へ報告する","Lắng nghe, ngừng phục vụ và báo người phụ trách",
"異物だけ取る","Chỉ lấy dị vật ra",
"無視する","Phớt lờ",
"A",
"異物混入の申し出は重大なため、状況確認と責任者への報告を行います。"],

["practical","service","judgment",
"通路に荷物が置かれ、お客様が通りにくくなっています。どうしますか。",
"Hàng hóa đặt trên lối đi khiến khách khó đi. Nên làm gì?",
"安全な場所へ移動して通路を確保する","Di chuyển đến chỗ an toàn để đảm bảo lối đi",
"そのままにする","Để nguyên",
"さらに荷物を置く","Đặt thêm hàng",
"A",
"お客様や従業員の安全のため、通路を確保します。"],

# ===== 実技 計画立案 6 =====
["practical","hygiene","planning",
"消毒液を1L作ります。原液100mlに対して水900mlを使います。3L作る場合、原液は何ml必要ですか。",
"Pha 1L dung dịch dùng 100ml dung dịch gốc và 900ml nước. Pha 3L cần bao nhiêu ml dung dịch gốc?",
"300ml","300ml","100ml","100ml","900ml","900ml",
"A",
"100ml × 3 = 300mlです。"],

["practical","hygiene","planning",
"冷蔵庫を1時間ごとに確認します。8時間勤務の場合、勤務開始時を除いて何回確認しますか。",
"Kiểm tra tủ lạnh mỗi giờ. Trong ca 8 giờ, không tính lúc bắt đầu thì kiểm tra bao nhiêu lần?",
"8回","8 lần","4回","4 lần","16回","16 lần",
"A",
"1時間ごとに8時間勤務するため、開始時を除けば8回の確認です。"],

["practical","cooking","planning",
"1人分に80gの肉を使います。25人分では何g必要ですか。",
"Mỗi phần dùng 80g thịt. 25 phần cần bao nhiêu gram?",
"2,000g","2.000g","800g","800g","3,200g","3.200g",
"A",
"80 × 25 = 2,000gです。"],

["practical","cooking","planning",
"1皿に40mlのスープを使います。18皿では何ml必要ですか。",
"Mỗi đĩa dùng 40ml súp. 18 đĩa cần bao nhiêu ml?",
"720ml","720ml","580ml","580ml","820ml","820ml",
"A",
"40 × 18 = 720mlです。"],

["practical","service","planning",
"会計は3,680円です。5,000円を受け取りました。お釣りはいくらですか。",
"Hóa đơn 3.680 yên, khách đưa 5.000 yên. Tiền thừa bao nhiêu?",
"1,320円","1.320 yên","1,420円","1.420 yên","2,320円","2.320 yên",
"A",
"5,000 - 3,680 = 1,320円です。"],

["practical","service","planning",
"4人のお客様がそれぞれ900円、1,100円、750円、1,250円の商品を注文しました。合計はいくらですか。",
"Bốn khách gọi món giá 900, 1.100, 750 và 1.250 yên. Tổng cộng bao nhiêu?",
"4,000円","4.000 yên","3,800円","3.800 yên","4,200円","4.200 yên",
"A",
"900 + 1,100 + 750 + 1,250 = 4,000円です。"],
]

assert len(data) == 45, f"Phải có 45 câu, hiện có {len(data)}"

existing = set(
    Question.objects.values_list("question_jp", flat=True)
)

duplicates = [x[3] for x in data if x[3] in existing]

if duplicates:
    print("❌ PHÁT HIỆN CÂU TRÙNG:")
    for q in duplicates:
        print(q)
    raise SystemExit("Dừng import để bảo vệ dữ liệu.")

payload = []

for row in data:
    section, category, ptype, qjp, qvi, a, avi, b, bvi, c, cvi, correct, explanation = row

    payload.append({
        "section": section,
        "category": category,
        "practical_type": ptype,
        "question_jp": qjp,
        "question_vi": qvi,
        "option_a": a,
        "option_a_vi": avi,
        "option_b": b,
        "option_b_vi": bvi,
        "option_c": c,
        "option_c_vi": cvi,
        "correct_answer": correct,
        "explanation": explanation,
    })

with open("exam02.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print("✅ Đã tạo exam02.json")
print("✅ Số câu:", len(payload))
print("✅ Không trùng câu nào trong database")

exam = Exam.objects.get(level="1", order=2)

if ExamQuestion.objects.filter(exam=exam).exists():
    raise SystemExit("❌ Đề 02 đã có câu. Không import để tránh trùng.")

for number, x in enumerate(payload, start=1):
    q = Question.objects.create(
        level="1",
        section=x["section"],
        practical_type=x["practical_type"],
        category=x["category"],
        question_jp=x["question_jp"],
        question_vi=x["question_vi"],
        question_ruby=ruby(x["question_jp"]),
        option_a=x["option_a"],
        option_a_vi=x["option_a_vi"],
        option_a_ruby=ruby(x["option_a"]),
        option_b=x["option_b"],
        option_b_vi=x["option_b_vi"],
        option_b_ruby=ruby(x["option_b"]),
        option_c=x["option_c"],
        option_c_vi=x["option_c_vi"],
        option_c_ruby=ruby(x["option_c"]),
        correct_answer=x["correct_answer"],
        explanation=x["explanation"],
    )

    ExamQuestion.objects.create(
        exam=exam,
        question=q,
        order=number
    )

print("🎉 ĐỀ 02 ĐÃ IMPORT THÀNH CÔNG: 45/45")
