import random
import math
# DEFF
def spaces():
    print('\n..............................................................')
BOT = random.choice(["Maisy","Magnus","Lucile","Vinnie","Kelvin","Zero","Crow","Cygnus"])
B_feel = random.choice(["happy","sad","calm","exciting","boring"])
joker = random.choice(["<< What is the best time to visit the dentist?\n\t>>> Tooth Hurty!", "<< Why is a bad joke like a broken pencil?\n\tIt has no point!"])
gamer = random.randint(0,5)
filler = " "
# INTRO
spaces()
print("Hello. My name is " + BOT +". Who are you?")
YOU = input(">> ")
print("....\n Hello, " + YOU + ". What a lovely name.") 
spaces()
#PRONOUNS
print("Just so I know, what are your pronouns?")
pro1 = input("He/She/They/etc?: ")
pro2 = input("His/Her/Their/etc?: ")
pro3 = pro2
if pro3 == "his" or pro3 == "His":
    pro3 = "him"
elif pro3 == "their" or pro3 == "Their":
    pro3 = "them"
spaces()
print("Has today been a good day for you?")
Y_feel = input(">> ")
print("......")
# FEELS
if Y_feel == "no" or Y_feel == "No":
    if B_feel == "sad" or B_feel == "boring":
        print("We've both had a rough day, it seems...")
    else:
        print("I'm sorry to hear that.Perhaps you'd like a joke...")
        filler = input(" ")
        print(joker)
elif Y_feel == "yes" or Y_feel == "Yes":
    print("Glad to hear that!")
elif Y_feel == "yeah" or Y_feel == "Yeah":
    print("Good to hear that!")
else:
    print("It's been like that for me today as well...")
spaces()
# GAMES
print("Do you want to play a game, " + YOU + " ?")
Gametime = input(">> ")
print("......")
if Gametime == "yes" or Gametime == "Yes" or Gametime == "Yeah" or Gametime == "yeah" or Gametime == "sure":
#NUM GAME
    if gamer > 6:
        print("Guess a number 1-10.")
        secret = random.randint(1,10)
        GUESS = int(input(">> "))
        while GUESS != secret:
            GUESS = int(input("Nope!\tTry Again: "))
        print("You've won this round...")
        print(".....\nGuess a number 1-100.")
        secret = random.randint(1,100)
        GUESS = int(input(">> "))
        count = 0
        while GUESS != secret:
            GUESS = int(input("Nope!\tTry Again: "))
            count = count + 1
            if count > 5:
                break
        if GUESS == secret:
            print("You Won again!\tCongrats, " + YOU + "!")
        else:
            print("Better luck next time! It was " + str(secret)+".")
# MAD LIBS
    elif gamer < 6:
        print("Lets do a mad lib!\tType 1 or 2....")
        GUESS = int(input(">> "))
        ving = input("Verb with -ing: ")
        place = input("Location/Place: ")
        adj = input("Adjective: ")
        n = input("Noun: ")
        v = input("Verb: ")
        pn = input("Plural Noun: ")
        quote = input("Phrase/Quote: ")
        adv = input("Adverb: ")
        adv2 = input("Adverb: ")
        print(" ")
        if GUESS == 1:
            print(BOT + " and " + YOU + " were " + ving + " in the " + place + " one day, when they saw a " + adj + " " + n +".")
            print("Suddenly, the " + n + " began to " + v + " and flew towards " + YOU +", nearly hitting " + pro3 +". " + BOT + ",") 
            print('meanwhile, shouted "' + quote + '!" and searched for ' + pn + ' that could help the situation. Then, ' + adv + ',')
            print("the " + n + " " + adv2 + " flew away, and " + BOT + " and " + YOU + " never saw it in the " + place + " again.")
        elif GUESS == 2:
            print(BOT + " went to " + YOU + "'s house one day, right next to the " + place + ". The house was " + adj + ", and outside it")
            print("was a " + n + " placed on top of a glass table. " + YOU + " opened the door and welcomed " + pro2 + " best friend.")
            print("It was then that " + BOT + " noticed something odd. Both of them were " + ving + " the same shirt! '" + quote + "!', said " + BOT +".")
            print("The two of them " + adv + " began to " + v + ". They " + adv2 + " sat down at the table and talked about " + pn + " for the next hour!")
        else:
            print(BOT + " and " + YOU +" " + adv2 + " walked around the park, lost and dreaming of " + pn + ".  They had spent hours " + ving)
            print("to find the " + place + " but found that they only had " + adj + " luck. '"+ quote +"!', exclaimed " + YOU + ". 'We'll never find it!'")
            print("Then, as if to answer " + pro2 + " call, a flying " + n + " " + adv + " came to them, with a map of the town! " + BOT + " thanked the")
            print("miraculous " + n + " and they and " + YOU + " began to " + v + "to the " + place + " happlily.")
