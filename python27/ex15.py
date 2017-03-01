#coding: utf-8

from sys import argv
script, filename = argv
# filename = raw_input('enter the file name: ')
txt = open(filename) # 根据文件名，打开提供的文件

print "Here's your file %r:" % filename
print txt.read() # 打印出文件内容

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()

# Study Drills
# 使用 raw_input() 可以先是提示符提醒用户，更友善。
