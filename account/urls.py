from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done
from . import views

urlpatterns = [
    # post views
    #url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^countries_list/$', views.countries_list, name='countries_list'),
    #url(r'^cities_by_country_list/(?P<country_id>\d+)/$', views.cities_by_country_list, name='cities_by_country_list'),

    # url(r'^password-change/$', password_change, name='password_change'),
    # url(r'^password-change/done/$', password_change_done, name='password_change_done'),
]
