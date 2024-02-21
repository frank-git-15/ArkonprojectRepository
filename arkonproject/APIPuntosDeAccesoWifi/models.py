from django.db import models

# Create your models here.

#Este modelo representa la tabla en la base de datos, tiene que tener los mismos atributos que las columnads de la tabla
class WifiAccesPoint(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    programa = models.CharField(max_length=50)
    fecha_instalacion = models.DateField(null=True, blank=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    colonia = models.CharField(max_length = 100)
    alcaldia = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.id
