from models import RequestLog

class RequestMiddleware(object):
    def process_request(self, request):
        RequestLog.objects.create(path = request.path)
        return None
