import random

number = random.randint(1,100)
easy = 10
hard = 3

def difficulty():
    level = input("Choose a difficulty. Type 'easy' 🙂 or 'hard'😎: ")
    if level == "easy":
        return easy
    else:
        return hard

def game():
    print("Welcome to the Guess Game! 🎮")
    print("Guess a number between 1 and 100. 🤔")
    turns = difficulty()
    guess = int(input("Enter the number to get the result: "))

    rgame = True
    
    while rgame == True:
        print(f"You have {turns} attempts remaining to guess the number.")
        turns -= 1
        
        if turns == 1:
            print(f"Pssst, the correct answer is {number} 😏")
        
        if guess == number:
            print(f"You guessed it right! {number} 😊")
            rgame = False
        elif guess < number:
            print("Try again, your guess is too low! 😐")
            guess = int(input("Enter the number to get the result: "))
        elif guess > number:
            print("Try again, your guess is too high! 😉")
            guess = int(input("Enter the number to get the result: "))
            
        if turns == 0 and guess != number:
            print("You've run out of guesses, you lose. 😥")
            return


game()