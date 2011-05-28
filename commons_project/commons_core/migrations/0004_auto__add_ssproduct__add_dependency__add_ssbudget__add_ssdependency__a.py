# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SSProduct'
        db.create_table('commons_core_ssproduct', (
            ('ssid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('commons_core', ['SSProduct'])

        # Adding model 'Dependency'
        db.create_table('commons_core_dependency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_apps', to=orm['commons_core.App'])),
            ('to_app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_apps', to=orm['commons_core.App'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.DependencyType'], null=True, blank=True)),
        ))
        db.send_create_signal('commons_core', ['Dependency'])

        # Adding model 'SSBudget'
        db.create_table('commons_core_ssbudget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orgid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSOrganization'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('commons_core', ['SSBudget'])

        # Adding model 'SSDependency'
        db.create_table('commons_core_ssdependency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prodid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSProduct'])),
            ('dependencyid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.DependencyType'])),
        ))
        db.send_create_signal('commons_core', ['SSDependency'])

        # Adding model 'SSOrganization'
        db.create_table('commons_core_ssorganization', (
            ('ssid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
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
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=30)),
        ))
        db.send_create_signal('commons_core', ['DependencyType'])

        # Deleting field 'App.ssid'
        db.delete_column('commons_core_app', 'ssid')

        # Adding field 'App.ssp'
        db.add_column('commons_core_app', 'ssp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSProduct'], null=True, blank=True), keep_default=False)

        # Deleting field 'Jurisdiction.ssid'
        db.delete_column('commons_core_jurisdiction', 'ssid')

        # Adding field 'Jurisdiction.sso'
        db.add_column('commons_core_jurisdiction', 'sso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons_core.SSOrganization'], null=True, blank=True), keep_default=False)

        # Adding field 'Jurisdiction.parent'
        db.add_column('commons_core_jurisdiction', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['commons_core.Jurisdiction']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'SSProduct'
        db.delete_table('commons_core_ssproduct')

        # Deleting model 'Dependency'
        db.delete_table('commons_core_dependency')

        # Deleting model 'SSBudget'
        db.delete_table('commons_core_ssbudget')

        # Deleting model 'SSDependency'
        db.delete_table('commons_core_ssdependency')

        # Deleting model 'SSOrganization'
        db.delete_table('commons_core_ssorganization')

        # Deleting model 'DependencyType'
        db.delete_table('commons_core_dependencytype')

        # Adding field 'App.ssid'
        db.add_column('commons_core_app', 'ssid', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'App.ssp'
        db.delete_column('commons_core_app', 'ssp_id')

        # Adding field 'Jurisdiction.ssid'
        db.add_column('commons_core_jurisdiction', 'ssid', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Jurisdiction.sso'
        db.delete_column('commons_core_jurisdiction', 'sso_id')

        # Deleting field 'Jurisdiction.parent'
        db.delete_column('commons_core_jurisdiction', 'parent_id')


    models = {
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'dependencies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dependents'", 'symmetrical': 'False', 'through': "orm['commons_core.Dependency']", 'to': "orm['commons_core.App']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ssp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']", 'null': 'True', 'blank': 'True'})
        },
        'commons_core.dependency': {
            'Meta': {'object_name': 'Dependency'},
            'from_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_apps'", 'to': "orm['commons_core.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_apps'", 'to': "orm['commons_core.App']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.DependencyType']", 'null': 'True', 'blank': 'True'})
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
            'sso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSOrganization']", 'null': 'True', 'blank': 'True'})
        },
        'commons_core.ssbudget': {
            'Meta': {'object_name': 'SSBudget'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orgid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSOrganization']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'commons_core.ssdependency': {
            'Meta': {'object_name': 'SSDependency'},
            'dependencyid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prodid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.DependencyType']"})
        },
        'commons_core.ssorganization': {
            'Meta': {'object_name': 'SSOrganization'},
            'geoarea': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geolat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geolong': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'geoname': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'govtype': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'parentid': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'parentname': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'commons_core.ssproduct': {
            'Meta': {'object_name': 'SSProduct'},
            'name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['commons_core']
