# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import sys
import imagefactory

def GetFileExtension(path):
    return os.path.splitext(path)[1]

if __name__=='__main__':
    args = sys.argv
    print(args)
    width=640
    height=960

    while args:
        arg = args.pop(0)
        if arg.lower() == 'size':
            size = args.pop(0).split('x')
            width,height=int(size[0]),int(size[1])

    currentPath = os.getcwd()
    targetDir = os.path.join(currentPath,'small_images')
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)


    for filename in os.listdir(currentPath):
        if GetFileExtension(filename) in ('.jpg','.jpeg','.png','.gif','.bmp'):
            print(u'正在处理图片：%s,处理后尺寸：%sx%s'%(filename,width,height))
            imagefactory.create_small_pic_from_file(filename,width,height,90,os.path.join(targetDir,filename))
