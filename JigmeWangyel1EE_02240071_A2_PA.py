
PlayAgain = True
while PlayAgain: 
    Menu = ["1.Guees the Number","2.Rock, paper and scissors","3.Trivia Quiz Game","4.Pokemon Binder Card Binder Manager","0.Exit Game"] 
    OverAllScore = 0
    for i in Menu:
        print(i)
    x = int(input("Please pick a number from 1-5 according to your interest!: "))
#Guess Game
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
                OverAllScore -= 2
            elif UserAnswer < Num:
                print("Your answer is a bit too Low!")
                OverAllScore -= 2
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
            OverAllScore += 20
        else:
            print("You lose :(")
            OverAllScore -= 5
        print(f"player : {Player}")
        print(f"Computer : {Computer}")
        
#Quiz Game
    if x== 3:
        print("You picked Trivia Quiz Game! ")
        Questions = ("When is the National Day of Bhutan?: ",
                     "What is Bhutan's National sport?: ",
                     "How many Alphabets are there?: ",
                     "Who came up with the Theory of Relativity?: ",
                     " What is the smallest country in the world by land area? :")
        Options = (("A. December 16 ","B. Decemeber 17 ","C. December 18 ","D. December 19"),
                   ("A. Football","B. Khuru ","C. Archary","D. Dego"),
                   ("A. 27 ","B. 25 ","C. 26 ","D. 28 "),
                   ("A. Sir Issac Newton ","B. Oppenheimer ","C. Bills gate ","D. Albert Einstein "),
                   ("A. Bhutan ","B. Sri Lanka ","C. Singapore ","D. Vatican City "))
        Answers = ("B","C","C","D","D")
        Question_Number = 0
        for question in Questions:
            print("---------------------------------")
            print(question)
            for option in Options[Question_Number]:
                print(option)
            Guess = input("Please enter the option (A,B,C, or D) as your answer: ").upper()
            if Guess == Answers[Question_Number]:
                print("Your Answer is Correct!")
                OverAllScore += 20
            else:
                print("Your Answer is Incorrect!")
                print(f"{Answers[Question_Number]} is the Correct Answer!")
                OverAllScore -= 5   

            Question_Number += 1
        
    if x == 4:
        from JigmeWangyel1EE_02240071_A2_PB import PokemonBinder
        binder = PokemonBinder()
    
            
    if x == 0:
        print("Exiting the Game")






































    if not input("Wanna Play Again? (yes/no)").lower() == "yes":
        PlayAgain = False
print(f"Your Overall Score is {OverAllScore}! Thanks For Playing!")
