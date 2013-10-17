from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from barreviews import views
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url=reverse_lazy('barreviews:index')), name='indexr'),
                       url(r'^index.html$', views.IndexView.as_view(), name='index'),
                       url(r'^bars/$', views.BarsView.as_view(), name='bars'),
                       url(r'^users/$', login_required(views.UsersView.as_view()), name='users'),
                       url(r'^drinks/$', views.DrinksView.as_view(), name='drinks'),
                       url(r'^reviews/$', views.ReviewsView.as_view(), name='reviews'),
                       url(r'^breweries/$', views.BreweriesView.as_view(), name='breweries'),
                       
                       #BARS
                       url(r'^bar/(?P<pk>\d+)/$', views.BarView.as_view(), name='bar'),
                       url(r'^bar/add/$', views.bar_add, name='bar_add'),
                       url(r'^bar/(?P<pk>\d+)/edit/$', views.bar_edit, name='bar_edit'),
                       url(r'^bar/(?P<pk>\d+)/delete/$', views.bar_delete, name='bar_delete'),
                       
                       #DRINKS
                       url(r'^drink/(?P<pk>\d+)/$', views.DrinkView.as_view(), name='drink'),
                       url(r'^drink/add/$', views.drink_add, name='drink_add'),
                       url(r'^drink/(?P<pk>\d+)/edit/$', views.drink_edit, name='drink_edit'),
                       url(r'^drink/(?P<pk>\d+)/delete/$', views.drink_delete, name='drink_delete'),
                       
                       #USERS
                       url(r'^user/(?P<pk>\d+)/$', login_required(views.UserView.as_view()), name='user'),
                       url(r'^user/add/$', views.user_add, name='user_add'),
                       ######!!!!!!url(r'^user/(?P<pk>\d+)/comment/add/$', views.comment_add, name='comment_add'),
                       url(r'^user/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),
                       url(r'^user/(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete'),
                       
                       #ACCOUNTS
                       url(r'^accounts/login/$',  views.login, name='login'),
                       url(r'^accounts/auth/$', views.auth_view, name='auth'),
                       url(r'^accounts/logout/$', views.logout, name='logout'),
                       url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
                       url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
                       
                       #REVIEWS
                       url(r'^review/(?P<pk>\d+)/$', views.ReviewView.as_view(), name='review'),
                       url(r'^review/add/$', views.review_add, name='review_add'),
                       url(r'^review/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
                       url(r'^review/(?P<pk>\d+)/delete/$', views.review_delete, name='review_delete'),
                       
                       url(r'^brewery/(?P<pk>\d+)/$', views.BreweryView.as_view(), name='brewery'),
                       url(r'^brewery/add/$', views.brewery_add, name='brewery_add'),
                       url(r'^brewery/(?P<pk>\d+)/edit/$', views.brewery_edit, name='brewery_edit'),
                       url(r'^brewery/(?P<pk>\d+)/delete/$', views.brewery_delete, name='brewery_delete')
                       )
