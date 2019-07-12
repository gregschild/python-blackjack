import constants

class Card:

  def __init__(self, rank, suit):
    self.rank      = rank
    self.suit      = suit
    self.is_hidden = False

  def value(self):
    value = constants.values[self.rank]
    return value

  def display(self):
    if not self.is_hidden:
      return str(self.rank) + ' of ' + self.suit
    else:
      return 'Hidden Card'

