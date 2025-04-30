from django.db import models

class ParkYeri(models.Model):
    plaka = models.CharField(max_length=20)
    giris_zamani = models.DateTimeField(auto_now_add=True)
    cikis_zamani = models.DateTimeField(null=True, blank=True)
    aktif_mi = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plaka} - {'Aktif' if self.aktif_mi else 'Çıkış yaptı'}"
