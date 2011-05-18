# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'App'
        db.create_table('commons_core_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commons_core', ['App'])

        # Adding model 'Jurisdiction'
        db.create_table('commons_core_jurisdiction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commons_core', ['Jurisdiction'])

        # Adding model 'Deployment'
        db.create_table('commons_core_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.Jurisdiction'])),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.App'])),
        ))
        db.send_create_signal('commons_core', ['Deployment'])


    def backwards(self, orm):
        
        # Deleting model 'App'
        db.delete_table('commons_core_app')

        # Deleting model 'Jurisdiction'
        db.delete_table('commons_core_jurisdiction')

        # Deleting model 'Deployment'
        db.delete_table('commons_core_deployment')


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
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
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['commons_core']
