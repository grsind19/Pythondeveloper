# Function calls itself
# Ex: serach for file in directories
# It should have breaking points
# It works with call stack

def countDown(x):
  if x==0:
    print("Gone")
    return
  else:
    print(x,'...')
    countDown(x-1)
    print("foo")


# countDown(5)


def power(num,pwr):
  if pwr == 0:
    return 1
  else:
    return num * power(num,pwr-1)

def factorial(num):
  if num == 0:
    return 1
  else:
    return num*factorial(num-1)

print(power(5,3))
print(factorial(0))