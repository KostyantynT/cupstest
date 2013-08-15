from django.test import TestCase
from contacts.models import Contact
from django.utils import timezone

class ContactModelTest(TestCase):
    def test_creating_a_new_contact_and_save_it_to_db(self):
        #create a new contact
        contact = Contact()
        contact.name = 'Kostyantyn'
        contact.surname = 'Surename'
        contact.birthdate = timezone.now()
        contact.bio = 'My bio'
        contact.contacts = 'contacts'

        contact.save()

        all_contacts = Contact.objects.all()
        self.assertEqual(len(all_contacts), 1)
        db_contact = all_contacts[0]
        self.assertEqual(db_contact, contact)

        self.assertEqual(db_contact.name, 'Kostyantyn')
        self.assertEqual(db_contact.surname, 'Surename')
        self.assertEqual(db_contact.birthdate, contact.birthdate)
        self.assertEqual(db_contact.bio, 'My bio')
        self.assertEqual(db_contact.contacts, 'contacts')