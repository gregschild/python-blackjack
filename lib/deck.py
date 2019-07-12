import constants
from card import Card
import random

class Deck:

  def __init__(self):
    self.deck = []

  def createDeck(self):
    for suit in constants.suits:
      for rank in constants.ranks:
        self.deck.append(Card(rank, suit))
    return self.deck

  def shuffle(self):
    random.shuffle(self.deck)
    return self.deck

  def deal(self):
    card = self.deck[0]
    self.deck.pop(0)
    return card

  def display(self):
    deck = ''
    for card in self.deck:
      deck += Card.display(card) + '\n'
    return deck

