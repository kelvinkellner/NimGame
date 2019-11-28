heaps = [3,4,5]

# Prints a visual display of all the heaps
def print_heaps(heaps):
  for i in range(len(heaps)):
    print("Heap {:d} - {:s}".format(i+1, "|"*heaps[i]))
  return

# One turn for a given player
def turn(name):
  print("\n\n{:s}'s turn!".format(name))

  print_heaps(heaps)

  move = ""
  while (not move.isdigit()) or int(move) > len(heaps):
    print("\nWhich heap will you take from?")
    move = input(" > ")
  taking_from = int(move)-1

  print("\nPerfect!")
  taking = ""
  while (not taking.isdigit()) or int(taking) < 1:
    print("\nHow many coins would you like to take from heap {}?".format(move))
    taking = input(" > ")
  print("\nFantastic!")

  heaps[taking_from] -= int(taking)

  total = 0
  for heap in heaps:
    total += heap
  if total > 0:
    print("\nYour turn is over.")
    return False
  else:
    print("\n\nGAME OVER.\n{:s} has lost the game!\n".format(name))
    return True


players = ["Kelvin","Marco","Nicole"]

over = False
while not over:
  for p in players:
    over = turn(p)