# SPECIAL GAME
    else:
        print("You want to play a game of Luck?")
        print("______________")
        print("**You will begin with 500 points.**Each Challenge will double your score or take points away**\nGet to 2500 points!")
        filling = input("Ready?\t>>")
        game_on = True
        points = 500
        print("~~~~~~~~~~~~~~~~\n")
        count = 1
        while game_on:
            play = random.randint(1,3)
            if play == 3:
                p3 = random.randint(1,2)
                print(" Game " + str(count) + ": Coin Toss")
                guess = input("Heads or Tails?\n>> ")
                if (guess == "heads" or guess == "Heads") and p3 == 1:
                    print("Correct!")
                    points = points * 2
                elif (guess == "tails" or guess == "Tails") and p3 == 2:
                    print("Correct!")
                    points = points * 2
                else:
                    print("Incorrect.")
                    points = points//2
            elif play == 2:
                print(" Game " + str(count) + ": Number Competition\n **See if your random number is higher than the other two!")
                seed = random.randint(-50,50)
                seed2 = random.randint(0,75)
                number = random.randint(0,120)
                print("Your number: " + str(number))
                filling = input("Enter to continue\n______________")
                if number > seed and number > seed2:
                    print("Congrats! You've won!")
                    points = points*2
                else:
                    print("Oh well. Better luck next time!")
                    points = points-(0.25*points)
            else:
                print("Game " + str(count) + ": Dice\n Both of us will roll a die, and the higher score wins!")
                filling = input("Ready, " + YOU + "?")
                sides = int(input("How many sides on the die?\n>> "))
                B_roll = random.randint(1,sides)
                Y_roll = random.randint(1,sides)
                print(".......")
                if Y_roll > B_roll:
                    print("You won with " + str(Y_roll) + ", I had " + str(B_roll))
                    points = points*2
                elif Y_roll == B_roll:
                    print("We tied with " + str(Y_roll))
                    points = points + 500
                else:
                    print("I won with " + str(B_roll) + ", you had " + str(Y_roll))
                    points = points-500
            print("____________________________")
            print("Current points: " + str(points))
            if points >= 2500:
                game_on = False
            else:
                print("You only need " + str(2500 - points) + " more points!")
            print("____________________________")
            count = count + 1
        print("You've Won, " + YOU + "! Congrats!")
else:
    print("Okay.")
spaces()
#end
print("Well, " + YOU + ", this has been a fun few minutes, hasn't it?")
filling = input(">>  ")
if filling == "yes" or filling == "Yes" or filling == "Yeah" or filling == "yeah" or filling == "sure":
    print("Glad to hear!")
elif filling == "no" or filling == "No":
    print("Well, you certainly still made my day!")
else:
    print("I think it has, at least....")
print("This is, however, the end of this conversation for now...\n\nBut I hope someday we can pick back up this conversation once more.....")
leave = input(" ")
print("I have to go, but know that I, " + BOT + ", \nwill always be your friend, " +YOU + "....\n...\nGood-Bye!")