#coding: utf-8

people = 30
cars = 10
trucks = 25

if cars > people: # 判断条件
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if not((trucks > cars) and (people > trucks)): #
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks: # 判断条件，比较多少
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."




# Study Drills
#  if 分支判断为假进入elif，接着判断elif后面表达式真假，为真，则执行elif代码块；为假，则进入else分支，由于上面判断均为假，直接执行else代码块
#  改变数值，影响if条件判断的分支，可输出不同内容
#  if not((trucks > cars) and (people > trucks)):
