#coding: UTF-8

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print
print '-' * 20
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print states
print '-' * 20
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#
print '-' * 20
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every states
print '-' * 20
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city
print '-' * 20
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# print both
print '-' * 20
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 20
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# Study Drills

# Dictionary key 不允许出现相同的键。
# 不可以用list做key
# Dictionary 无序的，不可排序
# cmp(dict1, dict2) 比较两个字典元素。
# len(dict) 计算字典元素个数，即键的总数。
# str(dict) 输出字典可打印的字符串表示。
# clear() 删除字典内所有元素
# get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
# has_key(key) 如果键在字典dict里返回true，否则返回false
# keys() 以列表返回一个字典所有的键
# setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# values() 以列表返回字典中的所有值
# fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# ...
