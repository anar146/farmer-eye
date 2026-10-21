from django.contrib import admin
from .models import Scan

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ("id", "crop", "disease", "confidence", "severity", "created_at")
    list_filter = ("crop", "disease")
