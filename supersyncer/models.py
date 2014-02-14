from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class BookGenre(models.Model):
    genre = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.genre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.genre)[:50]

        return super(BookGenre, self).save(*args, **kwargs)


class BookAuthor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(BookGenre, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class BookText(models.Model):
    from_book = models.ForeignKey(Book)
    text = models.TextField()
    total_words = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_words(self):
        return len(self.text.split(' '))

    def __unicode__(self):
        return "Text from " + self.from_book.title

    def save(self, *args, **kwargs):
        self.total_words = self.get_total_words()
        super(BookText, self).save(*args, **kwargs)


class BookTextQuestion(models.Model):
    from_book_text = models.ForeignKey(BookText)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.question


class BookTextQuestionChoice(models.Model):
    from_book_text_question = models.ForeignKey(BookTextQuestion)
    choice = models.TextField()
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.choice


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pass


class LeaderBoard(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pass
