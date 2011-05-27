# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Dependency'
        db.create_table('commons_core_dependency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_apps', to=orm['commons_core.App'])),
            ('to_app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_apps', to=orm['commons_core.App'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.DependencyType'])),
        ))
        db.send_create_signal('commons_core', ['Dependency'])

        # Adding field 'Jurisdiction.parent'
        db.add_column('commons_core_jurisdiction', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['commons_core.Jurisdiction']), keep_default=False)

        # Changing field 'DependencyType.name'
        db.alter_column('commons_core_dependencytype', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30))


    def backwards(self, orm):
        
        # Deleting model 'Dependency'
        db.delete_table('commons_core_dependency')

        # Deleting field 'Jurisdiction.parent'
        db.delete_column('commons_core_jurisdiction', 'parent_id')

        # Changing field 'DependencyType.name'
        db.alter_column('commons_core_dependencytype', 'name', self.gf('django.db.models.fields.TextField')(unique=True))


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'dependencies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dependents'", 'symmetrical': 'False', 'through': "orm['commons_core.Dependency']", 'to': "orm['commons_core.App']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']"})
        },
        'commons_core.dependency': {
            'Meta': {'object_name': 'Dependency'},
            'from_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_apps'", 'to': "orm['commons_core.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_apps'", 'to': "orm['commons_core.App']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.DependencyType']"})
        },
        'commons_core.dependencytype': {
            'Meta': {'object_name': 'DependencyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '30'})
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['commons_core.Jurisdiction']"}),
            'ssid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSOrganization']"})
        },
        'commons_core.ssbudget': {
            'Meta': {'object_name': 'SSBudget'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSOrganization']", 'to_field': "'ssid'"}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'commons_core.ssdependency': {
            'Meta': {'object_name': 'SSDependency'},
            'dependencyid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prodid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']", 'to_field': "'ssid'"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.DependencyType']", 'to_field': "'name'"})
        },
        'commons_core.ssorganization': {
            'Meta': {'object_name': 'SSOrganization'},
            'geoarea': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geolat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geolong': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geoname': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'govtype': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'parentid': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'parentname': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'commons_core.ssproduct': {
            'Meta': {'object_name': 'SSProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True'})
        }
    }

    complete_apps = ['commons_core']
