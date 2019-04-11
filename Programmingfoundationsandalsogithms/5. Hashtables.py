#keys, hash function, values
# Benefits
# key to value mapping, speed
items1 = dict({"key1":1, "key2":2, "key3":3})
print(items1)

items2 = {}
items2["key1"]=1
items2["key2"]=2
items2["key3"]=3

print(items2)

# print(items1["key6"])

for key, value in items2.items():
  print("key ",key, " value ",value)

