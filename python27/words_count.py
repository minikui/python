#coding: utf-8
from collections import Counter

my_file = open("happiness_seg.txt").read().decode("utf-8") # 读入文件
list_orig = my_file.split(" ") # 按空格分割组成列表，初始列表

list_final = [] # 最终列表，统计词频使用到
for i in range(0, len(list_orig) - 1):
    if (len(list_orig[i]) == 2 and len(list_orig[i+1]) == 2): # 判断列表中的元素长度，只对有用的进行操作
        line_str = list_orig[i] + list_orig[i+1] # 找到正确的，可直接拼成字符串，便于最后的统计输出
        list_final.append(line_str)

counter = Counter(list_final).most_common(10) # 使用Counter类对最终列表内的元素进行词频统计，并取出词频top10
print (str(counter).decode("unicode-escape")) # 中文输出，也可以使用下面三行依次输出每一项
#for element in counter:
#    for word_count in element:
#        print word_count
