from django.test import TestCase
from django.test.client import Client
from contacts.models import Contact
from django.utils import timezone
from cupstest import settings

class ContactModelTest(TestCase):
    fixtures=['initial_data.json']
    def test_creating_a_new_contact_and_save_it_to_db(self):
        #check for one contact from fixture
        all_contacts = Contact.objects.all()
        self.assertEqual(len(all_contacts), 1)
        
        #create a new contact
        contact = Contact()
        contact.name = 'Kostyantyn'
        contact.surname = 'Surename'
        contact.birthdate = timezone.now()
        contact.bio = 'My bio'

        contact.jabber = 'jabber'
        contact.email = 'admin@admin.com'
        contact.skype = 'skype'
        contact.other = 'bla-bla-bla'
        
        contact.save()
        
        all_contacts = Contact.objects.all()
        self.assertEqual(len(all_contacts), 2)
        db_contact = all_contacts.get(pk=contact.pk)
        
        self.assertEqual(db_contact.name, 'Kostyantyn')
        self.assertEqual(db_contact.surname, 'Surename')
        self.assertEqual(db_contact.birthdate, contact.birthdate)
        self.assertEqual(db_contact.bio, 'My bio')
        
        self.assertEqual(len(all_contacts), 2)
        
        self.assertEqual(db_contact.jabber, 'jabber')
        self.assertEqual(db_contact.email, 'admin@admin.com')
        self.assertEqual(db_contact.skype, 'skype')
        self.assertEqual(db_contact.other, 'bla-bla-bla')
        
class ContactClientTest(TestCase):
    fixtures=['initial_data.json']
    
    def test_checking_contact_view(self):
        c = Client()
        #lets check that default page is exist
        response = c.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        
        #check for css classes
        self.assertContains(response, "class='left'", 2, 200)
        
        #check if default contact exists
        self.assertIsNotNone(response.context['contact'])
        #Check templete which was used
        self.assertTemplateUsed(response, 'contacts/index.html')
        #try to find the Edit link
        self.assertNotContains(response, '/contacts/edit/'+ str(response.context['contact'].pk))
    
    def test_checking_contact_update(self):
        c = Client()
        response = c.get('/contacts/edit/1/')
        self.assertEqual(response.status_code, 302)
        
        res = c.login(username = 'admin', password='admin')
        self.assertTrue(res)
                
        response = c.get('/contacts/edit/1/')
        self.assertEqual(response.status_code, 200)
        
        contact = response.context["contact"] 
        
        #Check for correct contact to edit
        self.assertEqual(contact.surname , 'Surname')
        self.assertEqual(contact.name , 'Name')
        self.assertEqual(contact.photo , 'images/dave_web_gross.jpg')
        self.assertEqual(contact.email , 'admin@admin.com')
        self.assertEqual(contact.bio , 'some bio notest')
        
        
        #try to save wrong data
        response = c.post("/contacts/edit/1/", 
                          {
                           'name':'Name',
                           'surname':'Surname',
                           'photo':contact.photo,
                           'email':'admin1admin.com',
                           'bio':'admin@admin.com',
                           'birthdate':'1982-08-01 17:37:31',
                           'skype':'skype',
                           'other':contact.other,
                           'jabber':'jabber'
                           })
        
        self.assertContains(response, "Enter a valid email address.", 1)
        
        #perform good save and check redirect
        with open(settings.MEDIA_ROOT + '/images/dave_web_gross.jpg') as fp:
            response = c.post("/contacts/edit/1/", 
                              {
                               'name':'Name',
                               'surname':'Surname',
                               'photo':fp,
                               'email':'admin1@admin.com',
                               'bio':'admin@admin.com',
                               'birthdate':'1982-08-01 17:37:31',
                               'skype':'skype',
                               'other':contact.other,
                               'jabber':'jabber'
                               }, follow=True)
        self.assertRedirects(response, "/contacts/", 302)
        #check if data was actually changed
        self.assertEqual(response.context['contact'].email, 'admin1@admin.com')
        