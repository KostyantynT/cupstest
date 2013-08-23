from django.test import TestCase
from middleware.models import RequestLog
from django.test import Client
from django.core.urlresolvers import reverse

class MiddlewareTest(TestCase):
    def test_middleware_addition(self):
        #we should use empty database
        logs = RequestLog.objects.all()
        self.assertEqual(len(logs), 0)
        
        #lets add one request
        c = Client()
        resp = c.get(reverse("list"))
        
        logs = RequestLog.objects.all()
        self.assertEqual(len(logs), 1)
        #it will be required later...
        first_request = resp.context["requests"][0]
        
        #make sure we display it on the list
        self.assertContains(resp, reverse('list'), 1)
        
        #lets check we log wrong requests also
        resp = c.get('bad-path')
        self.assertEqual(resp.status_code, 404)
        
        #make sure we have 2 request in db now
        logs = RequestLog.objects.all()
        self.assertEqual(len(logs), 2)
        
        #lets add even more request
        for i in range(0,20):
            c.get(reverse('list'))
        
        logs = RequestLog.objects.all()
        self.assertEqual(len(logs), 22)
        #make sure we display only 10 request!
        resp = c.get(reverse('list'))
        requests = resp.context["requests"]
        count = len(requests)
        self.assertEqual(count, 10)
        
        #make sure that we display only first 10 request
        self.assertEqual(first_request, requests[0])        