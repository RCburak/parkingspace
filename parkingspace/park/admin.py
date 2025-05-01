from django.contrib import admin
from django.utils.html import format_html
from .models import ParkingLocation

@admin.register(ParkingLocation)
class ParkingLocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'latitude',
        'longitude',
        'colored_status',
        'video_url_display',
        'map_url_display',
    )
    search_fields = ('name',)
    list_filter = ('status',)
    ordering = ('name',)

    def colored_status(self, obj):
        color = 'green' if obj.status == 'Available' else 'red'
        return format_html('<strong style="color: {};">{}</strong>', color, obj.status)
    colored_status.short_description = 'Status'

    def video_url_display(self, obj):
        return format_html('<a href="{}" target="_blank">📹 Video</a>', obj.video_url)
    video_url_display.short_description = 'Video Link'

    def map_url_display(self, obj):
        return format_html('<a href="{}" target="_blank">🗺️ View Map</a>', obj.map_url)
    map_url_display.short_description = 'Map Link'
