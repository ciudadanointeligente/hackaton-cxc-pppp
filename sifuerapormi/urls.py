from django.conf.urls import patterns, include, url
from views import HomeTemplateView
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', HomeTemplateView.as_view(template_name="home.html"), name="home"),
	)