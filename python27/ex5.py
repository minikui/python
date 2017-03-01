#coding: utf-8
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 2.54 * height # 转成cm
weight = 180 # lbs
weight_kg = 0.45 * weight # 转成kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight

print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg

print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print round(10.05) # 四舍五入取值

# %r （无论是什么内容都输出）可以输出带有对象属性的一些内容，调试的时候更有用一些，用得多，%s 只是输出针对用户的显示内容
