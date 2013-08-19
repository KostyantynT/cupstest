from django.shortcuts import render

from models import RequestLog

def list(request):
    requests = RequestLog.objects.order_by('time')[:10]
    return render(request, 'middleware/list.html', {'requests' : requests})