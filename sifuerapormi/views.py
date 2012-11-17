# -*- coding: utf-8 -*-#
# Create your views here.

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from electoralarea.models import Comuna
from models import Comuna, Sector, Proyecto
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import json

class HomeTemplateView(TemplateView):
	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		comunas = Comuna.objects.all()

		context['comunas'] = comunas
		return context


class ComunaIndicesView(DetailView):
	template_name = "comuna_detail.html"
	model = Comuna

	def get_areas(self):
		areas_result = []
		areas = Sector.objects.all()
		for area in areas:
			area_dict = {
				"name": area.nombre,
				"children":[],
				"cost":0
			}
			subsector_cost_sum = 0
			for subsector in area.subsector_set.all():
				subsector_dict = {
					"name":subsector.nombre,
					"children":[],
					"cost" :0
				}
				proyecto_cost_sum = 0
				for proyecto in subsector.proyecto_set.all():
					if (proyecto.comuna == self.object):
						proyecto_cost_sum += proyecto.costo
						proyecto_dict = {
							"name":proyecto.nombre,
							"cost":proyecto.costo,
							"id":proyecto.id,
							"a_favor":proyecto.a_favor,
							"en_contra":proyecto.en_contra,
						}
						subsector_dict["children"].append(proyecto_dict)
				subsector_dict["cost"] = proyecto_cost_sum
				subsector_cost_sum += proyecto_cost_sum
				area_dict["children"].append(subsector_dict)
			area_dict["cost"] = subsector_cost_sum
			areas_result.append(area_dict)

		return json.dumps({"name":"padre","children":areas_result})


	def get_context_data(self, **kwargs):
		context = super(ComunaIndicesView, self).get_context_data(**kwargs)
		context['areas'] = self.get_areas()

		return context

#@require_POST
def thumbs_up(request):
	proyecto_pk = request.GET['pk']
	proyecto = Proyecto.objects.get(pk=proyecto_pk)
	if proyecto.a_favor is None:
		proyecto.a_favor = 0
	proyecto.a_favor = proyecto.a_favor + 1

	proyecto.save()
	return HttpResponse(proyecto.a_favor,content_type='application/json')


def thumbs_down(request):
	proyecto_pk = request.GET['pk']
	proyecto = Proyecto.objects.get(pk=proyecto_pk)
	if proyecto.en_contra is None:
		proyecto.en_contra = 0
	proyecto.en_contra = proyecto.en_contra + 1

	proyecto.save()
	return HttpResponse(proyecto.en_contra,content_type='application/json')
