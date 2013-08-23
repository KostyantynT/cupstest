from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from cupstest import settings

class CpntextProcessorTest(TestCase):
    def test_view_for_settings_variables(self):
        c = Client()
        response = c.get(reverse('list'))
        #lets check some wariable
        mr = response.context['MEDIA_ROOT']
        self.assertNotEqual(mr, None)
        #lets check that out Apps contains the current app
        apps = response.context['INSTALLED_APPS']
        self.assertIn("cupstest", apps)