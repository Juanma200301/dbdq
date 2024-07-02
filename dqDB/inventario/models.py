from django.db import models

# Create your models here.

from django.db import models

class IceCream(models.Model):
    SIZE_CHOICES = [
        ('Ch', 'Chico'),
        ('G', 'Grande'),
        ('C', 'Corazon'),
        ('R', 'Rectangular'),
    ]
    
    PHASE_CHOICES = [
        ('R', 'Relleno'),
        ('R', 'Rallado'),
        ('D', 'Decorado'),
        ('V', 'Vendido'),
    ]
    
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=100)
    phase = models.CharField(max_length=1, choices=PHASE_CHOICES)

    def __str__(self):
        return f"{self.get_size_display()} {self.flavor} ({self.get_phase_display()})"
