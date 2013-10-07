from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from barreviews import views

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url=reverse_lazy('barreviews:index')), name='indexr'),
                       url(r'^index.html$', views.IndexView.as_view(), name='index'),
                       url(r'^bars/$', views.BarsView.as_view(), name='bars'),
                       url(r'^users/$', views.UsersView.as_view(), name='users'),
                       url(r'^drinks/$', views.DrinksView.as_view(), name='drinks'),
                       url(r'^reviews/$', views.ReviewsView.as_view(), name='reviews')
                       )