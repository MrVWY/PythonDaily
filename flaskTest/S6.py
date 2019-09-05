from flask.globals import _request_ctx_stack
from functools import partial

def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError('没有')
    return getattr(top, name)


class  foo(object):
    def __init__(self):
        self.xxx = 123
        self.kkk = 345


req = partial(_lookup_req_object,'xxx')
XXX = partial(_lookup_req_object,'kkk')

_request_ctx_stack.push(foo())


v1 = req()
print(v1)
v2 = XXX()
print(v2)

_request_ctx_stack.pop()  #移除