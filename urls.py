from django.conf.urls.defaults import patterns, include, url
from hiddencloudserver.sitelogic.views import view_index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view_index, name='view_index'),
)