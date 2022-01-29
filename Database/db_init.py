import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DBPATH
alch = flask_sqlalchemy.SQLAlchemy(app)
from ORM_models import *
alch.create_all()

print('Database initializer imported!')