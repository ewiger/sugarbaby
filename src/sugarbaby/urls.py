from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='count/', permanent=False)),
    url(r'^count/', 'sugarbaby.migrosugar.views.home', name='home'),
    url(r'^list_products/', 'sugarbaby.migrosugar.views.list_products',
        name='list_products'),
    url(r'^get_sugar_values/(?P<selected_date>\w{0,50})',
        'sugarbaby.migrosugar.views.get_sugar_values'),
    url(r'^track_product/(?P<product>[\w,]{0,100})',
        'sugarbaby.migrosugar.views.track_product'),
    url(r'^diary/', 'sugarbaby.migrosugar.views.diary', name='diary'),
    url(r'^admin/', include(admin.site.urls)),
)
