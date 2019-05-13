# List is mutable sequence
# Tuple is immutable
# Dict
# Range is not mutable

x =(1,2,3,4,5,6)

for i  in x:
  print('i is {}'.format(i))

y = {'one': 1, 'two':2 }

for k,v in y.items():
  print(k,v)