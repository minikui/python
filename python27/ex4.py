#coding: utf-8
cars = 100 # 车辆数
space_in_a_car = 4.0 # 每辆车的可用空间
drivers = 30 # 司机数量
passengers = 90 # 乘客数量
cars_not_driven = cars - drivers # 没被驾驶的车辆
cars_driven = drivers # 有多少车辆被开 = 司机数量
carpool_capacity = cars_driven * space_in_a_car # 总的可用空间
average_passengers_per_car = passengers / cars_driven # 乘客平均占用

# 输出以上所有变量计算后的值
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"

# Study Drills
# 在数学计算中，将整型转成浮点型，可提高计算的精度，是最终的值更加准确
