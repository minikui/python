#coding: utf-8

def add(num1, num2):
    print "ADDING %d + %d" % (num1, num2)
    return num1 + num2

def subtract(num1, num2):
    print "SUBTRACTING %d - %d" % (num1, num2)
    return num1 - num2

def multiply(num1, num2):
    print "MULTIPLYING %d * %d" % (num1, num2)
    return num1 * num2

def divide(num1, num2):
    print "DIVIDING %d / %d" % (num1, num2)
    return num1 / num2
print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(200, 5)
weight = multiply(60, 2)
iq = divide(1000, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

# Study Drills
# 自定义函数，return字符串
def my_name():
    return "hello world"

my_str = my_name()
print my_str

# the normal formula
divide_2 = divide(iq, 5)
multiply_2 = multiply(weight, divide_2)
subtract_2 = subtract(height, multiply_2)
result_2 = add(age, subtract_2)

print "That becomes: ", result_2, "Yes, I can do it by hand!"

# another value.
divide_3 = divide(iq * 5, 4)
multiply_3 = multiply(weight, divide_3)
subtract_3 = subtract(height, multiply_3)
result_3 = add(age, subtract_3)

print "That becomes: ", result_3

# simple formula
result = divide(multiply(add(weight, subtract(age, height)), iq), 4)

print "That becomes: ", result, "Can you do it by hand?"
