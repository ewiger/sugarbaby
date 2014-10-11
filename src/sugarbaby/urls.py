from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'sugarbaby.migrosugar.views.home', name='home'),
    url(r'^list_products/', 'sugarbaby.migrosugar.views.list_products',
        name='list_products'),
    url(r'^admin/', include(admin.site.urls)),
)
