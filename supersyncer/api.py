from django.http import HttpResponse
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpForbidden
from tastypie.paginator import Paginator
from tastypie.resources import Resource, ModelResource
from tastypie.serializers import Serializer
from hiddencloudserver.supersyncer.models import Book, BookGenre, BookText, BookTextQuestion, BookTextQuestionChoice

class ApiKeyAuthenticationExtended(ApiKeyAuthentication):
    def get_identifier(self, request):
        return request.user.username


class BaseCorsResource(Resource):
    """
    Class implementing CORS, from: @danigosa
    """
    def create_response(self, *args, **kwargs):
        response = super(BaseCorsResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []

        request_method = request.method.lower()
        allows = ','.join(map(str.upper, allowed))

        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return request_method


class BaseModelResource(BaseCorsResource, ModelResource):
    """
    Abstract class sample with template data for the models, from: @danigosa
    """

    class Meta:
        abstract = True
        excludes = ['creation_time', 'modification_time', 'deleted']
        authentication = ApiKeyAuthenticationExtended()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        paginator_class = Paginator
        cache = SimpleCache()
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put']


class BookResource(BaseModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        filtering = { 'title' : ALL }
        # allowed_methods = ['get']


class BookGenreResource(BaseModelResource):
    class Meta:
        queryset = BookGenre.objects.all()
        resource_name = 'book_genre'
        # allowed_methods = ['get']


class BookTextResource(BaseModelResource):
    class Meta:
        queryset = BookText.objects.all()
        resource_name = 'book_text'
        # allowed_methods = ['get']


class BookTextQuestionResource(BaseModelResource):
    class Meta:
        queryset = BookTextQuestion.objects.all()
        resource_name = 'book_text_question'
        # allowed_methods = ['get']


class BookTextQuestionChoiceResource(BaseModelResource):
    class Meta:
        queryset = BookTextQuestionChoice.objects.all()
        resource_name = 'book_text_question_choice'
        # allowed_methods = ['get']