#coding: utf-8
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # 没有冒号
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop写错
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # 丢失括号
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 # 计算不对
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # \ 应该是 /
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # == 应该是 =，变量写错

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) # 丢失括号，变量写错


sentence = "All god\tthings come to those who weight."

words = break_words(sentence) # 不需ex25.
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) # 多 .
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words # print

print_first_and_last(sentence) # 函数写错

print_first_and_last_sorted(sentence) # 不用缩进，函数、参数写错