import os

SECRET_KEY = 'greedywindow123'
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '/database.db')

print('base directory:', BASE_DIR)
print('database used:', SQLALCHEMY_DATABASE_URI)
