from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminTest(LiveServerTestCase):
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
    
    contact_links = self.browser.find_element_by_link_text('Contacts')
    self.assertEqual(len(contact_links), 2)
