import random
filling = " "
BEHOLD = 0
#................
Y_Score = 0
B_Score = 0
Turn = 0
#..................
#................
print("P I G")
filling = input("Enter to Start\n>>")
print(".................")
while Y_Score < 100 and B_Score < 100:
    roll = 0
    turn = 0
    Turn = Turn + 1
    print(".................\n YOU: " + str(Y_Score) + " || COMPUTER: " + str(B_Score) + " \n.................")
    if Turn%2 == 0:
        filling = input("\nCOMPUTER is rolling\n>>>")
        while roll != 1:
            roll = random.randint(1,6)
            print(str(roll) + "!")
            if roll == 1:
                turn = 0
                print("T U R N   O V E R\n")
                continue
            else:
                turn = turn + roll
                BEHOLD = random.randint(1,3)
                if BEHOLD == 1:
                    filling = input("COMPUTER IS HOLDING\n>>>")
                    B_Score = B_Score + turn
                    roll = 1
                else:
                    filling = input("Keeping...\nTotal so far: " + str(turn) + "\n>>>")
    else:
        filling = input("\n_________\nYOU are rolling\n>>>")
        while roll != 1:
            roll = random.randint(1,6)
            print(str(roll) + "!")
            if roll == 1:
                turn = 0
                print("T U R N   O V E R\n")
                continue
            else:
                turn = turn + roll
                BEHOLD = input("To HOLD, enter 1. Enter anything else to KEEP.\n>>> ")
                if BEHOLD == "1":
                    filling = input("YOU ARE HOLDING\n>>>")
                    Y_Score = Y_Score + turn
                    roll = 1
                else:
                    filling = input("Keeping...\nTotal so far: " + str(turn) + "\n>>>")
print("\n\n...................\nYOU have won with " + str(Y_Score) + " Points!\n.....................")
