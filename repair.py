import venv, subprocess, os
from Back.Code import system

if __name__ == "__main__":
    os.chdir(os.path.split(__file__)[0])
    venv.create("venv", with_pip=True)
    if system() == 'Win':
        s = os.path.join('venv', 'Scripts', 'activate')
        spl = "&&"
    else:
        s = 'source ' + os.path.join('venv', 'bin', 'activate')
        spl = ";"
    exitcode = subprocess.Popen(f"cd {spl}{s}{spl}pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple", shell=True).wait()
    if exitcode:
        print('program exit with code:', exitcode)