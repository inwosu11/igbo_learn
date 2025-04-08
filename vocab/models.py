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
