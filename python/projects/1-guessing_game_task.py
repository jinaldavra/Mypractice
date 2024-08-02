import random

def play_game():
    num = random.randint(1, 100)
    limit = 0
    max_limit = 10

    while limit < max_limit:
        guess = int(input("Guess the number : "))
        limit += 1

        if guess > num:
            print("Too high, guess again!")
        elif guess < num:
            print("Too low, guess again!")
        else:
            print("YOU ARE WIN. YOUR GUESS IS CORRECT.")
            print(f"You guessed the number in {limit} attempts.")
            break

        if limit == max_limit:
            print(f"GAME OVER. The correct number is {num}.")

while True:
    play_game()
    play_again = input("Do you want to play again? : ")
    if play_again == "yes":
        print("Restart")
        guess = int(input("Guess the number : "))
    else:
        print("Thanks for playing.")
        print("EXIT")
        break
