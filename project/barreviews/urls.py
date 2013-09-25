from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from barreviews import views

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url=reverse_lazy('barreviews:index')), name='index'),
                       url(r'^bars/$', views.IndexView.as_view(), name='home')
                       url(r'^bars/$', views.BarsView.as_view(), name='bars')
                       )