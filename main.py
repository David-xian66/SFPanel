# coding=utf-8
import os
import subprocess
import sys

from Back.Code import Systeam

if __name__ == '__main__':
    # PYPath = sys.executable
    f = os.path.split(os.path.realpath(__file__))[0]
    f_u = os.path.abspath(f)
    post = 8000
    if Systeam() == 'Win':
        s = os.path.join('venv','Scripts','activate') + ';'
    else:
        s = 'source ' + os.path.join('venv','bin','activate') + ';'
    print(f_u)
    Front_ManageFile = os.path.join('Front', 'manage.py')
    Back_MainFile = os.path.join('Back', 'main.py')

    PyRun_S = str(sys.executable)

    FrontRun = 'cd ' + f_u + ';' + s + PyRun_S + ' ' + Front_ManageFile + ' runserver ' + str(post)
    BackRun = 'cd ' + f_u + ';' + s + PyRun_S + ' ' + Back_MainFile
    print(FrontRun)    
    print(BackRun)
    FrontRun_S = subprocess.Popen(FrontRun, shell=True)
    BackRun_S = subprocess.Popen(BackRun, shell=True)
    try:
        FrontRun_S.wait()
        BackRun_S.wait()
    except KeyboardInterrupt:
        FrontRun_S.terminate()
        BackRun_S.terminate()
        exit()
