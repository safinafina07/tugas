from django.db import models

# Create your models here.
    
class beranda(models.Model):
    pesanan = models.CharField(max_length=40)
    dikemas = models.CharField(max_length=40)
    