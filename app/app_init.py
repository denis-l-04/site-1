import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config.from_object('config')
alch = flask_sqlalchemy.SQLAlchemy(app)

print('app initializer included')
