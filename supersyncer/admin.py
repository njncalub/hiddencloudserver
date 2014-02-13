from django.contrib import admin
from hiddencloudserver.supersyncer.models import Book, BookGenre, BookText, BookTextQuestion, BookTextQuestionChoice

class BookAdmin(admin.ModelAdmin):
    pass


class BookGenreAdmin(admin.ModelAdmin):
    pass


class BookTextAdmin(admin.ModelAdmin):
    pass


class BookTextQuestionAdmin(admin.ModelAdmin):
    pass


class BookTextQuestionChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(BookText, BookTextAdmin)
admin.site.register(BookTextQuestion, BookTextQuestionAdmin)
admin.site.register(BookTextQuestionChoice, BookTextQuestionChoiceAdmin)