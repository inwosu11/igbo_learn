from django.contrib import admin
from .models import IgboAlphabet

# Register your models here.

# # Register the IgboAlphabet model with the admin site
# admin.site.register(IgboAlphabet)

@admin.register(IgboAlphabet)
class IgboAlphabetAdmin(admin.ModelAdmin):
    """
    igbo alphabet admin
    
    """
    list_display = ('alphabet', 'name', 'sound', 'sound_file')
    search_fields = ('alphabet', 'name')
    list_filter = ('alphabet',)
    ordering = ('alphabet',)
    