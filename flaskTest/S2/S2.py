from flask import Flask,request
from S2.utils.message  import  send_msgs
app = Flask(__name__)



@app.route('/index', methods=['GET'])
def index():

    data = request.query_string.get('val')
    if data  == 'xyy':
        send_msgs('message')

if __name__ == '__main__':
    app.run()