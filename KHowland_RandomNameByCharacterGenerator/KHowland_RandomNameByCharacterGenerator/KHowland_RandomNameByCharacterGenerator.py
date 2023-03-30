
#5/13 :: 12:00 - Creation of program
#5/13 :: 3;15 PM - Completion of First Version
#5/13 :: 3;20 PM - Reinforced NAME_NUM with Try/Except
import random
title = " "
first = " "
mid = " "
last = " "
#.....
add = 65
GEN = random.randint(1,100)
Qua = random.randint(1,2)
Triple = random.randint(1,4)
backlog = 0
apo_chance = random.randint(-10,1000)
dash_chance= random.randint(-10,1000)
#T
def G_T(gen_seed,title):
    if gen_seed == 1:
        title = random.choice(["Sir.","Mr.","Biye.", " "," "])
    elif gen_seed == 2:
        title = random.choice(["Miss.","Ms.","Madam."," ","Miye.","Lady."," "])
    elif gen_seed == 3:
        title = random.choice(["Mx.","Sera."," ","Dika.", "Miba."," "])
    else:
        title = random.choice(["Comrade."," ", "Captain.","Commander."," ","Doctor.", "Prof.","THE","Sergeant.", "Good Friend.", " ", " "])
    return title
#Def?
def if_vowel(start,a,b,c,d,e,q,backlog,apo,dash,count,L):
    seedling = random.randint(97,123)
    G = L-1
    if (apo > 975) and (backlog != 39 and backlog != 45) and (count != 0 and count != G):
        adds = 39
    elif (dash > 975) and (backlog != 39 and backlog != 45) and (count != 0 and count != G):
        adds = 45
    else:
        if start == a or start == b or start == c or start == d or start == e:
            if ( backlog == e or backlog == a or backlog == b or backlog == c or backlog == d ) and Triple == 2:
                if seedling <= 5:
                    adds = random.randint(98,100)
                elif seedling <= 105:
                    adds = random.randint(102,104)
                elif seedling <= 112:
                    adds = random.randint(106,110)
                elif seedling <= 118:
                    adds = random.randint(112,116)
                else:
                    adds = random.randint(118,122)
            else:
                adds = random.randint(97,122)
        elif start == q and Qua == 2:
            adds = 117
        elif GEN > 94:
            adds = random.randint(97,122)
        else:
            adds = random.choice([117,111,105,101,97])
    return adds
    
def builder(start,length,name,adds):
    name = chr(start)
    backlog = 0
    for i in range(length):
        apo_chance = random.randint(1,1000)
        dash_chance= random.randint(1,1000)
        GEN = random.randint(-10,100)
        Triple = random.randint(1,2)
        Qua = random.randint(1,2)
        #Below should determine the second letter based on whether 1st was vowel/consonant
        if i == 0:
            adds = if_vowel(start,65,69,73,79,85,81,backlog,apo_chance,dash_chance,i,length)
        else:
            adds = if_vowel(adds,97,101,105,111,117,113,backlog,apo_chance,dash_chance,i,length)
        backlog = adds
        name = name + chr(adds)
    return name
"""
ACTUAL INPUT CODE!!
"""
att = True
while att:
    try:
        NAME_NUM = int(input("How many names do you want?\n>>> "))
        print("----------------------------")
        for g in range(NAME_NUM):
            Initial = random.randint(65,90)
            Initial_2 = random.randint(65,90)
            Initial_3 = random.randint(65,90)
            gen_seed = random.randint(1,4)
            L1 =random.randint(2,10)
            L2 =random.randint(1,11)
            L3 =random.randint(3,12)
            title = G_T(gen_seed,title)
            first = builder(Initial,L1,first,add)
            mid = builder(Initial_2,L2,mid,add)
            last = builder(Initial_3,L3,last,add)
            #F
            print("\n" +title + " "+first + " " + mid + " " + last)
            print("----------------------------")
        att = False
    except ValueError:
        print("<<\nMust be INTEGER\n>>")
