from card import Card
from balance import Balance
from go import Round

class Hand:

  def __init__(self):
    self.cards = []
    self.final = False

  def deal_card_to_hand(self, card):
    self.cards.append(card)
    return self.cards

  def total(self):
    total = [0, 0]
    for card in self.cards:
      if not card.is_hidden:
        if card.rank == 'A':
          total[1] = total[0] + card.value()[1]
          total[0] = total[0] + card.value()[0]
        else:
          total[0] = total[0] + card.value()
          total[1] = total[1] + card.value()
    total = list(set(total))
    total.sort()
    if len(total) == 2:
      if total[1] > 21:
        del total[1]
    return total[-1]

  def is_blackjack(self):
    if self.total() == 21:
      return True
    else:
      return False

  def is_bust(self):
    if self.total() > 21:
      self.final = True
      return True
    else:
      return False

  def hit(self, card):
    self.deal_card_to_hand(card)
    return self.cards

  def stick(self):
    self.final = True
    return self.total()

  def double(self, bet, card):
    bet.double() 
    self.deal_card_to_hand(card)
    self.final = True
    return self.total()

  def display(self):
    cards = ''
    for card in self.cards:
      cards += Card.display(card) + '\n'
    return cards

