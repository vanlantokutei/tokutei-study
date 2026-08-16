from django.db import migrations


def remove_duplicate_vocabulary(apps, schema_editor):
    VocabularyEntry = apps.get_model('study', 'VocabularyEntry')

    # Keep the oldest entry for each exact Japanese word and remove later duplicates.
    seen = set()
    duplicate_ids = []
    for entry in VocabularyEntry.objects.all().order_by('id').only('id', 'word_jp'):
        key = (entry.word_jp or '').strip()
        if not key:
            continue
        if key in seen:
            duplicate_ids.append(entry.id)
        else:
            seen.add(key)

    if duplicate_ids:
        VocabularyEntry.objects.filter(id__in=duplicate_ids).delete()


class Migration(migrations.Migration):
    dependencies = [('study', '0021_premiumprofile_premiumrequest')]
    operations = [migrations.RunPython(remove_duplicate_vocabulary, migrations.RunPython.noop)]
