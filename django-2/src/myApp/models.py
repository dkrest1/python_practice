from django.db import models

# Create your models here.
class Product(models.Model):
    title        = models.CharField(max_length=100)
    description  = models.TextField(blank=True, null=True)
    price        = models.DecimalField(decimal_places=2, max_digits=10)
    summary      = models.TextField(blank=True, null=True)
    features     = models.BooleanField(default=True)
    
def get_absolute_url(self):
    return f"porduct/{self.id}"
