import random

decider = random.randrange(2)

if decider == 0:
  print("HEADS")
else:
  print("TAILS")

print("Toy  have rolled "+ str(random.randrange(1,7)))