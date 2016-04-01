easy_text = '''___1___s are used to store information and make ___2___s easier to understand. You can give a ___1___ a ___3___ and assign it to an ___4___.'''

easy_answers = ['variable', 'program', 'name', 'expression']

medium_text = '''A ___1___ is a sequence of ___2___s surrounded by ___3___s. You can add two ___1___s together, but you cannot add a ___1___ and a ___4___ together. You can multiply a ___1___ by a ___4___, which repeats the ___1___.'''

medium_answers = ['string', 'character', 'quote', 'number']

hard_text = '''Python is a ___1___, and like all ___1___s it has a structure called ___2___. The python ___2___ for arithmetic ___3___s involves two major ___4___s: ___3___s and ___5___s.'''

hard_answers = ['language', 'grammar', 'expression', 'non-terminal','operator']

def is_valid_choice(choice):
    '''Checks if the user given difficulty choice is valid.'''

    if choice == 'easy' or choice == 'medium' or choice == 'hard':
        print '''You've chosen ''' + choice + '''!
        '''
        return True
    else:
        print '''You've chosen ''' + choice + '''!
        '''
        print '''That is not a valid choice. Please try again.
        '''
        return False

def difficulty_choice(choice):
    '''Based on user's choice of difficulty, returns the associated text.'''

    if choice == 'easy':
        text = easy_text
    if choice == 'medium':
        text = medium_text
    if choice == 'hard':
        text = hard_text
    return text

def answer_choice(choice):
    '''Based on user's choice of difficulty, returns the associated answers.'''

    if choice == 'easy':
        answers = easy_answers
    if choice == 'medium':
        answers = medium_answers
    if choice == 'hard':
        answers = hard_answers
    return answers

def is_valid_guess_number(guess_number):
    '''Checks if user's choice of # of guesses is a number.'''

    if guess_number.isdigit():
        print '''You've chosen ''' + guess_number + ''' guesses.
    '''
        return True
    else:
        print '''You've chosen ''' + guess_number + ''' guesses.
        '''
        print '''That is not a valid number of guesses. Please try again and enter a number.
        '''
        return False

def is_good_answer(word, answers, index):
    '''Checks if the answer given is correct based on the ordered answer list.'''

    if word in answers[index]:
        return True
    else:
        return False

def is_complete(text):
    '''Checks if there are any unfilled blanks left.'''

    index = text.find("_")
    if index == -1:
        return True
    else:
        return False

def replaced_text(text, blank, answer):
    '''Replaces all specified blanks in the text with the user's input.'''

    text = text.replace(blank, answer)
    return text

def find_blank(text):
    '''Finds where the next blank is and sets a variable to the full blank.'''

    blank_index = text.find("_")
    blank = text[blank_index:blank_index + 7]
    return blank

def guesses_left(guess_number, attempts):
    '''Checks if the user still has guesses left.'''

    if attempts < guess_number:
        return True
    else:
        return False

def play_game():
    
    choice = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
    while not is_valid_choice(choice):
        choice = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
    text = difficulty_choice(choice)
    answers = answer_choice(choice)

    guess_number = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    while not is_valid_guess_number(guess_number):
        guess_number = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    guess_number = int(guess_number)


    print '''The current paragraph reads as such: ''' + text + '''
    '''
    answer_index = 0
    attempts = 0
    while not is_complete(text):
        blank = find_blank(text)
        user_input = raw_input("What should be substituted for " + blank + "? ")
        if is_good_answer(user_input, answers, answer_index):
            print '''That is correct!
            '''
            text = replaced_text(text, blank, user_input)
            print '''The current paragraph reads as such: 
''' + text + ''' 
        '''
            answer_index = answer_index + 1
            attempts = 0
        else: 
            attempts = attempts + 1
            if guesses_left(guess_number, attempts):
                remaining_tries = guess_number - attempts
                print '''That isn't the correct answer! You have ''' + str(remaining_tries) + ''' tries left.
                '''
            else:
                print '''Game over...#sadtrombone
                '''
                return "Have a nice day!"   
    return "You completed the game. Thanks for playing!"



print play_game()
        








