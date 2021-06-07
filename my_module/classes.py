"""Classes used throughout project"""
import pandas as pd

# define a class called User()
class User():

    def __init__(self):
        """ The constructor (__init__) takes no inputs, but set users to be an empty dictionary.

        Instance Attribute
        ----------
        users: dictionary
            A dictionary that stores all users' username, password and cards.
        """

        self.users = {'name':[],'password':[],'cards':[]}

    def add_user(self, name, password):
        """ Add user into the users
        
        Parameters
        ----------
        name : string
            The username of the user.
        password : string
            The password of the account.
        card: Card() object
            The cards for this user.
        """

        if not name in self.users['name']:
            self.users['name'].append(name)
            self.users['password'].append(password)
            self.users['cards'].append(Card())
            print('\nYou have created an account successfully!')
            print('Please try to login into your account! ')
        else: 
            print('\nThis username has been taken T^T Please try another username! ')

    def show_user(self):
        """ Print out all the existed username.
        """

        print("\nCurrent existed username:")
        print(self.users['name'])

"""-------------------------------------------------------------------------------------------------"""

# define a class called Card()
class Card():

    def __init__ (self):
        """ The constructor (__init__) takes no inputs, but set cards to be an empty DataFrame.

        Instance Attribute
        ----------
        cards: DataFrame
            A dataframe that stores all the cards
        """        
        self.cards = pd.DataFrame(columns=['term','definition'])


    def add_card (self, term, definition):
        """ Add card into the cards

        Parameters
        ----------
        term : string
            The key term of the card.
        definition : string
            The defintion of the key term.
        """

        # Create a dictionary from the values passed with the corresponding inputs: 'term', 'definition'
        # Append this dictionary to the cars attribute
        data = pd.DataFrame({'term':[term], 'definition':[definition]})
        self.cards = self.cards.append(data, ignore_index = True)


    def remove_card (self, term):
        """ Remove card from the cards.
            We choose to use term to find the card and remove the card.
    
        Parameters
        ----------
        term : string
            The key term of the card.
        """

        # use del to delete the particular card if it matches the term
        self.cards = self.cards[self.cards['term'] != term].reset_index(drop=True)


    def show_card (self):
        """ Print out the current cards DataFrame.
        """
        display(self.cards)
