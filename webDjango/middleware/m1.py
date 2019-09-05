from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('1')

    def process_response(self,request,response):
        print('6')
        return response


class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('2')
        #return HttpResponse('滚')

    def process_response(self,request,response):
        print('5')
        return response


class Row3(MiddlewareMixin):
    def process_request(self,request):
        print('3')

    def process_response(self,request,response):
        print('4')
        return response


class Row4(MiddlewareMixin):
    def process_request(self,request):
        print('A')
        #return HttpResponse('滚')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('C')

    def process_response(self,request,response):
        print('5')
        return response


class Row5(MiddlewareMixin):
    def process_request(self,request):
        print('B')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('D')

    def process_response(self,request,response):
        print('4')
        return response

    def process_exception(self,request,exception):
        if isinstance(exception,ValueError):
            return HttpResponse('It is has a falut')