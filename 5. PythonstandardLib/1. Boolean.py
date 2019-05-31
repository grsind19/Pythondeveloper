isRaining = False
isSunny = True

# Logical operators

if isRaining and isSunny:
  print("We might see a rainbow")


if isRaining or isSunny:
  print("it might be rainy or sunny")

if not isRaining:
  print("There is no rain")
ages =[12,18,39,87,7,2]

for age in ages:
  isAdult = age >17
  if not isAdult:
    print("Being "+str(age)+ " does not make you an adult")
