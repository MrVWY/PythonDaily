

from . import app

@app.route('/user')
def account():
    return 'user'