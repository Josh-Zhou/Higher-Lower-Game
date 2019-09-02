import random


# plays the game
def play_game(game_mode):
    max_attempts = 8
    value = random.randint(1, 100)

    if game_mode == "hard":
        hard_mode = True
    else:
        hard_mode = False

    guess_amount = 1
    guess = int(input("Guess a number: "))

    while guess != value:
        if hard_mode == True and guess_amount == max_attempts:
            print("Sorry you have run out of attempts! The correct number was",
                  value)
            return play_again()

        guess_amount += 1

        if guess < value:
            print("Incorrect! Your guess was lower.")
        else:
            print("Incorrect! Your guess was higher.")

        if hard_mode:
            print("You have", max_attempts - guess_amount + 1, "of attempt(s) "
                                                               "remaining\n")

        guess = int(input("Guess a number: "))

    print("Congratulations, you guessed the right number!")
    if guess_amount == 1:
        print("It took you 1 try! Exceptional!\n")
    else:
        print("It took you", guess_amount, "tries!\n")

    return play_again()


#Asks if user would like to play again.
def play_again():
    while True:
        value = str(input("Would you like to play again? (yes/no): "))
        if value == "no" or value == "yes":
            break
        else:
            print("Please input a proper answer (yes/no)")

    return value


#Driver
def main():
    print("Welcome to the higher-lower guessing game!\n"
          "The computer will pick a number between 1 and 100 (inclusive) and "
          "you need to guess which number it is!\nThere are 2 difficulties, "
          "easy and hard. On easy difficulty, you have a unlimited guesses "
          "however on hard, you only have 8 attempts before you lose.\n")

    while True:
        game_mode = str(input("Please enter a difficulty (easy/hard): "))
        if game_mode == "easy" or game_mode == "hard":
            break
        else:
            print(game_mode, "is not a difficulty.")

    while True:
        play = str(play_game(game_mode))
        if play == "no":
            print("Have a good day.")
            break
        else:
            game_mode = str(input("Please enter a difficulty (easy/hard): "))
            play_game(game_mode)


if __name__ == "__main__":
    main()
