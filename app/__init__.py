from app.app_init import *
from app.ORM_models import *
if not app_obj.config['TESTING']:
    alch.create_all()
from app.db_requests import *
from app.handlers import *

print('app module imported')