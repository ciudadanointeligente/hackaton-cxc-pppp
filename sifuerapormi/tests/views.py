from django.test import TestCase
from django.core.urlresolvers import reverse

from sifuerapormi.models import Proyecto, Sector, SubSector, Institucion
from electoralarea.models import Comuna
import json

class HomeViewTestCase(TestCase):
	def test_homeview(self):
		url= reverse("home")
		response = self.client.get(url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "home.html")
		self.assertTrue("comunas" in response.context)
		self.assertEquals(response.context["comunas"].count(), Comuna.objects.count())

class ComunaJsonViewTestCase(TestCase):

	def setUp(self):
		self.comuna1 = Comuna.objects.all()[0]
		self.comuna2 = Comuna.objects.all()[1]
		self.comuna3 = Comuna.objects.all()[2]
		self.comuna4 = Comuna.objects.all()[3]

		self.bibliotecas = SubSector.objects.create(nombre = u"Bibliotecas comunitarias", sector = Sector.objects.create(nombre = u"Educacion"))
		self.lentejas = SubSector.objects.create(nombre = u"lentejas", sector = Sector.objects.create(nombre = u"Legumbres"))
		self.fiera = SubSector.objects.create(nombre = u"Fiera", sector = Sector.objects.create(nombre = u"Perro"))


		municipalidad_de_valparaiso = Institucion.objects.create(nombre = u"Municipalidad de Valparaiso")

		proyecto1 = Proyecto.objects.create(
			codigo = u"12345-6",
			nombre = u"Proyecto de prueba",
			tipo = u"Tipo de prueba",
			etapa= u"Etapa de prueba",
			ano = 2012,
			comuna = self.comuna1,
			ubicacion = u"Holanda 895",
			subsector = self.bibliotecas,
			costo = 1,
			institucion = municipalidad_de_valparaiso,
			descripcion_etapa = u"Descripcion de prueba",
			situacion = u"Sitaucion de prueba",
			magnitud = u"Magnitud de prueba",
			valor_magnitud = 123456,
			vida_util = 10,
			beneficiarios = 123456
			)

		proyecto2 = Proyecto.objects.create(
			codigo = u"qwerty",
			nombre = u"Proyecto de prueba",
			tipo = u"Tipo de prueba",
			etapa= u"Etapa de prueba",
			ano = 2012,
			comuna = self.comuna1,
			ubicacion = u"Holanda 895",
			subsector = self.lentejas,
			costo = 2,
			institucion = municipalidad_de_valparaiso,
			descripcion_etapa = u"Descripcion de prueba",
			situacion = u"Sitaucion de prueba",
			magnitud = u"Magnitud de prueba",
			valor_magnitud = 123456,
			vida_util = 10,
			beneficiarios = 123456
			)

		proyecto3 = Proyecto.objects.create(
			codigo = u"asdf",
			nombre = u"Proyecto de prueba",
			tipo = u"Tipo de prueba",
			etapa= u"Etapa de prueba",
			ano = 2012,
			comuna = self.comuna2,
			ubicacion = u"Holanda 895",
			subsector = self.fiera,
			costo = 3,
			institucion = municipalidad_de_valparaiso,
			descripcion_etapa = u"Descripcion de prueba",
			situacion = u"Sitaucion de prueba",
			magnitud = u"Magnitud de prueba",
			valor_magnitud = 123456,
			vida_util = 10,
			beneficiarios = 123456
			)

		self.proyecto4 = Proyecto.objects.create(
			codigo = u"asdf",
			nombre = u"Proyecto de prueba",
			tipo = u"Tipo de prueba",
			etapa= u"Etapa de prueba",
			ano = 2012,
			comuna = self.comuna2,
			ubicacion = u"Holanda 895",
			subsector = self.lentejas,
			costo = 4,
			institucion = municipalidad_de_valparaiso,
			descripcion_etapa = u"Descripcion de prueba",
			situacion = u"Sitaucion de prueba",
			magnitud = u"Magnitud de prueba",
			valor_magnitud = 123456,
			vida_util = 10,
			beneficiarios = 123456
			)


	def test_get_page(self):
		url = reverse('comuna-detail', kwargs={
			'pk':self.comuna1.id
			})

		response = self.client.get(url)
		


		self.assertEquals(response.status_code, 200)

		self.assertTemplateUsed(response, "comuna_detail.html")


		self.assertTrue("areas" in response.context)

		areas = json.loads(response.context["areas"])
		self.assertEquals(len(areas), 2)
		self.assertTrue("name" in areas[0])
		self.assertEquals(areas[0]["name"],u"Educacion")
		self.assertTrue("children" in areas[0])
		self.assertEquals(len(areas[0]["children"]), 1) #subsectores
		self.assertTrue("name" in areas[0]["children"][0])
		self.assertEquals(areas[0]["children"][0]["name"],u"Bibliotecas comunitarias")
		self.assertTrue("children" in areas[0]["children"][0])
		self.assertEquals(len(areas[0]["children"][0]["children"]), 1)
		self.assertTrue(areas[0]["children"][0]["children"][0]["name"], u"Proyecto de prueba")
		self.assertEquals(areas[0]["children"][0]["cost"], 1)
		self.assertEquals(areas[0]["cost"],1)


	def test_add_thumbs_up(self):
		url = reverse("thumbs-up")
		data = { "pk":self.proyecto4.pk }

		response = self.client.get(url, data)

		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.content, "1") #representa la cantidad de votos a favor
		proyecto = Proyecto.objects.get(pk=self.proyecto4.pk)

		self.assertEquals(proyecto.a_favor, 1)
