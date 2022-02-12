from app.app_init import *
from app.ORM_models import *
alch.create_all()
from app.db_requests import *
from app.handlers import *

print('app module imported')