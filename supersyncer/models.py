from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class BookGenre(models.Model):
    genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.genre


class BookText(models.Model):
    from_book = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.from_book + " text"


class BookTextQuestion(models.Model):
    from_book = models.CharField(max_length=200)
    from_book_text = models.CharField(max_length=200)
    question = models.TextField()

    def __unicode__(self):
        return self.question + " from " + self.from_book


class Report(models.Model):
    pass


class LeaderBoard(models.Model):
    pass
