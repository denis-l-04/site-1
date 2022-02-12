from app.db_requests import *

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about', methods = ['GET', 'POST'])
def post_feedback():
    if flask.request.method == 'POST':
        new_comment = Feedback(name = flask.escape(flask.request.form.get('name')),
            email = flask.escape(flask.request.form.get('email')),
            text = flask.escape(flask.request.form.get('text')),)
        alch.session.add(new_comment)
        alch.session.commit()
    return flask.render_template('about.html', feedback = Feedback.query.all())

@app.route('/catalog')
def catalog():
    return flask.render_template('catalog.html')

print('web request handlers included')
