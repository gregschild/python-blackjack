import card
import deck
import hand
import balance
import game
import go

# Start game
game = game.Game()

# Create Deck and shuffle
deck = deck.Deck()
deck.createDeck()
deck.shuffle()

# Bring in starting stack
stack = input("How much would you like to bring to the table? ")
player_balance = balance.Balance(int(stack))

while not game.is_finished:
 
  print("Your balance is: {}".format(player_balance.get_balance()))

  bet = input("What would you like to bet? ")
  bet = int(bet)
  r = go.Round(bet)
  if not player_balance.bet_accepted(r.bet):
    print('Bet too much! Please choose a smaller amount')
    while not player_balance.bet_accepted(r.bet):
      bet = input("What would you like to bet? ")
      bet = int(bet)
      r = go.Round(bet) 

  # Define player and dealer hand
  player_hand = hand.Hand()
  dealer_hand = hand.Hand()

  # Deal cards
  player_hand.deal_card_to_hand(deck.deal())
  dealer_hand.deal_card_to_hand(deck.deal())
  player_hand.deal_card_to_hand(deck.deal())
  dealer_hand.deal_card_to_hand(deck.deal())

  # Hide one dealer card
  dealer_hand.cards[0].is_hidden = True


  print('Your hand: (' + str(player_hand.total()) + ')')
  print(player_hand.display())
  print('Dealer\'s hand: (' + str(dealer_hand.total()) + ')')
  print(dealer_hand.display())


  if player_hand.is_blackjack():
    print('BLACKJACK!')
    player_hand.stick()

# User options

  while not player_hand.final:
    option = input("(H)it, (D)ouble or (S)tick: ")
    if option == 'H':
      player_hand.hit(deck.deal())
      print('New Card: (' + str(player_hand.total()) + ')')
      print(player_hand.cards[-1].display())
      player_hand.is_bust()
    elif option == 'D':
      player_hand.double(r, deck.deal())
      print('Final Card: ' + player_hand.cards[-1].display())
      player_hand.is_bust()
    elif option == 'S':
      player_hand.stick()

    else:
      print('Incorrect input... sticking by default')
      player_hand.stick()

  print('Final value: ' + str(player_hand.total()))


  # Dealer runout

  dealer_hand.cards[0].is_hidden = False
  print('Dealer reveals the ' + dealer_hand.cards[0].display())
  print('Dealer has ' + str(dealer_hand.total()))

  while dealer_hand.total() < 17:
    dealer_hand.hit(deck.deal())
    print('Dealer draws the ' + dealer_hand.cards[-1].display())
    print('Dealer has ' + str(dealer_hand.total()))

  print('Dealer Final value: ' + str(dealer_hand.total()))


  # Determine winner
  if player_hand.is_blackjack():
    print('Player wins!')
    payout = r.bet * 1.5
    player_balance.add_to_stack(payout)
  elif player_hand.total() > 21:
    print('Player loses!')
    player_balance.remove_from_stack(r.bet)
  elif dealer_hand.total() > 21:
    print('Dealer busts...')
    print('Player wins!')
    player_balance.add_to_stack(r.bet)
  elif player_hand.total() > dealer_hand.total():
    print('Player wins!')
    player_balance.add_to_stack(r.bet)
  elif player_hand.total() == dealer_hand.total():
    print('Push!')
  elif player_hand.total() < dealer_hand.total():
    print('Player loses!')
    player_balance.remove_from_stack(r.bet)

  play_again = input("Would you like to play again? (Y/n):")
  game.play_again(play_again)

  
print("Your final balance is: {}".format(player_balance.get_balance()))

