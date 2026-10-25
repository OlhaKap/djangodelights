from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class UnitType(models.TextChoices):
    KG = 'kg', 'Kilograms'
    L = 'l', 'Liters'
    PCS = 'pcs', 'Pieces'
    
    
class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=3, default=0, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UnitType.choices)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])