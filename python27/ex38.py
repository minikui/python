#coding: UTF-8

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d things now." % len(stuff)

print "There we go: ", stuff

print "Let's do something with stuff."

print stuff[1]
print stuff[-2]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:6])

# Study Drills
# 函数调用的本质
# more_stuff.pop() 在 more_stuff 上做pop操作，将more_stuff对象传给pop，pop拿到more_stuff，对其进行一次pop出栈操作。
# object-oriented programming 面向对象编程
# class 面向对象的重要部分，所有现实事物，均可抽象成类：class
# 购物车 通讯录 等
