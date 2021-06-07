"""A collection of function for doing my project."""
import random
import pandas as pd
import numpy as np

"""functions for the user system"""

def login (user, user_name, password):
    """ Login into the users' flashcard

    Parameters
    ----------
    user : dictionary
        The collection of all users' name, password, and cards
    user_name : string
        The username of the account.
    password: sting
        The password of the account.
    """

    # search if the username in the system
    if (user_name in user['name']):
        # login into the user's flashcard collections
        if password == user['password'][user['name'].index(user_name)]:
            print('\nWelcome back ' + user_name + '!\n')
            start_card(user['cards'][user['name'].index(user_name)])
            print('\nSee you ' + user_name + '~')
        else:
            print('\nPlease check your password!\n')
    else:
        print('\nPlease check your user name!\n')


def signup (system, user_name, password):
    """ Signup a new account into User() object.

    Parameters
    ----------
    system : User() Object
        The collection of all users' name, password, and cards
    user_name : string
        The username of the account.
    password: sting
        The password of the account.
    """

    system.add_user(user_name, password)


def start (system):
    """ Start the entire program.

    Parameters
    ----------
    system : User() Object 
        The collection of all users' name, password, and cards
    """

    # Welcome and Instructions
    print('Hi! Welcome To Flashcards!\n')
    print('Instructions:')
    print("1. If you are the first time user, please type 'signup' to create your own flashcards!")
    print("2. If you've already have account, please type 'login' to access your flashcards!")
    print("3. If you want to see the current existed username, please type 'show user' to access the username list~")
    print("4. If you've done learning, please type 'end' to end the program!\n")
    print("Current Command: signup, login, show user, end")

    text = input("Please enter your command:")

    # Process user's input and execute the user's command
    while text != 'end':
        # Signup a new account
        if text == 'signup':
            user_name = input('Please enter a username:')
            password = input('Please create a password for this account:')
            signup (system, user_name, password)
        # Login into the account
        elif text == 'login':
            user_name = input('Please enter a username:')
            password = input('Please enter your password:')
            login (system.users, user_name, password)
        # Show the existed user
        elif text == 'show user':
            system.show_user()
        # Invalid command
        else:
            print ("You should enter one of the above command!")
        print("\nCurrent Command: signup, login, show user, end")
        text = input("Please type your command:")

    print('\nBye~~~~')


"""-------------------------------------------------------------------------------------------------"""
"""Below is the flashcard system"""

def quiz_fb (wrong):
    """ Feedback for the quiz

    Parameters
    ----------
    wrong : DataFrame
        The cards that the user got wrong on the quiz
    """

    # Check if the user got anything wrong
    if wrong.empty:
        print('Congratulations! You got them all correct!')
    else:
        wrong = wrong[['term', 'definition']]
        print('You got wrong on below card(s):')
        display(wrong)
    print('\n')


def quiz (cards, order, focus):
    """ Take the designed quiz based on user's requirement

    Parameters
    ----------
    cards : DataFrame
        User's flashcard collections
    order: string
        The order of the quiz taken on the flashcard collections
    foucs: string
        The foucs of the quiz taken on the flashcard collections
    """

    wrong = pd.DataFrame()

    # If the order is random, we use random.shuffle to randomize cards' order
    if order == 'random':
        test = cards.iloc[np.random.permutation(cards.index)].reset_index(drop=True)
    else:
        test = cards

    # If the focus is term, then we should only test on term and ask for its definition
    if focus == 'term':
        for index, row in test.iterrows():
            answer = input('Explain ' + row['term'] + '\n')
            # check if the user's input is same as the answer
            if answer == row['definition']:
                print("You are correct!")
            # if got wrong, show the answer then import the card into a wrong collection
            else:
                print("Nice try! But the answer is: " +  row['definition'])
                wrong = wrong.append (row, ignore_index = True)

    # If the focus is definition, then we should only test on definition and ask for its term
    elif focus == 'definition':
        for index, row in test.iterrows():
            answer = input('What is the term for: ' + row['definition'] + '\n')
            # check if the user's input is same as the answer
            if answer == row['term']:
                print("You are correct!")
            # if got wrong show the answer then import the card into a wrong collection
            else:
                print("Nice try! But the answer is: " +  row['term'])
                wrong = wrong.append (row, ignore_index = True)

    # If the foucs is mixed, then we will test term and definiton alternatively
    else:
        for index, row in test.iterrows():
            # user random.choice to randomly choose the question
            first = random.choice([0,1])
            if first % 2 == 1:
                answer = input('Explain ' + row['term'] + '\n')
                # check if the user's input is same as the answer
                if answer == row['definition']:
                    print("You are correct!")
                # if got wrong show the answer then import the card into a wrong collection
                else:
                    print("Nice try! But the answer is: " +  row['definition'])
                    wrong = wrong.append (row, ignore_index = True)
            else:
                answer = input('What is the term for: ' + row['definition'] + '\n')
                # check if the user's input is same as the answer
                if answer == row['term']:
                    print("You are correct!")
                # if got wrong show the answer then import the card into a wrong collection
                else:
                    print("Nice try! But the answer is: " +  row['term'])
                    wrong = wrong.append (row, ignore_index = True)

    # We called quiz_fb with the wrong answer DataFrame to get the quiz feedback
    quiz_fb(wrong)


def start_card(flashcard):
    """ Start the flashcard system.

    Parameters
    ----------
    falshcard : Card() Object
        User's flashcard collections system
    """

    # Instructions for the flashcard system
    print('Inside your flashcard, here are thing you can do:')
    print("1. Type 'add' to add a new card into your flashcard collections.")
    print("2. Type 'remove' to remove an existed card from your flashcard collections.")
    print("3. Type 'show card' to view your current entire flashcard collections.")
    print("4. Type 'quiz' to take a quiz on your flashcard collections.")
    print("5. Type 'logout' to logout your account.\n")
    print("Enjoy Studying ^v^\n")
    print("Current Command: add, remove, show card, quiz, logout")

    text=input("Please enter your command:")

    # Process and execute the user's command
    while text != 'logout':
        # Add card into the collection
        if text == 'add':
            term = input('Term: ')
            definition = input('Definition: ')
            flashcard.add_card(term, definition)
        # Remove card from the collection
        elif text == 'remove':
            term = input('Term: ')
            flashcard.remove_card(term)
        # Show the existed flashcards
        elif text == 'show card':
            flashcard.show_card()
        # Take the quiz
        elif text == 'quiz':
            order = input('Order is random or ordered?')
            focus = input('Focus on term, definition, or mixed?')
            quiz (flashcard.cards, order, focus)
        # Invalid command
        else:
            print('You should enter one of the above command!')
        print('\n')
        print ("Current Command: add, remove, show card, quiz, logout")
        text=input("Please enter your command:")
