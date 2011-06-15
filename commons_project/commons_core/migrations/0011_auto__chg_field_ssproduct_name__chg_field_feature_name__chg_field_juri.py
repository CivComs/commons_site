# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'SSProduct.name'
        db.alter_column('commons_core_ssproduct', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Feature.name'
        db.alter_column('commons_core_feature', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Jurisdiction.name'
        db.alter_column('commons_core_jurisdiction', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Screenshot.name'
        db.alter_column('commons_core_screenshot', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'App.name'
        db.alter_column('commons_core_app', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'SSOrganization.name'
        db.alter_column('commons_core_ssorganization', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'SSProduct.name'
        db.alter_column('commons_core_ssproduct', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Feature.name'
        db.alter_column('commons_core_feature', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Jurisdiction.name'
        db.alter_column('commons_core_jurisdiction', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Screenshot.name'
        db.alter_column('commons_core_screenshot', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'App.name'
        db.alter_column('commons_core_app', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SSOrganization.name'
        db.alter_column('commons_core_ssorganization', 'name', self.gf('django.db.models.fields.TextField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'commons_core.app': {
            'Meta': {'object_name': 'App'},
            'dependencies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dependents'", 'symmetrical': 'False', 'through': "orm['commons_core.Dependency']", 'to': "orm['commons_core.App']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['commons_core.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'screenshots': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['commons_core.Screenshot']", 'null': 'True', 'blank': 'True'}),
            'ssp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSProduct']", 'null': 'True', 'blank': 'True'})
        },
        'commons_core.ccprofile': {
            'Meta': {'object_name': 'CCProfile'},
            'affiliation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.Jurisdiction']", 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'commons_core.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'commons_core.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['commons_core.Jurisdiction']"}),
            'sso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commons_core.SSOrganization']", 'null': 'True', 'blank': 'True'})
        },
        'commons_core.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'parentid': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'parentname': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'commons_core.ssproduct': {
            'Meta': {'object_name': 'SSProduct'},
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'ssid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_file_type_plugin_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['commons_core']
