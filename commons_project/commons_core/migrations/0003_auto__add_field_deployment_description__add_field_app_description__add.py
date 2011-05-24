# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Deployment.description'
        db.add_column('commons_core_deployment', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'App.description'
        db.add_column('commons_core_app', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Jurisdiction.description'
        db.add_column('commons_core_jurisdiction', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Deployment.description'
        db.delete_column('commons_core_deployment', 'description')

        # Deleting field 'App.description'
        db.delete_column('commons_core_app', 'description')

        # Deleting field 'Jurisdiction.description'
        db.delete_column('commons_core_jurisdiction', 'description')


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'commons_core.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.App']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.Jurisdiction']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'commons_core.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['commons_core']
