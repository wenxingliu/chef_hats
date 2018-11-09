#author: hir lee
import os
import cv2 as cv
import numpy as np
from os import sep


def judgement_func(x):
    if x == 'q':
        return 1
    elif x == 'w':
        return 2
    else:
        return 0


path = 'D:\\backups\\video_classify10\\1\\'
path1 = os.path.expanduser(path)
s = path.split('\\')[-1]
path2 = os.listdir(path1)
videodict1 = {}
for i, e in enumerate(path2):
    dict1 = {i + 1: e}
    videodict1.update(dict1)
# print(videodict1)
for i in videodict1:
    print('正在读取第' + str(i) + '张图片')
    if i % 3 == 0:
        # dir1 = os.mkdir('./video_classify'+'/'+str(x1))
        src1 = cv.imread(path1 +videodict1[i - 2])
        src2 = cv.imread(path1 +videodict1[i - 1])
        src3 = cv.imread(path1 +videodict1[i])
        src4 = cv.resize(src1, (500, 500))
        src5 = cv.resize(src2, (500, 500))
        src6 = cv.resize(src3, (500, 500))
        src7 = np.array(src4)
        src8 = np.array(src5)
        src9 = np.array(src6)
        src = np.concatenate((src7, src8, src9), axis=1)
        cv.imshow('A', src)

        cv.waitKey(30)
        x = input('请输入你的判断 y/n/dn')
        x1 = judgement_func(x)
        if x1 == 1:
            cv.imwrite('C:\\Users\\Andy\\Desktop\\Black smoke vehicle information extraction\\' + videodict1[i - 2], src1)
            cv.imwrite('C:\\Users\\Andy\\Desktop\Black smoke vehicle information extraction\\'+ videodict1[i - 1], src2)
            cv.imwrite('C:\\Users\\Andy\\Desktop\\Black smoke vehicle information extraction\\' + videodict1[i], src3)
            cv.destroyAllWindows()
        else:
            continue
