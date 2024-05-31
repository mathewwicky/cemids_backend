from django.contrib import admin
from .models import ClimateEvent

class ClimateEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'location', 'date', 'time')
    list_filter = ('date', 'location')
    search_fields = ('event_title', 'location')

admin.site.register(ClimateEvent, ClimateEventAdmin)
