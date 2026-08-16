from django.db import migrations


def update_lessons(apps, schema_editor):
    LearningCategory = apps.get_model('study', 'LearningCategory')
    Lesson = apps.get_model('study', 'Lesson')
    QuickQuestion = apps.get_model('study', 'QuickQuestion')
    category = LearningCategory.objects.get(slug='hygiene-controls')

    data = {
        'food-poisoning-basics': {
            'title_jp': '<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>に<ruby>関<rt>かん</rt></ruby>する<ruby>基礎知識<rt>きそちしき</rt></ruby>',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>は、<ruby>細菌<rt>さいきん</rt></ruby>やウイルスなどが<ruby>付<rt>つ</rt></ruby>いた<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べることなどによって、<ruby>下痢<rt>げり</rt></ruby>、<ruby>腹痛<rt>ふくつう</rt></ruby>、<ruby>発熱<rt>はつねつ</rt></ruby>、<ruby>嘔吐<rt>おうと</rt></ruby>などの<ruby>症状<rt>しょうじょう</rt></ruby>が<ruby>出<rt>で</rt></ruby>ることです。\n\n<ruby>飲食店<rt>いんしょくてん</rt></ruby>では、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>やにおいだけで<ruby>食品<rt>しょくひん</rt></ruby>が<ruby>安全<rt>あんぜん</rt></ruby>かどうかを<ruby>判断<rt>はんだん</rt></ruby>できない<ruby>場合<rt>ばあい</rt></ruby>があります。\n\nそのため、<ruby>原材料<rt>げんざいりょう</rt></ruby>の<ruby>受入<rt>うけい</rt></ruby>れ、<ruby>保管<rt>ほかん</rt></ruby>、<ruby>調理<rt>ちょうり</rt></ruby>、<ruby>提供<rt>ていきょう</rt></ruby>まで<ruby>衛生管理<rt>えいせいかんり</rt></ruby>を<ruby>続<rt>つづ</rt></ruby>けることが<ruby>重要<rt>じゅうよう</rt></ruby>です。''',
        },
        'three-principles-food-poisoning-prevention': {
            'title_jp': '<ruby>食中毒予防<rt>しょくちゅうどくよぼう</rt></ruby>の3<ruby>原則<rt>げんそく</rt></ruby>',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>を<ruby>予防<rt>よぼう</rt></ruby>するための<ruby>基本<rt>きほん</rt></ruby>は「つけない」「<ruby>増<rt>ふ</rt></ruby>やさない」「やっつける」の3つです。\n\n① つけない\n<ruby>手<rt>て</rt></ruby>や<ruby>調理器具<rt>ちょうりきぐ</rt></ruby>などを<ruby>通<rt>とお</rt></ruby>して、<ruby>食品<rt>しょくひん</rt></ruby>に<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>となる<ruby>細菌<rt>さいきん</rt></ruby>などをつけないようにします。\n\n② <ruby>増<rt>ふ</rt></ruby>やさない\n<ruby>細菌<rt>さいきん</rt></ruby>は<ruby>条件<rt>じょうけん</rt></ruby>がそろうと<ruby>増<rt>ふ</rt></ruby>えるため、<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>温度<rt>おんど</rt></ruby>で<ruby>保管<rt>ほかん</rt></ruby>し、<ruby>室温<rt>しつおん</rt></ruby>に<ruby>長<rt>なが</rt></ruby>く<ruby>置<rt>お</rt></ruby>かないことが<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n③ やっつける\n<ruby>加熱<rt>かねつ</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>食品<rt>しょくひん</rt></ruby>は<ruby>中心部<rt>ちゅうしんぶ</rt></ruby>まで<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>加熱<rt>かねつ</rt></ruby>します。''',
        },
        'food-poisoning-bacteria-viruses': {
            'title_jp': '<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>となる<ruby>細菌<rt>さいきん</rt></ruby>・ウイルス',
            'content_jp': '''【<ruby>学習<rt>がくしゅう</rt></ruby>ポイント】\n<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>には、<ruby>細菌<rt>さいきん</rt></ruby>やウイルスなどがあります。<ruby>原因<rt>げんいん</rt></ruby>ごとに<ruby>特徴<rt>とくちょう</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>うため、<ruby>食品<rt>しょくひん</rt></ruby>の<ruby>取扱<rt>とりあつか</rt></ruby>い、<ruby>手洗<rt>てあら</rt></ruby>い、<ruby>加熱<rt>かねつ</rt></ruby>、<ruby>器具<rt>きぐ</rt></ruby>の<ruby>洗浄<rt>せんじょう</rt></ruby>・<ruby>消毒<rt>しょうどく</rt></ruby>などを<ruby>正<rt>ただ</rt></ruby>しく<ruby>行<rt>おこな</rt></ruby>うことが<ruby>重要<rt>じゅうよう</rt></ruby>です。\n\n<ruby>代表的<rt>だいひょうてき</rt></ruby>なものとして、カンピロバクター、サルモネラ<ruby>属菌<rt>ぞくきん</rt></ruby>、<ruby>腸管出血性大腸菌<rt>ちょうかんしゅっけつせいだいちょうきん</rt></ruby>、<ruby>黄色<rt>おうしょく</rt></ruby>ブドウ<ruby>球菌<rt>きゅうきん</rt></ruby>、ノロウイルスなどがあります。\n\nカンピロバクターは<ruby>鶏肉<rt>とりにく</rt></ruby>などの<ruby>取扱<rt>とりあつか</rt></ruby>いで<ruby>注意<rt>ちゅうい</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。<ruby>生<rt>なま</rt></ruby>や<ruby>加熱不十分<rt>かねつふじゅうぶん</rt></ruby>な<ruby>肉<rt>にく</rt></ruby>を<ruby>避<rt>さ</rt></ruby>け、<ruby>二次汚染<rt>にじおせん</rt></ruby>にも<ruby>注意<rt>ちゅうい</rt></ruby>します。''',
        },
        'receiving-ingredients-check': {
            'title_jp': '<ruby>原材料<rt>げんざいりょう</rt></ruby>の<ruby>受入<rt>うけい</rt></ruby>れ<ruby>確認<rt>かくにん</rt></ruby>',
        },
    }

    for slug, values in data.items():
        lesson = Lesson.objects.get(category=category, slug=slug)
        lesson.title_jp = values['title_jp']
        lesson.title_furigana = ''
        if 'content_jp' in values:
            lesson.content_jp = values['content_jp']
            lesson.content_furigana = ''
        lesson.save()

    # Add ruby to quick questions for lessons 1-3 while keeping existing wording.
    replacements = {
        'food-poisoning-basics': [
            ('<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>症状<rt>しょうじょう</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。'),
            ('<ruby>食品<rt>しょくひん</rt></ruby>は、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>やにおいが<ruby>普通<rt>ふつう</rt></ruby>なら<ruby>必<rt>かなら</rt></ruby>ず<ruby>安全<rt>あんぜん</rt></ruby>ですか。'),
            ('<ruby>飲食店<rt>いんしょくてん</rt></ruby>の<ruby>衛生管理<rt>えいせいかんり</rt></ruby>はいつ<ruby>行<rt>おこな</rt></ruby>いますか。'),
            ('<ruby>食中毒予防<rt>しょくちゅうどくよぼう</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>に<ruby>含<rt>ふく</rt></ruby>まれるものはどれですか。'),
            ('<ruby>嘔吐<rt>おうと</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>はどれですか。'),
        ],
        'three-principles-food-poisoning-prevention': [
            ('<ruby>食中毒予防<rt>しょくちゅうどくよぼう</rt></ruby>の3<ruby>原則<rt>げんそく</rt></ruby>として<ruby>正<rt>ただ</rt></ruby>しい<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせはどれですか。'),
            ('<ruby>生肉<rt>なまにく</rt></ruby>を<ruby>切<rt>き</rt></ruby>ったまな<ruby>板<rt>いた</rt></ruby>を、そのまま<ruby>加熱後<rt>かねつご</rt></ruby>の<ruby>食品<rt>しょくひん</rt></ruby>に<ruby>使<rt>つか</rt></ruby>わないことは<ruby>主<rt>おも</rt></ruby>にどの<ruby>原則<rt>げんそく</rt></ruby>ですか。'),
            ('<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>温度<rt>おんど</rt></ruby>で<ruby>保管<rt>ほかん</rt></ruby>することは<ruby>主<rt>おも</rt></ruby>にどの<ruby>原則<rt>げんそく</rt></ruby>ですか。'),
            ('<ruby>食品<rt>しょくひん</rt></ruby>を<ruby>中心部<rt>ちゅうしんぶ</rt></ruby>まで<ruby>適切<rt>てきせつ</rt></ruby>に<ruby>加熱<rt>かねつ</rt></ruby>することは<ruby>主<rt>おも</rt></ruby>にどの<ruby>原則<rt>げんそく</rt></ruby>ですか。'),
            ('<ruby>調理前<rt>ちょうりまえ</rt></ruby>に<ruby>正<rt>ただ</rt></ruby>しく<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>う<ruby>目的<rt>もくてき</rt></ruby>として<ruby>最<rt>もっと</rt></ruby>も<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。'),
        ],
        'food-poisoning-bacteria-viruses': [
            ('<ruby>鶏肉<rt>とりにく</rt></ruby>の<ruby>取扱<rt>とりあつか</rt></ruby>いで<ruby>特<rt>とく</rt></ruby>に<ruby>注意<rt>ちゅうい</rt></ruby>する<ruby>食中毒<rt>しょくちゅうどく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものはどれですか。'),
            ('<ruby>人<rt>ひと</rt></ruby>の<ruby>手<rt>て</rt></ruby>などを<ruby>介<rt>かい</rt></ruby>して<ruby>食品<rt>しょくひん</rt></ruby>に<ruby>付着<rt>ふちゃく</rt></ruby>することがあるものはどれですか。'),
            ('ノロウイルス<ruby>対策<rt>たいさく</rt></ruby>として<ruby>重要<rt>じゅうよう</rt></ruby>なものはどれですか。'),
            ('<ruby>生肉<rt>なまにく</rt></ruby>に<ruby>使<rt>つか</rt></ruby>った<ruby>器具<rt>きぐ</rt></ruby>から<ruby>他<rt>ほか</rt></ruby>の<ruby>食品<rt>しょくひん</rt></ruby>に<ruby>原因物質<rt>げんいんぶっしつ</rt></ruby>が<ruby>移<rt>うつ</rt></ruby>ることを<ruby>何<rt>なん</rt></ruby>と<ruby>考<rt>かんが</rt></ruby>えますか。'),
            ('<ruby>食中毒対策<rt>しょくちゅうどくたいさく</rt></ruby>として<ruby>不適切<rt>ふてきせつ</rt></ruby>なものはどれですか。'),
        ],
    }
    for slug, questions in replacements.items():
        lesson = Lesson.objects.get(category=category, slug=slug)
        for obj, ruby in zip(QuickQuestion.objects.filter(lesson=lesson).order_by('order', 'id'), questions):
            obj.question_furigana = ruby
            obj.save(update_fields=['question_furigana'])


class Migration(migrations.Migration):
    dependencies = [('study', '0029_add_ginou1_hygiene_lesson6')]
    operations = [migrations.RunPython(update_lessons, migrations.RunPython.noop)]
