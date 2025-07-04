from django.db import models

class IgboAlphabet(models.Model):
    """
    Igbo Alphabet Model
    """
    alphabet = models.CharField(max_length=1, unique=True)
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)
    sound_file = models.FileField(upload_to='alphabet_sounds/', null=True, blank=True)
   
    class Meta:
        verbose_name = "Igbo Alphabet"
        verbose_name_plural = "Igbo Alphabets"
   
    def __str__(self):
        return self.alphabet

class IgboWord(models.Model):
    """
    Igbo Word Model
    """
    word = models.CharField(max_length=100, unique=True)
    meaning = models.CharField(max_length=200)
    example_sentence = models.TextField(null=True, blank=True)
    sound_file = models.FileField(upload_to='word_sounds/', null=True, blank=True)

    class Meta:
        verbose_name = "Igbo Word"
        verbose_name_plural = "Igbo Words"

    def __str__(self):
        return self.word
class Word(models.Model):
    english_definition = models.TextField()
    part_of_speech = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.english_definition
class DialectWord(models.Model):
    DIALECT_CHOICES = [
        ('CENTRAL', 'Central'),
        ('NGWA', 'Ngwa'),
        ('NSUKKA', 'Nsukka'),
    ]

    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='dialect_words')
    dialect = models.CharField(max_length=20, choices=DIALECT_CHOICES)
    spelling = models.CharField(max_length=100)
    audio_pronunciation = models.FileField(upload_to='audio/', blank=True, null=True)

    class Meta:
        unique_together = ('word', 'dialect')

    def __str__(self):
        return f"{self.spelling} ({self.dialect})"