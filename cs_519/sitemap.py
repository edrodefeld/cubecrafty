from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from cubecrafty.models import *


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return['index', 'cart', 'checkout',]

    def location(self, item):
        return reverse(item)

class ProductSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Cube.objects.all()

    def lastmod(self, obj):
        return obj.date_created
