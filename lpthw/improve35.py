from sys import exit

def insular():
"""
桃花岛
东邪
八卦阵
"""
    print("你来到一座很大的岛，岛上到处都是桃花，美不胜收。")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def palace():
"""
皇宫
南帝
财富考验
"""
    print("你来到一座宫殿里，里面金碧辉煌，看得你眼睛都花了，你一点都不敢触摸。")

def mountain():
"""
白驼山
西毒
人性考验
"""
    print("你来到一座山上，传说这山上出现过白色的骆驼，当地人叫白驼山。")

def temple():
"""
铁枪庙
北丐
耐心考验
"""
    print("你来到一座庙宇里，庙里供着一位武将，武将手里拿着一根长长的铁枪。") 



def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("你来到一处神秘的地方.")
    print("东南西北都可以去.")
    print("你要去那边?")

    choice = input("> ")

    if choice == "east" or choice == "东":
        insular()
    elif choice == "south" or choice == "南":
        palace()
    elif choice == "west" or choice == "西":
        mountain()
    elif choice == "north" or choice == "北":
        temple()
    else:
        dead("这个方向没路走.")


start()
