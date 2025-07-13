import csv
from vocab.models import IgboAlphabet

with open('data/alphabet.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile) # this uses headers as keys
    
    for row in reader:
        letter = row['LETTER'].strip()
        
        # Check if it already exists to prevent duplicates
        if letter and not IgboAlphabet.objects.filter(alphabet=letter).exists():
            IgboAlphabet.objects.create(
                alphabet=letter,
                name=row['LETTER SOUND AND PHONETIC PRONOUNCIATION'].strip(),
                sound=row['IGBO WORD WITH WORD USAGE'].strip()
                # Add sound file if you ever add path logic
            )