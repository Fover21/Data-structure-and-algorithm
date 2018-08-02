import os

filePath = "/Users/busensei/wzy/filePath/"


def read(filePath, n):
    it = os.listdir(filePath)  # 打开文件夹
    for el in it:
        #  拿到路径
        fp = os.path.join(filePath, el)  # 获取到绝对路径
        if os.path.isdir(fp):  # 判断是否是文件夹
            print("\t" * n, el)
            read(fp, n + 1)  # 又是文件夹. 继续读取内部的内容 递归入口
        else:
            print("\t" * n, el)  # 递归出口


read(filePath, 0)