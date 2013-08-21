# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ContactDetail.email'
        db.alter_column(u'contacts_contactdetail', 'email', self.gf('django.db.models.fields.EmailField')(max_length=254))
        # Adding field 'Contact.photo'
        db.add_column(u'contacts_contact', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'ContactDetail.email'
        db.alter_column(u'contacts_contactdetail', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Deleting field 'Contact.photo'
        db.delete_column(u'contacts_contact', 'photo')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {}),
            'contactdetails': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.ContactDetail']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contacts.contactdetail': {
            'Meta': {'object_name': 'ContactDetail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contacts']