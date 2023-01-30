# coding=utf-8
import os
import subprocess
import sys

from Back.Code import Systeam
from Back.Log import Log as print

def Cheak():
    V = list(sys.version_info)
    print.INFO('--运行信息--')
    C = sys.implementation
    print.INFO('释解器信息: ' + str(C))
    V_2 = ''
    V_2_i = 0
    for V_1 in V[:3]:
        V_2_i += 1
        V_1 = str(V_1)
        if V_2_i < 3:
            V_1 += '.'
        else:
            pass
        V_2 += V_1
    print.INFO('释解器版本: ' + V_2)
    S = str(sys.platform)
    print.INFO('运行平台: ' + S)
    P = os.path.split(os.path.realpath(__file__))[0]
    print.INFO('运行目录: ' + str(P))
    print.INFO('--自检完毕--')
    

if __name__ == '__main__':
    # PYPath = sys.executable
    Cheak()
    
    f = os.path.split(os.path.realpath(__file__))[0]
    f_u = os.path.abspath(f)

    s = str(sys.platform)
    if s == 'Windows' or s == 'cygwin':
        f = '&&'
    else:
        f = ';'

    post = 8000
    if Systeam() == 'Win':
        s = os.path.join('venv','Scripts','activate') + f
    else:
        s = 'source ' + os.path.join('venv','bin','activate') + f
    Front_ManageFile = os.path.join('Front', 'manage.py')
    Back_MainFile = os.path.join('Back', 'main.py')

    PyRun_S = str(sys.executable)

    FrontRun = 'cd ' + f_u + f + s + PyRun_S + ' ' + Front_ManageFile + ' runserver ' + str(post)
    BackRun = 'cd ' + f_u + f + s + PyRun_S + ' ' + Back_MainFile
    print.INFO('前端启动命令' + FrontRun)    
    print.INFO('后端启动命令' + BackRun)
    FrontRun_S = subprocess.Popen(FrontRun, shell=True)
    BackRun_S = subprocess.Popen(BackRun, shell=True)
    try:
        FrontRun_S.wait()
        BackRun_S.wait()
    except KeyboardInterrupt:
        FrontRun_S.terminate()
        BackRun_S.terminate()
        exit()
