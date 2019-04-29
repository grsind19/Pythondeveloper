def function1():
  print("Im a function")

def function2(arg1, arg2):
  print(arg1," ", arg2)

def qube(arg):
  return arg*arg*arg

def power(num,x=1):
  result =1
  for i in range(x):
    result = result*num
  return result 

def multiargs(*args):
  result =0
  for x in args:
    result = result +x
  return result

function1()

print(function1())
print(function1)

print(function2(10,20))

print(qube(3))

print(power(4))
print(power(4,3))

print(multiargs(1,2,3,4,5))