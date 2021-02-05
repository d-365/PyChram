import threading
import subprocess
import psutil
import time


def adb_logcat():
    path = r"C:\Users\Administrator\Desktop\log.txt"
    command1 = 'adb logcat -v time > %s' % path
    p1 = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
    print(p1.pid)
    time.sleep(1)
    p = subprocess.Popen("adb logcat -c")
    print(p.pid)
    # pid = psutil.Process(p.pid)
    # # for c in pid.children(recursive=True):
    # #     c.kill
    # # time.sleep(1)
    subprocess.Popen('adb kill-server')


if __name__ == "__main__":
    # t = threading.Thread(target=adb_logcat())
    # t.start()
    # t.join()
    adb_logcat()
