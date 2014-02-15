# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BookTextQuestion.choice_4'
        db.alter_column('supersyncer_booktextquestion', 'choice_4', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_5'
        db.alter_column('supersyncer_booktextquestion', 'choice_5', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_6'
        db.alter_column('supersyncer_booktextquestion', 'choice_6', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_1'
        db.alter_column('supersyncer_booktextquestion', 'choice_1', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_2'
        db.alter_column('supersyncer_booktextquestion', 'choice_2', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_3'
        db.alter_column('supersyncer_booktextquestion', 'choice_3', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'BookTextQuestion.choice_4'
        db.alter_column('supersyncer_booktextquestion', 'choice_4', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_5'
        db.alter_column('supersyncer_booktextquestion', 'choice_5', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_6'
        db.alter_column('supersyncer_booktextquestion', 'choice_6', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_1'
        db.alter_column('supersyncer_booktextquestion', 'choice_1', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_2'
        db.alter_column('supersyncer_booktextquestion', 'choice_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'BookTextQuestion.choice_3'
        db.alter_column('supersyncer_booktextquestion', 'choice_3', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

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
            'choice_1': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'choice_2': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'choice_3': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'choice_4': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'choice_5': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'choice_6': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'correct': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_book_text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['supersyncer.BookText']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
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