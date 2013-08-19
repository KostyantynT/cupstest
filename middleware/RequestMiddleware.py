from models import RequestLog

class RequestMiddleware(object):
    def process_request(self, request):
        try:
            requestlog = RequestLog()
            requestlog.path = request.path;
            requestlog.save();
        except:
            pass
        
        return None
