import os
from threading import Timer
import time
# 远程URL
git_url = "https://github.com/Jojozzc/pratice"

# 要把代码放到本地哪个路径
target_dir = r'D:\code\demo\haha2'

# 更新代码的周期，单位为秒
duty_time_second = 5

def fetch_task():
    print(time.time())
    res = os.popen("cd {} && git pull {}".format(target_dir, git_url), mode='r').readlines()
    print(res)


def do_task():
    Timer(duty_time_second, do_task, ()).start()
    fetch_task()


if __name__ == '__main__':
    res = os.popen("git clone {} {}".format(git_url, target_dir), mode='r').readlines()
    do_task()