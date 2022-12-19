# coding=utf-8
import os
import subprocess

def Systeam():
    """
        return: Mac Win Linux

        (Cygwin算作Win AIX算作Linux)

        'win32':Windows
        'cygwin':Windows/Cygwin
        'darwin':macOS
        'aix':AIX
        'linux':Linux
    """
    from sys import platform
    a = str(platform)
    if a == 'win32' or a == 'cygwin':
        s = 'Win'
    elif a == 'darwin':
        s = 'Mac'
    elif a == 'linux' or a == 'aix':
        s = 'Linux'
    return s


if __name__ == '__main__':
    f = os.path.split(os.path.realpath(__file__))[0]
    f_u = os.path.abspath(f)
    post = 8000
    if Systeam() == 'Win':
        s = 'venv\Scripts\activate;'
    else:
        s = 'source venv/bin/activate;'
    FrontRun = 'cd ' + f_u + ';' + s + 'python manage.py runserver ' + str(post)
    BackRun = 'cd ' + f_u + ';' + s + 'python ./Back/main.py'
    FrontRun_S = subprocess.Popen(FrontRun, shell=True)
    BackRun_S = subprocess.Popen(BackRun, shell=True)
    try:
        FrontRun_S.wait()
        BackRun_S.wait()
    except KeyboardInterrupt:
        FrontRun_S.kill()
        BackRun_S.kill()
        exit()

