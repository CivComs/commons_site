# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SSProduct'
        db.create_table('commons_core_ssproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssid', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('commons_core', ['SSProduct'])

        # Adding model 'SSBudget'
        db.create_table('commons_core_ssbudget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orgid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSOrganization'], to_field='ssid')),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('commons_core', ['SSBudget'])

        # Adding model 'SSDependency'
        db.create_table('commons_core_ssdependency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prodid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSProduct'], to_field='ssid')),
            ('dependencyid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.DependencyType'], to_field='name')),
        ))
        db.send_create_signal('commons_core', ['SSDependency'])

        # Adding model 'SSOrganization'
        db.create_table('commons_core_ssorganization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssid', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parentid', self.gf('django.db.models.fields.TextField')(default='')),
            ('parentname', self.gf('django.db.models.fields.TextField')(default='')),
            ('geolong', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=4)),
            ('geolat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=4)),
            ('geoname', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('geoarea', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=4)),
            ('population', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('govtype', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('commons_core', ['SSOrganization'])

        # Adding model 'DependencyType'
        db.create_table('commons_core_dependencytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='', unique=True)),
        ))
        db.send_create_signal('commons_core', ['DependencyType'])

        # Renaming column for 'App.ssid' to match new field type.
        db.rename_column('commons_core_app', 'ssid', 'ssid_id')
        # Changing field 'App.ssid'
        db.alter_column('commons_core_app', 'ssid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSProduct']))

        # Adding index on 'App', fields ['ssid']
        db.create_index('commons_core_app', ['ssid_id'])

        # Renaming column for 'Jurisdiction.ssid' to match new field type.
        db.rename_column('commons_core_jurisdiction', 'ssid', 'ssid_id')
        # Changing field 'Jurisdiction.ssid'
        db.alter_column('commons_core_jurisdiction', 'ssid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSOrganization']))

        # Adding index on 'Jurisdiction', fields ['ssid']
        db.create_index('commons_core_jurisdiction', ['ssid_id'])


    def backwards(self, orm):
        
        # Removing index on 'Jurisdiction', fields ['ssid']
        db.delete_index('commons_core_jurisdiction', ['ssid_id'])

        # Removing index on 'App', fields ['ssid']
        db.delete_index('commons_core_app', ['ssid_id'])

        # Deleting model 'SSProduct'
        db.delete_table('commons_core_ssproduct')

        # Deleting model 'SSBudget'
        db.delete_table('commons_core_ssbudget')

        # Deleting model 'SSDependency'
        db.delete_table('commons_core_ssdependency')

        # Deleting model 'SSOrganization'
        db.delete_table('commons_core_ssorganization')

        # Deleting model 'DependencyType'
        db.delete_table('commons_core_dependencytype')

        # Renaming column for 'App.ssid' to match new field type.
        db.rename_column('commons_core_app', 'ssid_id', 'ssid')
        # Changing field 'App.ssid'
        db.alter_column('commons_core_app', 'ssid', self.gf('django.db.models.fields.IntegerField')())

        # Renaming column for 'Jurisdiction.ssid' to match new field type.
        db.rename_column('commons_core_jurisdiction', 'ssid_id', 'ssid')
        # Changing field 'Jurisdiction.ssid'
        db.alter_column('commons_core_jurisdiction', 'ssid', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']"})
        },
        'commons_core.dependencytype': {
            'Meta': {'object_name': 'DependencyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''", 'unique': 'True'})
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
