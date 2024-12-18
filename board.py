"""
Code Written by Jackson L. Davis

This class is for a decoding board used in the board game "Mastermind."
The decoding board will store the code, the guesses, and the response for each guess.

Here are some example guesses and responses:

If the code is "1234" and a guess is "1523", the response to the guess would be (1, 2) meaning that one peg is
the correct colour and in the correct position, and two pegs are the correct colour but in the wrong position.

If the code is "1234" and a guess is "2341", the response to the guess would be (0, 4).

If the code is "1234" and a guess is "1234", the response to the guess would be (4, 0).

If the code is "1234" and a guess is "5555", the response to the guess would be (0, 0).

If the code is "1234" and a guess is "1111", the response to the guess would be (1, 0). The first "1" is in the
correct position, but the extra 1's do not count for anything.

If the code is "1234" and a guess is "5111", the response to the guess would be (0, 1). There is only one "1" in the
code, so only one "1" counts for being the correct colour but in the wrong position.

If the code is "2111" and a guess is "1654", the response to the guess would be (0, 1).
"""


class Board:

    def __init__(self, code):
        """
        Constructor method for the decoding board
        :param code: a string of a four-digit number representing the code to break
        :precond: is_valid_code(code)
        """
        if not self.is_valid_code(code):
            raise Exception("Cannot make Board, code is not valid.")
        else:
            pass

        self.__code = code
        self.__max_guesses = 10
        self.__solved = False
        self.__guesses = []    # a list of strings where each string is a guess, ex. ["1234", "1256", "3344"]
        self.__responses = []  # a list of tuples where each tuple is the response to a guess
                               # ex. (2, 1) means that two pegs are the correct colour and position,
                               # and one peg is the correct colour but incorrect position

    @property
    def code(self):
        return self.__code

    @property
    def max_guesses(self):
        return self.__max_guesses

    @property
    def solved(self):
        return self.__solved

    @property
    def guesses(self):
        return self.__guesses

    @property
    def responses(self):
        return self.__responses

    def add_guess(self, guess):
        """
        Add a guess for the code, and add a response
        :param guess: a string of a four-digit number representing a guess
        :precond: is_valid_code(guess)
        :precond: len(self.__guesses) < self.__max_guesses and not self.__solved
        :postcond: guess is added to guesses, and a response for the guess is added to responses
                   unless the preconditions are not met
        """
        if not self.is_valid_code(guess):
            raise Exception("Cannot add guess because the guess is not valid.")
        elif len(self.__guesses) < self.__max_guesses and not self.__solved:
            self.__guesses.append(guess)
            resp = self.create_response(guess)
            self.__responses.append(resp)
            if resp == (4, 0):
                self.__solved = True
            else:
                pass
        else:
            pass

    def create_response(self, guess):
        """
        Create a response based on the guess
        :param guess: a string of a four-digit number representing a guess
        :precond: guess should be a four-digit number where each digit can be 1, 2, 3, 4, 5, or 6, add_guess() would have already checked this
        :return: a tuple representing a response
        """
        correct_colour_and_position = 0
        correct_colour_wrong_position = 0
        code_peg_taken = [False] * 4   # list to keep track of which pegs in the code are taken by a peg in the guess
        guess_peg_taken = [False] * 4  # list to keep track of which pegs in the guess are taken by a peg in the code

        # check for correct colour and position
        for i in range(4):
            if guess[i] == self.__code[i]:
                correct_colour_and_position += 1
                code_peg_taken[i] = True
                guess_peg_taken[i] = True
            else:
                pass

        # check correct colour wrong position
        for j in range(4):
            if not guess_peg_taken[j]:
                for k in range(4):
                    if j != k:
                        if guess[j] == self.__code[k] and not code_peg_taken[k]:
                            correct_colour_wrong_position += 1
                            code_peg_taken[k] = True
                            guess_peg_taken[j] = True
                            break
                    else:
                        pass
            else:
                pass

        return (correct_colour_and_position, correct_colour_wrong_position)

    def __repr__(self):
        """
        Make a representation of the decoding board that looks exactly like
        the way one would make it in code
        :return: a string representation of the code necessary to make the decoding board
        """
        return f"{self.__class__.__name__}(\"{self.__code}\")"

    def __str__(self):
        """
        Create a string representation of the decoding board
        :return: a string representation of the decoding board
        """
        st = ""

        # print guesses and results
        for i in range(len(self.__guesses)):
            st += self.__guesses[i]
            st += " | "
            st += str(self.__responses[i])
            st += "\n"

        # print blank lines
        blank_lines = self.__max_guesses - len(self.__guesses)
        for j in range(blank_lines):
            st += "     |\n"
        st += "-----+\n"

        # print code if the puzzle is solved or if all guesses are used up
        if blank_lines == 0 or self.__solved:
            st += self.__code
        else:
            st += "????"
        st += "\n"
        return st

    @staticmethod
    def is_valid_code(code):
        """
        Determine whether the parameter code is a valid code.
        A code should be a four-digit number where each digit can be 1, 2, 3, 4, 5, or 6,
        ex. "1246" is allowed, but "2024" is not
        :param code: a string representing a code to check
        :return: True if the code is valid, False otherwise
        """
        if len(code) != 4:
            return False
        else:
            valid_characters = ["1", "2", "3", "4", "5", "6"]
            for char in code:
                if char not in valid_characters:
                    return False
                else:
                    pass
        return True


