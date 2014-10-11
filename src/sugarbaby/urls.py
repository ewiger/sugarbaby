from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^count/', 'sugarbaby.migrosugar.views.home', name='home'),
    url(r'^list_products/', 'sugarbaby.migrosugar.views.list_products',
        name='list_products'),
    url(r'^diary/', 'sugarbaby.migrosugar.views.diary', name='diary'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='count/', permanent=False)),
)
