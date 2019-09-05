# from flask import  flash , Flask, get_flashed_messages,request,redirect
#
# app = Flask(__name__)
#
#
# @app.route('/index')
# def index():
#     val = request.args.get('v')
#     if val == 'ZJL':
#         return 'Hello world'
#     flash('超时错误',category='x1')
#     return 'Hello'
#
# @app.route('/error')
# def error():
#     data = get_flashed_messages(category_filter=['x1'])
#     print(data)
#     if data:
#         msg = data[0]
#     else:
#         msg = '...'
#     return '错误信息：%s' %(msg)
#
# if __name__ == '__main__':
#     app.run()
#
#----上面有错

from flask import Flask,session,flash,get_flashed_messages

app = Flask(__name__)
app.secret_key = "sdfgergrshhsh"
@app.route("/x1",methods=["GET","POST"])
def login():
    # session['msg'] = "回复哈哈哈哈哈哈"  #这是基于session做的
    flash("的工作过热1",category='x1')    #这是另一种方法，设置flash，这个内部也是基于session做的，flash其实就是把这个值设置到session上
    flash("色方法二果然够",category='x2')#category表示对数据进行分类
    return "视图函数x1"

@app.route("/x2",methods=["GET","POST"])
def index():
    data = get_flashed_messages(category_filter=['x1']) #这个是取上面我们设置的类似于错误信息的东西，这个其实就是在session上把他上面设置的值拿到并且删除
    #category_filter = ['x1'] 这个意思就是取x1那个对应的数据，两个都要拿就category_filter = ['x1','x1']
    print(data)
    # msg = session.pop('msg')  #这个拿完以后就没有了，这是基于session实现的，看完以后就删除了
    return "视图函数x2"

if __name__ == '__main__':
    app.run()