if __name__ == '__main__':
    print("Testing board.py")
    errors = 0
    bad_responses = 0  # number of incorrect responses given

    # test is_valid_code()
    valid_codes = ["1111", "2345", "6666", "1122", "1616"]
    for vc in valid_codes:
        if not Board.is_valid_code(vc):
            print("Error: is_valid_code() returned False for a valid code.")
            errors += 1
        else:
            pass

    invalid_codes = ["111", "11111", "0000", "7777", "2024", "abcd"]
    for ic in invalid_codes:
        if Board.is_valid_code(ic):
            print("Error: is_valid_code() returned True for an invalid code.")
            errors += 1
        else:
            pass


    # test __init__()
    try:
        valid_board = Board("1111")
        # test add_guess() with valid and invalid guesses
        try:
            valid_board.add_guess("2525")
        except:
            print("Error: add_guess() threw an exception for valid guess.")
            errors += 1
        try:
            valid_board.add_guess("7890")
            print("Error: add_guess() did not throw and exception for invalid guess.")
            errors += 1
        except:
            pass
    except:
        print("Error: __init__() threw an exception for a valid code.")
        errors += 1

    try:
        invalid_board = Board("0")
        print("Error: __init__() did not throw an exception for invalid code.")
        errors += 1
    except:
        pass

    print("First board")
    test_board = Board("1234")

    # test __repr__() and __str__()
    print(repr(test_board))
    print(test_board)

    # test getter methods with no guesses
    print(test_board.code)
    print(test_board.max_guesses)
    print(test_board.solved)
    print(test_board.guesses)
    print(test_board.responses)
    print()

    # test add_guess()
    print("Add some guesses.")
    test_board.add_guess("1523")
    test_board.add_guess("2341")
    test_board.add_guess("5555")
    test_board.add_guess("1111")
    test_board.add_guess("5111")
    test_board.add_guess("1342")
    test_board.add_guess("2134")
    test_board.add_guess("2543")
    print(test_board)
    print("Add the correct code.")
    test_board.add_guess("1234")
    print(test_board)
    print("Add a guess even though the code was broken.")
    test_board.add_guess("4321")
    print(test_board)

    # test create_response() with the guesses
    test_guesses = ["1523", "2341", "5555", "1111", "5111", "1342", "2134", "2543", "1234"]
    test_responses = [(1, 2), (0, 4), (0, 0), (1, 0), (0, 1), (1, 3), (2, 2), (0, 3), (4, 0)]
    for g in range(len(test_guesses)):
        if test_board.create_response(test_guesses[g]) != test_responses[g]:
            print("Bad response for guess " + test_guesses[g] + ", expected " + str(test_responses[g]) + ", got " + str(test_board.create_response(test_guesses[g])))
            bad_responses += 1
        else:
            pass

    # test getter methods with guesses
    print(test_board.code)
    print(test_board.max_guesses)
    print(test_board.solved)
    print(test_board.guesses)
    print(test_board.responses)
    print()

    print("Second board")
    test_board_2 = Board("2111")

    # test getter methods with no guesses
    print(test_board_2.code)
    print(test_board_2.max_guesses)
    print(test_board_2.solved)
    print(test_board_2.guesses)
    print(test_board_2.responses)
    print()

    print("Add 10 wrong guesses")
    test_board_2.add_guess("1654")
    test_board_2.add_guess("1555")
    test_board_2.add_guess("1111")
    test_board_2.add_guess("2222")
    test_board_2.add_guess("3333")
    test_board_2.add_guess("1222")
    test_board_2.add_guess("2112")
    test_board_2.add_guess("1234")
    test_board_2.add_guess("6111")
    test_board_2.add_guess("2121")
    print(test_board_2)
    print("Add the correct code even though we are out of guesses.")
    test_board_2.add_guess("2111")
    print(test_board_2)

    # test create_response() with the guesses
    test_guesses_2 = ["1654", "1555", "1111", "2222", "3333", "1222", "2112", "1234", "6111", "2121"]
    test_responses_2 = [(0, 1), (0, 1), (3, 0), (1, 0), (0, 0), (0, 2), (3, 0), (0, 2), (3, 0), (3, 0)]
    for g in range(len(test_guesses_2)):
        if test_board_2.create_response(test_guesses_2[g]) != test_responses_2[g]:
            print("Bad response for guess " + test_guesses_2[g] + ", expected " + str(test_responses_2[g]) + ", got " + str(test_board_2.create_response(test_guesses_2[g])))
            bad_responses += 1
        else:
            pass

    # test getter methods with guesses
    print(test_board_2.code)
    print(test_board_2.max_guesses)
    print(test_board_2.solved)
    print(test_board_2.guesses)
    print(test_board_2.responses)
    print()

    print("Third board")
    test_board_3 = Board("5566")

    # test getter methods with no guesses
    print(test_board_3.code)
    print(test_board_3.max_guesses)
    print(test_board_3.solved)
    print(test_board_3.guesses)
    print(test_board_3.responses)
    print()

    print("Add some guesses")
    test_board_3.add_guess("5454")
    test_board_3.add_guess("5646")
    test_board_3.add_guess("5561")
    test_board_3.add_guess("5556")
    test_board_3.add_guess("1234")
    test_board_3.add_guess("5446")
    test_board_3.add_guess("6445")
    test_board_3.add_guess("5656")
    test_board_3.add_guess("6655")
    print(test_board_3)

    print("Make the tenth guess correct")
    test_board_3.add_guess("5566")
    print(test_board_3)
    print("Add a guess even though the code was broken and we are out of guesses.")
    test_board_3.add_guess("4321")
    print(test_board_3)

    # test create_response() with the guesses
    test_guesses_3 = ["5454", "5646", "5561", "5556", "1234", "5446", "6445", "5656", "6655", "5566"]
    test_responses_3 = [(1, 1), (2, 1), (3, 0), (3, 0), (0, 0), (2, 0), (0, 2), (2, 2), (0, 4), (4, 0)]
    for g in range(len(test_guesses_3)):
        if test_board_3.create_response(test_guesses_3[g]) != test_responses_3[g]:
            print("Bad response for guess " + test_guesses_3[g] + ", expected " + str(test_responses_3[g]) + ", got " + str(test_board_3.create_response(test_guesses_3[g])))
            bad_responses += 1
        else:
            pass

    # test getter methods with guesses
    print(test_board_3.code)
    print(test_board_3.max_guesses)
    print(test_board_3.solved)
    print(test_board_3.guesses)
    print(test_board_3.responses)
    print()

    print("Finished testing with " + str(errors) + " errors.")
    print("Finished testing with " + str(bad_responses) + " bad responses.")
