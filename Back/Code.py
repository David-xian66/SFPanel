# coding=utf-8
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