class Round:
  def __init__(self, bet):
    self.bet = bet

  def double(self):
    self.bet = 2 * self.bet
