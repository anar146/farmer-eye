from django.db import models

class Scan(models.Model):
    image = models.ImageField(upload_to="scans/%Y/%m/")
    crop = models.CharField(max_length=100, blank=True)
    disease = models.CharField(max_length=150, blank=True)
    confidence = models.FloatField(default=0)
    severity = models.CharField(max_length=20, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.crop} - {self.disease} ({self.created_at:%d %b %H:%M})"
