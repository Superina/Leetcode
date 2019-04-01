'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''

alist = [1, 6, -5, 7, 3]  
target = 4

def twoSum(alist,target):  
  adict = {}
  
  for index in range(len(alist)):
    adict[target - alist[index]] = index
    
    if alist[index] in adict:
      return sorted([index,adict[alist[index]]])


print(twoSum(alist,target))