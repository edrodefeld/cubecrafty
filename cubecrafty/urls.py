from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from cs_519.sitemap import *
from django.http import HttpResponse
from . import views

sitemaps = {'static': StaticViewSitemap,}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/crafty_cubes/$', views.crafty_cubes, name='crafty_cubes'),
    url(r'^categories/basic_cubes/$', views.basic_cubes, name='basic_cubes'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^confirmation/$', views.confirmation, name='confirmation'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain"))
]
