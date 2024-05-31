from django.contrib import admin
from .models import ProfileSettings

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'email', 'phonenumber', 'gender', 'nationality', 'date_of_birth', 'job_title')
    search_fields = ('first_name', 'surname', 'email', 'phonenumber')
    list_filter = ('gender', 'nationality', 'job_title')
    ordering = ('first_name', 'surname')

admin.site.register(ProfileSettings, ProfileAdmin)
