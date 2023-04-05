import random
randy = int(input("Number of Places (may not be exact/perfect) : "))
sticks = int(input("# of numbers needed: "))
seed_1 = 0
ans = 0
fin = 0
for i in range(sticks):
    seed_1 =random.randint(100000,1000000)
    if randy == 1:
        ans = seed_1//100000
    elif randy == 2:
        ans = seed_1//10000
    elif randy == 3:
        ans = seed_1//1000
    elif randy == 4:
        ans = seed_1//100
    elif randy == 5:
        ans = seed_1//10
    else:
        ans = seed_1
    if sticks > 10 and (i == 10 or i%10 ==0) and i%100 != 0:
        print("____________________________________")
        print("---------- "+str(i)+" -------------")
        print("____________________________________")
    elif sticks > 100 and (i == 100 or i%100 ==0):
        print("____________________")
        print(" ")
        print("! "+str(i)+" !")
        print("____________________")
    print(ans)
    

'''
obj = random.choice(["ancient trees ","walls around you ","clocks ","raindrops ","shadows on the walls "])
verb = random.choice(["slowly sway,","wait patiently and listen,","continue thier rythyms,", "bring you silence,","watch nervously and patiently,"])
purpose = random.choice([" to maintain balance."," in hope of change."," to preserve the past.",""," and nothing more." ])
print("The " + obj + verb + purpose)
'''
