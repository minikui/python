#coding: utf-8

def print_two (*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two("ok", "google")
print_two_again("ok", "Google")
print_one("Google")
print_none()
# Study Drills
# 定义和调用函数，函数可以有多种形式的形参列表
