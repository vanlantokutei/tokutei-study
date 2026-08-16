from django.db import migrations


TOPIC_WORDS = {
    'food_poisoning': [
        '食中毒', '予防', '三原則', '細菌', 'ウイルス', '腸管出血性大腸菌',
        'カンピロバクター', 'サルモネラ属菌', '黄色ブドウ球菌', 'ウェルシュ菌',
        'セレウス菌', '腸炎ビブリオ', 'ノロウイルス', '寄生虫', 'アニサキス',
        '交差汚染', '二次汚染', '体調不良', 'おう吐', '下痢', '腹痛', '異物', '混入',
    ],
    'ingredients_tools': [
        '原材料', '調理器具', 'まな板', '包丁', '生肉', '二枚貝', '食材', '調味料',
        '塩', '砂糖', '酢', '醤油', '味噌', '出汁', '香辛料', '鍋', 'フライパン',
        'オーブン', '電子レンジ', '炊飯器', '計量器',
    ],
    'cooking_actions': [
        '下処理', '解凍', '切る', '刻む', 'むく', '洗う', '混ぜる', 'こねる', '焼く',
        '煮る', '蒸す', '揚げる', '炒める', '茹でる', '炊く', '盛り付け', '沸騰',
        '予熱', '焦げる', '生焼け', '水切り', '湯切り', '水にさらす', '千切り',
        'みじん切り', '輪切り', 'くし形切り', 'さいの目切り', '薄切り', '冷却', '解凍',
    ],
    'temperature_numbers': [
        '温度管理', '保存', '賞味期限', '消費期限', '中心温度', '加熱', '加熱不足',
        '火加減', '強火', '中火', '弱火', '油温', '焼き加減', '冷蔵庫', '冷凍庫',
    ],
    'communication': [
        '接客全般', '接客サービス', 'お客様', '挨拶', '表情', '姿勢', 'お辞儀', '案内',
        '注文', '注文を受ける', '復唱', '配膳', '下膳', '提供',
    ],
    'store_operations': [
        '会計', '伝票', '現金', 'お釣り', '領収書', '予約', '満席', '空席', '禁煙席',
        '営業時間', '開店', '閉店', '営業準備', '清掃作業', '苦情', '責任者', '報告',
        '対応', '謝罪', '納品', '受入れ',
    ],
    'allergy_diversity': [
        '食物アレルギー', 'アレルゲン', '特定原材料', '飲酒', '未成年者', '年齢確認',
        '栄養', '味覚', '甘味', '塩味', '酸味', '苦味', 'うま味', '宗教',
        'ベジタリアン', '車いす', '補助犬', '高齢者',
    ],
    'workplace_safety': [
        '非常口', '避難', '防災', '清掃', '廃棄物', '処理', '消毒', '殺菌', '洗浄',
        '健康管理', '作業着', '着用', '手洗い', '従業員', '身だしなみ',
    ],
    'practical_planning': [
        '計量', '歩留まり', '可食部', '廃棄率', '記録', '重要管理ポイント',
        '飲食物調理', '衛生管理',
    ],
}


def classify_topics(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    VocabularyEntry.objects.update(topic='core')
    for topic, words in TOPIC_WORDS.items():
        VocabularyEntry.objects.filter(word_jp__in=words).update(topic=topic)


def reset_topics(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')
    VocabularyEntry.objects.update(topic='core')


class Migration(migrations.Migration):
    dependencies = [('study', '0015_vocabularyentry_topic_and_more')]
    operations = [migrations.RunPython(classify_topics, reset_topics)]
