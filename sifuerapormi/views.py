# -*- coding: utf-8 -*-#
# Create your views here.

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from electoralarea.models import Comuna
from models import Comuna, Sector
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
							"id":proyecto.id
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
