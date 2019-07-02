import random
import sys
import time
pos_p1: int=0
pos_p2: int=0
name1=input("enter name of player 1 : ")
name2=input("enter name of player 2 : ")
while 1:
    p1 = random.randint(1, 6)
    pos_p1+=p1
    print("you got ",p1," so ",name1 ,"at ",pos_p1)
    if pos_p1>=100:
        print(name1," win")
        sys.exit()
    if pos_p1==9:
        pos_p1=56
    elif pos_p1==61:
        pos_p1=89
    elif pos_p1==32:
        pos_p1=90
    elif pos_p1==99:
        pos_p1=8
    elif pos_p1==50:
        pos_p1=20
    elif pos_p1==22:
        pos_p1=12
    time.sleep(.5)
    p2 = random.randint(1, 6)
    pos_p2+=p2
    print("you got ",p2," so ",name2," at ",pos_p2)
    if pos_p2>=100:
        print(name2," win")
        sys.exit()
    if pos_p2 == 9:
        pos_p2 = 56
    elif pos_p2 == 61:
        pos_p2 = 89
    elif pos_p2 == 32:
        pos_p2 = 90
    elif pos_p2 == 99:
        pos_p2 = 9
    elif pos_p2 == 50:
        pos_p2 = 20
    elif pos_p2 == 22:
        pos_p2 = 12
    time.sleep(.5)





