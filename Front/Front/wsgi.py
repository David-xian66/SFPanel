"""
WSGI config for Front project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os,requests

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Front.settings')

application = get_wsgi_application()

from Back.Log import Log as print
from manage import INFO
print.INFO('前端启动成功')
BackURL = INFO.BackURL
print.INFO('尝试连接到后端 -> ' + BackURL)

while True:
    a = requests.get(BackURL)
    j = a.json()
    if str(j) == "{'hello': 'world'}":
        break
print.INFO('后端连接成功')



