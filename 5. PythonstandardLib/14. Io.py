# Command line arguements

import sys

print(len(sys.argv))

print("Args",sys.argv)

sys.argv.remove(sys.argv[0])
print("Args",sys.argv)

arguements = sys.argv
sum = 0

for arg in arguements:
  try:
    number = int(arg)
    sum = sum + number
  except Exception:
    print("Bad input")

print(sum)