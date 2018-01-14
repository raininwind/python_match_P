#!/usr/bin/env python
# coding=utf-8

import os
from TouchandRemoveTxt import Touch

file_name = 'jjjj.txt'
targetdir = './aaa'
Touch.touch(file_name,'.')

sourceFile=os.path.join('.',file_name)
if os.path.exists(targetdir):
    targetFile = os.path.join(targetdir,file_name)
else:
    os.makedirs(r"{0}".format(targetdir))
    targetFile = os.path.join(targetdir,file_name)

open(targetFile, "wb").write(open(sourceFile, "rb").read())
