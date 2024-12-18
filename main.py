"""
Code Written by Jackson L. Davis

This is the main Python file to run.
This program sets up a game of Mastermind.
Information about the board game "Mastermind" can be found here:
https://en.wikipedia.org/wiki/Mastermind_(board_game)

In this program, the user can either set up a code for the computer to break,
or the computer can set up a code for the user to break.
The codemaker has to make a code with four pegs. The pegs come in six "colours" (I will use numbers instead of colours).
The codebreaker has ten tries to break the code.
"""

from board import Board
from computer_player import ComputerPlayer
import random as rand

if __name__ == '__main__':
    print("Welcome to Mastermind.")
    print("----------------------------------------------------------------------------------------")
    print("Instructions:")
    print("The codemaker has to set up a code with four pegs.")
    print("The pegs come in six \"colours\" (this program uses numbers 1-6 instead of colours).")
    print("An example of a code is 1256.")
    print("The codebreaker has ten tries to guess the code.")
    print("After each guess, the codebreaker gets the results of the guess indicating how many")
    print("pegs are the right colour and in the right place, and how many pegs are the right colour")
    print("but in the wrong place.")
    print("----------------------------------------------------------------------------------------")
    print("Do you want to be the codemaker or the codebreaker?")
    print("If you are the codemaker, a computer player will try to break your code.")
    print("If you are the codebreaker, you will try to break a randomly generated code.")
    print("Press 1 and enter to be the codemaker, or press 2 and enter to be the codebreaker.")
    game_type = "0"
    while game_type != "1" and game_type != "2":
        game_type = input("Enter choice here: ")

    if game_type == "1":
        # user enters code
        user_code = input("Enter your code here: ")
        board_set_up = False
        while not board_set_up:
            try:
                decoding_board = Board(user_code)
                board_set_up = True
            except:
                print(user_code + " is not a valid code.")
                user_code = input("Enter your code here: ")
        # computer player tries to break the code
        cp = ComputerPlayer(decoding_board)
        print("A computer player will attempt to break your code.")
        print("This may take a few moments.")
        solve_time = cp.solve()
        if decoding_board.solved:
            print("The computer player broke your code in " + str(solve_time) + " seconds.")
        else:
            print("The computer player did not break your code.")
    else:
        # set up random code
        code = ""
        for i in range(4):
            code += str(rand.randint(1, 6))

        # set up board
        decoding_board = Board(code)

        # guesses
        print("You can enter guesses, or press q and enter to quit.")
        next_guess = ""
        while len(decoding_board.guesses) < decoding_board.max_guesses and not decoding_board.solved:
            next_guess = input("Enter your next guess: ")
            if next_guess == "q":
                break
            # add guess and get results
            try:
                decoding_board.add_guess(next_guess)
                print("Correct colour and correct place: " + str(decoding_board.responses[-1][0]))
                print("Correct colour but wrong place:   " + str(decoding_board.responses[-1][1]))
                print(decoding_board)
            except:
                print(next_guess + " is not a valid guess.")

        # quit
        if next_guess == "q":
            print("You quit. The code was " + decoding_board.code + ".")
        # out of guesses - loss
        elif not decoding_board.solved:
            print("You lost. The code was " + decoding_board.code + ".")
        # correct guess - win
        else:
            print("You win!")
