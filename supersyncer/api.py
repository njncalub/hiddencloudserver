from tastypie.resources import ModelResource
from tastypie.constants import ALL
from hiddencloudserver.supersyncer.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        filtering = { 'title' : ALL }
        allowed_methods = ['get']