from django.contrib import admin
from hiddencloudserver.supersyncer.models import Book, BookGenre, BookText, BookTextQuestion

class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)