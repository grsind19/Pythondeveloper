items =["apple","peer","orange","banana","apple","peer","orange","banana","apple","peer","orange","banana"]

filter = dict()

for item in items:
  filter[item]=0

result = set(filter.keys())
print(result)

counter = dict()
for item in items:
  if item in counter.keys():
    counter[item] +=1
  else:
    counter[item] =1

print(counter)

