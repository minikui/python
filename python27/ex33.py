#coding: UTF-8

i = 0
numbers = []

while i < 7:
    print "At the top i is %d" % i
    numbers.append(i)

    i+=1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "
for num in numbers:
    print num,



# Study Drills
# 定义函数 terms_append，接收一个参数作list的长度，step表示步长，默认等于1，调用的时候不手动设置，则步进1，
def terms_append(terms_v, step = 1):
    n = 0
    terms = []

    while n < terms_v:
        print "while开始 n = %d" % n
        terms.append(n)

        if step <= 0:
            step = 1
        n+=step
        print "terms里面的值: ", terms
        print "while结束 n = %d" % n

    print "while结束以后，terms的值: "

    for term in terms:
        print term,

print "\n\t创建一个从0开始的list？(Y/N)"
yorn = raw_input("> ")

if yorn == "Y" or yorn == "y":
    print "list长度？："
    list_len = int(raw_input("> "))
    print "list内数据的差值，默认是1，输入非正数不设置："
    step_len = int(raw_input("> "))
    terms_append(list_len, step_len)

elif yorn == "N" or yorn == "n":
    print "不创建list"

else :
    print "输入错误，再试一次"
