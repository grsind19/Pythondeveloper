items=[6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
  if len(dataset)>1:
    mid = len(dataset)//2
    leftArr = dataset[:mid]
    rightArr = dataset[mid:]

    mergeSort(leftArr)
    mergeSort(rightArr)

    i,j,k=0,0,0

    while i < len(leftArr) and j <len(rightArr):
      if leftArr[i]<rightArr[j]:
        dataset[k] = leftArr[i]
        i += 1
      else:
        dataset[k] = rightArr[j]
        j += 1
      
      k += 1
    
    while i <len(leftArr):
      dataset[k] = leftArr[i]
      i += 1
      k += 1
    
    while j < len(rightArr):
      dataset[k] = rightArr[j]
      j += 1
      k += 1


print(items)
mergeSort(items)
print(items)