import os
import sys
import inspect
db_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(db_dir, os.path.dirname(db_dir), os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))