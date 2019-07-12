
class Balance:

  def __init__(self, stack):
    self.stack = stack

  def bet_accepted(self, value):
    if value > self.stack:
      return False
    elif value <= self.stack:
      return True

  def add_to_stack(self, value):
    self.stack = self.stack + value
    return self.stack

  def remove_from_stack(self, value):
    self.stack = self.stack - value
    return self.stack

  def get_balance(self):
    return self.stack
