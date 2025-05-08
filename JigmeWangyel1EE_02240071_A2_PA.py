import random

class GuessTheNumber:
    def __init__(self):
        self.score = 0

    def play(self):
        print("You chose the game, Guess the number!")
        end_number = int(input("Please enter the range till where you want the Number to be (The starting Range is 1): "))
        num = random.randint(1, end_number)
        print(f"You picked the Range from 1 to {end_number}")
        user_answer = 0

        while user_answer != num:
            user_answer = int(input("Guess the number generated: "))
            if user_answer < 0:
                print("The number is Between 1 And Your Given Range!")
            elif user_answer > num:
                print("Your answer is a bit too High!")
                self.score -= 2
            elif user_answer < num:
                print("Your answer is a bit too Low!")
                self.score -= 2
            else:
                print("CONGRATS! You have Guessed the Right ANSWER! 🎉")
                self.score += 20

        return self.score


class RockPaperScissors:
    def __init__(self):
        self.score = 0

    def play(self):
        print("You chose Rock, Paper Scissors game!")
        items = ["Rock", "Paper", "Scissors"]
        computer = random.choice(items)
        player = input("Please Enter Rock, Paper or Scissors!: ")

        if player == computer:
            print("Both you and Computer picked the same item!")
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            print("You won!")
            self.score += 20
        else:
            print("You lose :(")
            self.score -= 5

        print(f"Player: {player}")
        print(f"Computer: {computer}")
        return self.score


class TriviaQuiz:
    def __init__(self):
        self.score = 0

    def play(self):
        print("You picked Trivia Quiz Game!")
        questions = (
            "When is the National Day of Bhutan?: ",
            "What is Bhutan's National sport?: ",
            "How many Alphabets are there?: ",
            "Who came up with the Theory of Relativity?: ",
            "What is the smallest country in the world by land area?: "
        )
        options = (
            ("A. December 16", "B. Decemeber 17", "C. December 18", "D. December 19"),
            ("A. Football", "B. Khuru", "C. Archary", "D. Dego"),
            ("A. 27", "B. 25", "C. 26", "D. 28"),
            ("A. Sir Issac Newton", "B. Oppenheimer", "C. Bills gate", "D. Albert Einstein"),
            ("A. Bhutan", "B. Sri Lanka", "C. Singapore", "D. Vatican City")
        )
        answers = ("B", "C", "C", "D", "D")

        for i, question in enumerate(questions):
            print("---------------------------------")
            print(question)
            for option in options[i]:
                print(option)
            guess = input("Please enter the option (A, B, C, or D) as your answer: ").upper()
            if guess == answers[i]:
                print("Your Answer is Correct!")
                self.score += 20
            else:
                print("Your Answer is Incorrect!")
                print(f"{answers[i]} is the Correct Answer!")
                self.score -= 5

        return self.score


class GameManager:
    def __init__(self):
        self.overall_score = 0

    def display_menu(self):
        print("\nMenu:")
        print("1. Guess the Number")
        print("2. Rock, Paper and Scissors")
        print("3. Trivia Quiz Game")
        print("0. Exit Game")

    def run(self):
        play_again = True
        while play_again:
            self.display_menu()
            choice = input("Please pick a number from 1-3 according to your interest (or 0 to exit): ")

            if choice == "1":
                game = GuessTheNumber()
                self.overall_score += game.play()

            elif choice == "2":
                game = RockPaperScissors()
                self.overall_score += game.play()

            elif choice == "3":
                game = TriviaQuiz()
                self.overall_score += game.play()

            elif choice == "0":
                print("Exiting the game.")
                break

            else:
                print("Invalid choice. Please try again.")

            if input("Wanna Play Again? (yes/no): ").lower() != "yes":
                play_again = False

        print(f"Your Overall Score is {self.overall_score}! Thanks for playing!")


# Run the game
if __name__ == "__main__":
    manager = GameManager()
    manager.run()
