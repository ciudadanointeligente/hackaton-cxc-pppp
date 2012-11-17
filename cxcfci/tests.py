from django.test import TestCase

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
		sitaucion = u"Sitaucion de prueba"
		magnitud = u"Magnitud de prueba"
		valor_magnitud = 123456
		vida_util = u"10 anos"
		beneficiarios = 123456
		proyecto = Proyecto.objects.create(
			codigo,
			nombre,
			tipo,
			etapa,
			ano,
			comuna,
			ubicacion,
			#subsector,
			costo,
			#institucion,
			descripcion_etapa,
			sitaucion,
			magnitud,
			valor_magnitud,
			vida_util,
			beneficiarios
			)


#bd sector/subsector del proyecto

#bd institucion

#bd usuario

#db comentario

#bd voto