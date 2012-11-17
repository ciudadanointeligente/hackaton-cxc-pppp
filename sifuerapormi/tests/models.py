"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from sifuerapormi.models import Proyecto, Sector, SubSector, Institucion
from electoralarea.models import Comuna

#bd proyectos
class ProyectoTestCase(TestCase):
	def test_create_proyecto(self):
		codigo = u"12345-6"
		nombre = u"Proyecto de prueba"
		tipo = u"Tipo de prueba"
		etapa = u"Etapa de prueba"
		ano = 2012
		comuna = Comuna.objects.all()[0]
		ubicacion = u"Holanda 895"
		subsector = SubSector.objects.create(nombre = u"Bibliotecas comunitarias", sector = Sector.objects.create(nombre = u"Educacion"))
		costo = 123456
		municipalidad_de_valparaiso = Institucion.objects.create(nombre = u"Municipalidad de Valparaiso")
		descripcion_etapa = u"Descripcion de prueba"
		situacion = u"Sitaucion de prueba"
		magnitud = u"Magnitud de prueba"
		valor_magnitud = 123456
		vida_util = 10
		beneficiarios = 123456
		proyecto, created = Proyecto.objects.get_or_create(
			codigo = codigo,
			nombre = nombre,
			tipo = tipo,
			etapa= etapa,
			ano = ano,
			comuna = comuna,
			ubicacion = ubicacion,
			subsector = subsector,
			costo = costo,
			institucion = municipalidad_de_valparaiso,
			descripcion_etapa = descripcion_etapa,
			situacion = situacion,
			magnitud = magnitud,
			valor_magnitud = valor_magnitud,
			vida_util = vida_util,
			beneficiarios = beneficiarios
			)
		self.assertTrue(created)
		self.assertEquals(codigo, proyecto.codigo)
		self.assertEquals(comuna,proyecto.comuna)
		self.assertEquals(subsector, proyecto.subsector)
		self.assertEquals(municipalidad_de_valparaiso, proyecto.institucion)	


#bd sector/subsector del proyecto
class SectorTestCase(TestCase):
	def test_create_proyecto(self):
		sector, created = Sector.objects.get_or_create(
			nombre = u"Educacion")
		self.assertTrue(created)
		self.assertEquals(sector.nombre, u"Educacion")

class SubSectorTestCase(TestCase):
	def test_create_subsector(self):
		sector = Sector.objects.create(nombre = u"Educacion")
		subsector, created = SubSector.objects.get_or_create(
			nombre = u"Bibliotecas comunitarias",
			sector = sector
			)
		self.assertTrue(created)
		self.assertEquals(subsector.nombre, u"Bibliotecas comunitarias")
		self.assertEquals(subsector.sector, sector)

#bd institucion
class InstitucionTestCase(TestCase):
	def test_create_institucion(self):
		nombre = u"Municipalidad de Valparaiso"
		institucion, created = Institucion.objects.get_or_create(
			nombre = nombre
			)
		self.assertTrue(created)
		self.assertEquals(institucion.nombre, nombre)

#bd usuario
#db comentario
#bd voto

class HomeViewTestCase(TestCase):
	def test_homeview(self):
		url= reverse("home")
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "home.html")
		self.assertTrue("comunas" in response.context)
		self.assertEquals(response.context["comunas"].count(), Comuna.objects.count())