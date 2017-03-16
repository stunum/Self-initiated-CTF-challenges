#coding=utf-8
#!/usr/bin/python
#crack.py

import os
import subprocess
import time

def password_crack(password):
    command='decode -X -P %s sound.mp3 '% password
    # print command
    p = subprocess.Popen(command, stdin = subprocess.PIPE,
    stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    if "unexpected end of cipher message."not in p.communicate()[1]:
        print '[>] Password is find:%s' %password
        print command
        flag = open('sound.mp3.txt')
        print flag.read()
        return True

def generate_birthday():
    start = time.clock()
    # password_find = False
    year = '1995'
    for month in xrange(11,13):
        month = str(month)
        for day in xrange(1,32):
            day = str(day).zfill(2)
            birthday = year + month + day
            password_find = password_crack(birthday)
            if password_find is True:
                end = time.clock()
                print '[>] Used time %f' %(end - start)
                exit()
                
    print '[>] Used time %f' %(end - start)

def main():
    generate_birthday()

if __name__ == '__main__':
    main()
