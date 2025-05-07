#Menu
PlayAgain = True
while PlayAgain: 
    Menu = ["1.Guees the Number","2.Rock,paper and scissors"] 
    OverAllScore = 0
    for i in Menu:
        print(i)
    x = int(input("Please pick a number from 1-5 according to your interest!: "))
    if x == 1:
        print("You chose the game, Guess the number!: ")
        import random
        EndNumber = int(input("Please enter the range till where you want the Number to be (The starting Range is 1) :"))
        Num = random.randint(1,EndNumber)
        print(f"You picked the Range from 1 to {EndNumber}")
        UserAnswer = 0
        
        while UserAnswer != Num:
            UserAnswer = int(input("Guess the number Generated!: "))
            if UserAnswer < 0:
                print("The number is Between 1 And Your Given Range!")
            elif UserAnswer > Num:
                print("Your answer is a bit too High!")
                OverAllScore -= 1
            elif UserAnswer < Num:
                print("Your answer is a bit too Low!")
                OverAllScore -= 1
            else:
                print("CONGRATS! You have Guessed the Right ANSWER!🎉")
                OverAllScore += 20


    #Rock Paper Scissors Game
    if x == 2:
        print("You chose Rock, Paper Scissors game!")
        import random
        Items = ["Rock","Paper","Scissors"]
        Computer = random.choice(Items)
        Player = input("Please Enter Rock, Paper or Scissors!: ")
        if Player == Computer:
            print("Both you and Computer Picked the same Item!")
        elif Player == "Rock" and Computer == "Scissors":
            print("You won!")
            OverAllScore += 20
        elif Player == "Paper" and Computer == "Rock":
            print("You won!")
            OverAllScore += 20
        elif Player == "Scissors" and Computer == "Paper":
            print("You Won!:)")
            OverAllScore -= 4
        else:
            print("You lose :(")
        print(f"player : {Player}")
        print(f"Computer : {Computer}")
    if not input("Wanna Play Again? (yes/no)").lower() == "yes":
        PlayAgain = False
print(f"Your Overall Score is {OverAllScore}! Thanks For Playing!")