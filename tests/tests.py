from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminTest(LiveServerTestCase):
    fixtures=['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_login_to_admin_site(self):
        self.browser.get(self.live_server_url+'/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        contact_links = self.browser.find_elements_by_link_text('Contacts')
        self.assertEqual(len(contact_links), 2)
        
class ContactTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_checking_detail_page(self):
        self.browser.get(self.live_server_url+'/contacts/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('42 Coffee Cups Test Assignment', body.text)
        
        self.assertIn('Name', body.text)
        self.assertIn('Surname', body.text)
        self.assertIn('bio info', body.text)
        self.assertIn('1982', body.text)
        self.assertIn('skype', body.text)
        self.assertIn('admin@admin.com', body.text)
        self.assertIn('jabber', body.text)
        self.assertIn('other....', body.text)
