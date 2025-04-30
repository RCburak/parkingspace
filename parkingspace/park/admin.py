from django.contrib import admin
from .models import ParkYeri

@admin.register(ParkYeri)
class ParkYeriAdmin(admin.ModelAdmin):
    list_display = ('plaka', 'giris_zamani', 'cikis_zamani', 'aktif_mi')
    search_fields = ('plaka',)
    list_filter = ('aktif_mi',)
    ordering = ('-giris_zamani',)
