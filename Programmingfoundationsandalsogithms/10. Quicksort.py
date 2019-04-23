items=[6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def quickSort(dataset, first, last):
  if first < last:
    pivotrIdx = partition(dataset, first, last)

    quickSort(dataset, first, pivotrIdx-1)
    quickSort(dataset, pivotrIdx+1, last)


def partition(dataset, first, last):
  pivotValue = dataset[first]
  lower = first+1
  upper = last

  done = False

  while not done:
    while pivotValue >= dataset[lower] and upper >= lower:
      lower +=1
    while pivotValue <= dataset[upper] and upper >= lower:
      upper -= 1
    
    if upper < lower:
      done = True
    else:
      temp = dataset[lower]
      dataset[lower] = dataset[upper]
      dataset[upper] = temp
  
  temp = dataset[first]
  dataset[first] = dataset[upper]
  dataset[upper] = temp
  return upper
    




print(items)
quickSort(items,0, len(items)-1)
print(items)