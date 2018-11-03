#!/usr/bin/python
#coding=utf-8

import os
import sys
#获取目录

print("工作目录:"+os.getcwd()) #获取的是执行该代码的命令所在的目录,即工作目录

print("工程目录:"+sys.path[0]) #获取当前工程所在目录

print("工程目录相对路径:"+__file__)#工程目录相对工作目录[如果目录没有一致的部分，就是绝对路径]

print("工程目录绝对路径:"+os.path.abspath(__file__))

print("获取工作路径上一级路径:"+os.path.dirname(os.getcwd()))#获取某个路径上一级工作目录

#获取传参
print("当前程序的传参是:"+str(sys.argv)) #第一个参数是相对工作路径 后面的是依次传入的 转为字符串,整体是个List

#获取当前操作系统
print("当前的操作系统是:"+sys.platform)

#print("当前以及加载的模块:"+str(sys.modules))#是一个字典





