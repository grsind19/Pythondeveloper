# Greatest common denominator
def gc(a,b):
  while(b!=0):
    t = a
    a = b
    b = t % b
  return a

print(gc(20,8))

# Mearsure how an alogoriith responsds to the dtaset size

# 1. Big O Notation - Classifies performce as the input size grows - O order of operation
