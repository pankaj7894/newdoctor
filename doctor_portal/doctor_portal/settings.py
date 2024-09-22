import os
from decouple import config
print('settings_local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE', default='doctor_portal.settings_local'))
