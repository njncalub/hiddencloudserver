from django.contrib import admin
from hiddencloudserver.supersyncer.models import UserProfile, UserLog, UserProgress
from hiddencloudserver.supersyncer.models import BookGenre, BookAuthor, Book, BookText, BookTextQuestion


class UserProfileAdmin(admin.ModelAdmin):
    pass


class UserLogAdmin(admin.ModelAdmin):
    pass


class UserProgressAdmin(admin.ModelAdmin):
    pass


class BookGenreAdmin(admin.ModelAdmin):
    pass


class BookAuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("genre", "author")


# class BookTextQuestionChoiceInline(admin.TabularInline):
#     model = BookTextQuestionChoice
#     extra = 3


class BookTextQuestionInline(admin.StackedInline):
    model = BookTextQuestion
    extra = 3


# class BookTextQuestionAdmin(admin.ModelAdmin):
#     inlines = [BookTextQuestionChoiceInline]
#     extra = 3


# class BookTextQuestionChoiceAdmin(admin.ModelAdmin):
#     pass


class BookTextAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'get_genres', 'total_words')
    # list_filter = ("from_book",)
    inlines = [BookTextQuestionInline]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLog, UserLogAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookText, BookTextAdmin)
# admin.site.register(BookTextQuestion, BookTextQuestionAdmin)
# admin.site.register(BookTextQuestionChoice, BookTextQuestionChoiceAdmin)