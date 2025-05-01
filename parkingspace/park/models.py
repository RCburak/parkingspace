from django.db import models

class ParkingLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Full', 'Full')], default='Available')
    
    # Gerçekçi varsayılan URL'ler
    video_url = models.URLField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ')  # YouTube video örneği
    map_url = models.URLField(default='https://www.google.com/maps?q=41.09599179259704,29.092028542328315')  # Google Maps URL'si

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"
