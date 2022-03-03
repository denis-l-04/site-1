import hashlib
from app.db_requests import *

@app_obj.route('/')
def index():
    return flask.render_template('index.html')

@app_obj.route('/about', methods = ['GET', 'POST'])
def post_feedback():
    if flask.request.method == 'POST':
        new_comment = Feedback(name = flask.escape(flask.request.form.get('name')),
            email = flask.escape(flask.request.form.get('email')),
            text = flask.escape(flask.request.form.get('text')),)
        alch.session.add(new_comment)
        alch.session.commit()
    return flask.render_template('about.html', feedback = Feedback.query.all())

@app_obj.route('/catalog')
def catalog():
    return flask.render_template('catalog.html')

@app_obj.route('/registration', methods = ['GET', 'POST'])
def registration():
    if flask.request.method == 'POST':
        if Users.query.filter_by(email = flask.request.form.get('email')).all():
            flask.flash('Пользователь с таким адресом почты уже существует.', '#f66')
        elif flask.request.form.get('email')=='' or flask.request.form.get('password')=='' or flask.request.form.get('name')=='' or flask.request.form.get('surname')=='' or flask.request.form.get('birth_date')=='':
            flask.flash('Не заполнены все необходимые поля.', '#f66')
        else:
            try:
                birth_date = datetime.datetime.fromisoformat(flask.request.form.get('birth_date'))
            except Exception:
                flask.flash('Некорректная дата рождения.', '#f66')
                return flask.render_template('registration.html')
            new_user = Users(
                email = flask.escape(flask.request.form.get('email')),\
                phone = flask.escape(flask.request.form.get('phone')),\
                password_hash = hashlib.md5(flask.request.form.get('password').encode('utf8')).hexdigest(),\
                name = flask.escape(flask.request.form.get('name')),\
                surname = flask.escape(flask.request.form.get('surname')),\
                birth_date = birth_date,\
                sign_up_date = datetime.datetime.now()\
            )
            alch.session.add(new_user)
            alch.session.commit()
            flask.flash('Успешная регистрация.', '#6f6')
            resp = flask.redirect('/')
            flask.session['email'] = flask.request.form.get('email')
            resp.set_cookie('name', new_user.name)
            return resp
    return flask.render_template('registration.html')

@app_obj.route('/login', methods = ['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        current_user = None
        for u in Users.query.filter_by(email = flask.request.form.get('email'),\
        password_hash = hashlib.md5(flask.request.form.get('password').encode('utf8')).hexdigest()):
            current_user = u
            break
        if current_user:
            resp = flask.redirect('/')
            flask.session['email'] = flask.request.form.get('email')
            resp.set_cookie('name', current_user.name)
            flask.flash(f'Добро пожаловать, {current_user.name}!', '#6f6')
            return resp
        else:
            flask.flash('Неправильный адрес почты или пароль.', '#f66')
    return flask.render_template('login.html')

@app_obj.route('/logout')
def logout():
    resp = flask.redirect('/')
    if flask.session.get('email'):
        flask.session.pop('email')
        resp.set_cookie('name', '', expires = 0)
    return resp

print('web request handlers included')
