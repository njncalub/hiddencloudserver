from django.conf.urls.defaults import patterns, include, url
from hiddencloudserver.sitelogic.views import view_index
from tastypie.api import Api
from hiddencloudserver.supersyncer.api import UserResource, UserProfileResource, UserLogResource, UserProgressResource
from hiddencloudserver.supersyncer.api import BookResource, BookGenreResource, BookTextResource, BookTextQuestionResource
from hiddencloudserver.supersyncer.api import GameResultResource, SurveyResource

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UserProfileResource())
v1_api.register(UserLogResource())
v1_api.register(UserProgressResource())
v1_api.register(BookResource())
v1_api.register(BookGenreResource())
v1_api.register(BookTextResource())
v1_api.register(BookTextQuestionResource())
v1_api.register(GameResultResource())
v1_api.register(SurveyResource())

urlpatterns += patterns('',
    url(r'^api/', include(v1_api.urls)),
)

urlpatterns += patterns('',
    url(r'^$', view_index, name='view_index'),
)