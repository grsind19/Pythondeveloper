items1 = [6,8,19,20,23,41,49,53,56,87]
items2=[6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def isSorted(itemList):
  # for i in range(len(itemList)-1):
  #   if itemList[i]>itemList[i+1]:
  #     return False

  return all(itemList[i]<=itemList[i+1] for i in range(len(itemList)-1))
  # return True


print(isSorted(items1))
print(isSorted(items2))