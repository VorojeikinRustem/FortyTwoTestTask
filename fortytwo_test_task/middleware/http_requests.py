import re

from apps.hello.models import HttpRequests

class HttpRequest(object):
    def process_request(self, request): 

        http_request = HttpRequests(http_request=str(request.META['REQUEST_METHOD'] + ' ' + request.META['PATH_INFO'] + ' ' + request.META['SERVER_PROTOCOL']))
        http_request.save()

        return None