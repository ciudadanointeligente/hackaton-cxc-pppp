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
	institucion = models.ForeignKey("Institucion",null=True)
	descripcion_etapa = models.CharField(max_length=4096,null=True)
	situacion = models.CharField(max_length=255,null=True)
	magnitud = models.CharField(max_length=255,null=True)
	valor_magnitud = models.IntegerField(null=True)
	vida_util = models.IntegerField(null=True)
	beneficiarios = models.IntegerField(null=True)
	a_favor = models.IntegerField(default=0)
	en_contra = models.IntegerField(default=0)


class Sector(models.Model):
	nombre = models.CharField(max_length=255)

class SubSector(models.Model):
	nombre = models.CharField(max_length=1024)
	sector = models.ForeignKey(Sector)

class Institucion(models.Model):
	nombre = models.CharField(max_length=255)