#coding: utf-8

the_count = [1, 2, 4, 5, 7]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# first kind of for-loop
for number in the_count:
    print "This is count %d" % number

# second for-loop
for fruit in fruits:
    print "A fruit of type: %r" % fruit

# mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6, 2):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Study Drills
# range()可以接受三个参数，第三个参数可选，默认是1，表示步长是1；range函数的功能：按照第三个参数指定的步长，按等差数列选取前两个参数之间的数据，含有第一个参数，不含第二个参数;
# for-loop将range()指定的数据追加到list
# cmp(list1, list2): 比较两个列表的元素
# len(list): 列表中的个数
#  list.count(obj): 统计某个元素在列表中出现的次数
#  list.extend(seq): 在列表末尾一次性追加另一个序列中的多个值
#  list.index(obj): 从列表中找出某个值第一个匹配项的索引位置
#  list.insert(index, obj): 将对象插入列表
#  list.pop(): 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#  list.remove(obj): 移除列表中某个值的第一个匹配项
#  list.reverse(): 反向列表中元素
#  list.sort(): 对原列表进行排序
