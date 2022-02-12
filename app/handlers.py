from app.db_requests import *

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/catalog')
def catalog():
    return flask.render_template('catalog.html')

print('web request handlers included')
