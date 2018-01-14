#!/usr/bin/env python
# coding=utf-8

import os
import re
class Touch(object):
    def touch(file_name,localdir):
        if file_name in os.listdir(localdir):
            print(file_name+" is exist!")
        else:
            targetfile = os.path.join(localdir,file_name)
            fl=open(targetfile,'wb')
            fl.close()

class Remove(object):
    def remove(file_name,localdir,match):
        if file_name in os.listdir(localdir):
            if re.match(r'{0}'.format(match),file_name):
                targetfile = os.path.join(localdir,file_name)
                os.remove(targetfile)
###如果该文件被其他文件引入，需要该文件自身的输出添加if——main，否则引用文件会执行全部内容
if __name__=="__main__":
    for i in  range(1,100):
        file_name=str(i)+'.txt'
        Touch.touch(file_name,'../')
    print(os.listdir('../'))
    for file_name in os.listdir('../'):
        Remove.remove(file_name,'../','\d+\.txt')

