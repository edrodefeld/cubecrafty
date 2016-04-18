from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/crafty_cubes/$', views.crafty_cubes, name='crafty_cubes'),
    url(r'^categories/basic_cubes/$', views.basic_cubes, name='basic_cubes'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^confirmation/$', views.confirmation, name='confirmation'),
]
