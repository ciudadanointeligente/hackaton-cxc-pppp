# coding= utf-8
from django.core.management.base import BaseCommand, CommandError
import csv


class CsvReader(object):
    def detectBip(self, line):
        from sifuerapormi.models import Proyecto, Sector, SubSector
        from electoralarea.models import Comuna
        sector, created = Sector.objects.get_or_create(nombre=line[6])
        subsector, created = SubSector.objects.get_or_create(sector=sector, nombre=line[7])
        # institucion, created = Institucion.objects.get_or_create(nombre= line[10])
        comuna_nombre = line[5].decode('utf-8').strip().title()
        
        try:
            comuna = Comuna.objects.get(name= comuna_nombre)


            proyecto, created = Proyecto.objects.get_or_create(
            													codigo = line[0], 
            													nombre=line[1],
            													tipo=line[2],
            													etapa=line[3],
            													ano = line[4],
            													comuna = comuna,
            													# ubicacion = line[12],
            													subsector = subsector,
            													costo = line[8])
            													# institucion = institucion,
            													# # descripcion_etapa = line[17],
            													# # descripcion_proyecto = line[17],
            													# situacion = line[13],
            													# magnitud = line[14],
            													# valor_magnitud = line[15],
            													# vida_util = line[16],
            													# beneficiarios = line[17])

            return proyecto
        except Exception, ex:
            print ex
            return False
  # Código BIP    Nombre Iniciativa   Tipología   Etapa que postula   Año de Postulación  Comuna  Sector  Sub Sector  Costo Total
  

class Command(BaseCommand):
    def handle(self, *args, **options):
        reader = csv.reader(open(args[0], 'rU'), delimiter='\t')
        csvReader = CsvReader()
        for line in reader:
            proyecto = csvReader.detectBip(line)