#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:52:03 2018

@author: xc

1、
import os
root = "C:\\dir"

for dirpath, dirnames, filenames in os.walk(root):
    for filepath in filenames:
        print os.path.join(dirpath, filepath)

2、
import os

def listDir(path):
    for filename in os.listdir(path):
        pathname = os.path.join(path, filename)
        if (os.path.isfile(filename)):
            print pathname
        else:
            listDir(pathname)

"""
import os
import shutil
path = r"E:\project\Python\labelclassify\done\251_y"
target = r"E:\project\Python\labelclassify\done\251\y"

def list_allfilespath(path):
    filespath = []
    list = os.listdir(path)   #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           pathtemp = os.path.join(path,list[i])
           if os.path.isdir(pathtemp):
              filespath.extend(list_allfilespath(pathtemp))
           if os.path.isfile(pathtemp):
              filespath.append(pathtemp)
    return filespath

allfiles_path = list_allfilespath(path)

#将所有文件重新放入指定文件夹下
###缺点同名文件会被覆盖###
#shutil.copy()
for x in allfiles_path:
    shutil.move(x,target)
print('done!')