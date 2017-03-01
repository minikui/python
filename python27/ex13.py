#coding: utf-8

from sys import argv
script, first, second, third, anthoer = argv

print "The script is called:", script
print "The first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study Drills
# valueError: need more than 1 value to unpack
from sys import argv
script, first, second = argv

print "你好，我是：%r，你是谁？" % script
print "你的名字是：", first
print "你姓：", second

print "还差一个middle name"
third = raw_input('> ')
print "middle name：", third
