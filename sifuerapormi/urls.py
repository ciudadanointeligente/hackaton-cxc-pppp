from django.conf.urls import patterns, include, url
from views import HomeTemplateView, ComunaIndicesView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from models import Proyecto

urlpatterns = patterns('',
	url(r'^$', HomeTemplateView.as_view(template_name="home.html"), name="home"),
	url(r'^(?P<pk>[-\d]+)/?$', ComunaIndicesView.as_view(template_name = "dibujo.html"), name='comuna-detail-dibujo'),
	url(r'^(?P<pk>[-\d]+).json$', ComunaIndicesView.as_view(), name='comuna-detail'),
	url(r'^proyecto/(?P<pk>[-\d]+)/$', DetailView.as_view(model=Proyecto, template_name="proyecto-detail.html"), name='comuna-detail'),
	)