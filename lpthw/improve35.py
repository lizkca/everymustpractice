from sys import exit
import random

def eight_formation():
    print("你一踏进小道，就觉得仿佛走进了另外一个世界一样。")
    print("前后左右全看不清，但是你又知道有八个方向可以让你选择走。(e , s ,w ,n ,es, en, ws, wn)")
    print("请问你怎么走？")
    
    choice = input("> ")
    change = random.choice(["clockwise", "anticlockwise"])
    if change == "clockwise":
        if choice == "n":
            print("突然之间，那个老人出现在你面前。哈哈大笑，说道，好，你能通过我这阴阳八卦阵，我就收你为徒，传你一身本领。")
            print("恭喜，你成为东邪黄药师的徒弟。")
        else:
            dead("你进入了一个永远也走不出的地方。")
    elif change == "anticlockwise":
        if choice == "s":
            print("突然之间，那个老人出现在你面前。哈哈大笑，说道，好，你能通过我这阴阳八卦阵，我就收你为徒，传你一身本领。")
            print("恭喜，你成为东邪黄药师的徒弟。")
        else:
            dead("你进入了一个永远也走不出的地方。")
    else:
        dead("你死于不明原因。")
        
def insular():
    """
    桃花岛
    东邪
    八卦阵
    """
    print("你来到一座很大的岛，岛上到处都是桃花，美不胜收。")
    print("不远处看到一个青衫老人，腰里插着一支玉箫，神情傲然。")
    print("你前面是一条幽深小道，一眼看不到头，不知通往何处。")
    print("你准备怎么做？")

    choice = input("> ")
    if choice == "talk" or choice == "搭讪老人":
        dead("老人回头看了你一眼，不知那里飞来一颗小石子，你就不省人事了。")
    elif choice == "walk" or choice == "走进小道": 
        eight_formation()
    else:
        dead("一阵箫声传来，你就不省人事了。")

def palace():
    """
    皇宫
    南帝
    财富考验
    """
    print("你来到一座宫殿里，里面金碧辉煌，看得你眼睛都花了，你一点都不敢触摸。")
    print("你沿着路直走，来到一间看到一位老僧，慈眉善眼的。")
    print("旁边是一间密室，门是开着的，一推就开。")
    print("你准备怎么做？")


    choice = input("> ")
    if choice == "talk" or choice == "问话":
        print("阿弥陀佛。老僧对你念了一句。")
    elif choice == "open" or choice == "push" or choice == "开门":
        print("一进密室，你发现这里都是一块块的黄金。金光灿灿的。你准备拿多少块？") 
        gold = input("> ")
        if gold.isdigit():
            how_much = int(gold)
            if how_much > 100:
                dead("你得到一堆黄金了。")
            elif how_much < 5:
                dead("你得到了你拿的黄金。")
            elif how_much == 6:
                print("你拿了六块黄金。突然老僧出现在你面前，慈祥的对你说，老衲愿意收你为徒，你可乐意？")
                print("恭喜，你成为南帝的门下。")
            else:
                luck = random.choice([1,2,3,4,5,6])
                if luck == 6:
                    print("突然老僧出现在你面前，说，你运气太好了。你成为南帝的门下。")
                else:
                    dead("门突然关上了，你不知道怎样才能出来。")
        else:
            dead("大哥，学一下输入数字吧。")
        

def mountain():
    """
    白驼山
    西毒
    人性考验
    """
    luck = random.choice([1,2,3,4,5,6,7,8,9,10])
    print("你来到一座山上，传说这山上出现过白色的骆驼，当地人叫白驼山。")
    print("你突然看到一条颜色鲜艳的蛇，显然是一条很毒的🐍，在咬一位老者的胳膊。")
    print("你准备怎么做？")
    
    choice = input("> ")
    if choice == "打蛇":
        print("老者勃然大怒，敢打我的蛇，去死吧。")
        dead("你被西毒打死了。")
    elif choice == "打老者":
        print("老者哈哈大笑，你心肠够毒，正合我胃口，我就收你为徒吧。")
        print("恭喜，你成为西毒门下。")
    else:
        if luck < 5:
            dead("突然，不知什么时候，你觉得自己中毒了。")
        elif luck >= 5 and luck < 8:
            print("忽然之间，从老者的衣袖飞出两条蛇来，盘在你的两只手。")
            print("你吓得一动不敢动。")
            print("老者对你笑了笑，说，你我有缘，这两条蛇送你了。我再给你个宝贝，它们就会认你当主人了。")
            dead("你获得一个控蛇珠，和两条剧毒的金冠角蛇。")
        elif luck >= 8:
            print("老者对着你看了又看。说，是你了，我终于等到你了。我将把我的全部功夫传授给你，你将成为白驼山的少主人。继承我的一切。")

def temple():
    """
    铁枪庙
    北丐
    耐心考验
    """
    print("你来到一座庙宇里，庙里供着一位武将，武将手里拿着一根长长的铁枪。") 
    print("你看到一位中年的乞丐，在睡觉。")
    print("你准备怎么做？")
    
    choice = input("> ")
    wait_times = random.choice([10,20,30])
    for i in range(wait_times):
        if choice == "wait" or choice == "等":
            print("你等了又等。乞丐还是呼呼大睡。")
            choice = input("> ")
        else:
            dead("不知怎么了，一股神奇的力量，托着你，你像腾云驾雾一样飞出了庙宇。你再也没有勇气进去了。")
    print("乞丐终于睡醒了。伸伸懒腰。说，走我带你去吃好吃的。顺便教你两手。")
    print("恭喜，你成为北丐门下。")

        

def dead(why):
    print(why, "挺不错的!")
    exit(0)


def start():
    print("你来到一处神秘的地方。")
    print("东南西北都可以去。")
    print("你要去那边?")

    choice = input("> ")

    if choice == "east" or choice == "e" or choice == "东":
        insular()
    elif choice == "south" or choice == "s" or choice == "南":
        palace()
    elif choice == "west" or choice == "w" or choice == "西":
        mountain()
    elif choice == "north" or choice == "n" or choice == "北":
        temple()
    else:
        dead("这个方向没路走。")

start()
