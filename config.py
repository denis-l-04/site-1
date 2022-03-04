import os

SECRET_KEY = 'greedywindow123'
DEBUG = False
TESTING = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if not TESTING:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app\\testing\\temp.db')

print('base directory:', BASE_DIR)
print('database used:', SQLALCHEMY_DATABASE_URI)
