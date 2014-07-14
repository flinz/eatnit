from django.conf.urls import patterns, url
from eatnit.apps.food import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='eatnit_index'),
    # url(r'^meals/$', views.meal_index, name='meal_index'),
    # url(r'^meals/(?P<meal_id>\d+)/$', views.meal_detail, name='meal_detail'),

    # url(r'^restaurants/$', views.restaurant_index, name='restaurant_index'),
    # url(r'^restaurants/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name='restaurant_detail'),
)