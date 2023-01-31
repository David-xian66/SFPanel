# coding=utf-8
import json
import os
import subprocess
import sys

from Back.Code import system, JsonWrite, JsonRead
from Back.Log import Log as print

print = print('Starter')


def Config():
    print.INFO('开始检查config.json')
    Json = {
        'Back': {
            'comments': '后端设置-本地启动',
            'IPAndPost': {
                'IP': '0.0.0.0',
                'Post': 9000
            },
            'Enable': True,
            'comments-Enable': '是否启用(True or False)'
        },
        'Front': {
            'comments': '前端设置-本地启动',
            'IPAndPost': {
                'IP': '0.0.0.0',
                'Post': 8000
            },
            'Enable': True,
            'comments-Enable': '是否启用(True or False)'
        }
    }
    JsonFile_Path = os.path.join('config.json')
    if not os.path.exists(JsonFile_Path) or not os.path.getsize(JsonFile_Path):
        JsonWrite(JsonFile_Path, Json)
    else:
        try:
            print.INFO('Json检查开始')
            j_f = JsonRead(JsonFile_Path)
            for j in Json:
                if j in j_f:
                    # 如果存在就判断值是不是字典
                    print.INFO(type(Json[j]))
        except json.decoder.JSONDecodeError:
            print.ERROR('Json配置文件损坏,请修复或删除文件配置文件并重启(会自动为您生成新配置文件)')
            exit(-1)


def Check():
    print.INFO('Start Running……')
    Config()
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
    print.INFO('解释器版本: ' + V_2)
    S = str(sys.platform)
    print.INFO('运行平台: ' + S)
    P = os.path.split(os.path.realpath(__file__))[0]
    print.INFO('运行目录: ' + str(P))
    print.INFO('--自检完毕--')


if __name__ == '__main__':
    # PYPath = sys.executable
    Check()

    f = os.path.split(os.path.realpath(__file__))[0]
    f_u = os.path.abspath(f)

    s = str(sys.platform)
    if s == 'win32' or s == 'cygwin':
        f = '&&'
    else:
        f = ';'

    post = 8000
    if system() == 'Win':
        s = os.path.join('venv', 'Scripts', 'activate') + f
    else:
        s = 'source ' + os.path.join('venv', 'bin', 'activate') + f
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
