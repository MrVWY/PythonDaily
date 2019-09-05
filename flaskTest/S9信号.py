from flask import Flask ,current_app , flash ,render_template,signals
from flask.signals import  _signals

from flask_session import  RedisSessionInterface

app = Flask(__name__)

#自定义信号
Custom_Signal = _signals.signal('Hello')

def func(sender,*args,**kwargs):
    print(sender)

#自定义信号中注册函数
Custom_Signal.connect(func)

#signals.request_started.connect()

@app.route("/")
def index():
    # 触发信号
    Custom_Signal.send('123123', k1='v1')
    return 'Index'


if __name__ == '__main__':
    app.run()
