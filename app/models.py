from django.db import models

# Create your models here.

class comentarios(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fecha = models.DateField()
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email