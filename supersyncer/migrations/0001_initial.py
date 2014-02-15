# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('supersyncer_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=200, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('cluster', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('speed_benchmark', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comp_benchmark', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['UserProfile'])

        # Adding model 'UserLog'
        db.create_table('supersyncer_userlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supersyncer.UserProfile'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['UserLog'])

        # Adding model 'UserProgress'
        db.create_table('supersyncer_userprogress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supersyncer.UserProfile'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['UserProgress'])

        # Adding model 'BookGenre'
        db.create_table('supersyncer_bookgenre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['BookGenre'])

        # Adding model 'BookAuthor'
        db.create_table('supersyncer_bookauthor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['BookAuthor'])

        # Adding model 'Book'
        db.create_table('supersyncer_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total_words', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('book_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['Book'])

        # Adding M2M table for field genre on 'Book'
        m2m_table_name = db.shorten_name('supersyncer_book_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['supersyncer.book'], null=False)),
            ('bookgenre', models.ForeignKey(orm['supersyncer.bookgenre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'bookgenre_id'])

        # Adding M2M table for field author on 'Book'
        m2m_table_name = db.shorten_name('supersyncer_book_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['supersyncer.book'], null=False)),
            ('bookauthor', models.ForeignKey(orm['supersyncer.bookauthor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'bookauthor_id'])

        # Adding model 'BookText'
        db.create_table('supersyncer_booktext', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('from_book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supersyncer.Book'])),
            ('difficulty', self.gf('django.db.models.fields.CharField')(default='EA', max_length=2)),
            ('total_words', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['BookText'])

        # Adding model 'BookTextQuestion'
        db.create_table('supersyncer_booktextquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('from_book_text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supersyncer.BookText'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['BookTextQuestion'])

        # Adding model 'BookTextQuestionChoice'
        db.create_table('supersyncer_booktextquestionchoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_book_text_question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supersyncer.BookTextQuestion'])),
            ('choice', self.gf('django.db.models.fields.TextField')()),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['BookTextQuestionChoice'])

        # Adding model 'Report'
        db.create_table('supersyncer_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['Report'])

        # Adding model 'LeaderBoard'
        db.create_table('supersyncer_leaderboard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('supersyncer', ['LeaderBoard'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('supersyncer_userprofile')

        # Deleting model 'UserLog'
        db.delete_table('supersyncer_userlog')

        # Deleting model 'UserProgress'
        db.delete_table('supersyncer_userprogress')

        # Deleting model 'BookGenre'
        db.delete_table('supersyncer_bookgenre')

        # Deleting model 'BookAuthor'
        db.delete_table('supersyncer_bookauthor')

        # Deleting model 'Book'
        db.delete_table('supersyncer_book')

        # Removing M2M table for field genre on 'Book'
        db.delete_table(db.shorten_name('supersyncer_book_genre'))

        # Removing M2M table for field author on 'Book'
        db.delete_table(db.shorten_name('supersyncer_book_author'))

        # Deleting model 'BookText'
        db.delete_table('supersyncer_booktext')

        # Deleting model 'BookTextQuestion'
        db.delete_table('supersyncer_booktextquestion')

        # Deleting model 'BookTextQuestionChoice'
        db.delete_table('supersyncer_booktextquestionchoice')

        # Deleting model 'Report'
        db.delete_table('supersyncer_report')

        # Deleting model 'LeaderBoard'
        db.delete_table('supersyncer_leaderboard')


    models = {
        'supersyncer.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['supersyncer.BookAuthor']", 'null': 'True', 'blank': 'True'}),
            'book_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['supersyncer.BookGenre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_words': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'supersyncer.bookauthor': {
            'Meta': {'object_name': 'BookAuthor'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'supersyncer.bookgenre': {
            'Meta': {'object_name': 'BookGenre'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'supersyncer.booktext': {
            'Meta': {'object_name': 'BookText'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'default': "'EA'", 'max_length': '2'}),
            'from_book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'total_words': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'supersyncer.booktextquestion': {
            'Meta': {'object_name': 'BookTextQuestion'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_book_text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.BookText']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        'supersyncer.booktextquestionchoice': {
            'Meta': {'object_name': 'BookTextQuestionChoice'},
            'choice': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_book_text_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.BookTextQuestion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'supersyncer.leaderboard': {
            'Meta': {'object_name': 'LeaderBoard'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'supersyncer.report': {
            'Meta': {'object_name': 'Report'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'supersyncer.userlog': {
            'Meta': {'object_name': 'UserLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.UserProfile']"})
        },
        'supersyncer.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'cluster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comp_benchmark': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'speed_benchmark': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'supersyncer.userprogress': {
            'Meta': {'object_name': 'UserProgress'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.UserProfile']"})
        }
    }

    complete_apps = ['supersyncer']