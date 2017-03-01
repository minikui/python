#coding: UTF-8

def terms_append(terms_v, step = 1):
    n = 0
    terms = []

    if step <= 0:
        step = 1

    for i in range(n, terms_v, step):
        print "for开始 i = %d" % i
        terms.append(i)
        print "terms里面的值: ", terms
        print "for结束 i = %d" % i

    print "for结束以后，terms的值: "

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
