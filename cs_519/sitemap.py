from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from cubecrafty.models import *


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return[]

    def location(self, item):
        return reverse(item)
