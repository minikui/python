#coding: utf-8

people = 25
cats = 30
dogs = 20

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 10
if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# Study Drills
# if 条件判断语句，根据if 后面的表达式的真假，选择执行if分支或者if以外的语句分支
# 缩进表示这行语句是 if 语句的分支，告诉python这是if的代码块，选择执行
# 不缩进，if语句后面有冒号 : 所以首先收到python错误提示
# if True or False:
# 可以改变后面 if 条件判断的分支选择
