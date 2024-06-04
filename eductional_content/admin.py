from django.contrib import admin
from .models import EducationalContent

class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'author', 'readmore')
    search_fields = ('subtitle', 'author')

admin.site.register(EducationalContent, EducationalContentAdmin)
