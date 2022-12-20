# coding=utf-8
"""日志系统"""
import datetime

# 日志系统 这个列表是暂存的 主窗口会定时 获取 -> 写入 -> 清空 (全局变量)
r = []


class Print_Colour:
    """
        HEADER:偏粉的紫色
        OKBLUE:蓝色
        OKCYAN:青色
        OKGREEN:绿色
        OKGREEN_2:有下划线的绿色
        WARNING:黄色
        WARNING_2:有下划线的黄色
        FAIL:红色
        FAIL_2:加粗的红色
        FAIL_3:有下划线的红色
        ENDC:正常的黑色
        BOLD:加粗的黑色
        UNDERLINE:有下横线的黑色
        GRAY:灰色
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[32m'
    OKGREEN_2 = '\033[4;32m'
    WARNING = '\033[93m'
    WARNING_2 = '\033[4;93m'
    FAIL = '\033[91m'
    FAIL_2 = '\033[1;91m'
    FAIL_3 = '\033[4;91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[37m'


class Log():
    def INFO(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        I = Print_Colour.OKGREEN + '[' +'INFO' + ']' + Print_Colour.ENDC + ' '
        P_ = Print_Colour.GRAY + P + Print_Colour.ENDC
        print(Time+I+P_)
        r.append(Time_+' '+'INFO '+P)
    def BEBUG(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%H:%M:%S')
        Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        I = Print_Colour.WARNING + '[' +'BEBUG' + ']' + Print_Colour.ENDC + ' '
        P_ = Print_Colour.GRAY + P + Print_Colour.ENDC
        print(Time+I+P_)
        r.append(Time_+' '+'BEBUG '+P)
    def ERROR(P):
        P = str(P)
        Time_ = datetime.datetime.now().strftime('%H:%M:%S')
        Time = Print_Colour.OKBLUE + '[' + Time_ + ']' + Print_Colour.ENDC + ' '
        I = Print_Colour.FAIL + '[' +'ERROR' + ']' + Print_Colour.ENDC + ' '
        P_ = Print_Colour.GRAY + P + Print_Colour.ENDC
        print(Time+I+P_)
        r.append(Time_+' '+'ERROR '+P)




def Log_Return():
    """获取日志"""
    global r
    return r


def Log_Clear():
    """清空日志"""
    global r
    r = []


if __name__ == '__main__':
    r = []
    Log.ERROR('1111')
    Log.INFO('asdasdas')
    Log.BEBUG('askdnasnnaksldnklas')
