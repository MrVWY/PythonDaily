from flask import Flask,request,redirect,render_template,session,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)


@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    user = session.get('user_info')
    if not user:
        url = url_for('lt')
        return redirect(url)
    return  render_template('detail.html',info=nid)

@app.route('/index', methods=['GET'])
def index():
    user  = session.get('user_info')
    if not user :
        url = url_for('lt')
        return redirect(url)
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'],endpoint='lt')
def login():
    if request.method == 'GET':
        return  render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'al' and pwd == '123':
            session['user_info'] = user
            return redirect('https://www.baidu.com')
        return render_template('login.html',error = '用户名或密码错误')

#app.add_url_rule()

if __name__ == '__main__':
    app.__call__
    app.run()
