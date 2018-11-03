#!/usr/bin/python
#coding=utf-8

import os
import sys

#交互 输入输出
TEST_INPUT = False
sys.stdout.write('hello world')
if TEST_INPUT:
    print("输入一行数据:")
    readline = sys.stdin.readline().strip('\n')#输入的内容带换行符
    print("输入的内容是:"+readline)
    print("打印输入完成")

    print("输入内容:")
    inputT = input()
    print("输入的是:"+inputT)
    print("打印输入完成")


#改变输出目录为myOut.log
myOutPath = os.path.dirname(os.path.abspath(__file__))+os.sep+'myOut.log'
outFile=open(myOutPath,'w')
sys.stdout=outFile
print("期待输出到文件myOut中")
sys.stdout=sys.__stdout__
print("期待输出到命令行")
outFile.close()

inFile = open(myOutPath,'r')
sys.stdin = inFile
readResult = sys.stdin.readline()
print('readResult is '+readResult)


