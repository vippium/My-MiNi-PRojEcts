'''
Author: Vipin Prajapat
Date:  29 September,2022
Purpose: Practice Problem

'''
from termcolor import cprint

def number_guess(num_of_guesses, num):

    while(num_of_guesses != 8):

        guess = int(input("ENTER THE NUMBER TO GUESS :-\n"))
        if guess > num:

            num_of_guesses += 1
            print("LOWER NUMBER PLEASE!")
            print("BE PATIENT, TRY AGAIN!")
            print("YOU USED YOUR", num_of_guesses, "LIFE.")

        elif guess < num:

            num_of_guesses += 1
            print("HIGHER NUMBER PLEASE!")
            print("BE PATIENT, TRY AGAIN!")
            print("YOU USED YOUR", num_of_guesses, "LIFE.")
        else:
            print("HURRAY! YOU GUESSED THE NUMBER. ")
            print("THE NUMBER YOUR OPPONENT CHOOSES IS ", num)
            print("YOU GUESSED THE NUMBER IN", num_of_guesses + 1, "ATTEMPTS ")
            break

        if num_of_guesses == 8:
            print("GAME OVER!")
            print("YOU LOSE! BETTER LUCK NEXT TIME.")
            # break

    restart_game()


def restart_game():
    print("WANT TO PLAY AGAIN?\nType y for yes and n for no : ")

    again_play = input()
    if again_play == "y":

        number_guess(num_of_guesses, num)
    else:

        print("THANK YOU FOR PLAYING!!\nCOME BACK SOON.")
if __name__ == "__main__":
    cprint("#" * 50, "magenta")
    cprint((f"NUMBER GUESSING GAME ").center(50), "yellow")
    cprint((f"(Created by Vipin) ").center(50), "cyan")
    cprint("#" * 50, "magenta")
    print("\t\t\t  <-- TO WIN THIS YOU HAVE ONLY 8 LIFES --> ")
    num = 43
    num_of_guesses = 0
    number_guess(num_of_guesses, num)

