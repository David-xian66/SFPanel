# coding=utf-8
import json


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


def JsonWrite(JsonFile,Json_):
    """
        写入Json
        :param JsonFile: Json路径
        :param Json_: Json内容
    """
    with open(JsonFile, 'w+', encoding='utf_8') as f:
        json.dump(Json_, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


def JsonRead(JsonFile):
    """
        读取Json
        JsonFile = Json的目录
    """
    with open(JsonFile, 'r', encoding='utf_8') as f:
        r = json.load(f, strict=False)
    return r
