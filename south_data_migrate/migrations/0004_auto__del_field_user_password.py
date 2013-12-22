# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.password'
        db.delete_column(u'south_data_migrate_user', 'password')


    def backwards(self, orm):
        # Adding field 'User.password'
        db.add_column(u'south_data_migrate_user', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)


    models = {
        u'south_data_migrate.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['south_data_migrate']