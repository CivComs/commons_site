# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'App'
        db.create_table('commons_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commons', ['App'])

        # Adding model 'Jurisdiction'
        db.create_table('commons_jurisdiction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commons', ['Jurisdiction'])

        # Adding model 'Deployment'
        db.create_table('commons_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.Jurisdiction'])),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.App'])),
        ))
        db.send_create_signal('commons', ['Deployment'])


    def backwards(self, orm):
        
        # Deleting model 'App'
        db.delete_table('commons_app')

        # Deleting model 'Jurisdiction'
        db.delete_table('commons_jurisdiction')

        # Deleting model 'Deployment'
        db.delete_table('commons_deployment')


    models = {
        'commons.app': {
            'Meta': {'object_name': 'App'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'commons.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons.Jurisdiction']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'commons.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['commons']
