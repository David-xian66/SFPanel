"""
WSGI config for Front project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os,requests,sys,traceback,time

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Front.settings')

sys.path.append(os.getcwd)

sys.path.append("./")
sys.path.append("../")
sys.path.append(".../")

application = get_wsgi_application()

from Back.Log import Log as print
from manage import INFO

print.INFO('前端启动成功')
BackURL = INFO.BackURL + '/ping'
print.INFO('尝试连接到后端 -> ' + BackURL)

while True:
    try:
        a = ''
        a = requests.get(BackURL)
        print(a)
        j = a.json()
        print.INFO(j)
        if str(j) == "{'hello': 'world'}":
            break
        else:
            print.ERROR('连接失败 5s后重试,收到了异常回复,请检查IP 端口设置是否正确,收到的异常输出: ' + str(j))
            time.sleep(5)
    except:
        del a
        ErrorInfo = traceback.format_exc()
        print.ERROR('连接失败 5s后重试,发生错误,错误输出: ' + str(ErrorInfo))
        time.sleep(5)
print.INFO('后端连接成功')



