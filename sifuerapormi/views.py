# -*- coding: utf-8 -*-#
# Create your views here.

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from electoralarea.models import Comuna

class HomeTemplateView(TemplateView):
	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		comunas = Comuna.objects.all()

		context['comunas'] = comunas
		return context