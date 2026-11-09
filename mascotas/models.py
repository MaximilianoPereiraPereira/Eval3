from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(null=False,max_length=100)
    correo = models.EmailField(null=False,unique=True)
    rut = models.CharField(null=False,max_length=20)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(null=False,max_length=100)
    anio_nacimiento = models.PositiveBigIntegerField(null=False)
    especie = models.CharField(null=False,max_length=50)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre