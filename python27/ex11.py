#coding: utf-8
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills
# raw_input() 输入语句，读取输入到终端显示器的内容，可以接受任何类型的输入，默认返回字符串类型
# raw_input('> ') 和上面一样，只是带有提示符，提醒用户输入。
# int(raw_input()) 直接将用户输入的内容（数字）转成数字类型
# 输出显示 '7\'25"'，使用 ''显示输出 ，字符串带有 ' ，需要用转义字符 \
