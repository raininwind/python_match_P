#!/usr/bin/env python
# coding=utf-8

import os
import re

def Touch(file_name,localdir):
    if file_name in os.listdir(localdir):
        print(file_name+" is exist!")
    else:
        targetfile = os.path.join(localdir,file_name)
        fl=open(targetfile,'wb')
        fl.close()

def Remove(file_name,localdir,match):
    if file_name in os.listdir(localdir):
        if re.match(r'{0}'.format(match),file_name):
            targetfile = os.path.join(localdir,file_name)
            os.remove(targetfile)


for i in  range(1,100):
    file_name=str(i)+'.txt'
    Touch(file_name,'../')



print(os.listdir('../'))

for file_name in os.listdir('../'):
    Remove(file_name,'../','\d+\.txt')

