#Menu
Menu = ["1.Guees the Number","2.Rock,paper and scissors"] 
for i in Menu:
    print(i)
x = int(input("Please pick a number from 1-5 according to your interest!"))
if x == 1:
    print("You chose the game, Guess the number!: ")
    import random
    Num = random.randint(1,int(input("Please enter the range till where you want the Number to be (The starting Range is 1) :")))
    UserAnswer = 0
    while UserAnswer != Num:
        UserAnswer = int(input("Guess the number Generated!: "))
        if UserAnswer < 0:
            print("The number is Between 1 And Your Given Range!")
        elif UserAnswer > Num:
            print("Your answer is a bit too High!")
        elif UserAnswer < Num:
            print("Your answer is a bit too Low!")
        else:
            print("CONGRATS! You have Guessed the Right ANSWER!🎉")


     
    