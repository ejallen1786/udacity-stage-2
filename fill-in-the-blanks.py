easy_text = '''___1___s are used to store information and make ___2___s easier to understand. You can give a ___1___ a ___3___ and assign it to an ___4___.'''

easy_answers = ['variable', 'program', 'name', 'expression']

medium_text = '''A ___1___ is a sequence of ___2___s surrounded by ___3___s. You can add two ___1___s together, but you cannot add a ___1___ and a ___4___ together. You can multiply a ___1___ by a ___4___, which repeats the ___1___.'''

medium_answers = ['string', 'character', 'quote', 'number']

hard_text = '''Python is a ___1___, and like all ___1___s it has a structure called ___2___. The python ___2___ for arithmetic ___3___s involves two major ___4___s: ___3___s and ___5___s.'''

hard_answers = ['language', 'grammar', 'expression', 'non-terminal','operator']

def get_user_choice():
    '''Takes no inputs and asks user for a difficulty choice, validates the choice, and returns the choice.'''

    choice = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
    while not is_valid_choice(choice):
        choice = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
    return choice

def get_user_guesses():
    '''Takes no inputs and asks for a guess number, validates the guess number, and returns the guess number.'''

    guess_number = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    while not is_valid_guess_number(guess_number):
        guess_number = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    return guess_number

def is_valid_choice(choice):
    '''Takes the user-given difficulty choice as input and returns True if the choice is valid.'''

    if choice == 'easy' or choice == 'medium' or choice == 'hard':
        print "You've chosen " + choice + "!"
        return True
    else:
        print "You've chosen " + choice + "!"
        print "That is not a valid choice. Please try again."
        return False

def difficulty_choice(choice):
    '''Takes the user's choice of difficulty as input and returns the associated text.'''

    if choice == 'easy':
        text = easy_text
    if choice == 'medium':
        text = medium_text
    if choice == 'hard':
        text = hard_text
    return text

def answer_choice(choice):
    '''Takes the user's choice of difficulty and returns the associated answers.'''

    if choice == 'easy':
        answers = easy_answers
    if choice == 'medium':
        answers = medium_answers
    if choice == 'hard':
        answers = hard_answers
    return answers

def is_valid_guess_number(guess_number):
    '''Takes the user-given guess number as input and checks if the input is a number. Returns True if it's a number.'''

    if guess_number.isdigit():
        print "You've chosen " + guess_number +  " guesses."
        return True
    else:
        print "You've chosen " + guess_number + " guesses."
        print "That is not a valid number of guesses. Please try again and enter a number."
        return False

def get_user_answer(blank, answers, index):
    '''Takes the blank, the answers list, and the answer index as inputs. Asks user to fill in the blank and validates the answer. Returns the answer if valid.'''

    user_input = raw_input("What should be substituted for " + blank + "? ")
    if is_good_answer(user_input, answers, index):
        return user_input
    else:
        return None


def is_good_answer(word, answers, index):
    '''Takes the users answer, the answer index and the list of answers as inputs. If the answer given is correct based on the ordered answer list, returns True.'''
    
    if word == answers[index]:
        return True
    else:
        return False
                  

def is_complete(text):
    '''Takes the text as input and checks if there are any unfilled blanks left. If there are no unfilled blanks, returns True.'''

    index = text.find("_")
    if index == -1:
        return True
    else:
        return False

def get_new_text(text, blank, answers, index, guess_number):
    '''Takes the text, blank, answers list, answer index and guess number as inputs. Retrieves the user's answer and retries the question until the answer is correct or 
    the guesses have been used up. Once correct answer given, replaces the blank with the answer and returns the new text. If the guesses are used up, returns game over message.'''

    attempts = 0
    user_input = get_user_answer(blank, answers, index)
    while user_input == None: 
        attempts = attempts + 1
        if is_game_over(guess_number, attempts):
            print "Game over...#sadtrombone"
            return None
        user_input = get_user_answer(blank, answers, index)
    print "That is correct!"
    new_text = text.replace(blank, user_input)
    print "The current paragraph reads as such: " + new_text
    return new_text  


def find_blank(text):
    '''Takes the text as input and finds where the next blank is. Sets a variable to the full blank and returns the blank.'''

    blank_index = text.find("_")
    blank = text[blank_index:blank_index + 7]
    return blank

def is_game_over(guess_number, attempts):
    '''Takes guess number and attempts as input and returns True if there are no more guesses left. Returns a message and False if there are guesses left.'''

    remaining_tries = guess_number - attempts
    if remaining_tries == 0:
        return True
    else:
        print "That isn't the correct answer! You have " + str(remaining_tries) + " tries left."
        return False

def play_game():
    '''Takes no inputs. Gets the user's difficulty choice and guess number. Based on input, sets the text and answer list for the game. Presents the text to the
    user and tries to get the user to fill in the blank until the game is complete and there are no more blanks in the text.'''
    
    choice = get_user_choice()
    text = difficulty_choice(choice)
    answers = answer_choice(choice)
    guess_number = int(get_user_guesses())

    answer_index = 0
    print "The current paragraph reads as such: " + text
    while not is_complete(text):
        blank = find_blank(text)
        new_text = get_new_text(text, blank, answers, answer_index, guess_number)
        if new_text != None:
            text = new_text
            answer_index = answer_index + 1
        else:
            return "Have a nice day!"
                   
    return "Thanks for playing!"



print play_game()
        








