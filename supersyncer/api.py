from django.contrib.auth.models import User
from django.http import HttpResponse
from tastypie import fields
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpForbidden
from tastypie.paginator import Paginator
from tastypie.resources import Resource, ModelResource
from tastypie.serializers import Serializer
from hiddencloudserver.supersyncer.models import UserProfile, UserLog, UserProgress
from hiddencloudserver.supersyncer.models import Book, BookGenre, BookAuthor, BookText, BookTextQuestion

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
        excludes = ['created_at', 'deleted']
        # authentication = ApiKeyAuthenticationExtended()
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        paginator_class = Paginator
        cache = SimpleCache()
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put']


class UserResource(BaseModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


class UserProfileResource(BaseModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['post', 'put']


class UserLogResource(BaseModelResource):
    user = fields.ForeignKey(UserProfileResource, "user")

    class Meta:
        queryset = UserLog.objects.all()
        resource_name = 'user_log'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['post']


class UserProgressResource(BaseModelResource):
    class Meta:
        queryset = UserProgress.objects.all()
        resource_name = 'user_progress'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['post']


class BookGenreResource(BaseModelResource):
    class Meta:
        queryset = BookGenre.objects.all()
        resource_name = 'book_genre'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get']


class BookAuthorResource(BaseModelResource):
    class Meta:
        queryset = BookAuthor.objects.all()
        resource_name = 'book_author'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get']


class BookResource(BaseModelResource):
    genre = fields.ManyToManyField(BookGenreResource, 'genre')
    author = fields.ManyToManyField(BookAuthorResource, 'author')

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get']


class BookTextResource(BaseModelResource):
    from_book = fields.ForeignKey(BookResource, 'from_book')

    class Meta:
        queryset = BookText.objects.all()
        resource_name = 'book_text'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get']


class BookTextQuestionResource(BaseModelResource):
    from_book_text = fields.ForeignKey(BookTextResource, 'from_book_text')

    class Meta:
        queryset = BookTextQuestion.objects.all()
        resource_name = 'book_text_question'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get']


# class BookTextQuestionChoiceResource(ModelResource):
#     from_book_text_question = fields.ForeignKey(BookTextQuestionResource, 'from_book_text_question')

#     class Meta:
#         queryset = BookTextQuestionChoice.objects.all()
#         resource_name = 'book_text_question_choice'
#         allowed_methods = ['get']