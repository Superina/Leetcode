'''
Given a list [2,3,0,5,1,4], input = 5

Return [(2,3)(0,5),(1,4)]
'''

def twoSum(array,target):
	alist = []
	adict = {}
	
	for index in range(len(array)):
		diff = target - array[index]
		adict[diff] = index

		if array[index] in adict:
			alist.append((array[index],array[adict[array[index]]]))


	return alist



array = [2,3,0,5,1,4]
target = 5
print(twoSum(array,target))