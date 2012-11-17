"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Proyecto
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
		#subsector = Subsector.objects.all()[0]
		costo = 123456
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
			#subsector,
			costo = costo,
			#institucion,
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


#bd sector/subsector del proyecto

#bd institucion

#bd usuario

#db comentario

#bd voto