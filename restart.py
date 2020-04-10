#! /usr/bin/python3
import os,subprocess
if __name__ == '__main__':
    #s = os.system('ps -aux | grep uwsgi')
    s=subprocess.Popen("ps -aux | grep uwsgi",bufsize=0,shell=True,stdout=subprocess.PIPE,universal_newlines=True)
    while True:
        nextline=s.stdout.readline()
        if nextline=="" and s.poll()!=None:
            break
        print('-'*50)
        line = nextline.strip().split()
        os.system("kill -9 "+line[1])