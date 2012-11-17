from django.conf.urls import patterns, include, url
from views import HomeTemplateView, ComunaIndicesView
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', HomeTemplateView.as_view(template_name="home.html"), name="home"),
	url(r'^(?P<pk>[-\d]+)/?$', ComunaIndicesView.as_view(), name='comuna-detail'),
	)