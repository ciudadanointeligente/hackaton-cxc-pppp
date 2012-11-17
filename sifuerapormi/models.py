from django.db import models
from electoralarea.models import Comuna

# Create your models here.
class Proyecto(models.Model):
	codigo = models.CharField(max_length=255)
	nombre = models.CharField(max_length=1024)
	tipo = models.CharField(max_length=255)
	etapa = models.CharField(max_length=255)
	ano = models.IntegerField()
	comuna = models.ForeignKey(Comuna)
	ubicacion = models.CharField(max_length=1024)
	subsector = models.ForeignKey("SubSector")
	costo = models.IntegerField()
	descripcion_etapa = models.CharField(max_length=4096)
	situacion = models.CharField(max_length=255)
	magnitud = models.CharField(max_length=255)
	valor_magnitud = models.IntegerField()
	vida_util = models.IntegerField()
	beneficiarios = models.IntegerField()

class Sector(models.Model):
	nombre = models.CharField(max_length=255)

class SubSector(models.Model):
	nombre = models.CharField(max_length=1024)
	sector = models.ForeignKey(Sector)