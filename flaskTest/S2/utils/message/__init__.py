import S2.settings
import importlib

def send_msgs(msg):

    for path in  S2.settings.MSG_list:
        m,c = path.rstrip('.',maxsplit=1)
        md = importlib.import_module(m)
        obj = getattr(md,c)
        obj.send(msg)
