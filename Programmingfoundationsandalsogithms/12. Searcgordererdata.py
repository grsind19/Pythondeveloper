items=[6, 8, 19, 20, 23,41, 49, 53, 87]


def binarySearch(item, itemlist):
  lowerIdx =0
  upperIdx = len(itemlist)-1
  while lowerIdx <= upperIdx:
    midPt = (lowerIdx+upperIdx)//2
    if item == itemlist[midPt]:
      return midPt
    
    if item > itemlist[midPt]:
      lowerIdx = midPt+1
    else:
      upperIdx = midPt - 1

  
  if lowerIdx > upperIdx:
    return None


print(binarySearch(23, items))
print(binarySearch(87, items))
print(binarySearch(230, items))

  
