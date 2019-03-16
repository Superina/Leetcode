alist = [1, 6, -5, 7, 3]  
target = -2

def two_sum(alist,target):
  adict = {}
  for index in range(len(alist)):
    adict[target-alist[index]] = index
    if alist[index] in adict:
      return [index,adict[alist[index]]]
  return [-1, -1]



print(two_sum(alist,target))


