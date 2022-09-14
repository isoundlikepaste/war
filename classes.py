import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


# Card class which includes Suit, Rank and Value of the card
class Card():

    def __init__(self, suit, rank):
        self.suit = suit.title()
        self.rank = rank.title()
        self.value = values[rank.title()]

    def __str__(self):
        return self.rank + " of " + self.suit

    def __len__(self):
        return self.value

# Deck class which will include 52 Cards as a list
class Deck():

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#Player class with methods to play and add cards to hand
class Player():

    def __init__(self, name):
        self.name = name
        self.my_cards = []

    def remove_one(self):
        return self.my_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.my_cards.extend(new_cards)
        else:
            self.my_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.my_cards)} cards.'







