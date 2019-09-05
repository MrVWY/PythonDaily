import time
from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
Visit_Recording = {}
class Visit_control(BaseThrottle):
    ''' 60秒 3次'''
    def __init__(self):
        self.history = None

    def allow_request(self,request,view):
        #remote_addr = request.META.get('REMOTE_ADDR')
        remote_addr = self.get_ident(request)
        ctime = time.time()
        if remote_addr not in Visit_Recording:
            Visit_Recording[remote_addr] = [ctime,]
            return True
        history = Visit_Recording.get(remote_addr)
        self.history = history
        while history and history[-1] < ctime-60:
            history.pop()
        if len(history) < 3 :
            history.insert(0,ctime)
            return True

    def wait(self):
        ctime = time.time()
        return  60-(ctime-self.history[-1])

class VisitThrottle(SimpleRateThrottle):
    scope = 'ZJL'

    def get_cache_key(self, request, view):
        return self.get_ident(request)