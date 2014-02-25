from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

class UserProfile(models.Model):
    """
    This defines the Profiles of Users.
    """

    uid = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200, blank=True, null=True)         # not required
    first_name = models.CharField(max_length=200, blank=True, null=True)        # not required
    middle_name = models.CharField(max_length=200, blank=True, null=True)       # not required
    birth_date = models.DateField(blank=True, null=True)
    email_address = models.EmailField(max_length=200, blank=True, null=True)    # not required
    gender = models.CharField(max_length=6, blank=True, null=True)
    current_year = models.CharField(max_length=1, blank=True, null=True)
    cluster = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    benchmark_speed = models.IntegerField(blank=True, null=True)
    benchmark_correct_items = models.IntegerField(blank=True, null=True)
    benchmark_wrong_items = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.uid + " " + self.last_name


class UserLog(models.Model):
    """
    This defines the Log for User logins.
    """

    user = models.ForeignKey(UserProfile)
    data = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.uid + " " + self.user.last_name


class UserProgress(models.Model):
    """
    This defines the Log for User Progress.
    """

    user = models.ForeignKey(UserProfile)
    previous_speed = models.IntegerField(blank=True, null=True)
    total_words_read = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    current_speed = models.IntegerField(blank=True, null=True)
    correct_items = models.IntegerField(blank=True, null=True)
    wrong_items = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "user progress"

    def __unicode__(self):
        return self.user.uid + " " + self.user.last_name


class BookGenre(models.Model):
    """
    This defines the Genres of the Books.
    """

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
    """
    This defines the Authors of the Books.
    """

    full_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.full_name


class Book(models.Model):
    """
    This defines the Books.
    """

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    total_words = models.IntegerField(default=0, blank=True, null=True, verbose_name="total words (auto)")
    genre = models.ManyToManyField(BookGenre, blank=True, null=True)
    author = models.ManyToManyField(BookAuthor, blank=True, null=True)
    book_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_words(self):
        return len(self.text.split(' '))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.total_words = self.get_total_words()
        super(Book, self).save(*args, **kwargs)


class BookText(models.Model):
    """
    This defines the Passages/Text from the Books.
    """

    EASY = 'EA'
    MEDIUM = 'ME'
    HARD = 'HA'
    EXPERT = 'EX'
    ASIAN = 'AS'
    DIFFICULTY = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
        (EXPERT, 'Expert'),
        (ASIAN, 'Asian'),
    )

    text = models.TextField()
    from_book = models.ForeignKey(Book)
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY, default=EASY)
    total_words = models.IntegerField(default=0, blank=True, null=True, verbose_name="total words (auto)")
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_genres(self):
        return ', '.join(g.genre for g in self.from_book.genre.all())

    def get_total_words(self):
        return len(self.text.split(' '))

    def __unicode__(self):
        return "Text from " + self.from_book.title

    def save(self, *args, **kwargs):
        self.total_words = self.get_total_words()
        super(BookText, self).save(*args, **kwargs)


class BookTextQuestion(models.Model):
    """
    This defines the Questions and Choices from the Book Texts.
    """

    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    CHOICES = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (SIX, '6'),
    )

    question = models.TextField()
    choice_1 = models.CharField(max_length=200, blank=True, null=True)
    choice_2 = models.CharField(max_length=200, blank=True, null=True)
    choice_3 = models.CharField(max_length=200, blank=True, null=True)
    choice_4 = models.CharField(max_length=200, blank=True, null=True)
    choice_5 = models.CharField(max_length=200, blank=True, null=True)
    choice_6 = models.CharField(max_length=200, blank=True, null=True)
    correct = models.CharField(max_length=1, choices=CHOICES, default=ONE, verbose_name="correct choice")
    from_book_text = models.ForeignKey(BookText)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_book_title(self):
        return self.from_book_text.from_book.title

    def __unicode__(self):
        return self.question


# class BookTextQuestionChoice(models.Model):
#     """
#     This defines the Questions from the Book Texts.
#     """

#     from_book_text_question = models.ForeignKey(BookTextQuestion)
#     choice = models.TextField()
#     is_correct = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __unicode__(self):
#         return self.choice


class GameResult(models.Model):
    uid = models.CharField(max_length=100, blank=True, null=True)
    training_date = models.DateTimeField(blank=True, null=True)
    average_wpm = models.IntegerField(default=0, blank=True, null=True)
    average_rc = models.FloatField(default=0.0, blank=True, null=True)
    total_correct = models.IntegerField(default=0, blank=True, null=True)
    quiz_score = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.uid + " result on " + unicode(self.created_at)


class Survey(models.Model):
    uid = models.CharField(max_length=100, blank=True, null=True)
    survey_date = models.DateTimeField(blank=True, null=True)
    q_enjoy_reading = models.IntegerField(default=0, blank=True, null=True)
    q_want_to_improve = models.IntegerField(default=0, blank=True, null=True)
    q_like_visuals = models.IntegerField(default=0, blank=True, null=True)
    q_like_music = models.IntegerField(default=0, blank=True, null=True)
    q_like_story = models.IntegerField(default=0, blank=True, null=True)
    q_continue_playing = models.IntegerField(default=0, blank=True, null=True)
    q_find_way_easily = models.IntegerField(default=0, blank=True, null=True)
    q_gets_difficult = models.IntegerField(default=0, blank=True, null=True)
    q_good_rewards = models.IntegerField(default=0, blank=True, null=True)
    q_relevant_feedback = models.IntegerField(default=0, blank=True, null=True)
    q_game_helped = models.IntegerField(default=0, blank=True, null=True)
    q_recommend_to_friends = models.IntegerField(default=0, blank=True, null=True)
    b_awpm = models.IntegerField(default=0, blank=True, null=True)
    s_awpm = models.IntegerField(default=0, blank=True, null=True)
    s_rc = models.FloatField(default=0.0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.uid + " survey on " + unicode(self.created_at)


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pass


class LeaderBoard(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    pass
