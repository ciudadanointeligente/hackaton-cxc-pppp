# coding= utf-8
from django.core.management.base import BaseCommand, CommandError
import csv


class CsvReader(object):
    def detectBip(self, line):
        from sifuerapormi.models import Proyecto, Sector, SubSector, Institucion
        sector, created = Sector.objects.get_or_create(nombre=line[8])
        subsector, created = SubSector.objects.get_or_create(sector=sector, nombre=line[9])
        institucion, created = Institucion.objects.get_or_create(nombre= line[36])
        proyecto, created = Proyecto.objects.get_or_create(
        													codigo = line[0], 
        													nombre=line[1],
        													tipo=line[2],
        													etapa=line[3],
        													ano = line[4],
        													comuna = line[7],
        													ubicacion = line[18],
        													subsector = subsector,
        													costo = line[11],
        													institucion = institucion,
        													descripcion_etapa = line[17],
        													descripcion_proyecto = line[17],
        													situacion = line[27],
        													magnitud = line[44],
        													valor_magnitud = line[45],
        													vida_util = line[46],
        													beneficiarios = line[47])
        return proyecto

    

class Command(BaseCommand):
    def handle(self, *args, **options):
        reader = csv.reader(open(args[0], 'rU'), delimiter='\t')
        csvReader = CsvReader()
        for line in reader:
            print line
            proyecto = csvReader.detectBip(line)