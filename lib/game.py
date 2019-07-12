class Game:

    def __init__(self):
      self.is_finished = False
  
    def play_again(self, value):
      if value == 'Y' or value == 'y':
        self.is_finished = False
      else:
        self.is_finished = True
      return self.is_finished

      
