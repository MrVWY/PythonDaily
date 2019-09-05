
from . import app

@app.route('/login')
def login():
    return 'login'


@app.route('/logout')
def logout():
    return 'logout'