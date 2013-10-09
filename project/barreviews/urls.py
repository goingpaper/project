from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from barreviews import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url=reverse_lazy('barreviews:index')), name='indexr'),
                       url(r'^index.html$', views.IndexView.as_view(), name='index'),
                       url(r'^bars/$', views.BarsView.as_view(), name='bars'),
                       url(r'^users/$', views.UsersView.as_view(), name='users'),
                       url(r'^drinks/$', views.DrinksView.as_view(), name='drinks'),
                       url(r'^reviews/$', views.ReviewsView.as_view(), name='reviews'),
                       
                       url(r'^bar/(?P<pk>\d+)/$', views.BarView.as_view(), name='bar'),
                       url(r'^bar/add/$', views.bar_add, name='bar_add'),
                       url(r'^bar/(?P<pk>\d+)/edit/$', views.bar_edit, name='bar_edit'),
                       url(r'^bar/(?P<pk>\d+)/delete/$', views.bar_delete, name='bar_delete'),
                       
                       url(r'^drink/(?P<pk>\d+)/$', views.DrinkView.as_view(), name='drink'),
                       url(r'^drink/add/$', views.drink_add, name='drink_add'),
                       url(r'^drink/(?P<pk>\d+)/edit/$', views.drink_edit, name='drink_edit'),
                       url(r'^drink/(?P<pk>\d+)/delete/$', views.drink_delete, name='drink_delete'),
                       
                       url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='user'),
                       url(r'^user/add/$', views.user_add, name='user_add'),
                       url(r'^user/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),
                       url(r'^user/(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete')
                       #(r'^accounts/login/$',  login),
                       #(r'^accounts/logout/$', logout)
                       )
