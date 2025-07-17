import csv
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from vocab.models import IgboWord, DialectWord
file_path = 'data/words.csv'

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0 
    for row in reader:
        word = row['IGBO WORD'].strip()
        meaning = row['ENGLISH TRANSLATION'].strip()
        sentence = row['IGBO SENTENCE'].strip()
        dialect_info = row.get('DIALECT/VARIA', '').strip()
        spelling_variant = row.get('SPELLING VAR', '').strip()
        
        if not word or not meaning:
            continue
        
        igbo_word, created = IgboWord.objects.get_or_create(
            word = word,
            defaults={
                'meaning': meaning,
                'example_sentence': sentence or None,
            }
        )
        
        if dialect_info and spelling_variant:
            dialects = [d.strip().upper() for d in dialect_info.split('/')]
            spellings = [s.strip() for s in spelling_variant.split('/')]
            for dialect, spelling in zip(dialects, spellings):
                if dialect in dict(DialectWord.DIALECT_CHOICES).keys():
                    DialectWord.objects.get_or_create(
                        word=igbo_word,
                        dialect=dialect,
                        spelling=spelling
                    )

        count += 1

print(f"Imported {count} Igbo words.")