# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'App.ssid'
        db.add_column('commons_core_app', 'ssid', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Jurisdiction.ssid'
        db.add_column('commons_core_jurisdiction', 'ssid', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'App.ssid'
        db.delete_column('commons_core_app', 'ssid')

        # Deleting field 'Jurisdiction.ssid'
        db.delete_column('commons_core_jurisdiction', 'ssid')


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'commons_core.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.Jurisdiction']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'commons_core.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['commons_core']
