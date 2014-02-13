from tastypie.resources import ModelResource
from tastypie.constants import ALL
from hiddencloudserver.supersyncer.models import Book, BookGenre, BookText, BookTextQuestion, BookTextQuestionChoice

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        filtering = { 'title' : ALL }
        allowed_methods = ['get']


class BookGenreResource(ModelResource):
    class Meta:
        queryset = BookGenre.objects.all()
        resource_name = 'book_genre'
        allowed_methods = ['get']


class BookTextResource(ModelResource):
    class Meta:
        queryset = BookText.objects.all()
        resource_name = 'book_text'
        allowed_methods = ['get']


class BookTextQuestionResource(ModelResource):
    class Meta:
        queryset = BookTextQuestion.objects.all()
        resource_name = 'book_text_question'
        allowed_methods = ['get']


class BookTextQuestionChoiceResource(ModelResource):
    class Meta:
        queryset = BookTextQuestionChoice.objects.all()
        resource_name = 'book_text_question_choice'
        allowed_methods = ['get']