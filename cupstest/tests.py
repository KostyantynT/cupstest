from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from cupstest import settings

class CpntextProcessorTest(TestCase):
    def test_view_for_settings_variables(self):
        c = Client()
        response = c.get(reverse('list'))
        #lets check some wariable
        sett = response.context['settings']
        self.assertTrue(hasattr(sett, 'MEDIA_ROOT'))
        self.assertTrue(hasattr(sett, 'STATIC_ROOT'))