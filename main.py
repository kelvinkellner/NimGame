# Imports
from random import choice, randint

# Constants for input/output, so the game feels smarter and more sentient, lol.
YES_PHRASES = ["y","yes","sure","ok","okay","yes please","alright","bet"]
NO_PHRASES = ["n","no","nah","nahhh","nope","no thank you"]
AFFIRMATION = ["perfect","awesome","fantastic","amazing","nice","great","okie dokie","sounds good","okay","solid","cool, cool","alrighty","magnificent","excellent","tiiight"]

# Prints a visual display of all the heaps
def print_heaps(heaps):
  for i in range(len(heaps)):
    print("Heap {:d} - {:s}".format(i+1, "|"*heaps[i]))
  return

# Adds a phrase of affirmation, followed by a '.'
def affirm():
  word_choice = choice(AFFIRMATION)
  affirmative = "{:s}.".format(word_choice[0].upper() + word_choice[1:].lower())
  print(affirmative)
  return affirmative

# Plays through one turn for a given player
def turn(name, heaps):
  print("\n\n\n{:s}'s turn!\n".format(name))

  print_heaps(heaps)

  move = ""
  while not move.isdigit() or int(move) > len(heaps):
    print("\nWhich Heap will you take from?")
    move = input(" > ")
  taking_from = int(move)-1
  affirm()

  taking = ""
  while not taking.isdigit() or int(taking) < 1:
    print("\nHow many coins would you like to take from Heap {}?".format(move))
    taking = input(" > ")
  affirm()

  heaps[taking_from] -= int(taking)

  total = 0
  for heap in heaps:
    total += heap
  print(total)
  if total > 0:
    print("\nYour turn is over.")
    return False
  else:
    print("\n\n\nGAME OVER.\n{:s} has lost the game!\n\n".format(name))
    return True

# Does all the magic to start and run a new game
def new_game():
  print("\n\nWelcome to Nim!\nThis is a two-player thinking game coded using Python.")
  print("\n\nHow this game works:\nEither player takes turns taking 1-3 coins from any one Heap of their choosing.\nWhichever player takes the last coin loses the game.")
  
  said = ""
  while said not in YES_PHRASES and said not in NO_PHRASES:
    print("\nNim is a two-player game.\nYou can choose to play against a bot, or against a friend.\n\n\nWould you like to play against a bot?")
    said = input(" > ").lower()
  bot = said in YES_PHRASES
  affirm()

  said = ""
  while said not in YES_PHRASES and said not in NO_PHRASES:
    print("\n\nWould you like to customize the Heap setup?")
    said = input(" > ").lower()
  custom_game = said in YES_PHRASES
  affirm()

  if custom_game:
    heaps = []
    said = ""
    while not said.isdigit() or int(said) < 1:
      print("\n\nHow many Heaps would you like to play with (default is 3)?")
      said = input(" > ")
    for i in range(int(said)):
      said = ""
      while not said.isdigit() or int(said) < 1:
        print("\n\nHow many coins would you like in Heap {:d}?".format(i+1))
        said = input(" > ")
      heaps.append(int(said))
      affirm()
    print("\n\n{:s}\nWe are all done now.\n\nSo let's play some Nim!".format(affirm()))
  else:
    heaps = [3,4,5]
    affirm()

  players = ["Kelvin","Marco","Nicole"]

  # Loop through turns until the game is over
  over = False
  if bot:
    ""
  else:
    while not over:
      for p in players:
        if not over:
          over = turn(p, heaps)


  
# Start the game
new_game()