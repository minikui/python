#coding: utf-8

# 修改自ex35.py，主要就是增加选择分支
from sys import exit

def gold_room():
    print "原来金刚芭比是海盗，这是她私藏的宝藏啊，你也想要吗？告诉他你想要多少"

    choice = raw_input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("输入数量！")

    if how_much < 50000000:
        print "太少了"
        exit(0)
    elif how_much > 100000000:
        dead("太多了")
    else:
        print "有了钱，赶紧和她结婚吧"
        dead("突然梦醒了")


def boss_room():
    print "公司来了三个女同事，分别是：美，丑，富"
    print "你喜欢什么样的？"
    say_yes = False

    while True:
        choice = raw_input("> ")

        if choice == "美":
            dead("我还能说什么，你没睡醒！")
        elif choice == "丑" and not say_yes:
            print "她没听见，再叫一遍试试"
            say_yes = True
        elif choice == "丑" and say_yes:
            print "金刚芭比撞开一扇门，拉着你跑了，，，"
            gold_room()
        elif choice == "富":
            dead("这么有钱，谁还来上班，")
        else:
            print "只有三个！"

def ghost_room():
    print "还睡，想不想醒？"

    choice = raw_input("> ")

    if "想" in choice:
        print "做梦不是你想醒，想醒就能醒"
        start()
    elif "不想" in choice:
        dead("啊，你睡死了。。。")
    else:
        ghost_room()

def dead(why):
    print why, "死心了吗！"
    exit(0)

def start():
    print "游戏开始，你有两个选择！上班，还是继续睡觉？"

    choice = raw_input("> ")

    if "上班" in choice:
        boss_room()
    elif "睡觉" in choice:
        ghost_room()
    else:
        dead("你的人生没有第三种选择，")

start()
