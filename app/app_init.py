import flask
import flask_sqlalchemy

app_obj = flask.Flask(__name__)
app_obj.config.from_object('config')
alch = flask_sqlalchemy.SQLAlchemy(app_obj)

print('app initializer included')
